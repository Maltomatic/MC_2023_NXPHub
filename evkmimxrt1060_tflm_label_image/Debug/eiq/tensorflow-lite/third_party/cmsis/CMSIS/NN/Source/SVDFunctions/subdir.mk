################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../eiq/tensorflow-lite/third_party/cmsis/CMSIS/NN/Source/SVDFunctions/arm_svdf_s8.c \
../eiq/tensorflow-lite/third_party/cmsis/CMSIS/NN/Source/SVDFunctions/arm_svdf_state_s16_s8.c 

C_DEPS += \
./eiq/tensorflow-lite/third_party/cmsis/CMSIS/NN/Source/SVDFunctions/arm_svdf_s8.d \
./eiq/tensorflow-lite/third_party/cmsis/CMSIS/NN/Source/SVDFunctions/arm_svdf_state_s16_s8.d 

OBJS += \
./eiq/tensorflow-lite/third_party/cmsis/CMSIS/NN/Source/SVDFunctions/arm_svdf_s8.o \
./eiq/tensorflow-lite/third_party/cmsis/CMSIS/NN/Source/SVDFunctions/arm_svdf_state_s16_s8.o 


# Each subdirectory must supply rules for building sources it contributes
eiq/tensorflow-lite/third_party/cmsis/CMSIS/NN/Source/SVDFunctions/%.o: ../eiq/tensorflow-lite/third_party/cmsis/CMSIS/NN/Source/SVDFunctions/%.c eiq/tensorflow-lite/third_party/cmsis/CMSIS/NN/Source/SVDFunctions/subdir.mk
	@echo 'Building file: $<'
	@echo 'Invoking: MCU C Compiler'
	arm-none-eabi-gcc -std=gnu99 -D__NEWLIB__ -DCPU_MIMXRT1062DVL6A -DCPU_MIMXRT1062DVL6A_cm7 -DXIP_BOOT_HEADER_DCD_ENABLE=1 -DSKIP_SYSCLK_INIT -DDATA_SECTION_IS_CACHEABLE=1 -DSDK_DEBUGCONSOLE=1 -DXIP_EXTERNAL_FLASH=1 -DXIP_BOOT_HEADER_ENABLE=1 -DSDK_DEBUGCONSOLE_UART -DARM_MATH_CM7 -D__FPU_PRESENT=1 -DSDK_I2C_BASED_COMPONENT_USED=1 -DEIQ_GUI_PRINTF -DTF_LITE_STATIC_MEMORY -DCMSIS_NN -DMCUXPRESSO_SDK -DPRINTF_FLOAT_ENABLE=1 -D__MCUXPRESSO -D__USE_CMSIS -DDEBUG -I"C:\Users\JERRY\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\source" -I"C:\Users\JERRY\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\video" -I"C:\Users\JERRY\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\drivers" -I"C:\Users\JERRY\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\utilities" -I"C:\Users\JERRY\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\source\video" -I"C:\Users\JERRY\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\source\gprintf" -I"C:\Users\JERRY\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\eiq\tensorflow-lite" -I"C:\Users\JERRY\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\component\lists" -I"C:\Users\JERRY\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\component\uart" -I"C:\Users\JERRY\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\device" -I"C:\Users\JERRY\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\xip" -I"C:\Users\JERRY\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\CMSIS" -I"C:\Users\JERRY\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\eiq\tensorflow-lite\third_party\flatbuffers\include" -I"C:\Users\JERRY\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\eiq\tensorflow-lite\third_party\gemmlowp" -I"C:\Users\JERRY\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\eiq\tensorflow-lite\third_party\ruy" -I"C:\Users\JERRY\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\eiq\tensorflow-lite\third_party\cmsis" -I"C:\Users\JERRY\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\eiq\tensorflow-lite\third_party\cmsis\CMSIS\NN\Include" -I"C:\Users\JERRY\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\eiq\tensorflow-lite\third_party\cmsis\CMSIS\Core\Include" -I"C:\Users\JERRY\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\eiq\tensorflow-lite\third_party\cmsis\CMSIS\DSP\Include" -I"C:\Users\JERRY\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\source\image" -I"C:\Users\JERRY\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\source\model" -I"C:\Users\JERRY\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\board" -O0 -fno-common -g3 -Wall -Wno-strict-aliasing -c -ffunction-sections -fdata-sections -fmerge-constants -fmacro-prefix-map="$(<D)/"= -mcpu=cortex-m7 -mfpu=fpv5-d16 -mfloat-abi=hard -mthumb -D__NEWLIB__ -fstack-usage -specs=nano.specs -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.o)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


clean: clean-eiq-2f-tensorflow-2d-lite-2f-third_party-2f-cmsis-2f-CMSIS-2f-NN-2f-Source-2f-SVDFunctions

clean-eiq-2f-tensorflow-2d-lite-2f-third_party-2f-cmsis-2f-CMSIS-2f-NN-2f-Source-2f-SVDFunctions:
	-$(RM) ./eiq/tensorflow-lite/third_party/cmsis/CMSIS/NN/Source/SVDFunctions/arm_svdf_s8.d ./eiq/tensorflow-lite/third_party/cmsis/CMSIS/NN/Source/SVDFunctions/arm_svdf_s8.o ./eiq/tensorflow-lite/third_party/cmsis/CMSIS/NN/Source/SVDFunctions/arm_svdf_state_s16_s8.d ./eiq/tensorflow-lite/third_party/cmsis/CMSIS/NN/Source/SVDFunctions/arm_svdf_state_s16_s8.o

.PHONY: clean-eiq-2f-tensorflow-2d-lite-2f-third_party-2f-cmsis-2f-CMSIS-2f-NN-2f-Source-2f-SVDFunctions

