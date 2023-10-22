################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
CPP_SRCS += \
../eiq/tensorflow-lite/tensorflow/lite/micro/all_ops_resolver.cpp \
../eiq/tensorflow-lite/tensorflow/lite/micro/debug_log.cpp \
../eiq/tensorflow-lite/tensorflow/lite/micro/fake_micro_context.cpp \
../eiq/tensorflow-lite/tensorflow/lite/micro/flatbuffer_utils.cpp \
../eiq/tensorflow-lite/tensorflow/lite/micro/memory_helpers.cpp \
../eiq/tensorflow-lite/tensorflow/lite/micro/micro_allocation_info.cpp \
../eiq/tensorflow-lite/tensorflow/lite/micro/micro_allocator.cpp \
../eiq/tensorflow-lite/tensorflow/lite/micro/micro_context.cpp \
../eiq/tensorflow-lite/tensorflow/lite/micro/micro_error_reporter.cpp \
../eiq/tensorflow-lite/tensorflow/lite/micro/micro_graph.cpp \
../eiq/tensorflow-lite/tensorflow/lite/micro/micro_interpreter.cpp \
../eiq/tensorflow-lite/tensorflow/lite/micro/micro_log.cpp \
../eiq/tensorflow-lite/tensorflow/lite/micro/micro_profiler.cpp \
../eiq/tensorflow-lite/tensorflow/lite/micro/micro_resource_variable.cpp \
../eiq/tensorflow-lite/tensorflow/lite/micro/micro_string.cpp \
../eiq/tensorflow-lite/tensorflow/lite/micro/micro_time.cpp \
../eiq/tensorflow-lite/tensorflow/lite/micro/micro_utils.cpp \
../eiq/tensorflow-lite/tensorflow/lite/micro/recording_micro_allocator.cpp 

CPP_DEPS += \
./eiq/tensorflow-lite/tensorflow/lite/micro/all_ops_resolver.d \
./eiq/tensorflow-lite/tensorflow/lite/micro/debug_log.d \
./eiq/tensorflow-lite/tensorflow/lite/micro/fake_micro_context.d \
./eiq/tensorflow-lite/tensorflow/lite/micro/flatbuffer_utils.d \
./eiq/tensorflow-lite/tensorflow/lite/micro/memory_helpers.d \
./eiq/tensorflow-lite/tensorflow/lite/micro/micro_allocation_info.d \
./eiq/tensorflow-lite/tensorflow/lite/micro/micro_allocator.d \
./eiq/tensorflow-lite/tensorflow/lite/micro/micro_context.d \
./eiq/tensorflow-lite/tensorflow/lite/micro/micro_error_reporter.d \
./eiq/tensorflow-lite/tensorflow/lite/micro/micro_graph.d \
./eiq/tensorflow-lite/tensorflow/lite/micro/micro_interpreter.d \
./eiq/tensorflow-lite/tensorflow/lite/micro/micro_log.d \
./eiq/tensorflow-lite/tensorflow/lite/micro/micro_profiler.d \
./eiq/tensorflow-lite/tensorflow/lite/micro/micro_resource_variable.d \
./eiq/tensorflow-lite/tensorflow/lite/micro/micro_string.d \
./eiq/tensorflow-lite/tensorflow/lite/micro/micro_time.d \
./eiq/tensorflow-lite/tensorflow/lite/micro/micro_utils.d \
./eiq/tensorflow-lite/tensorflow/lite/micro/recording_micro_allocator.d 

