/* Copyright 2019 The TensorFlow Authors. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
==============================================================================*/
#ifndef TENSORFLOW_LITE_KERNELS_INTERNAL_REFERENCE_DEQUANTIZE_H_
#define TENSORFLOW_LITE_KERNELS_INTERNAL_REFERENCE_DEQUANTIZE_H_

#include <limits.h>

#include <vector>

#include "tensorflow/lite/kernels/internal/common.h"
#include "tensorflow/lite/kernels/internal/types.h"

namespace tflite {

namespace reference_ops {

// Dequantizes into a float without rounding.
template <typename InputT, typename OutputT>
inline void Dequantize(const tflite::DequantizationParams& op_params,
                       const RuntimeShape& input_shape,
                       const InputT* input_data,
                       const RuntimeShape& output_shape, OutputT* output_data) {
  int32_t zero_point = op_params.zero_point;
  const double scale = op_params.scale;
  const int flat_size = MatchingFlatSize(input_shape, output_shape);

  for (int i = 0; i < flat_size; i++) {
    const int32_t val = input_data[i];
    const OutputT result = static_cast<OutputT>(scale * (val - zero_point));
    output_data[i] = result;
  }
}

inline void DequantizeF16F32(const tflite::DequantizationParams& op_params,
                      const RuntimeShape& input_shape,
                      const uint16_t* input_data,
                      const RuntimeShape& output_shape, float* output_data) {
  int32_t zero_point = op_params.zero_point;
  const double scale = op_params.scale;
  const int flat_size = MatchingFlatSize(input_shape, output_shape);
  for (int i = 0; i < flat_size; i++) {
    // const int32_t val = input_data[i];
    // handle float16 to float32 conversion
    uint16_t raw = input_data[i];
    uint16_t sign = raw & 0x8000;
    uint16_t exponent = raw & 0x7C00;
    uint16_t mantissa = raw & 0x03FF;
    uint32_t cast_float;
    if (exponent == 0x7C00) {  // Inf or NaN
      cast_float = (sign << 16) | 0x7F800000 | (mantissa << 13);
    } else if (exponent == 0) {
        if (mantissa == 0) {  // Zero
          cast_float = (sign << 16);
        } else {  // Denormal
          // mantissa * 2^(1 - 15) * 2^(-10) = mantissa * 2^(-24)
          // make a float directly
          float v = mantissa * 0.000000059604644775390625f;
          cast_float = (sign << 16) | *reinterpret_cast<uint32_t*>(&v);
        }
    }
    else {  // Normal number
      uint16_t new_exponent = (exponent >> 10) - 15 + 127;
      uint16_t new_mantissa = mantissa << 13;
      cast_float = (sign << 16) | (new_exponent << 23) | new_mantissa;
    }
    float val = *reinterpret_cast<float*>(&cast_float);
    const float result = static_cast<float>(scale * (val - zero_point));
    output_data[i] = result;
  }
}

// Dequantizes per-channel quantized tensor to float.
template <typename T>
inline void PerChannelDequantize(
    const tflite::PerChannelDequantizationParams& op_params,
    const RuntimeShape& input_shape, const T* input_data,
    const RuntimeShape& output_shape, float* output_data) {
  // Ensure flat size is same.
  MatchingFlatSize(input_shape, output_shape);

  const int32_t* zero_point = op_params.zero_point;
  const float* scale = op_params.scale;
  const int32_t quantized_dimension = op_params.quantized_dimension;
  const int32_t num_dims = input_shape.DimensionsCount();
  const int32_t* dims_data = input_shape.DimsData();
  std::vector<int> current_dim(num_dims, 0);

  do {
    size_t offset =
        ReducedOutputOffset(num_dims, reinterpret_cast<const int*>(dims_data),
                            current_dim.data(), 0, nullptr);
    const int channel = current_dim[quantized_dimension];
    const int32_t val = input_data[offset];
    const float result =
        static_cast<float>(scale[channel] * (val - zero_point[channel]));
    output_data[offset] = result;
  } while (NextIndex(num_dims, reinterpret_cast<const int*>(dims_data),
                     current_dim.data()));
}

}  // namespace reference_ops

}  // namespace tflite
#endif  // TENSORFLOW_LITE_KERNELS_INTERNAL_REFERENCE_DEQUANTIZE_H_
