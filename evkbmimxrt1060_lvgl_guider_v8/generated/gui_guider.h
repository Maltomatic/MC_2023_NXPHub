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
	lv_obj_t *screen_btn_1;
	lv_obj_t *screen_btn_1_label;
	lv_obj_t *screen1;
	bool screen1_del;
	lv_obj_t *screen1_img_1;
	lv_obj_t *screen1_label_2;
	lv_obj_t *screen1_label_1;
	lv_obj_t *screen1_Menu;
	lv_obj_t *screen1_Menu_label;
	lv_obj_t *screen1_btn_1;
	lv_obj_t *screen1_btn_1_label;
	lv_obj_t *screen1_sw_1;
	lv_obj_t *screen1_sw_2;
	lv_obj_t *screen1_btn_2;
	lv_obj_t *screen1_btn_2_label;
	lv_obj_t *screen1_T1;
	lv_obj_t *screen1_H1;
	lv_obj_t *screen1_label_3;
	lv_obj_t *screen1_label_4;
	lv_obj_t *screen2;
	bool screen2_del;
	lv_obj_t *screen2_img_1;
	lv_obj_t *screen2_label_7;
	lv_obj_t *screen2_label_6;
	lv_obj_t *screen2_Menu;
	lv_obj_t *screen2_Menu_label;
	lv_obj_t *screen2_btn_1;
	lv_obj_t *screen2_btn_1_label;
	lv_obj_t *screen2_sw_1;
	lv_obj_t *screen2_sw_2;
	lv_obj_t *screen2_H2;
	lv_obj_t *screen2_label_5;
	lv_obj_t *screen2_T2;
	lv_obj_t *screen2_label_3;
	lv_obj_t *screen3;
	bool screen3_del;
	lv_obj_t *screen3_img_1;
	lv_obj_t *screen3_Menu;
	lv_obj_t *screen3_Menu_label;
	lv_obj_t *screen3_btn_1;
	lv_obj_t *screen3_btn_1_label;
	lv_obj_t *screen3_H3;
	lv_obj_t *screen3_label_5;
	lv_obj_t *screen3_T3;
	lv_obj_t *screen3_label_3;
	lv_obj_t *screen3_label_7;
	lv_obj_t *screen3_label_6;
	lv_obj_t *screen3_sw_1;
	lv_obj_t *screen3_sw_2;
	lv_obj_t *screen_1;
	bool screen_1_del;
	lv_obj_t *screen_1_img_2;
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
	lv_obj_t *screen_1_Reset_T;
	lv_obj_t *screen_1_Reset_T_label;
	lv_obj_t *screen_1_Reset_H;
	lv_obj_t *screen_1_Reset_H_label;
	lv_obj_t *screen_1_label_1;
	lv_obj_t *screen_1_label_2;
	lv_obj_t *screen_2;
	bool screen_2_del;
	lv_obj_t *screen_2_img_1;
	lv_obj_t *screen_2_back;
	lv_obj_t *screen_2_back_label;
	lv_obj_t *screen_2_Temp2;
	lv_obj_t *screen_2_T_plus;
	lv_obj_t *screen_2_T_plus_label;
	lv_obj_t *screen_2_T_minus;
	lv_obj_t *screen_2_T_minus_label;
	lv_obj_t *screen_2_H_minus;
	lv_obj_t *screen_2_H_minus_label;
	lv_obj_t *screen_2_H_plus;
	lv_obj_t *screen_2_H_plus_label;
	lv_obj_t *screen_2_Humidity2;
	lv_obj_t *screen_2_btn_2;
	lv_obj_t *screen_2_btn_2_label;
	lv_obj_t *screen_2_btn_1;
	lv_obj_t *screen_2_btn_1_label;
	lv_obj_t *screen_2_label_1;
	lv_obj_t *screen_2_label_2;
	lv_obj_t *screen_3;
	bool screen_3_del;
	lv_obj_t *screen_3_img_1;
	lv_obj_t *screen_3_back;
	lv_obj_t *screen_3_back_label;
	lv_obj_t *screen_3_Temp3;
	lv_obj_t *screen_3_T_plus;
	lv_obj_t *screen_3_T_plus_label;
	lv_obj_t *screen_3_T_minus;
	lv_obj_t *screen_3_T_minus_label;
	lv_obj_t *screen_3_H_minus;
	lv_obj_t *screen_3_H_minus_label;
	lv_obj_t *screen_3_H_plus;
	lv_obj_t *screen_3_H_plus_label;
	lv_obj_t *screen_3_Humidity3;
	lv_obj_t *screen_3_btn_2;
	lv_obj_t *screen_3_btn_2_label;
	lv_obj_t *screen_3_btn_1;
	lv_obj_t *screen_3_btn_1_label;
	lv_obj_t *screen_3_label_1;
	lv_obj_t *screen_3_label_2;
	lv_obj_t *add;
	bool add_del;
	lv_obj_t *add_label_1;
	lv_obj_t *add_btn_1;
	lv_obj_t *add_btn_1_label;
}lv_ui;

void ui_init_style(lv_style_t * style);
void init_scr_del_flag(lv_ui *ui);
void setup_ui(lv_ui *ui);
extern lv_ui guider_ui;

void setup_scr_screen(lv_ui *ui);
void setup_scr_screen1(lv_ui *ui);
void setup_scr_screen2(lv_ui *ui);
void setup_scr_screen3(lv_ui *ui);
void setup_scr_screen_1(lv_ui *ui);
void setup_scr_screen_2(lv_ui *ui);
void setup_scr_screen_3(lv_ui *ui);
void setup_scr_add(lv_ui *ui);
LV_IMG_DECLARE(_OIP_alpha_181x110);
LV_IMG_DECLARE(_photo_6168027389217584763_y_alpha_176x122);
LV_IMG_DECLARE(_R_alpha_180x115);
LV_IMG_DECLARE(_OIP_alpha_486x276);
LV_IMG_DECLARE(_photo_6168027389217584763_y_alpha_482x300);
LV_IMG_DECLARE(_R_alpha_483x285);
LV_IMG_DECLARE(_OIP_alpha_486x276);
LV_IMG_DECLARE(_photo_6168027389217584763_y_alpha_482x300);
LV_IMG_DECLARE(_R_alpha_483x285);

LV_FONT_DECLARE(lv_font_Acme_Regular_30)
LV_FONT_DECLARE(lv_font_montserratMedium_16)
LV_FONT_DECLARE(lv_font_montserratMedium_12)
LV_FONT_DECLARE(lv_font_Alatsi_Regular_16)
LV_FONT_DECLARE(lv_font_simsun_16)
LV_FONT_DECLARE(lv_font_Amiko_Regular_16)
LV_FONT_DECLARE(lv_font_Adventpro_regular_20)
LV_FONT_DECLARE(lv_font_Alatsi_Regular_30)
LV_FONT_DECLARE(lv_font_Alatsi_Regular_33)
LV_FONT_DECLARE(lv_font_simsun_18)
LV_FONT_DECLARE(lv_font_Alatsi_Regular_32)


#ifdef __cplusplus
}
#endif
#endif