OBJS += \
./eiq/tensorflow-lite/tensorflow/lite/micro/all_ops_resolver.o \
./eiq/tensorflow-lite/tensorflow/lite/micro/debug_log.o \
./eiq/tensorflow-lite/tensorflow/lite/micro/fake_micro_context.o \
./eiq/tensorflow-lite/tensorflow/lite/micro/flatbuffer_utils.o \
./eiq/tensorflow-lite/tensorflow/lite/micro/memory_helpers.o \
./eiq/tensorflow-lite/tensorflow/lite/micro/micro_allocation_info.o \
./eiq/tensorflow-lite/tensorflow/lite/micro/micro_allocator.o \
./eiq/tensorflow-lite/tensorflow/lite/micro/micro_context.o \
./eiq/tensorflow-lite/tensorflow/lite/micro/micro_error_reporter.o \
./eiq/tensorflow-lite/tensorflow/lite/micro/micro_graph.o \
./eiq/tensorflow-lite/tensorflow/lite/micro/micro_interpreter.o \
./eiq/tensorflow-lite/tensorflow/lite/micro/micro_log.o \
./eiq/tensorflow-lite/tensorflow/lite/micro/micro_profiler.o \
./eiq/tensorflow-lite/tensorflow/lite/micro/micro_resource_variable.o \
./eiq/tensorflow-lite/tensorflow/lite/micro/micro_string.o \
./eiq/tensorflow-lite/tensorflow/lite/micro/micro_time.o \
./eiq/tensorflow-lite/tensorflow/lite/micro/micro_utils.o \
./eiq/tensorflow-lite/tensorflow/lite/micro/recording_micro_allocator.o 


# Each subdirectory must supply rules for building sources it contributes
eiq/tensorflow-lite/tensorflow/lite/micro/%.o: ../eiq/tensorflow-lite/tensorflow/lite/micro/%.cpp eiq/tensorflow-lite/tensorflow/lite/micro/subdir.mk
	@echo 'Building file: $<'
	@echo 'Invoking: MCU C++ Compiler'
	arm-none-eabi-c++ -std=gnu++11 -DCPU_MIMXRT1062DVL6A -DCPU_MIMXRT1062DVL6A_cm7 -DSDK_DEBUGCONSOLE_UART -DARM_MATH_CM7 -D__FPU_PRESENT=1 -DSDK_I2C_BASED_COMPONENT_USED=1 -DEIQ_GUI_PRINTF -DTF_LITE_STATIC_MEMORY -DCMSIS_NN -DMCUXPRESSO_SDK -DSDK_DEBUGCONSOLE=1 -D__MCUXPRESSO -D__USE_CMSIS -DDEBUG -D__NEWLIB__ -I"C:\Users\JERRY\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\source" -I"C:\Users\JERRY\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\video" -I"C:\Users\JERRY\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\drivers" -I"C:\Users\JERRY\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\utilities" -I"C:\Users\JERRY\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\source\video" -I"C:\Users\JERRY\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\source\gprintf" -I"C:\Users\JERRY\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\eiq\tensorflow-lite" -I"C:\Users\JERRY\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\component\lists" -I"C:\Users\JERRY\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\component\uart" -I"C:\Users\JERRY\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\device" -I"C:\Users\JERRY\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\xip" -I"C:\Users\JERRY\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\CMSIS" -I"C:\Users\JERRY\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\eiq\tensorflow-lite\third_party\flatbuffers\include" -I"C:\Users\JERRY\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\eiq\tensorflow-lite\third_party\gemmlowp" -I"C:\Users\JERRY\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\eiq\tensorflow-lite\third_party\ruy" -I"C:\Users\JERRY\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\eiq\tensorflow-lite\third_party\cmsis" -I"C:\Users\JERRY\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\eiq\tensorflow-lite\third_party\cmsis\CMSIS\NN\Include" -I"C:\Users\JERRY\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\eiq\tensorflow-lite\third_party\cmsis\CMSIS\Core\Include" -I"C:\Users\JERRY\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\eiq\tensorflow-lite\third_party\cmsis\CMSIS\DSP\Include" -I"C:\Users\JERRY\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\source\image" -I"C:\Users\JERRY\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\source\model" -I"C:\Users\JERRY\Documents\MCUXpressoIDE_11.8.0_1165\workspace\evkmimxrt1060_tflm_label_image\board" -O0 -fno-common -g3 -Wall -fno-rtti -fno-exceptions -Wno-sign-compare -Wno-strict-aliasing -c -ffunction-sections -fdata-sections -fmerge-constants -fmacro-prefix-map="$(<D)/"= -mcpu=cortex-m7 -mfpu=fpv5-d16 -mfloat-abi=hard -mthumb -D__NEWLIB__ -fstack-usage -specs=nano.specs -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.o)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


