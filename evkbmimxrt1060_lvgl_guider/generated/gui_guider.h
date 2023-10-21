/*
* Copyright 2023 NXP
* NXP Confidential and Proprietary. This software is owned or controlled by NXP and may only be used strictly in
* accordance with the applicable license terms. By expressly accepting such terms or by downloading, installing,
* activating and/or otherwise using the software, you are agreeing that you have read, and that you agree to
* comply with and are bound by, such license terms.  If you do not agree to be bound by the applicable license
* terms, then you may not retain, install, activate or otherwise use the software.
*/

#ifndef GUI_GUIDER_H
#define GUI_GUIDER_H
#ifdef __cplusplus
extern "C" {
#endif

#include "lvgl.h"

typedef struct
{
  
	lv_obj_t *screen;
	bool screen_del;
	lv_obj_t *screen_img_1;
	lv_obj_t *screen_img_2;
	lv_obj_t *screen_img_3;
	lv_obj_t *screen_ddlist_1;
	lv_obj_t *screen_1;
	bool screen_1_del;
	lv_obj_t *screen_1_img_1;
	lv_obj_t *screen_1_back;
	lv_obj_t *screen_1_back_label;
	lv_obj_t *screen_1_Temp;
	lv_obj_t *screen_1_T_plus;
	lv_obj_t *screen_1_T_plus_label;
	lv_obj_t *screen_1_T_minus;
	lv_obj_t *screen_1_T_minus_label;
	lv_obj_t *screen_1_H_minus;
	lv_obj_t *screen_1_H_minus_label;
	lv_obj_t *screen_1_H_plus;
	lv_obj_t *screen_1_H_plus_label;
	lv_obj_t *screen_1_Humidity;
	lv_obj_t *screen_2;
	bool screen_2_del;
	lv_obj_t *screen_2_img_1;
	lv_obj_t *screen_2_back;
	lv_obj_t *screen_2_back_label;
	lv_obj_t *screen_2_Temp;
	lv_obj_t *screen_2_T_plus;
	lv_obj_t *screen_2_T_plus_label;
	lv_obj_t *screen_2_T_minus;
	lv_obj_t *screen_2_T_minus_label;
	lv_obj_t *screen_2_H_minus;
	lv_obj_t *screen_2_H_minus_label;
	lv_obj_t *screen_2_H_plus;
	lv_obj_t *screen_2_H_plus_label;
	lv_obj_t *screen_2_Humidity;
	lv_obj_t *screen_3;
	bool screen_3_del;
	lv_obj_t *screen_3_img_1;
	lv_obj_t *screen_3_back;
	lv_obj_t *screen_3_back_label;
	lv_obj_t *screen_3_Temp;
	lv_obj_t *screen_3_T_plus;
	lv_obj_t *screen_3_T_plus_label;
	lv_obj_t *screen_3_T_minus;
	lv_obj_t *screen_3_T_minus_label;
	lv_obj_t *screen_3_H_minus;
	lv_obj_t *screen_3_H_minus_label;
	lv_obj_t *screen_3_H_plus;
	lv_obj_t *screen_3_H_plus_label;
	lv_obj_t *screen_3_Humidity;
}lv_ui;

void ui_init_style(lv_style_t * style);
void init_scr_del_flag(lv_ui *ui);
void setup_ui(lv_ui *ui);
extern lv_ui guider_ui;

void setup_scr_screen(lv_ui *ui);
void setup_scr_screen_1(lv_ui *ui);
void setup_scr_screen_2(lv_ui *ui);
void setup_scr_screen_3(lv_ui *ui);
LV_IMG_DECLARE(__alpha_204x114);
LV_IMG_DECLARE(__alpha_180x105);
LV_IMG_DECLARE(__alpha_200x117);
LV_IMG_DECLARE(__alpha_433x102);
LV_IMG_DECLARE(__alpha_433x102);
LV_IMG_DECLARE(__alpha_433x102);

LV_FONT_DECLARE(lv_font_montserratMedium_12)
LV_FONT_DECLARE(lv_font_montserratMedium_16)
LV_FONT_DECLARE(lv_font_Alatsi_Regular_33)


#ifdef __cplusplus
}
#endif
#endif
