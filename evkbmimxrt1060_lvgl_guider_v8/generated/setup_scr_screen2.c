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


void setup_scr_screen2(lv_ui *ui)
{
	//Write codes screen2
	ui->screen2 = lv_obj_create(NULL);
	lv_obj_set_size(ui->screen2, 480, 272);
	lv_obj_set_scrollbar_mode(ui->screen2, LV_SCROLLBAR_MODE_OFF);

	//Write style for screen2, Part: LV_PART_MAIN, State: LV_STATE_DEFAULT.
	lv_obj_set_style_bg_opa(ui->screen2, 0, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes screen2_img_1
	ui->screen2_img_1 = lv_img_create(ui->screen2);
	lv_obj_add_flag(ui->screen2_img_1, LV_OBJ_FLAG_CLICKABLE);
	lv_img_set_src(ui->screen2_img_1, &_photo_6168027389217584763_y_alpha_482x300);
	lv_img_set_pivot(ui->screen2_img_1, 50,50);
	lv_img_set_angle(ui->screen2_img_1, 0);
	lv_obj_set_pos(ui->screen2_img_1, -1, -22);
	lv_obj_set_size(ui->screen2_img_1, 482, 300);
	lv_obj_set_scrollbar_mode(ui->screen2_img_1, LV_SCROLLBAR_MODE_OFF);

	//Write style for screen2_img_1, Part: LV_PART_MAIN, State: LV_STATE_DEFAULT.
	lv_obj_set_style_img_opa(ui->screen2_img_1, 144, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes screen2_label_7
	ui->screen2_label_7 = lv_label_create(ui->screen2);
	lv_label_set_text(ui->screen2_label_7, " Camera ");
	lv_label_set_long_mode(ui->screen2_label_7, LV_LABEL_LONG_WRAP);
	lv_obj_set_pos(ui->screen2_label_7, 255, 196);
	lv_obj_set_size(ui->screen2_label_7, 127, 17);
	lv_obj_set_scrollbar_mode(ui->screen2_label_7, LV_SCROLLBAR_MODE_OFF);

	//Write style for screen2_label_7, Part: LV_PART_MAIN, State: LV_STATE_DEFAULT.
	lv_obj_set_style_border_width(ui->screen2_label_7, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_radius(ui->screen2_label_7, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_color(ui->screen2_label_7, lv_color_hex(0x000000), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_font(ui->screen2_label_7, &lv_font_Alatsi_Regular_16, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_letter_space(ui->screen2_label_7, 2, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_line_space(ui->screen2_label_7, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_align(ui->screen2_label_7, LV_TEXT_ALIGN_LEFT, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_opa(ui->screen2_label_7, 150, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_color(ui->screen2_label_7, lv_color_hex(0xf1f1f1), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_grad_dir(ui->screen2_label_7, LV_GRAD_DIR_HOR, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_grad_color(ui->screen2_label_7, lv_color_hex(0x0078f1), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_top(ui->screen2_label_7, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_right(ui->screen2_label_7, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_bottom(ui->screen2_label_7, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_left(ui->screen2_label_7, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_shadow_width(ui->screen2_label_7, 0, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes screen2_label_6
	ui->screen2_label_6 = lv_label_create(ui->screen2);
	lv_label_set_text(ui->screen2_label_6, " Fan");
	lv_label_set_long_mode(ui->screen2_label_6, LV_LABEL_LONG_WRAP);
	lv_obj_set_pos(ui->screen2_label_6, 255, 224);
	lv_obj_set_size(ui->screen2_label_6, 127, 17);
	lv_obj_set_scrollbar_mode(ui->screen2_label_6, LV_SCROLLBAR_MODE_OFF);

	//Write style for screen2_label_6, Part: LV_PART_MAIN, State: LV_STATE_DEFAULT.
	lv_obj_set_style_border_width(ui->screen2_label_6, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_radius(ui->screen2_label_6, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_color(ui->screen2_label_6, lv_color_hex(0x000000), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_font(ui->screen2_label_6, &lv_font_Alatsi_Regular_16, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_letter_space(ui->screen2_label_6, 2, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_line_space(ui->screen2_label_6, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_align(ui->screen2_label_6, LV_TEXT_ALIGN_LEFT, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_opa(ui->screen2_label_6, 165, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_color(ui->screen2_label_6, lv_color_hex(0xd9dbdb), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_grad_dir(ui->screen2_label_6, LV_GRAD_DIR_HOR, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_grad_color(ui->screen2_label_6, lv_color_hex(0xa6ff00), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_top(ui->screen2_label_6, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_right(ui->screen2_label_6, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_bottom(ui->screen2_label_6, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_left(ui->screen2_label_6, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_shadow_width(ui->screen2_label_6, 0, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes screen2_Menu
	ui->screen2_Menu = lv_btn_create(ui->screen2);
	ui->screen2_Menu_label = lv_label_create(ui->screen2_Menu);
	lv_label_set_text(ui->screen2_Menu_label, "Menu");
	lv_label_set_long_mode(ui->screen2_Menu_label, LV_LABEL_LONG_WRAP);
	lv_obj_align(ui->screen2_Menu_label, LV_ALIGN_CENTER, 0, 0);
	lv_obj_set_style_pad_all(ui->screen2_Menu, 0, LV_STATE_DEFAULT);
	lv_obj_set_pos(ui->screen2_Menu, 25, 16);
	lv_obj_set_size(ui->screen2_Menu, 100, 36);
	lv_obj_set_scrollbar_mode(ui->screen2_Menu, LV_SCROLLBAR_MODE_OFF);

	//Write style for screen2_Menu, Part: LV_PART_MAIN, State: LV_STATE_DEFAULT.
	lv_obj_set_style_bg_opa(ui->screen2_Menu, 255, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_color(ui->screen2_Menu, lv_color_hex(0x08c3e4), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_border_width(ui->screen2_Menu, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_radius(ui->screen2_Menu, 5, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_shadow_width(ui->screen2_Menu, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_color(ui->screen2_Menu, lv_color_hex(0xffffff), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_font(ui->screen2_Menu, &lv_font_montserratMedium_16, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_align(ui->screen2_Menu, LV_TEXT_ALIGN_CENTER, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes screen2_btn_1
	ui->screen2_btn_1 = lv_btn_create(ui->screen2);
	ui->screen2_btn_1_label = lv_label_create(ui->screen2_btn_1);
	lv_label_set_text(ui->screen2_btn_1_label, "Temperature\n& Humidity");
	lv_label_set_long_mode(ui->screen2_btn_1_label, LV_LABEL_LONG_WRAP);
	lv_obj_align(ui->screen2_btn_1_label, LV_ALIGN_CENTER, 0, 0);
	lv_obj_set_style_pad_all(ui->screen2_btn_1, 0, LV_STATE_DEFAULT);
	lv_obj_set_pos(ui->screen2_btn_1, 106, 194);
	lv_obj_set_size(ui->screen2_btn_1, 107, 53);
	lv_obj_set_scrollbar_mode(ui->screen2_btn_1, LV_SCROLLBAR_MODE_OFF);

	//Write style for screen2_btn_1, Part: LV_PART_MAIN, State: LV_STATE_DEFAULT.
	lv_obj_set_style_bg_opa(ui->screen2_btn_1, 255, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_color(ui->screen2_btn_1, lv_color_hex(0x07624a), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_border_width(ui->screen2_btn_1, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_radius(ui->screen2_btn_1, 5, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_shadow_width(ui->screen2_btn_1, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_color(ui->screen2_btn_1, lv_color_hex(0xffffff), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_font(ui->screen2_btn_1, &lv_font_simsun_16, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_align(ui->screen2_btn_1, LV_TEXT_ALIGN_CENTER, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes screen2_sw_1
	ui->screen2_sw_1 = lv_switch_create(ui->screen2);
	lv_obj_set_pos(ui->screen2_sw_1, 346, 193);
	lv_obj_set_size(ui->screen2_sw_1, 40, 20);
	lv_obj_set_scrollbar_mode(ui->screen2_sw_1, LV_SCROLLBAR_MODE_OFF);

	//Write style for screen2_sw_1, Part: LV_PART_MAIN, State: LV_STATE_DEFAULT.
	lv_obj_set_style_bg_opa(ui->screen2_sw_1, 165, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_color(ui->screen2_sw_1, lv_color_hex(0x2F92DA), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_border_width(ui->screen2_sw_1, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_radius(ui->screen2_sw_1, 10, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_shadow_width(ui->screen2_sw_1, 0, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write style for screen2_sw_1, Part: LV_PART_INDICATOR, State: LV_STATE_CHECKED.
	lv_obj_set_style_bg_opa(ui->screen2_sw_1, 255, LV_PART_INDICATOR|LV_STATE_CHECKED);
	lv_obj_set_style_bg_color(ui->screen2_sw_1, lv_color_hex(0x2195f6), LV_PART_INDICATOR|LV_STATE_CHECKED);
	lv_obj_set_style_border_width(ui->screen2_sw_1, 0, LV_PART_INDICATOR|LV_STATE_CHECKED);

	//Write style for screen2_sw_1, Part: LV_PART_KNOB, State: LV_STATE_DEFAULT.
	lv_obj_set_style_bg_opa(ui->screen2_sw_1, 255, LV_PART_KNOB|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_color(ui->screen2_sw_1, lv_color_hex(0xffffff), LV_PART_KNOB|LV_STATE_DEFAULT);
	lv_obj_set_style_border_width(ui->screen2_sw_1, 0, LV_PART_KNOB|LV_STATE_DEFAULT);
	lv_obj_set_style_radius(ui->screen2_sw_1, 100, LV_PART_KNOB|LV_STATE_DEFAULT);

	//Write codes screen2_sw_2
	ui->screen2_sw_2 = lv_switch_create(ui->screen2);
	lv_obj_set_pos(ui->screen2_sw_2, 346, 221);
	lv_obj_set_size(ui->screen2_sw_2, 40, 20);
	lv_obj_set_scrollbar_mode(ui->screen2_sw_2, LV_SCROLLBAR_MODE_OFF);

	//Write style for screen2_sw_2, Part: LV_PART_MAIN, State: LV_STATE_DEFAULT.
	lv_obj_set_style_bg_opa(ui->screen2_sw_2, 165, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_color(ui->screen2_sw_2, lv_color_hex(0xbcd202), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_border_width(ui->screen2_sw_2, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_radius(ui->screen2_sw_2, 10, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_shadow_width(ui->screen2_sw_2, 0, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write style for screen2_sw_2, Part: LV_PART_INDICATOR, State: LV_STATE_CHECKED.
	lv_obj_set_style_bg_opa(ui->screen2_sw_2, 255, LV_PART_INDICATOR|LV_STATE_CHECKED);
	lv_obj_set_style_bg_color(ui->screen2_sw_2, lv_color_hex(0x2195f6), LV_PART_INDICATOR|LV_STATE_CHECKED);
	lv_obj_set_style_border_width(ui->screen2_sw_2, 0, LV_PART_INDICATOR|LV_STATE_CHECKED);

	//Write style for screen2_sw_2, Part: LV_PART_KNOB, State: LV_STATE_DEFAULT.
	lv_obj_set_style_bg_opa(ui->screen2_sw_2, 255, LV_PART_KNOB|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_color(ui->screen2_sw_2, lv_color_hex(0xffffff), LV_PART_KNOB|LV_STATE_DEFAULT);
	lv_obj_set_style_border_width(ui->screen2_sw_2, 0, LV_PART_KNOB|LV_STATE_DEFAULT);
	lv_obj_set_style_radius(ui->screen2_sw_2, 100, LV_PART_KNOB|LV_STATE_DEFAULT);

	//Write codes screen2_H2
	ui->screen2_H2 = lv_label_create(ui->screen2);
	lv_label_set_text(ui->screen2_H2, "H");
	lv_label_set_long_mode(ui->screen2_H2, LV_LABEL_LONG_WRAP);
	lv_obj_set_pos(ui->screen2_H2, 348, 42);
	lv_obj_set_size(ui->screen2_H2, 92, 18);
	lv_obj_set_scrollbar_mode(ui->screen2_H2, LV_SCROLLBAR_MODE_OFF);

	//Write style for screen2_H2, Part: LV_PART_MAIN, State: LV_STATE_DEFAULT.
	lv_obj_set_style_border_width(ui->screen2_H2, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_radius(ui->screen2_H2, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_color(ui->screen2_H2, lv_color_hex(0x000000), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_font(ui->screen2_H2, &lv_font_Amiko_Regular_16, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_letter_space(ui->screen2_H2, 2, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_line_space(ui->screen2_H2, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_align(ui->screen2_H2, LV_TEXT_ALIGN_CENTER, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_opa(ui->screen2_H2, 120, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_color(ui->screen2_H2, lv_color_hex(0x00c894), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_grad_dir(ui->screen2_H2, LV_GRAD_DIR_HOR, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_grad_color(ui->screen2_H2, lv_color_hex(0x2195f6), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_top(ui->screen2_H2, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_right(ui->screen2_H2, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_bottom(ui->screen2_H2, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_left(ui->screen2_H2, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_shadow_width(ui->screen2_H2, 0, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes screen2_label_5
	ui->screen2_label_5 = lv_label_create(ui->screen2);
	lv_label_set_text(ui->screen2_label_5, "Humidity");
	lv_label_set_long_mode(ui->screen2_label_5, LV_LABEL_LONG_WRAP);
	lv_obj_set_pos(ui->screen2_label_5, 348, 19);
	lv_obj_set_size(ui->screen2_label_5, 93, 23);
	lv_obj_set_scrollbar_mode(ui->screen2_label_5, LV_SCROLLBAR_MODE_OFF);

	//Write style for screen2_label_5, Part: LV_PART_MAIN, State: LV_STATE_DEFAULT.
	lv_obj_set_style_border_width(ui->screen2_label_5, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_radius(ui->screen2_label_5, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_color(ui->screen2_label_5, lv_color_hex(0x000000), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_font(ui->screen2_label_5, &lv_font_Adventpro_regular_20, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_letter_space(ui->screen2_label_5, 2, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_line_space(ui->screen2_label_5, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_align(ui->screen2_label_5, LV_TEXT_ALIGN_CENTER, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_opa(ui->screen2_label_5, 134, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_color(ui->screen2_label_5, lv_color_hex(0xffffff), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_top(ui->screen2_label_5, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_right(ui->screen2_label_5, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_bottom(ui->screen2_label_5, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_left(ui->screen2_label_5, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_shadow_width(ui->screen2_label_5, 0, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes screen2_T2
	ui->screen2_T2 = lv_label_create(ui->screen2);
	lv_label_set_text(ui->screen2_T2, "T");
	lv_label_set_long_mode(ui->screen2_T2, LV_LABEL_LONG_WRAP);
	lv_obj_set_pos(ui->screen2_T2, 186, 42);
	lv_obj_set_size(ui->screen2_T2, 109, 17);
	lv_obj_set_scrollbar_mode(ui->screen2_T2, LV_SCROLLBAR_MODE_OFF);

	//Write style for screen2_T2, Part: LV_PART_MAIN, State: LV_STATE_DEFAULT.
	lv_obj_set_style_border_width(ui->screen2_T2, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_radius(ui->screen2_T2, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_color(ui->screen2_T2, lv_color_hex(0x000000), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_font(ui->screen2_T2, &lv_font_Amiko_Regular_16, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_letter_space(ui->screen2_T2, 2, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_line_space(ui->screen2_T2, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_align(ui->screen2_T2, LV_TEXT_ALIGN_CENTER, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_opa(ui->screen2_T2, 115, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_color(ui->screen2_T2, lv_color_hex(0xff00db), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_grad_dir(ui->screen2_T2, LV_GRAD_DIR_HOR, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_grad_color(ui->screen2_T2, lv_color_hex(0x2195f6), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_top(ui->screen2_T2, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_right(ui->screen2_T2, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_bottom(ui->screen2_T2, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_left(ui->screen2_T2, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_shadow_width(ui->screen2_T2, 0, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes screen2_label_3
	ui->screen2_label_3 = lv_label_create(ui->screen2);
	lv_label_set_text(ui->screen2_label_3, "Temperature");
	lv_label_set_long_mode(ui->screen2_label_3, LV_LABEL_LONG_WRAP);
	lv_obj_set_pos(ui->screen2_label_3, 184, 19);
	lv_obj_set_size(ui->screen2_label_3, 112, 23);
	lv_obj_set_scrollbar_mode(ui->screen2_label_3, LV_SCROLLBAR_MODE_OFF);

	//Write style for screen2_label_3, Part: LV_PART_MAIN, State: LV_STATE_DEFAULT.
	lv_obj_set_style_border_width(ui->screen2_label_3, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_radius(ui->screen2_label_3, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_color(ui->screen2_label_3, lv_color_hex(0x000000), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_font(ui->screen2_label_3, &lv_font_Adventpro_regular_20, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_letter_space(ui->screen2_label_3, 2, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_line_space(ui->screen2_label_3, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_align(ui->screen2_label_3, LV_TEXT_ALIGN_CENTER, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_opa(ui->screen2_label_3, 134, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_color(ui->screen2_label_3, lv_color_hex(0xffffff), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_top(ui->screen2_label_3, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_right(ui->screen2_label_3, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_bottom(ui->screen2_label_3, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_left(ui->screen2_label_3, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_shadow_width(ui->screen2_label_3, 0, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Update current screen layout.
	lv_obj_update_layout(ui->screen2);

	
	//Init events for screen.
	events_init_screen2(ui);
}
