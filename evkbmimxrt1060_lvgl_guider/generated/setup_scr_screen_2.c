/*
* Copyright 2023 NXP
* NXP Confidential and Proprietary. This software is owned or controlled by NXP and may only be used strictly in
* accordance with the applicable license terms. By expressly accepting such terms or by downloading, installing,
* activating and/or otherwise using the software, you are agreeing that you have read, and that you agree to
* comply with and are bound by, such license terms.  If you do not agree to be bound by the applicable license
* terms, then you may not retain, install, activate or otherwise use the software.
*/

#include "lvgl.h"
#include <stdio.h>
#include "gui_guider.h"
#include "events_init.h"
#include "widgets_init.h"
#include "custom.h"


void setup_scr_screen_2(lv_ui *ui)
{
	//Write codes screen_2
	ui->screen_2 = lv_obj_create(NULL);
	lv_obj_set_size(ui->screen_2, 480, 272);
	lv_obj_set_scrollbar_mode(ui->screen_2, LV_SCROLLBAR_MODE_OFF);

	//Write style for screen_2, Part: LV_PART_MAIN, State: LV_STATE_DEFAULT.
	lv_obj_set_style_bg_opa(ui->screen_2, 0, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes screen_2_img_1
	ui->screen_2_img_1 = lv_img_create(ui->screen_2);
	lv_obj_add_flag(ui->screen_2_img_1, LV_OBJ_FLAG_CLICKABLE);
	lv_img_set_pivot(ui->screen_2_img_1, 50,50);
	lv_img_set_angle(ui->screen_2_img_1, 0);
	lv_obj_set_pos(ui->screen_2_img_1, 25, 16);
	lv_obj_set_size(ui->screen_2_img_1, 433, 102);
	lv_obj_set_scrollbar_mode(ui->screen_2_img_1, LV_SCROLLBAR_MODE_OFF);

	//Write style for screen_2_img_1, Part: LV_PART_MAIN, State: LV_STATE_DEFAULT.
	lv_obj_set_style_img_opa(ui->screen_2_img_1, 255, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes screen_2_back
	ui->screen_2_back = lv_btn_create(ui->screen_2);
	ui->screen_2_back_label = lv_label_create(ui->screen_2_back);
	lv_label_set_text(ui->screen_2_back_label, "Back");
	lv_label_set_long_mode(ui->screen_2_back_label, LV_LABEL_LONG_WRAP);
	lv_obj_align(ui->screen_2_back_label, LV_ALIGN_CENTER, 0, 0);
	lv_obj_set_style_pad_all(ui->screen_2_back, 0, LV_STATE_DEFAULT);
	lv_obj_set_pos(ui->screen_2_back, 25, 16);
	lv_obj_set_size(ui->screen_2_back, 100, 36);
	lv_obj_set_scrollbar_mode(ui->screen_2_back, LV_SCROLLBAR_MODE_OFF);

	//Write style for screen_2_back, Part: LV_PART_MAIN, State: LV_STATE_DEFAULT.
	lv_obj_set_style_bg_opa(ui->screen_2_back, 255, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_color(ui->screen_2_back, lv_color_hex(0x2195f6), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_border_width(ui->screen_2_back, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_radius(ui->screen_2_back, 5, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_shadow_width(ui->screen_2_back, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_color(ui->screen_2_back, lv_color_hex(0xffffff), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_font(ui->screen_2_back, &lv_font_montserratMedium_16, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_align(ui->screen_2_back, LV_TEXT_ALIGN_CENTER, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes screen_2_Temp
	ui->screen_2_Temp = lv_label_create(ui->screen_2);
	lv_label_set_text(ui->screen_2_Temp, "0");
	lv_label_set_long_mode(ui->screen_2_Temp, LV_LABEL_LONG_WRAP);
	lv_obj_set_pos(ui->screen_2_Temp, 62, 146);
	lv_obj_set_size(ui->screen_2_Temp, 100, 32);
	lv_obj_set_scrollbar_mode(ui->screen_2_Temp, LV_SCROLLBAR_MODE_OFF);

	//Write style for screen_2_Temp, Part: LV_PART_MAIN, State: LV_STATE_DEFAULT.
	lv_obj_set_style_border_width(ui->screen_2_Temp, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_radius(ui->screen_2_Temp, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_color(ui->screen_2_Temp, lv_color_hex(0x000000), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_font(ui->screen_2_Temp, &lv_font_montserratMedium_16, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_letter_space(ui->screen_2_Temp, 2, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_line_space(ui->screen_2_Temp, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_align(ui->screen_2_Temp, LV_TEXT_ALIGN_CENTER, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_opa(ui->screen_2_Temp, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_top(ui->screen_2_Temp, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_right(ui->screen_2_Temp, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_bottom(ui->screen_2_Temp, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_left(ui->screen_2_Temp, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_shadow_width(ui->screen_2_Temp, 0, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes screen_2_T_plus
	ui->screen_2_T_plus = lv_btn_create(ui->screen_2);
	ui->screen_2_T_plus_label = lv_label_create(ui->screen_2_T_plus);
	lv_label_set_text(ui->screen_2_T_plus_label, "+");
	lv_label_set_long_mode(ui->screen_2_T_plus_label, LV_LABEL_LONG_WRAP);
	lv_obj_align(ui->screen_2_T_plus_label, LV_ALIGN_CENTER, 0, 0);
	lv_obj_set_style_pad_all(ui->screen_2_T_plus, 0, LV_STATE_DEFAULT);
	lv_obj_set_pos(ui->screen_2_T_plus, 10, 119);
	lv_obj_set_size(ui->screen_2_T_plus, 41, 35);
	lv_obj_set_scrollbar_mode(ui->screen_2_T_plus, LV_SCROLLBAR_MODE_OFF);

	//Write style for screen_2_T_plus, Part: LV_PART_MAIN, State: LV_STATE_DEFAULT.
	lv_obj_set_style_bg_opa(ui->screen_2_T_plus, 255, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_color(ui->screen_2_T_plus, lv_color_hex(0xD01FBB), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_border_width(ui->screen_2_T_plus, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_radius(ui->screen_2_T_plus, 5, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_shadow_width(ui->screen_2_T_plus, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_color(ui->screen_2_T_plus, lv_color_hex(0xffffff), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_font(ui->screen_2_T_plus, &lv_font_Alatsi_Regular_33, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_align(ui->screen_2_T_plus, LV_TEXT_ALIGN_CENTER, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes screen_2_T_minus
	ui->screen_2_T_minus = lv_btn_create(ui->screen_2);
	ui->screen_2_T_minus_label = lv_label_create(ui->screen_2_T_minus);
	lv_label_set_text(ui->screen_2_T_minus_label, "-");
	lv_label_set_long_mode(ui->screen_2_T_minus_label, LV_LABEL_LONG_WRAP);
	lv_obj_align(ui->screen_2_T_minus_label, LV_ALIGN_CENTER, 0, 0);
	lv_obj_set_style_pad_all(ui->screen_2_T_minus, 0, LV_STATE_DEFAULT);
	lv_obj_set_pos(ui->screen_2_T_minus, 10, 167);
	lv_obj_set_size(ui->screen_2_T_minus, 41, 35);
	lv_obj_set_scrollbar_mode(ui->screen_2_T_minus, LV_SCROLLBAR_MODE_OFF);

	//Write style for screen_2_T_minus, Part: LV_PART_MAIN, State: LV_STATE_DEFAULT.
	lv_obj_set_style_bg_opa(ui->screen_2_T_minus, 255, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_color(ui->screen_2_T_minus, lv_color_hex(0xD01FBB), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_border_width(ui->screen_2_T_minus, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_radius(ui->screen_2_T_minus, 5, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_shadow_width(ui->screen_2_T_minus, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_color(ui->screen_2_T_minus, lv_color_hex(0xffffff), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_font(ui->screen_2_T_minus, &lv_font_Alatsi_Regular_33, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_align(ui->screen_2_T_minus, LV_TEXT_ALIGN_CENTER, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes screen_2_H_minus
	ui->screen_2_H_minus = lv_btn_create(ui->screen_2);
	ui->screen_2_H_minus_label = lv_label_create(ui->screen_2_H_minus);
	lv_label_set_text(ui->screen_2_H_minus_label, "-");
	lv_label_set_long_mode(ui->screen_2_H_minus_label, LV_LABEL_LONG_WRAP);
	lv_obj_align(ui->screen_2_H_minus_label, LV_ALIGN_CENTER, 0, 0);
	lv_obj_set_style_pad_all(ui->screen_2_H_minus, 0, LV_STATE_DEFAULT);
	lv_obj_set_pos(ui->screen_2_H_minus, 220, 167);
	lv_obj_set_size(ui->screen_2_H_minus, 41, 35);
	lv_obj_set_scrollbar_mode(ui->screen_2_H_minus, LV_SCROLLBAR_MODE_OFF);

	//Write style for screen_2_H_minus, Part: LV_PART_MAIN, State: LV_STATE_DEFAULT.
	lv_obj_set_style_bg_opa(ui->screen_2_H_minus, 255, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_color(ui->screen_2_H_minus, lv_color_hex(0x00bdff), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_border_width(ui->screen_2_H_minus, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_radius(ui->screen_2_H_minus, 5, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_shadow_width(ui->screen_2_H_minus, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_color(ui->screen_2_H_minus, lv_color_hex(0xffffff), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_font(ui->screen_2_H_minus, &lv_font_Alatsi_Regular_33, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_align(ui->screen_2_H_minus, LV_TEXT_ALIGN_CENTER, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes screen_2_H_plus
	ui->screen_2_H_plus = lv_btn_create(ui->screen_2);
	ui->screen_2_H_plus_label = lv_label_create(ui->screen_2_H_plus);
	lv_label_set_text(ui->screen_2_H_plus_label, "+");
	lv_label_set_long_mode(ui->screen_2_H_plus_label, LV_LABEL_LONG_WRAP);
	lv_obj_align(ui->screen_2_H_plus_label, LV_ALIGN_CENTER, 0, 0);
	lv_obj_set_style_pad_all(ui->screen_2_H_plus, 0, LV_STATE_DEFAULT);
	lv_obj_set_pos(ui->screen_2_H_plus, 220, 114);
	lv_obj_set_size(ui->screen_2_H_plus, 41, 35);
	lv_obj_set_scrollbar_mode(ui->screen_2_H_plus, LV_SCROLLBAR_MODE_OFF);

	//Write style for screen_2_H_plus, Part: LV_PART_MAIN, State: LV_STATE_DEFAULT.
	lv_obj_set_style_bg_opa(ui->screen_2_H_plus, 255, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_color(ui->screen_2_H_plus, lv_color_hex(0x00c4ff), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_border_width(ui->screen_2_H_plus, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_radius(ui->screen_2_H_plus, 5, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_shadow_width(ui->screen_2_H_plus, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_color(ui->screen_2_H_plus, lv_color_hex(0xffffff), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_font(ui->screen_2_H_plus, &lv_font_Alatsi_Regular_33, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_align(ui->screen_2_H_plus, LV_TEXT_ALIGN_CENTER, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes screen_2_Humidity
	ui->screen_2_Humidity = lv_label_create(ui->screen_2);
	lv_label_set_text(ui->screen_2_Humidity, "0 %");
	lv_label_set_long_mode(ui->screen_2_Humidity, LV_LABEL_LONG_WRAP);
	lv_obj_set_pos(ui->screen_2_Humidity, 292, 149);
	lv_obj_set_size(ui->screen_2_Humidity, 100, 32);
	lv_obj_set_scrollbar_mode(ui->screen_2_Humidity, LV_SCROLLBAR_MODE_OFF);

	//Write style for screen_2_Humidity, Part: LV_PART_MAIN, State: LV_STATE_DEFAULT.
	lv_obj_set_style_border_width(ui->screen_2_Humidity, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_radius(ui->screen_2_Humidity, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_color(ui->screen_2_Humidity, lv_color_hex(0x000000), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_font(ui->screen_2_Humidity, &lv_font_montserratMedium_16, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_letter_space(ui->screen_2_Humidity, 2, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_line_space(ui->screen_2_Humidity, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_align(ui->screen_2_Humidity, LV_TEXT_ALIGN_CENTER, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_opa(ui->screen_2_Humidity, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_top(ui->screen_2_Humidity, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_right(ui->screen_2_Humidity, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_bottom(ui->screen_2_Humidity, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_left(ui->screen_2_Humidity, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_shadow_width(ui->screen_2_Humidity, 0, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Update current screen layout.
	lv_obj_update_layout(ui->screen_2);

	
	//Init events for screen.
	events_init_screen_2(ui);
}
