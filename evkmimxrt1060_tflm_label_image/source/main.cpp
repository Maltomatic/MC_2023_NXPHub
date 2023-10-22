/*
 * Copyright 2020-2022 NXP
 * All rights reserved.
 *
 * SPDX-License-Identifier: BSD-3-Clause
 */

#include "board_init.h"
#include "demo_config.h"
#include "demo_info.h"
#include "fsl_debug_console.h"
#include "image.h"
#include "image_utils.h"
#include "model.h"
#include "output_postproc.h"
#include "timer.h"

int main(void)
{
    BOARD_Init();
    TIMER_Init();

//    DEMO_PrintInfo();

    if (MODEL_Init() != kStatus_Success)
    {
        PRINTF("Failed initializing model" EOL);
        for (;;) {}
    }

    tensor_dims_t inputDims;
    tensor_type_t inputType;
    uint8_t* inputData = MODEL_GetInputTensorData(&inputDims, &inputType);

    tensor_dims_t outputDims;
    tensor_type_t outputType;
    uint8_t* outputData = MODEL_GetOutputTensorData(&outputDims, &outputType);
    PRINTF("Recognizing faces..." EOL);
    PRINTF("%d %d %d %d" EOL, inputDims.data[0], inputDims.data[1], inputDims.data[2], inputDims.data[3]);
    PRINTF("%d %d %d" EOL, outputDims.data[0], outputDims.data[1], outputDims.data[2]);
    switch (inputType)
    {
        case kTensorType_FLOAT32:
            PRINTF("kTensorType_FLOAT32" EOL);
            break;
        case kTensorType_UINT8:
        	PRINTF("kTensorType_UINT8" EOL);
            break;
        case kTensorType_INT8:
        	PRINTF("kTensorType_INT8" EOL);
            break;
        default:
        	PRINTF("Unknown input tensor data type" EOL);
    };
    while (1)
    {
        /* Expected tensor dimensions: [batches, height, width, channels] */
        if (IMAGE_GetImage(inputData, inputDims.data[2], inputDims.data[1], inputDims.data[3]) != kStatus_Success)
        {
            PRINTF("Failed retrieving input image" EOL);
            for (;;) {}
        }

        MODEL_ConvertInput(inputData, &inputDims, inputType);

        auto startTime = TIMER_GetTimeInUS();
        MODEL_RunInference();
        auto endTime = TIMER_GetTimeInUS();

        MODEL_ProcessOutput(outputData, &outputDims, outputType, endTime - startTime);
    }
}
