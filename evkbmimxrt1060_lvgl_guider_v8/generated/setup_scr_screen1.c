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


void setup_scr_screen1(lv_ui *ui)
{
	//Write codes screen1
	ui->screen1 = lv_obj_create(NULL);
	lv_obj_set_size(ui->screen1, 480, 272);
	lv_obj_set_scrollbar_mode(ui->screen1, LV_SCROLLBAR_MODE_OFF);

	//Write style for screen1, Part: LV_PART_MAIN, State: LV_STATE_DEFAULT.
	lv_obj_set_style_bg_opa(ui->screen1, 0, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes screen1_img_1
	ui->screen1_img_1 = lv_img_create(ui->screen1);
	lv_obj_add_flag(ui->screen1_img_1, LV_OBJ_FLAG_CLICKABLE);
	lv_img_set_src(ui->screen1_img_1, &_OIP_alpha_486x276);
	lv_img_set_pivot(ui->screen1_img_1, 50,50);
	lv_img_set_angle(ui->screen1_img_1, 0);
	lv_obj_set_pos(ui->screen1_img_1, -5, -3);
	lv_obj_set_size(ui->screen1_img_1, 486, 276);
	lv_obj_set_scrollbar_mode(ui->screen1_img_1, LV_SCROLLBAR_MODE_OFF);

	//Write style for screen1_img_1, Part: LV_PART_MAIN, State: LV_STATE_DEFAULT.
	lv_obj_set_style_img_opa(ui->screen1_img_1, 144, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes screen1_label_2
	ui->screen1_label_2 = lv_label_create(ui->screen1);
	lv_label_set_text(ui->screen1_label_2, " Fan");
	lv_label_set_long_mode(ui->screen1_label_2, LV_LABEL_LONG_WRAP);
	lv_obj_set_pos(ui->screen1_label_2, 173, 212);
	lv_obj_set_size(ui->screen1_label_2, 127, 17);
	lv_obj_set_scrollbar_mode(ui->screen1_label_2, LV_SCROLLBAR_MODE_OFF);

	//Write style for screen1_label_2, Part: LV_PART_MAIN, State: LV_STATE_DEFAULT.
	lv_obj_set_style_border_width(ui->screen1_label_2, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_radius(ui->screen1_label_2, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_color(ui->screen1_label_2, lv_color_hex(0x000000), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_font(ui->screen1_label_2, &lv_font_Alatsi_Regular_16, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_letter_space(ui->screen1_label_2, 2, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_line_space(ui->screen1_label_2, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_align(ui->screen1_label_2, LV_TEXT_ALIGN_LEFT, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_opa(ui->screen1_label_2, 165, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_color(ui->screen1_label_2, lv_color_hex(0xd9dbdb), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_grad_dir(ui->screen1_label_2, LV_GRAD_DIR_HOR, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_grad_color(ui->screen1_label_2, lv_color_hex(0xa6ff00), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_top(ui->screen1_label_2, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_right(ui->screen1_label_2, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_bottom(ui->screen1_label_2, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_left(ui->screen1_label_2, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_shadow_width(ui->screen1_label_2, 0, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes screen1_label_1
	ui->screen1_label_1 = lv_label_create(ui->screen1);
	lv_label_set_text(ui->screen1_label_1, " Camera ");
	lv_label_set_long_mode(ui->screen1_label_1, LV_LABEL_LONG_WRAP);
	lv_obj_set_pos(ui->screen1_label_1, 173, 181);
	lv_obj_set_size(ui->screen1_label_1, 127, 17);
	lv_obj_set_scrollbar_mode(ui->screen1_label_1, LV_SCROLLBAR_MODE_OFF);

	//Write style for screen1_label_1, Part: LV_PART_MAIN, State: LV_STATE_DEFAULT.
	lv_obj_set_style_border_width(ui->screen1_label_1, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_radius(ui->screen1_label_1, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_color(ui->screen1_label_1, lv_color_hex(0x000000), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_font(ui->screen1_label_1, &lv_font_Alatsi_Regular_16, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_letter_space(ui->screen1_label_1, 2, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_line_space(ui->screen1_label_1, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_align(ui->screen1_label_1, LV_TEXT_ALIGN_LEFT, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_opa(ui->screen1_label_1, 150, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_color(ui->screen1_label_1, lv_color_hex(0xf1f1f1), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_grad_dir(ui->screen1_label_1, LV_GRAD_DIR_HOR, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_grad_color(ui->screen1_label_1, lv_color_hex(0x0078f1), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_top(ui->screen1_label_1, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_right(ui->screen1_label_1, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_bottom(ui->screen1_label_1, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_left(ui->screen1_label_1, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_shadow_width(ui->screen1_label_1, 0, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes screen1_Menu
	ui->screen1_Menu = lv_btn_create(ui->screen1);
	ui->screen1_Menu_label = lv_label_create(ui->screen1_Menu);
	lv_label_set_text(ui->screen1_Menu_label, "Menu");
	lv_label_set_long_mode(ui->screen1_Menu_label, LV_LABEL_LONG_WRAP);
	lv_obj_align(ui->screen1_Menu_label, LV_ALIGN_CENTER, 0, 0);
	lv_obj_set_style_pad_all(ui->screen1_Menu, 0, LV_STATE_DEFAULT);
	lv_obj_set_pos(ui->screen1_Menu, 25, 19);
	lv_obj_set_size(ui->screen1_Menu, 100, 36);
	lv_obj_set_scrollbar_mode(ui->screen1_Menu, LV_SCROLLBAR_MODE_OFF);

	//Write style for screen1_Menu, Part: LV_PART_MAIN, State: LV_STATE_DEFAULT.
	lv_obj_set_style_bg_opa(ui->screen1_Menu, 255, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_color(ui->screen1_Menu, lv_color_hex(0x37abf5), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_border_width(ui->screen1_Menu, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_radius(ui->screen1_Menu, 5, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_shadow_width(ui->screen1_Menu, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_color(ui->screen1_Menu, lv_color_hex(0xffffff), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_font(ui->screen1_Menu, &lv_font_montserratMedium_16, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_align(ui->screen1_Menu, LV_TEXT_ALIGN_CENTER, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes screen1_btn_1
	ui->screen1_btn_1 = lv_btn_create(ui->screen1);
	ui->screen1_btn_1_label = lv_label_create(ui->screen1_btn_1);
	lv_label_set_text(ui->screen1_btn_1_label, "Temperature\n& Humidity");
	lv_label_set_long_mode(ui->screen1_btn_1_label, LV_LABEL_LONG_WRAP);
	lv_obj_align(ui->screen1_btn_1_label, LV_ALIGN_CENTER, 0, 0);
	lv_obj_set_style_pad_all(ui->screen1_btn_1, 0, LV_STATE_DEFAULT);
	lv_obj_set_pos(ui->screen1_btn_1, 25, 177);
	lv_obj_set_size(ui->screen1_btn_1, 107, 53);
	lv_obj_set_scrollbar_mode(ui->screen1_btn_1, LV_SCROLLBAR_MODE_OFF);

	//Write style for screen1_btn_1, Part: LV_PART_MAIN, State: LV_STATE_DEFAULT.
	lv_obj_set_style_bg_opa(ui->screen1_btn_1, 255, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_color(ui->screen1_btn_1, lv_color_hex(0x07624a), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_border_width(ui->screen1_btn_1, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_radius(ui->screen1_btn_1, 5, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_shadow_width(ui->screen1_btn_1, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_color(ui->screen1_btn_1, lv_color_hex(0xffffff), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_font(ui->screen1_btn_1, &lv_font_simsun_16, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_align(ui->screen1_btn_1, LV_TEXT_ALIGN_CENTER, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes screen1_sw_1
	ui->screen1_sw_1 = lv_switch_create(ui->screen1);
	lv_obj_set_pos(ui->screen1_sw_1, 264, 181);
	lv_obj_set_size(ui->screen1_sw_1, 40, 20);
	lv_obj_set_scrollbar_mode(ui->screen1_sw_1, LV_SCROLLBAR_MODE_OFF);

	//Write style for screen1_sw_1, Part: LV_PART_MAIN, State: LV_STATE_DEFAULT.
	lv_obj_set_style_bg_opa(ui->screen1_sw_1, 165, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_color(ui->screen1_sw_1, lv_color_hex(0x2F92DA), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_border_width(ui->screen1_sw_1, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_radius(ui->screen1_sw_1, 10, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_shadow_width(ui->screen1_sw_1, 0, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write style for screen1_sw_1, Part: LV_PART_INDICATOR, State: LV_STATE_CHECKED.
	lv_obj_set_style_bg_opa(ui->screen1_sw_1, 255, LV_PART_INDICATOR|LV_STATE_CHECKED);
	lv_obj_set_style_bg_color(ui->screen1_sw_1, lv_color_hex(0x2195f6), LV_PART_INDICATOR|LV_STATE_CHECKED);
	lv_obj_set_style_border_width(ui->screen1_sw_1, 0, LV_PART_INDICATOR|LV_STATE_CHECKED);

	//Write style for screen1_sw_1, Part: LV_PART_KNOB, State: LV_STATE_DEFAULT.
	lv_obj_set_style_bg_opa(ui->screen1_sw_1, 255, LV_PART_KNOB|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_color(ui->screen1_sw_1, lv_color_hex(0xffffff), LV_PART_KNOB|LV_STATE_DEFAULT);
	lv_obj_set_style_border_width(ui->screen1_sw_1, 0, LV_PART_KNOB|LV_STATE_DEFAULT);
	lv_obj_set_style_radius(ui->screen1_sw_1, 100, LV_PART_KNOB|LV_STATE_DEFAULT);

	//Write codes screen1_sw_2
	ui->screen1_sw_2 = lv_switch_create(ui->screen1);
	lv_obj_set_pos(ui->screen1_sw_2, 264, 209);
	lv_obj_set_size(ui->screen1_sw_2, 40, 20);
	lv_obj_set_scrollbar_mode(ui->screen1_sw_2, LV_SCROLLBAR_MODE_OFF);

	//Write style for screen1_sw_2, Part: LV_PART_MAIN, State: LV_STATE_DEFAULT.
	lv_obj_set_style_bg_opa(ui->screen1_sw_2, 165, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_color(ui->screen1_sw_2, lv_color_hex(0xbcd202), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_border_width(ui->screen1_sw_2, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_radius(ui->screen1_sw_2, 10, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_shadow_width(ui->screen1_sw_2, 0, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write style for screen1_sw_2, Part: LV_PART_INDICATOR, State: LV_STATE_CHECKED.
	lv_obj_set_style_bg_opa(ui->screen1_sw_2, 255, LV_PART_INDICATOR|LV_STATE_CHECKED);
	lv_obj_set_style_bg_color(ui->screen1_sw_2, lv_color_hex(0x2195f6), LV_PART_INDICATOR|LV_STATE_CHECKED);
	lv_obj_set_style_border_width(ui->screen1_sw_2, 0, LV_PART_INDICATOR|LV_STATE_CHECKED);

	//Write style for screen1_sw_2, Part: LV_PART_KNOB, State: LV_STATE_DEFAULT.
	lv_obj_set_style_bg_opa(ui->screen1_sw_2, 255, LV_PART_KNOB|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_color(ui->screen1_sw_2, lv_color_hex(0xffffff), LV_PART_KNOB|LV_STATE_DEFAULT);
	lv_obj_set_style_border_width(ui->screen1_sw_2, 0, LV_PART_KNOB|LV_STATE_DEFAULT);
	lv_obj_set_style_radius(ui->screen1_sw_2, 100, LV_PART_KNOB|LV_STATE_DEFAULT);

	//Write codes screen1_btn_2
	ui->screen1_btn_2 = lv_btn_create(ui->screen1);
	ui->screen1_btn_2_label = lv_label_create(ui->screen1_btn_2);
	lv_label_set_text(ui->screen1_btn_2_label, "Baby\nAlarm");
	lv_label_set_long_mode(ui->screen1_btn_2_label, LV_LABEL_LONG_WRAP);
	lv_obj_align(ui->screen1_btn_2_label, LV_ALIGN_CENTER, 0, 0);
	lv_obj_set_style_pad_all(ui->screen1_btn_2, 0, LV_STATE_DEFAULT);
	lv_obj_set_pos(ui->screen1_btn_2, 348, 176);
	lv_obj_set_size(ui->screen1_btn_2, 107, 53);
	lv_obj_set_scrollbar_mode(ui->screen1_btn_2, LV_SCROLLBAR_MODE_OFF);

	//Write style for screen1_btn_2, Part: LV_PART_MAIN, State: LV_STATE_DEFAULT.
	lv_obj_set_style_bg_opa(ui->screen1_btn_2, 255, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_color(ui->screen1_btn_2, lv_color_hex(0xd60025), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_border_width(ui->screen1_btn_2, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_radius(ui->screen1_btn_2, 5, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_shadow_width(ui->screen1_btn_2, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_color(ui->screen1_btn_2, lv_color_hex(0xffffff), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_font(ui->screen1_btn_2, &lv_font_simsun_16, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_align(ui->screen1_btn_2, LV_TEXT_ALIGN_CENTER, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes screen1_T1
	ui->screen1_T1 = lv_label_create(ui->screen1);
	lv_label_set_text(ui->screen1_T1, "T");
	lv_label_set_long_mode(ui->screen1_T1, LV_LABEL_LONG_WRAP);
	lv_obj_set_pos(ui->screen1_T1, 186, 42);
	lv_obj_set_size(ui->screen1_T1, 109, 17);
	lv_obj_set_scrollbar_mode(ui->screen1_T1, LV_SCROLLBAR_MODE_OFF);

	//Write style for screen1_T1, Part: LV_PART_MAIN, State: LV_STATE_DEFAULT.
	lv_obj_set_style_border_width(ui->screen1_T1, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_radius(ui->screen1_T1, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_color(ui->screen1_T1, lv_color_hex(0x000000), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_font(ui->screen1_T1, &lv_font_Amiko_Regular_16, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_letter_space(ui->screen1_T1, 2, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_line_space(ui->screen1_T1, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_align(ui->screen1_T1, LV_TEXT_ALIGN_CENTER, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_opa(ui->screen1_T1, 172, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_color(ui->screen1_T1, lv_color_hex(0x585df6), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_grad_dir(ui->screen1_T1, LV_GRAD_DIR_HOR, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_grad_color(ui->screen1_T1, lv_color_hex(0xee80fe), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_top(ui->screen1_T1, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_right(ui->screen1_T1, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_bottom(ui->screen1_T1, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_left(ui->screen1_T1, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_shadow_width(ui->screen1_T1, 0, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes screen1_H1
	ui->screen1_H1 = lv_label_create(ui->screen1);
	lv_label_set_text(ui->screen1_H1, "H");
	lv_label_set_long_mode(ui->screen1_H1, LV_LABEL_LONG_WRAP);
	lv_obj_set_pos(ui->screen1_H1, 348, 42);
	lv_obj_set_size(ui->screen1_H1, 92, 18);
	lv_obj_set_scrollbar_mode(ui->screen1_H1, LV_SCROLLBAR_MODE_OFF);

	//Write style for screen1_H1, Part: LV_PART_MAIN, State: LV_STATE_DEFAULT.
	lv_obj_set_style_border_width(ui->screen1_H1, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_radius(ui->screen1_H1, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_color(ui->screen1_H1, lv_color_hex(0x000000), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_font(ui->screen1_H1, &lv_font_Amiko_Regular_16, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_letter_space(ui->screen1_H1, 2, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_line_space(ui->screen1_H1, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_align(ui->screen1_H1, LV_TEXT_ALIGN_CENTER, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_opa(ui->screen1_H1, 120, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_color(ui->screen1_H1, lv_color_hex(0x0dcb75), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_grad_dir(ui->screen1_H1, LV_GRAD_DIR_HOR, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_grad_color(ui->screen1_H1, lv_color_hex(0x3cb6f6), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_top(ui->screen1_H1, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_right(ui->screen1_H1, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_bottom(ui->screen1_H1, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_left(ui->screen1_H1, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_shadow_width(ui->screen1_H1, 0, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes screen1_label_3
	ui->screen1_label_3 = lv_label_create(ui->screen1);
	lv_label_set_text(ui->screen1_label_3, "Humidity");
	lv_label_set_long_mode(ui->screen1_label_3, LV_LABEL_LONG_WRAP);
	lv_obj_set_pos(ui->screen1_label_3, 348, 19);
	lv_obj_set_size(ui->screen1_label_3, 93, 23);
	lv_obj_set_scrollbar_mode(ui->screen1_label_3, LV_SCROLLBAR_MODE_OFF);

	//Write style for screen1_label_3, Part: LV_PART_MAIN, State: LV_STATE_DEFAULT.
	lv_obj_set_style_border_width(ui->screen1_label_3, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_radius(ui->screen1_label_3, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_color(ui->screen1_label_3, lv_color_hex(0x000000), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_font(ui->screen1_label_3, &lv_font_Adventpro_regular_20, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_letter_space(ui->screen1_label_3, 2, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_line_space(ui->screen1_label_3, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_align(ui->screen1_label_3, LV_TEXT_ALIGN_CENTER, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_opa(ui->screen1_label_3, 134, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_color(ui->screen1_label_3, lv_color_hex(0xffffff), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_top(ui->screen1_label_3, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_right(ui->screen1_label_3, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_bottom(ui->screen1_label_3, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_left(ui->screen1_label_3, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_shadow_width(ui->screen1_label_3, 0, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes screen1_label_4
	ui->screen1_label_4 = lv_label_create(ui->screen1);
	lv_label_set_text(ui->screen1_label_4, "Temperature");
	lv_label_set_long_mode(ui->screen1_label_4, LV_LABEL_LONG_WRAP);
	lv_obj_set_pos(ui->screen1_label_4, 184, 19);
	lv_obj_set_size(ui->screen1_label_4, 112, 23);
	lv_obj_set_scrollbar_mode(ui->screen1_label_4, LV_SCROLLBAR_MODE_OFF);

	//Write style for screen1_label_4, Part: LV_PART_MAIN, State: LV_STATE_DEFAULT.
	lv_obj_set_style_border_width(ui->screen1_label_4, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_radius(ui->screen1_label_4, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_color(ui->screen1_label_4, lv_color_hex(0x000000), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_font(ui->screen1_label_4, &lv_font_Adventpro_regular_20, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_letter_space(ui->screen1_label_4, 2, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_line_space(ui->screen1_label_4, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_align(ui->screen1_label_4, LV_TEXT_ALIGN_CENTER, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_opa(ui->screen1_label_4, 134, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_color(ui->screen1_label_4, lv_color_hex(0xffffff), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_top(ui->screen1_label_4, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_right(ui->screen1_label_4, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_bottom(ui->screen1_label_4, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_left(ui->screen1_label_4, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_shadow_width(ui->screen1_label_4, 0, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Update current screen layout.
	lv_obj_update_layout(ui->screen1);

	
	//Init events for screen.
	events_init_screen1(ui);
}
