################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../source/image/image_capture.c \
../source/image/image_conv.c \
../source/image/image_decode_raw.c \
../source/image/image_draw.c \
../source/image/image_resize_nearest.c 

C_DEPS += \
./source/image/image_capture.d \
./source/image/image_conv.d \
./source/image/image_decode_raw.d \
./source/image/image_draw.d \
./source/image/image_resize_nearest.d 

OBJS += \
./source/image/image_capture.o \
./source/image/image_conv.o \
./source/image/image_decode_raw.o \
./source/image/image_draw.o \
./source/image/image_resize_nearest.o 


# Each subdirectory must supply rules for building sources it contributes
source/image/%.o: ../source/image/%.c source/image/subdir.mk
	@echo 'Building file: $<'
	@echo 'Invoking: MCU C Compiler'
	arm-none-eabi-gcc -std=gnu99 -DCPU_MIMXRT1062DVL6A -DCPU_MIMXRT1062DVL6A_cm7 -DXIP_BOOT_HEADER_DCD_ENABLE=1 -DSKIP_SYSCLK_INIT -DDATA_SECTION_IS_CACHEABLE=1 -DSDK_DEBUGCONSOLE=1 -DXIP_EXTERNAL_FLASH=1 -DXIP_BOOT_HEADER_ENABLE=1 -DSDK_DEBUGCONSOLE_UART -DARM_MATH_CM7 -D__FPU_PRESENT=1 -DSDK_I2C_BASED_COMPONENT_USED=1 -DEIQ_GUI_PRINTF -DTF_LITE_STATIC_MEMORY -DCMSIS_NN -DMCUXPRESSO_SDK -DCR_INTEGER_PRINTF -D__MCUXPRESSO -D__USE_CMSIS -DNDEBUG -D__NEWLIB__ -I"C:\Users\jj910\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\source" -I"C:\Users\jj910\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\video" -I"C:\Users\jj910\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\drivers" -I"C:\Users\jj910\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\utilities" -I"C:\Users\jj910\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\source\video" -I"C:\Users\jj910\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\source\gprintf" -I"C:\Users\jj910\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\eiq\tensorflow-lite" -I"C:\Users\jj910\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\component\lists" -I"C:\Users\jj910\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\component\uart" -I"C:\Users\jj910\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\device" -I"C:\Users\jj910\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\xip" -I"C:\Users\jj910\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\CMSIS" -I"C:\Users\jj910\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\eiq\tensorflow-lite\third_party\flatbuffers\include" -I"C:\Users\jj910\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\eiq\tensorflow-lite\third_party\gemmlowp" -I"C:\Users\jj910\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\eiq\tensorflow-lite\third_party\ruy" -I"C:\Users\jj910\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\eiq\tensorflow-lite\third_party\cmsis" -I"C:\Users\jj910\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\eiq\tensorflow-lite\third_party\cmsis\CMSIS\NN\Include" -I"C:\Users\jj910\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\eiq\tensorflow-lite\third_party\cmsis\CMSIS\Core\Include" -I"C:\Users\jj910\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\eiq\tensorflow-lite\third_party\cmsis\CMSIS\DSP\Include" -I"C:\Users\jj910\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\source\image" -I"C:\Users\jj910\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\source\model" -I"C:\Users\jj910\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\board" -O3 -fno-common -g -Wall -Wno-strict-aliasing -c -ffunction-sections -fdata-sections -fmacro-prefix-map="$(<D)/"= -mcpu=cortex-m7 -mfpu=fpv5-d16 -mfloat-abi=hard -mthumb -D__NEWLIB__ -fstack-usage -specs=nano.specs -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.o)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


clean: clean-source-2f-image

clean-source-2f-image:
	-$(RM) ./source/image/image_capture.d ./source/image/image_capture.o ./source/image/image_conv.d ./source/image/image_conv.o ./source/image/image_decode_raw.d ./source/image/image_decode_raw.o ./source/image/image_draw.d ./source/image/image_draw.o ./source/image/image_resize_nearest.d ./source/image/image_resize_nearest.o

.PHONY: clean-source-2f-image