clean: clean-eiq-2f-tensorflow-2d-lite-2f-tensorflow-2f-lite-2f-micro

clean-eiq-2f-tensorflow-2d-lite-2f-tensorflow-2f-lite-2f-micro:
	-$(RM) ./eiq/tensorflow-lite/tensorflow/lite/micro/all_ops_resolver.d ./eiq/tensorflow-lite/tensorflow/lite/micro/all_ops_resolver.o ./eiq/tensorflow-lite/tensorflow/lite/micro/debug_log.d ./eiq/tensorflow-lite/tensorflow/lite/micro/debug_log.o ./eiq/tensorflow-lite/tensorflow/lite/micro/fake_micro_context.d ./eiq/tensorflow-lite/tensorflow/lite/micro/fake_micro_context.o ./eiq/tensorflow-lite/tensorflow/lite/micro/flatbuffer_utils.d ./eiq/tensorflow-lite/tensorflow/lite/micro/flatbuffer_utils.o ./eiq/tensorflow-lite/tensorflow/lite/micro/memory_helpers.d ./eiq/tensorflow-lite/tensorflow/lite/micro/memory_helpers.o ./eiq/tensorflow-lite/tensorflow/lite/micro/micro_allocation_info.d ./eiq/tensorflow-lite/tensorflow/lite/micro/micro_allocation_info.o ./eiq/tensorflow-lite/tensorflow/lite/micro/micro_allocator.d ./eiq/tensorflow-lite/tensorflow/lite/micro/micro_allocator.o ./eiq/tensorflow-lite/tensorflow/lite/micro/micro_context.d ./eiq/tensorflow-lite/tensorflow/lite/micro/micro_context.o ./eiq/tensorflow-lite/tensorflow/lite/micro/micro_error_reporter.d ./eiq/tensorflow-lite/tensorflow/lite/micro/micro_error_reporter.o ./eiq/tensorflow-lite/tensorflow/lite/micro/micro_graph.d ./eiq/tensorflow-lite/tensorflow/lite/micro/micro_graph.o ./eiq/tensorflow-lite/tensorflow/lite/micro/micro_interpreter.d ./eiq/tensorflow-lite/tensorflow/lite/micro/micro_interpreter.o ./eiq/tensorflow-lite/tensorflow/lite/micro/micro_log.d ./eiq/tensorflow-lite/tensorflow/lite/micro/micro_log.o ./eiq/tensorflow-lite/tensorflow/lite/micro/micro_profiler.d ./eiq/tensorflow-lite/tensorflow/lite/micro/micro_profiler.o ./eiq/tensorflow-lite/tensorflow/lite/micro/micro_resource_variable.d ./eiq/tensorflow-lite/tensorflow/lite/micro/micro_resource_variable.o ./eiq/tensorflow-lite/tensorflow/lite/micro/micro_string.d ./eiq/tensorflow-lite/tensorflow/lite/micro/micro_string.o ./eiq/tensorflow-lite/tensorflow/lite/micro/micro_time.d ./eiq/tensorflow-lite/tensorflow/lite/micro/micro_time.o ./eiq/tensorflow-lite/tensorflow/lite/micro/micro_utils.d ./eiq/tensorflow-lite/tensorflow/lite/micro/micro_utils.o ./eiq/tensorflow-lite/tensorflow/lite/micro/recording_micro_allocator.d ./eiq/tensorflow-lite/tensorflow/lite/micro/recording_micro_allocator.o

.PHONY: clean-eiq-2f-tensorflow-2d-lite-2f-tensorflow-2f-lite-2f-micro

