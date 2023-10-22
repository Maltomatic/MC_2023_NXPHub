/*
 * Copyright 2020-2022 NXP
 * All rights reserved.
 *
 * SPDX-License-Identifier: BSD-3-Clause
 */

#include "fsl_debug_console.h"
#include "output_postproc.h"
#include "get_top_n.h"
#include "demo_config.h"
//#include "labels.h"
#include "flower_labels.h"
#ifdef EIQ_GUI_PRINTF
#include "chgui.h"
#endif
// data should be received from output(1)
status_t MODEL_ProcessOutput(const uint8_t* data, const tensor_dims_t* dims,
                             tensor_type_t type, int inferenceTime)
{
//    const float threshold = (float)DETECTION_TRESHOLD / 100;
//    result_t topResults[NUM_RESULTS];
//    const char* label = "No label detected";
//
//    /* Find best label candidates. */
//    MODEL_GetTopN(data, dims->data[dims->size - 1], type, NUM_RESULTS, threshold, topResults);
//
//    float confidence = 0;
//    if (topResults[0].index >= 0)
//    {
//        auto result = topResults[0];
//        confidence = result.score;
//        int index = result.index;
//        if (confidence * 100 > DETECTION_TRESHOLD)
//        {
//            label = labels[index];
//        }
//    }
//
//    int score = (int)(confidence * 100);
//    PRINTF("----------------------------------------" EOL);
//    PRINTF("     Inference time: %d ms" EOL, inferenceTime / 1000);
//    PRINTF("     Detected: %s (%d%%)" EOL, label, score);
//    PRINTF("----------------------------------------" EOL);
//
//#ifdef EIQ_GUI_PRINTF
//    GUI_PrintfToBuffer(GUI_X_POS, GUI_Y_POS, "Detected: %.20s (%d%%)", label, score);
//#endif
	assert(type == kTensorType_FLOAT32);
	int size = dims->data[2] * dims->data[1];
//	assert(size == 896); // (1, 896, 1)
	const float* data_f = reinterpret_cast<const float*>(data);
	bool hasFace = false;
	for (int i = 0; i < size; i++)
	{
//		reinterpret_cast<float*>(data)[i] =
//			(static_cast<int>(data[i]) - MODEL_INPUT_MEAN) / MODEL_INPUT_STD;
		if(data_f[i] > 0.7)
		{
			hasFace = true;
			break;
		};
	}
	if(hasFace) {
		PRINTF("There is a face" EOL);
	}
	else {
		PRINTF("There is no face" EOL);
	}
	// i have to know hasFace outside this func
    return kStatus_Success;
}
