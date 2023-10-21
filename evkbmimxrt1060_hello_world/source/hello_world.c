/*
 * Copyright (c) 2013 - 2015, Freescale Semiconductor, Inc.
 * Copyright 2016-2017 NXP
 * All rights reserved.
 *
 * SPDX-License-Identifier: BSD-3-Clause
 */

#include "fsl_device_registers.h"
#include "fsl_debug_console.h"
#include "pin_mux.h"
#include "clock_config.h"
#include "board.h"
#include "fsl_gpt.h"

/*******************************************************************************
 * Definitions
 ******************************************************************************/
#define GPT_IRQ_ID             GPT2_IRQn
#define EXAMPLE_GPT            GPT2
#define EXAMPLE_GPT_IRQHandler GPT2_IRQHandler

/* Get source clock for GPT driver (GPT prescaler = 0) */
#define EXAMPLE_GPT_CLK_FREQ CLOCK_GetFreq(kCLOCK_PerClk)

/*******************************************************************************
 * Prototypes
 ******************************************************************************/


/*******************************************************************************
 * Variables
 ******************************************************************************/

volatile bool gptIsrFlag = false;

/*******************************************************************************
 * Code
 ******************************************************************************/
void EXAMPLE_GPT_IRQHandler(void)
{
    /* Clear interrupt flag.*/
    GPT_ClearStatusFlags(EXAMPLE_GPT, kGPT_OutputCompare1Flag);

    gptIsrFlag = true;
    PRINTF("\r\n GPT interrupt is occurred !");
	gptIsrFlag = false;
/* Add for ARM errata 838869, affects Cortex-M4, Cortex-M4F, Cortex-M7, Cortex-M7F Store immediate overlapping
  exception return operation might vector to incorrect interrupt */
    SDK_ISR_EXIT_BARRIER;
}

/*!
 * @brief Main function
 */
int main(void)
{
    char ch;
    uint32_t gptFreq;
    gpt_config_t gptConfig;

    /* Init board hardware. */
    BOARD_ConfigMPU();
    BOARD_InitBootPins();
    BOARD_InitBootClocks();
    BOARD_InitDebugConsole();

    GPT_GetDefaultConfig(&gptConfig);

    /* Initialize GPT module */
	GPT_Init(EXAMPLE_GPT, &gptConfig);

	/* Divide GPT clock source frequency by 3 inside GPT module */
	GPT_SetClockDivider(EXAMPLE_GPT, 3);

	/* Get GPT clock frequency */
	gptFreq = EXAMPLE_GPT_CLK_FREQ/10;

	/* GPT frequency is divided by 3 inside module */
	gptFreq /= 3;

	/* Set both GPT modules to 1 second duration */
	GPT_SetOutputCompareValue(EXAMPLE_GPT, kGPT_OutputCompare_Channel1, gptFreq);

	/* Enable GPT Output Compare1 interrupt */
	GPT_EnableInterrupts(EXAMPLE_GPT, kGPT_OutputCompare1InterruptEnable);

	/* Enable at the Interrupt */
	EnableIRQ(GPT_IRQ_ID);

    /* Just enable the trace clock, leave coresight initialization to IDE debugger */
    SystemCoreClockUpdate();
    CLOCK_EnableClock(kCLOCK_Trace);

    PRINTF("hello world.\r\n");

    PRINTF("\r\nPress any key to start the example");
	GETCHAR();

	/* Start Timer */
	PRINTF("\r\nStarting GPT timer ...");
	GPT_StartTimer(EXAMPLE_GPT);

    while (1)
    {



        ch = GETCHAR();
		PUTCHAR(ch+1);
		if(ch == 'o'){
			PRINTF("Toggle fan\n");
			USER_FAN_TOGGLE();
		}
    }
}
