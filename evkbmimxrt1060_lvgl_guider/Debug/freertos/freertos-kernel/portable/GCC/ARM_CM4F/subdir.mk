################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../freertos/freertos-kernel/portable/GCC/ARM_CM4F/port.c 

C_DEPS += \
./freertos/freertos-kernel/portable/GCC/ARM_CM4F/port.d 

OBJS += \
./freertos/freertos-kernel/portable/GCC/ARM_CM4F/port.o 


# Each subdirectory must supply rules for building sources it contributes
freertos/freertos-kernel/portable/GCC/ARM_CM4F/%.o: ../freertos/freertos-kernel/portable/GCC/ARM_CM4F/%.c freertos/freertos-kernel/portable/GCC/ARM_CM4F/subdir.mk
	@echo 'Building file: $<'
	@echo 'Invoking: MCU C Compiler'
	arm-none-eabi-gcc -std=gnu99 -D__NEWLIB__ -DCPU_MIMXRT1062DVL6B -DCPU_MIMXRT1062DVL6B_cm7 -DXIP_BOOT_HEADER_DCD_ENABLE=1 -DSKIP_SYSCLK_INIT -DDATA_SECTION_IS_CACHEABLE=1 -DSDK_DEBUGCONSOLE=1 -DXIP_EXTERNAL_FLASH=1 -DXIP_BOOT_HEADER_ENABLE=1 -DFSL_SDK_DRIVER_QUICK_ACCESS_ENABLE=1 -DLV_CONF_INCLUDE_SIMPLE=1 -DMCUXPRESSO_SDK -DSDK_I2C_BASED_COMPONENT_USED=1 -DSERIAL_PORT_TYPE_UART=1 -DSDK_OS_FREE_RTOS -DCR_INTEGER_PRINTF -D__MCUXPRESSO -D__USE_CMSIS -DDEBUG -I"C:\Users\justi\Documents\MCUXpressoIDE_11.8.0_1165\practice\evkbmimxrt1060_lvgl_guider\source" -I"C:\Users\justi\Documents\MCUXpressoIDE_11.8.0_1165\practice\evkbmimxrt1060_lvgl_guider\drivers" -I"C:\Users\justi\Documents\MCUXpressoIDE_11.8.0_1165\practice\evkbmimxrt1060_lvgl_guider\touchpanel" -I"C:\Users\justi\Documents\MCUXpressoIDE_11.8.0_1165\practice\evkbmimxrt1060_lvgl_guider\video" -I"C:\Users\justi\Documents\MCUXpressoIDE_11.8.0_1165\practice\evkbmimxrt1060_lvgl_guider\lvgl\lvgl" -I"C:\Users\justi\Documents\MCUXpressoIDE_11.8.0_1165\practice\evkbmimxrt1060_lvgl_guider\lvgl\lvgl\src" -I"C:\Users\justi\Documents\MCUXpressoIDE_11.8.0_1165\practice\evkbmimxrt1060_lvgl_guider\lvgl" -I"C:\Users\justi\Documents\MCUXpressoIDE_11.8.0_1165\practice\evkbmimxrt1060_lvgl_guider\device" -I"C:\Users\justi\Documents\MCUXpressoIDE_11.8.0_1165\practice\evkbmimxrt1060_lvgl_guider\utilities" -I"C:\Users\justi\Documents\MCUXpressoIDE_11.8.0_1165\practice\evkbmimxrt1060_lvgl_guider\component\uart" -I"C:\Users\justi\Documents\MCUXpressoIDE_11.8.0_1165\practice\evkbmimxrt1060_lvgl_guider\component\serial_manager" -I"C:\Users\justi\Documents\MCUXpressoIDE_11.8.0_1165\practice\evkbmimxrt1060_lvgl_guider\component\lists" -I"C:\Users\justi\Documents\MCUXpressoIDE_11.8.0_1165\practice\evkbmimxrt1060_lvgl_guider\xip" -I"C:\Users\justi\Documents\MCUXpressoIDE_11.8.0_1165\practice\evkbmimxrt1060_lvgl_guider\freertos\freertos-kernel\include" -I"C:\Users\justi\Documents\MCUXpressoIDE_11.8.0_1165\practice\evkbmimxrt1060_lvgl_guider\freertos\freertos-kernel\portable\GCC\ARM_CM4F" -I"C:\Users\justi\Documents\MCUXpressoIDE_11.8.0_1165\practice\evkbmimxrt1060_lvgl_guider\CMSIS" -I"C:\Users\justi\Documents\MCUXpressoIDE_11.8.0_1165\practice\evkbmimxrt1060_lvgl_guider\board" -I"C:\Users\justi\Documents\MCUXpressoIDE_11.8.0_1165\practice\evkbmimxrt1060_lvgl_guider\generated" -I"C:\Users\justi\Documents\MCUXpressoIDE_11.8.0_1165\practice\evkbmimxrt1060_lvgl_guider\custom" -I"C:\Users\justi\Documents\MCUXpressoIDE_11.8.0_1165\practice\evkbmimxrt1060_lvgl_guider\generated\guider_customer_fonts" -I"C:\Users\justi\Documents\MCUXpressoIDE_11.8.0_1165\practice\evkbmimxrt1060_lvgl_guider\generated\guider_fonts" -I"C:\Users\justi\Documents\MCUXpressoIDE_11.8.0_1165\practice\evkbmimxrt1060_lvgl_guider\evkbmimxrt1060\lvgl_examples\lvgl_guider" -O0 -fno-common -g3 -Wall -c -ffunction-sections -fdata-sections -ffreestanding -fno-builtin -Wno-format -fmerge-constants -fmacro-prefix-map="$(<D)/"= -mcpu=cortex-m7 -mfpu=fpv5-d16 -mfloat-abi=hard -mthumb -D__NEWLIB__ -fstack-usage -specs=nano.specs -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.o)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


clean: clean-freertos-2f-freertos-2d-kernel-2f-portable-2f-GCC-2f-ARM_CM4F

clean-freertos-2f-freertos-2d-kernel-2f-portable-2f-GCC-2f-ARM_CM4F:
	-$(RM) ./freertos/freertos-kernel/portable/GCC/ARM_CM4F/port.d ./freertos/freertos-kernel/portable/GCC/ARM_CM4F/port.o

.PHONY: clean-freertos-2f-freertos-2d-kernel-2f-portable-2f-GCC-2f-ARM_CM4F

