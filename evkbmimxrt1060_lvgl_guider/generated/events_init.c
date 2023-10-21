/*
* Copyright 2023 NXP
* NXP Confidential and Proprietary. This software is owned or controlled by NXP and may only be used strictly in
* accordance with the applicable license terms. By expressly accepting such terms or by downloading, installing,
* activating and/or otherwise using the software, you are agreeing that you have read, and that you agree to
* comply with and are bound by, such license terms.  If you do not agree to be bound by the applicable license
* terms, then you may not retain, install, activate or otherwise use the software.
*/

#include "events_init.h"
#include <stdio.h>
#include "lvgl.h"


static unsigned int Temp = 0;
static char tem[3];
static unsigned int Humidity = 0;
static char hum[3];
static void screen_img_1_event_handler (lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);

	switch (code) {
	case LV_EVENT_CLICKED:
	{
		//Write the load screen code.
	    lv_obj_t * act_scr = lv_scr_act();
	    lv_disp_t * d = lv_obj_get_disp(act_scr);
	    if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr)) {
	        if (guider_ui.screen_1_del == true) {
	          setup_scr_screen_1(&guider_ui);
	        }
	        lv_scr_load_anim(guider_ui.screen_1, LV_SCR_LOAD_ANIM_NONE, 200, 200, true);
	        guider_ui.screen_1_del = true;
	    }
		break;
	}
	default:
		break;
	}
}
static void screen_img_2_event_handler (lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);

	switch (code) {
	case LV_EVENT_CLICKED:
	{
		//Write the load screen code.
	    lv_obj_t * act_scr = lv_scr_act();
	    lv_disp_t * d = lv_obj_get_disp(act_scr);
	    if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr)) {
	        if (guider_ui.screen_2_del == true) {
	          setup_scr_screen_2(&guider_ui);
	        }
	        lv_scr_load_anim(guider_ui.screen_2, LV_SCR_LOAD_ANIM_NONE, 200, 200, true);
	        guider_ui.screen_2_del = true;
	    }
		break;
	}
	default:
		break;
	}
}
static void screen_img_3_event_handler (lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);

	switch (code) {
	case LV_EVENT_CLICKED:
	{
		//Write the load screen code.
	    lv_obj_t * act_scr = lv_scr_act();
	    lv_disp_t * d = lv_obj_get_disp(act_scr);
	    if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr)) {
	        if (guider_ui.screen_3_del == true) {
	          setup_scr_screen_3(&guider_ui);
	        }
	        lv_scr_load_anim(guider_ui.screen_3, LV_SCR_LOAD_ANIM_NONE, 200, 200, true);
	        guider_ui.screen_3_del = true;
	    }
		break;
	}
	default:
		break;
	}
}
void events_init_screen(lv_ui *ui)
{
	lv_obj_add_event_cb(ui->screen_img_1, screen_img_1_event_handler, LV_EVENT_ALL, NULL);
	lv_obj_add_event_cb(ui->screen_img_2, screen_img_2_event_handler, LV_EVENT_ALL, NULL);
	lv_obj_add_event_cb(ui->screen_img_3, screen_img_3_event_handler, LV_EVENT_ALL, NULL);
}
static void screen_1_back_event_handler (lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);

	switch (code) {
	case LV_EVENT_CLICKED:
	{
		//Write the load screen code.
	    lv_obj_t * act_scr = lv_scr_act();
	    lv_disp_t * d = lv_obj_get_disp(act_scr);
	    if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr)) {
	        if (guider_ui.screen_del == true) {
	          setup_scr_screen(&guider_ui);
	        }
	        lv_scr_load_anim(guider_ui.screen, LV_SCR_LOAD_ANIM_NONE, 200, 200, true);
	        guider_ui.screen_del = true;
	    }
		Temp = 0;
	Humidity = 0;
		break;
	}
	default:
		break;
	}
}
static void screen_1_T_plus_event_handler (lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);

	switch (code) {
	case LV_EVENT_CLICKED:
	{
		Temp++;
	sprintf(tem,  "%d" , Temp);
	lv_label_set_text(guider_ui.screen_1_Temp, tem);
		break;
	}
	default:
		break;
	}
}
static void screen_1_T_minus_event_handler (lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);

	switch (code) {
	case LV_EVENT_CLICKED:
	{
		Temp--;
	sprintf(tem,  "%d" , Temp);
	lv_label_set_text(guider_ui.screen_1_Temp, tem);
		break;
	}
	default:
		break;
	}
}
static void screen_1_H_minus_event_handler (lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);

	switch (code) {
	case LV_EVENT_CLICKED:
	{
		if(Humidity<=0){
	  break;
	}
	else{
	  Humidity--;
	  sprintf(hum,  "%d %%" , Humidity);
	  lv_label_set_text(guider_ui.screen_1_Humidity, hum);
	}
		break;
	}
	default:
		break;
	}
}
static void screen_1_H_plus_event_handler (lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);

	switch (code) {
	case LV_EVENT_CLICKED:
	{
		Humidity++;
	sprintf(hum,  "%d %%" , Humidity);
	lv_label_set_text(guider_ui.screen_1_Humidity, hum);
	
		break;
	}
	default:
		break;
	}
}
void events_init_screen_1(lv_ui *ui)
{
	lv_obj_add_event_cb(ui->screen_1_back, screen_1_back_event_handler, LV_EVENT_ALL, NULL);
	lv_obj_add_event_cb(ui->screen_1_T_plus, screen_1_T_plus_event_handler, LV_EVENT_ALL, NULL);
	lv_obj_add_event_cb(ui->screen_1_T_minus, screen_1_T_minus_event_handler, LV_EVENT_ALL, NULL);
	lv_obj_add_event_cb(ui->screen_1_H_minus, screen_1_H_minus_event_handler, LV_EVENT_ALL, NULL);
	lv_obj_add_event_cb(ui->screen_1_H_plus, screen_1_H_plus_event_handler, LV_EVENT_ALL, NULL);
}
static void screen_2_back_event_handler (lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);

	switch (code) {
	case LV_EVENT_CLICKED:
	{
		//Write the load screen code.
	    lv_obj_t * act_scr = lv_scr_act();
	    lv_disp_t * d = lv_obj_get_disp(act_scr);
	    if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr)) {
	        if (guider_ui.screen_del == true) {
	          setup_scr_screen(&guider_ui);
	        }
	        lv_scr_load_anim(guider_ui.screen, LV_SCR_LOAD_ANIM_NONE, 200, 200, true);
	        guider_ui.screen_del = true;
	    }
		Temp = 0;
	Humidity = 0;
		break;
	}
	default:
		break;
	}
}
static void screen_2_T_plus_event_handler (lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);

	switch (code) {
	case LV_EVENT_CLICKED:
	{
		Temp++;
	sprintf(tem,  "%d" , Temp);
	lv_label_set_text(guider_ui.screen_2_Temp, tem);
		break;
	}
	default:
		break;
	}
}
static void screen_2_T_minus_event_handler (lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);

	switch (code) {
	case LV_EVENT_CLICKED:
	{
		Temp--;
	sprintf(tem,  "%d" , Temp);
	lv_label_set_text(guider_ui.screen_2_Temp, tem);
		break;
	}
	default:
		break;
	}
}
static void screen_2_H_minus_event_handler (lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);

	switch (code) {
	case LV_EVENT_CLICKED:
	{
		if(Humidity<=0){
	  break;
	}
	else{
	  Humidity--;
	  sprintf(hum,  "%d %%" , Humidity);
	  lv_label_set_text(guider_ui.screen_2_Humidity, hum);
	}
	
		break;
	}
	default:
		break;
	}
}
static void screen_2_H_plus_event_handler (lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);

	switch (code) {
	case LV_EVENT_CLICKED:
	{
		Humidity++;
	sprintf(hum,  "%d %%" , Humidity);
	lv_label_set_text(guider_ui.screen_2_Humidity, hum);
	
		break;
	}
	default:
		break;
	}
}
void events_init_screen_2(lv_ui *ui)
{
	lv_obj_add_event_cb(ui->screen_2_back, screen_2_back_event_handler, LV_EVENT_ALL, NULL);
	lv_obj_add_event_cb(ui->screen_2_T_plus, screen_2_T_plus_event_handler, LV_EVENT_ALL, NULL);
	lv_obj_add_event_cb(ui->screen_2_T_minus, screen_2_T_minus_event_handler, LV_EVENT_ALL, NULL);
	lv_obj_add_event_cb(ui->screen_2_H_minus, screen_2_H_minus_event_handler, LV_EVENT_ALL, NULL);
	lv_obj_add_event_cb(ui->screen_2_H_plus, screen_2_H_plus_event_handler, LV_EVENT_ALL, NULL);
}
static void screen_3_back_event_handler (lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);

	switch (code) {
	case LV_EVENT_CLICKED:
	{
		//Write the load screen code.
	    lv_obj_t * act_scr = lv_scr_act();
	    lv_disp_t * d = lv_obj_get_disp(act_scr);
	    if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr)) {
	        if (guider_ui.screen_del == true) {
	          setup_scr_screen(&guider_ui);
	        }
	        lv_scr_load_anim(guider_ui.screen, LV_SCR_LOAD_ANIM_NONE, 200, 200, true);
	        guider_ui.screen_del = true;
	    }
		Temp = 0;
	Humidity = 0;
		break;
	}
	default:
		break;
	}
}
static void screen_3_T_plus_event_handler (lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);

	switch (code) {
	case LV_EVENT_CLICKED:
	{
		Temp++;
	sprintf(tem,  "%d" , Temp);
	lv_label_set_text(guider_ui.screen_3_Temp, tem);
		break;
	}
	default:
		break;
	}
}
static void screen_3_T_minus_event_handler (lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);

	switch (code) {
	case LV_EVENT_CLICKED:
	{
		Temp--;
	sprintf(tem,  "%d" , Temp);
	lv_label_set_text(guider_ui.screen_3_Temp, tem);
		break;
	}
	default:
		break;
	}
}
static void screen_3_H_minus_event_handler (lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);

	switch (code) {
	case LV_EVENT_CLICKED:
	{
		if(Humidity<=0){
	  break;
	}
	else{
	  Humidity--;
	  sprintf(hum,  "%d %%" , Humidity);
	  lv_label_set_text(guider_ui.screen_3_Humidity, hum);
	}
		break;
	}
	default:
		break;
	}
}
static void screen_3_H_plus_event_handler (lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);

	switch (code) {
	case LV_EVENT_CLICKED:
	{
		Humidity++;
	sprintf(hum,  "%d %%" , Humidity);
	lv_label_set_text(guider_ui.screen_3_Humidity, hum);
	
		break;
	}
	default:
		break;
	}
}
void events_init_screen_3(lv_ui *ui)
{
	lv_obj_add_event_cb(ui->screen_3_back, screen_3_back_event_handler, LV_EVENT_ALL, NULL);
	lv_obj_add_event_cb(ui->screen_3_T_plus, screen_3_T_plus_event_handler, LV_EVENT_ALL, NULL);
	lv_obj_add_event_cb(ui->screen_3_T_minus, screen_3_T_minus_event_handler, LV_EVENT_ALL, NULL);
	lv_obj_add_event_cb(ui->screen_3_H_minus, screen_3_H_minus_event_handler, LV_EVENT_ALL, NULL);
	lv_obj_add_event_cb(ui->screen_3_H_plus, screen_3_H_plus_event_handler, LV_EVENT_ALL, NULL);
}

void events_init(lv_ui *ui)
{

}
