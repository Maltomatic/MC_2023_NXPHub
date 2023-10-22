################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../generated/images/_OIP_alpha_181x110.c \
../generated/images/_OIP_alpha_486x276.c \
../generated/images/_R_alpha_180x115.c \
../generated/images/_R_alpha_483x285.c \
../generated/images/_photo_6168027389217584763_y_alpha_176x122.c \
../generated/images/_photo_6168027389217584763_y_alpha_482x300.c \
../generated/images/images.c 

C_DEPS += \
./generated/images/_OIP_alpha_181x110.d \
./generated/images/_OIP_alpha_486x276.d \
./generated/images/_R_alpha_180x115.d \
./generated/images/_R_alpha_483x285.d \
./generated/images/_photo_6168027389217584763_y_alpha_176x122.d \
./generated/images/_photo_6168027389217584763_y_alpha_482x300.d \
./generated/images/images.d 

OBJS += \
./generated/images/_OIP_alpha_181x110.o \
./generated/images/_OIP_alpha_486x276.o \
./generated/images/_R_alpha_180x115.o \
./generated/images/_R_alpha_483x285.o \
./generated/images/_photo_6168027389217584763_y_alpha_176x122.o \
./generated/images/_photo_6168027389217584763_y_alpha_482x300.o \
./generated/images/images.o 


# Each subdirectory must supply rules for building sources it contributes
generated/images/%.o: ../generated/images/%.c generated/images/subdir.mk
	@echo 'Building file: $<'
	@echo 'Invoking: MCU C Compiler'
	arm-none-eabi-gcc -std=gnu99 -D__NEWLIB__ -DCPU_MIMXRT1062DVL6B -DCPU_MIMXRT1062DVL6B_cm7 -DXIP_BOOT_HEADER_DCD_ENABLE=1 -DSKIP_SYSCLK_INIT -DDATA_SECTION_IS_CACHEABLE=1 -DSDK_DEBUGCONSOLE=1 -DXIP_EXTERNAL_FLASH=1 -DXIP_BOOT_HEADER_ENABLE=1 -DFSL_SDK_DRIVER_QUICK_ACCESS_ENABLE=1 -DLV_CONF_INCLUDE_SIMPLE=1 -DMCUXPRESSO_SDK -DSDK_I2C_BASED_COMPONENT_USED=1 -DSERIAL_PORT_TYPE_UART=1 -DSDK_OS_FREE_RTOS -DCR_INTEGER_PRINTF -D__MCUXPRESSO -D__USE_CMSIS -DDEBUG -I"C:\Users\justi\Documents\MCUXpressoIDE_11.8.0_1165\practice\evkbmimxrt1060_lvgl_guider\source" -I"C:\Users\justi\Documents\MCUXpressoIDE_11.8.0_1165\practice\evkbmimxrt1060_lvgl_guider\drivers" -I"C:\Users\justi\Documents\MCUXpressoIDE_11.8.0_1165\practice\evkbmimxrt1060_lvgl_guider\touchpanel" -I"C:\Users\justi\Documents\MCUXpressoIDE_11.8.0_1165\practice\evkbmimxrt1060_lvgl_guider\video" -I"C:\Users\justi\Documents\MCUXpressoIDE_11.8.0_1165\practice\evkbmimxrt1060_lvgl_guider\lvgl\lvgl" -I"C:\Users\justi\Documents\MCUXpressoIDE_11.8.0_1165\practice\evkbmimxrt1060_lvgl_guider\lvgl\lvgl\src" -I"C:\Users\justi\Documents\MCUXpressoIDE_11.8.0_1165\practice\evkbmimxrt1060_lvgl_guider\lvgl" -I"C:\Users\justi\Documents\MCUXpressoIDE_11.8.0_1165\practice\evkbmimxrt1060_lvgl_guider\device" -I"C:\Users\justi\Documents\MCUXpressoIDE_11.8.0_1165\practice\evkbmimxrt1060_lvgl_guider\utilities" -I"C:\Users\justi\Documents\MCUXpressoIDE_11.8.0_1165\practice\evkbmimxrt1060_lvgl_guider\component\uart" -I"C:\Users\justi\Documents\MCUXpressoIDE_11.8.0_1165\practice\evkbmimxrt1060_lvgl_guider\component\serial_manager" -I"C:\Users\justi\Documents\MCUXpressoIDE_11.8.0_1165\practice\evkbmimxrt1060_lvgl_guider\component\lists" -I"C:\Users\justi\Documents\MCUXpressoIDE_11.8.0_1165\practice\evkbmimxrt1060_lvgl_guider\xip" -I"C:\Users\justi\Documents\MCUXpressoIDE_11.8.0_1165\practice\evkbmimxrt1060_lvgl_guider\freertos\freertos-kernel\include" -I"C:\Users\justi\Documents\MCUXpressoIDE_11.8.0_1165\practice\evkbmimxrt1060_lvgl_guider\freertos\freertos-kernel\portable\GCC\ARM_CM4F" -I"C:\Users\justi\Documents\MCUXpressoIDE_11.8.0_1165\practice\evkbmimxrt1060_lvgl_guider\CMSIS" -I"C:\Users\justi\Documents\MCUXpressoIDE_11.8.0_1165\practice\evkbmimxrt1060_lvgl_guider\board" -I"C:\Users\justi\Documents\MCUXpressoIDE_11.8.0_1165\practice\evkbmimxrt1060_lvgl_guider\generated" -I"C:\Users\justi\Documents\MCUXpressoIDE_11.8.0_1165\practice\evkbmimxrt1060_lvgl_guider\custom" -I"C:\Users\justi\Documents\MCUXpressoIDE_11.8.0_1165\practice\evkbmimxrt1060_lvgl_guider\generated\guider_customer_fonts" -I"C:\Users\justi\Documents\MCUXpressoIDE_11.8.0_1165\practice\evkbmimxrt1060_lvgl_guider\generated\guider_fonts" -I"C:\Users\justi\Documents\MCUXpressoIDE_11.8.0_1165\practice\evkbmimxrt1060_lvgl_guider\evkbmimxrt1060\lvgl_examples\lvgl_guider" -O0 -fno-common -g3 -Wall -c -ffunction-sections -fdata-sections -ffreestanding -fno-builtin -Wno-format -fmerge-constants -fmacro-prefix-map="$(<D)/"= -mcpu=cortex-m7 -mfpu=fpv5-d16 -mfloat-abi=hard -mthumb -D__NEWLIB__ -fstack-usage -specs=nano.specs -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.o)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


clean: clean-generated-2f-images

clean-generated-2f-images:
	-$(RM) ./generated/images/_OIP_alpha_181x110.d ./generated/images/_OIP_alpha_181x110.o ./generated/images/_OIP_alpha_486x276.d ./generated/images/_OIP_alpha_486x276.o ./generated/images/_R_alpha_180x115.d ./generated/images/_R_alpha_180x115.o ./generated/images/_R_alpha_483x285.d ./generated/images/_R_alpha_483x285.o ./generated/images/_photo_6168027389217584763_y_alpha_176x122.d ./generated/images/_photo_6168027389217584763_y_alpha_176x122.o ./generated/images/_photo_6168027389217584763_y_alpha_482x300.d ./generated/images/_photo_6168027389217584763_y_alpha_482x300.o ./generated/images/images.d ./generated/images/images.o

.PHONY: clean-generated-2f-images

