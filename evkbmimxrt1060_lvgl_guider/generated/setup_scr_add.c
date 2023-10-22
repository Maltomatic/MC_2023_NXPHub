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


void setup_scr_add(lv_ui *ui)
{
	//Write codes add
	ui->add = lv_obj_create(NULL);
	lv_obj_set_size(ui->add, 480, 272);
	lv_obj_set_scrollbar_mode(ui->add, LV_SCROLLBAR_MODE_OFF);

	//Write style for add, Part: LV_PART_MAIN, State: LV_STATE_DEFAULT.
	lv_obj_set_style_bg_opa(ui->add, 0, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes add_label_1
	ui->add_label_1 = lv_label_create(ui->add);
	lv_label_set_text(ui->add_label_1, "Add Profile");
	lv_label_set_long_mode(ui->add_label_1, LV_LABEL_LONG_WRAP);
	lv_obj_set_pos(ui->add_label_1, 69, 26);
	lv_obj_set_size(ui->add_label_1, 342, 35);
	lv_obj_set_scrollbar_mode(ui->add_label_1, LV_SCROLLBAR_MODE_OFF);

	//Write style for add_label_1, Part: LV_PART_MAIN, State: LV_STATE_DEFAULT.
	lv_obj_set_style_border_width(ui->add_label_1, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_radius(ui->add_label_1, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_color(ui->add_label_1, lv_color_hex(0x000000), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_font(ui->add_label_1, &lv_font_Acme_Regular_30, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_letter_space(ui->add_label_1, 2, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_line_space(ui->add_label_1, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_align(ui->add_label_1, LV_TEXT_ALIGN_CENTER, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_opa(ui->add_label_1, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_top(ui->add_label_1, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_right(ui->add_label_1, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_bottom(ui->add_label_1, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_pad_left(ui->add_label_1, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_shadow_width(ui->add_label_1, 0, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes add_btn_1
	ui->add_btn_1 = lv_btn_create(ui->add);
	ui->add_btn_1_label = lv_label_create(ui->add_btn_1);
	lv_label_set_text(ui->add_btn_1_label, "Menu");
	lv_label_set_long_mode(ui->add_btn_1_label, LV_LABEL_LONG_WRAP);
	lv_obj_align(ui->add_btn_1_label, LV_ALIGN_CENTER, 0, 0);
	lv_obj_set_style_pad_all(ui->add_btn_1, 0, LV_STATE_DEFAULT);
	lv_obj_set_pos(ui->add_btn_1, 366, 223);
	lv_obj_set_size(ui->add_btn_1, 100, 36);
	lv_obj_set_scrollbar_mode(ui->add_btn_1, LV_SCROLLBAR_MODE_OFF);

	//Write style for add_btn_1, Part: LV_PART_MAIN, State: LV_STATE_DEFAULT.
	lv_obj_set_style_bg_opa(ui->add_btn_1, 255, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_bg_color(ui->add_btn_1, lv_color_hex(0x08c3e4), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_border_width(ui->add_btn_1, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_radius(ui->add_btn_1, 5, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_shadow_width(ui->add_btn_1, 0, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_color(ui->add_btn_1, lv_color_hex(0xffffff), LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_font(ui->add_btn_1, &lv_font_montserratMedium_16, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_set_style_text_align(ui->add_btn_1, LV_TEXT_ALIGN_CENTER, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Update current screen layout.
	lv_obj_update_layout(ui->add);

	
	//Init events for screen.
	events_init_add(ui);
}
