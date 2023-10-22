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


void setup_scr_screen_3(lv_ui *ui)
{
	//Write codes screen_3
	ui->screen_3 = lv_obj_create(NULL);
	lv_obj_set_size(ui->screen_3, 480, 272);
	lv_obj_set_scrollbar_mode(ui->screen_3, LV_SCROLLBAR_MODE_OFF);

	//Write style for screen_3, Part: LV_PART_MAIN, State: LV_STATE_DEFAULT.
	lv_obj_set_style_bg_opa(ui->screen_3, 0, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes screen_3_img_1
	ui->screen_3_img_1 = lv_img_create(ui->screen_3);
	lv_obj_add_flag(ui->screen_3_img_1, LV_OBJ_FLAG_CLICKABLE);
	lv_img_set_src(ui->screen_3_img_1, &_R_alpha_483x285);
	lv_img_set_pivot(ui->screen_3_img_1, 50,50);
	lv_img_set_angle(ui->screen_3_img_1, 0);
	lv_obj_set_pos(ui->screen_3_img_1, -1, 0);
	lv_obj_set_size(ui->screen_3_img_1, 483, 285);
	lv_obj_set_scrollbar_mode(ui->screen_3_img_1, LV_SCROLLBAR_MODE_OFF);

	//Write style for screen_3_img_1, Part: LV_PART_MAIN, State: LV_STATE_DEFAULT.
	lv_obj_set_style_img_opa(ui->screen_3_img_1, 160, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes screen_3_back
	ui->screen_3_back = lv_btn_create(ui->screen_3);
	ui->screen_3_back_label = lv_label_create(ui->screen_3_back);
	lv_label_set_text(ui->screen_3_back_label, "Back");
	lv_label_set_long_mode(ui->screen_3_back_label, LV_LABEL_LONG_WRAP);
	lv_obj_align(ui->screen_3_back_label, LV_ALIGN_CENTER, 0, 0);
	lv_obj_set_style_pad_all(ui->screen_3_back, 0, LV_STATE_DEFAULT);
	lv_obj_set_pos(ui->screen_3_back, 25, 16);
	lv_obj_set_size(ui->screen_3_back, 100, 36);
	lv_obj_set_scrollbar_mode(ui->screen_3_back, LV_SCROLLBAR_MODE_OFF);

	//Write style for screen_3_back, Part: LV_PART_MAIN, State: LV_STATE_DEFAULT.
	lv_obj_set_style_bg_opa(ui->screen_3_back, 255, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_color(ui->screen_3_back, lv_color_hex(0x2195f6), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_border_width(ui->screen_3_back, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_radius(ui->screen_3_back, 5, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_shadow_width(ui->screen_3_back, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_color(ui->screen_3_back, lv_color_hex(0xffffff), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_font(ui->screen_3_back, &lv_font_montserratMedium_16, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_align(ui->screen_3_back, LV_TEXT_ALIGN_CENTER, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes screen_3_Temp3
	ui->screen_3_Temp3 = lv_label_create(ui->screen_3);
	lv_label_set_text(ui->screen_3_Temp3, "0");
	lv_label_set_long_mode(ui->screen_3_Temp3, LV_LABEL_LONG_WRAP);
	lv_obj_set_pos(ui->screen_3_Temp3, 191, 146);
	lv_obj_set_size(ui->screen_3_Temp3, 37, 21);
	lv_obj_set_scrollbar_mode(ui->screen_3_Temp3, LV_SCROLLBAR_MODE_OFF);

	//Write style for screen_3_Temp3, Part: LV_PART_MAIN, State: LV_STATE_DEFAULT.
	lv_obj_set_style_border_width(ui->screen_3_Temp3, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_radius(ui->screen_3_Temp3, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_color(ui->screen_3_Temp3, lv_color_hex(0x000000), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_font(ui->screen_3_Temp3, &lv_font_montserratMedium_16, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_letter_space(ui->screen_3_Temp3, 2, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_line_space(ui->screen_3_Temp3, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_align(ui->screen_3_Temp3, LV_TEXT_ALIGN_CENTER, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_opa(ui->screen_3_Temp3, 129, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_color(ui->screen_3_Temp3, lv_color_hex(0xf9eaf7), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_top(ui->screen_3_Temp3, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_right(ui->screen_3_Temp3, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_bottom(ui->screen_3_Temp3, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_left(ui->screen_3_Temp3, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_shadow_width(ui->screen_3_Temp3, 0, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes screen_3_T_plus
	ui->screen_3_T_plus = lv_btn_create(ui->screen_3);
	ui->screen_3_T_plus_label = lv_label_create(ui->screen_3_T_plus);
	lv_label_set_text(ui->screen_3_T_plus_label, "+");
	lv_label_set_long_mode(ui->screen_3_T_plus_label, LV_LABEL_LONG_WRAP);
	lv_obj_align(ui->screen_3_T_plus_label, LV_ALIGN_CENTER, 0, 0);
	lv_obj_set_style_pad_all(ui->screen_3_T_plus, 0, LV_STATE_DEFAULT);
	lv_obj_set_pos(ui->screen_3_T_plus, 27, 115);
	lv_obj_set_size(ui->screen_3_T_plus, 43, 42);
	lv_obj_set_scrollbar_mode(ui->screen_3_T_plus, LV_SCROLLBAR_MODE_OFF);

	//Write style for screen_3_T_plus, Part: LV_PART_MAIN, State: LV_STATE_DEFAULT.
	lv_obj_set_style_bg_opa(ui->screen_3_T_plus, 255, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_color(ui->screen_3_T_plus, lv_color_hex(0x009ea9), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_border_width(ui->screen_3_T_plus, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_radius(ui->screen_3_T_plus, 25, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_shadow_width(ui->screen_3_T_plus, 3, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_shadow_color(ui->screen_3_T_plus, lv_color_hex(0x0d4b3b), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_shadow_opa(ui->screen_3_T_plus, 255, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_shadow_spread(ui->screen_3_T_plus, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_shadow_ofs_x(ui->screen_3_T_plus, 1, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_shadow_ofs_y(ui->screen_3_T_plus, 2, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_color(ui->screen_3_T_plus, lv_color_hex(0xffffff), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_font(ui->screen_3_T_plus, &lv_font_Acme_Regular_30, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_align(ui->screen_3_T_plus, LV_TEXT_ALIGN_CENTER, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes screen_3_T_minus
	ui->screen_3_T_minus = lv_btn_create(ui->screen_3);
	ui->screen_3_T_minus_label = lv_label_create(ui->screen_3_T_minus);
	lv_label_set_text(ui->screen_3_T_minus_label, "-");
	lv_label_set_long_mode(ui->screen_3_T_minus_label, LV_LABEL_LONG_WRAP);
	lv_obj_align(ui->screen_3_T_minus_label, LV_ALIGN_CENTER, 0, 0);
	lv_obj_set_style_pad_all(ui->screen_3_T_minus, 0, LV_STATE_DEFAULT);
	lv_obj_set_pos(ui->screen_3_T_minus, 27, 167);
	lv_obj_set_size(ui->screen_3_T_minus, 42, 42);
	lv_obj_set_scrollbar_mode(ui->screen_3_T_minus, LV_SCROLLBAR_MODE_OFF);

	//Write style for screen_3_T_minus, Part: LV_PART_MAIN, State: LV_STATE_DEFAULT.
	lv_obj_set_style_bg_opa(ui->screen_3_T_minus, 255, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_color(ui->screen_3_T_minus, lv_color_hex(0x009ea9), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_border_width(ui->screen_3_T_minus, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_radius(ui->screen_3_T_minus, 25, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_shadow_width(ui->screen_3_T_minus, 3, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_shadow_color(ui->screen_3_T_minus, lv_color_hex(0x0d4b3b), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_shadow_opa(ui->screen_3_T_minus, 255, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_shadow_spread(ui->screen_3_T_minus, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_shadow_ofs_x(ui->screen_3_T_minus, 1, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_shadow_ofs_y(ui->screen_3_T_minus, 2, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_color(ui->screen_3_T_minus, lv_color_hex(0xffffff), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_font(ui->screen_3_T_minus, &lv_font_Alatsi_Regular_30, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_align(ui->screen_3_T_minus, LV_TEXT_ALIGN_CENTER, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes screen_3_H_minus
	ui->screen_3_H_minus = lv_btn_create(ui->screen_3);
	ui->screen_3_H_minus_label = lv_label_create(ui->screen_3_H_minus);
	lv_label_set_text(ui->screen_3_H_minus_label, "-");
	lv_label_set_long_mode(ui->screen_3_H_minus_label, LV_LABEL_LONG_WRAP);
	lv_obj_align(ui->screen_3_H_minus_label, LV_ALIGN_CENTER, 0, 0);
	lv_obj_set_style_pad_all(ui->screen_3_H_minus, 0, LV_STATE_DEFAULT);
	lv_obj_set_pos(ui->screen_3_H_minus, 408, 167);
	lv_obj_set_size(ui->screen_3_H_minus, 41, 35);
	lv_obj_set_scrollbar_mode(ui->screen_3_H_minus, LV_SCROLLBAR_MODE_OFF);

	//Write style for screen_3_H_minus, Part: LV_PART_MAIN, State: LV_STATE_DEFAULT.
	lv_obj_set_style_bg_opa(ui->screen_3_H_minus, 255, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_color(ui->screen_3_H_minus, lv_color_hex(0x00bdff), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_border_width(ui->screen_3_H_minus, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_radius(ui->screen_3_H_minus, 5, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_shadow_width(ui->screen_3_H_minus, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_color(ui->screen_3_H_minus, lv_color_hex(0xffffff), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_font(ui->screen_3_H_minus, &lv_font_Alatsi_Regular_33, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_align(ui->screen_3_H_minus, LV_TEXT_ALIGN_CENTER, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes screen_3_H_plus
	ui->screen_3_H_plus = lv_btn_create(ui->screen_3);
	ui->screen_3_H_plus_label = lv_label_create(ui->screen_3_H_plus);
	lv_label_set_text(ui->screen_3_H_plus_label, "+");
	lv_label_set_long_mode(ui->screen_3_H_plus_label, LV_LABEL_LONG_WRAP);
	lv_obj_align(ui->screen_3_H_plus_label, LV_ALIGN_CENTER, 0, 0);
	lv_obj_set_style_pad_all(ui->screen_3_H_plus, 0, LV_STATE_DEFAULT);
	lv_obj_set_pos(ui->screen_3_H_plus, 408, 119);
	lv_obj_set_size(ui->screen_3_H_plus, 41, 35);
	lv_obj_set_scrollbar_mode(ui->screen_3_H_plus, LV_SCROLLBAR_MODE_OFF);

	//Write style for screen_3_H_plus, Part: LV_PART_MAIN, State: LV_STATE_DEFAULT.
	lv_obj_set_style_bg_opa(ui->screen_3_H_plus, 255, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_color(ui->screen_3_H_plus, lv_color_hex(0x00c4ff), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_border_width(ui->screen_3_H_plus, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_radius(ui->screen_3_H_plus, 5, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_shadow_width(ui->screen_3_H_plus, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_color(ui->screen_3_H_plus, lv_color_hex(0xffffff), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_font(ui->screen_3_H_plus, &lv_font_Alatsi_Regular_33, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_align(ui->screen_3_H_plus, LV_TEXT_ALIGN_CENTER, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes screen_3_Humidity3
	ui->screen_3_Humidity3 = lv_label_create(ui->screen_3);
	lv_label_set_text(ui->screen_3_Humidity3, "0 %");
	lv_label_set_long_mode(ui->screen_3_Humidity3, LV_LABEL_LONG_WRAP);
	lv_obj_set_pos(ui->screen_3_Humidity3, 353, 145);
	lv_obj_set_size(ui->screen_3_Humidity3, 41, 23);
	lv_obj_set_scrollbar_mode(ui->screen_3_Humidity3, LV_SCROLLBAR_MODE_OFF);

	//Write style for screen_3_Humidity3, Part: LV_PART_MAIN, State: LV_STATE_DEFAULT.
	lv_obj_set_style_border_width(ui->screen_3_Humidity3, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_radius(ui->screen_3_Humidity3, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_color(ui->screen_3_Humidity3, lv_color_hex(0x000000), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_font(ui->screen_3_Humidity3, &lv_font_montserratMedium_16, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_letter_space(ui->screen_3_Humidity3, 2, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_line_space(ui->screen_3_Humidity3, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_align(ui->screen_3_Humidity3, LV_TEXT_ALIGN_CENTER, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_opa(ui->screen_3_Humidity3, 97, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_color(ui->screen_3_Humidity3, lv_color_hex(0xfdf7fc), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_top(ui->screen_3_Humidity3, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_right(ui->screen_3_Humidity3, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_bottom(ui->screen_3_Humidity3, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_left(ui->screen_3_Humidity3, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_shadow_width(ui->screen_3_Humidity3, 0, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes screen_3_btn_2
	ui->screen_3_btn_2 = lv_btn_create(ui->screen_3);
	ui->screen_3_btn_2_label = lv_label_create(ui->screen_3_btn_2);
	lv_label_set_text(ui->screen_3_btn_2_label, "Reset");
	lv_label_set_long_mode(ui->screen_3_btn_2_label, LV_LABEL_LONG_WRAP);
	lv_obj_align(ui->screen_3_btn_2_label, LV_ALIGN_CENTER, 0, 0);
	lv_obj_set_style_pad_all(ui->screen_3_btn_2, 0, LV_STATE_DEFAULT);
	lv_obj_set_pos(ui->screen_3_btn_2, 382, 217);
	lv_obj_set_size(ui->screen_3_btn_2, 74, 37);
	lv_obj_set_scrollbar_mode(ui->screen_3_btn_2, LV_SCROLLBAR_MODE_OFF);

	//Write style for screen_3_btn_2, Part: LV_PART_MAIN, State: LV_STATE_DEFAULT.
	lv_obj_set_style_bg_opa(ui->screen_3_btn_2, 255, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_color(ui->screen_3_btn_2, lv_color_hex(0x292929), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_border_width(ui->screen_3_btn_2, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_radius(ui->screen_3_btn_2, 5, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_shadow_width(ui->screen_3_btn_2, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_color(ui->screen_3_btn_2, lv_color_hex(0xffffff), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_font(ui->screen_3_btn_2, &lv_font_simsun_18, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_align(ui->screen_3_btn_2, LV_TEXT_ALIGN_CENTER, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes screen_3_btn_1
	ui->screen_3_btn_1 = lv_btn_create(ui->screen_3);
	ui->screen_3_btn_1_label = lv_label_create(ui->screen_3_btn_1);
	lv_label_set_text(ui->screen_3_btn_1_label, "Reset");
	lv_label_set_long_mode(ui->screen_3_btn_1_label, LV_LABEL_LONG_WRAP);
	lv_obj_align(ui->screen_3_btn_1_label, LV_ALIGN_CENTER, 0, 0);
	lv_obj_set_style_pad_all(ui->screen_3_btn_1, 0, LV_STATE_DEFAULT);
	lv_obj_set_pos(ui->screen_3_btn_1, 27, 217);
	lv_obj_set_size(ui->screen_3_btn_1, 74, 37);
	lv_obj_set_scrollbar_mode(ui->screen_3_btn_1, LV_SCROLLBAR_MODE_OFF);

	//Write style for screen_3_btn_1, Part: LV_PART_MAIN, State: LV_STATE_DEFAULT.
	lv_obj_set_style_bg_opa(ui->screen_3_btn_1, 255, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_color(ui->screen_3_btn_1, lv_color_hex(0x292929), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_border_width(ui->screen_3_btn_1, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_radius(ui->screen_3_btn_1, 5, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_shadow_width(ui->screen_3_btn_1, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_color(ui->screen_3_btn_1, lv_color_hex(0xffffff), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_font(ui->screen_3_btn_1, &lv_font_simsun_18, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_align(ui->screen_3_btn_1, LV_TEXT_ALIGN_CENTER, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes screen_3_label_1
	ui->screen_3_label_1 = lv_label_create(ui->screen_3);
	lv_label_set_text(ui->screen_3_label_1, "Temperature");
	lv_label_set_long_mode(ui->screen_3_label_1, LV_LABEL_LONG_WRAP);
	lv_obj_set_pos(ui->screen_3_label_1, 79, 145);
	lv_obj_set_size(ui->screen_3_label_1, 112, 23);
	lv_obj_set_scrollbar_mode(ui->screen_3_label_1, LV_SCROLLBAR_MODE_OFF);

	//Write style for screen_3_label_1, Part: LV_PART_MAIN, State: LV_STATE_DEFAULT.
	lv_obj_set_style_border_width(ui->screen_3_label_1, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_radius(ui->screen_3_label_1, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_color(ui->screen_3_label_1, lv_color_hex(0x000000), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_font(ui->screen_3_label_1, &lv_font_Adventpro_regular_20, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_letter_space(ui->screen_3_label_1, 2, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_line_space(ui->screen_3_label_1, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_align(ui->screen_3_label_1, LV_TEXT_ALIGN_CENTER, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_opa(ui->screen_3_label_1, 134, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_color(ui->screen_3_label_1, lv_color_hex(0xffffff), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_top(ui->screen_3_label_1, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_right(ui->screen_3_label_1, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_bottom(ui->screen_3_label_1, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_left(ui->screen_3_label_1, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_shadow_width(ui->screen_3_label_1, 0, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes screen_3_label_2
	ui->screen_3_label_2 = lv_label_create(ui->screen_3);
	lv_label_set_text(ui->screen_3_label_2, "Humidity");
	lv_label_set_long_mode(ui->screen_3_label_2, LV_LABEL_LONG_WRAP);
	lv_obj_set_pos(ui->screen_3_label_2, 260, 145);
	lv_obj_set_size(ui->screen_3_label_2, 93, 23);
	lv_obj_set_scrollbar_mode(ui->screen_3_label_2, LV_SCROLLBAR_MODE_OFF);

	//Write style for screen_3_label_2, Part: LV_PART_MAIN, State: LV_STATE_DEFAULT.
	lv_obj_set_style_border_width(ui->screen_3_label_2, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_radius(ui->screen_3_label_2, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_color(ui->screen_3_label_2, lv_color_hex(0x000000), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_font(ui->screen_3_label_2, &lv_font_Adventpro_regular_20, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_letter_space(ui->screen_3_label_2, 2, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_line_space(ui->screen_3_label_2, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_align(ui->screen_3_label_2, LV_TEXT_ALIGN_CENTER, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_opa(ui->screen_3_label_2, 134, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_color(ui->screen_3_label_2, lv_color_hex(0xffffff), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_top(ui->screen_3_label_2, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_right(ui->screen_3_label_2, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_bottom(ui->screen_3_label_2, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_left(ui->screen_3_label_2, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_shadow_width(ui->screen_3_label_2, 0, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Update current screen layout.
	lv_obj_update_layout(ui->screen_3);

	
	//Init events for screen.
	events_init_screen_3(ui);
}
