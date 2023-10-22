/*
* Copyright 2023 NXP
* NXP Confidential and Proprietary. This software is owned or controlled by NXP and may only be used strictly in
* accordance with the applicable license terms. By expressly accepting such terms or by downloading, installing,
* activating and/or otherwise using the software, you are agreeing that you have read, and that you agree to
* comply with and are bound by, such license terms.  If you do not agree to be bound by the applicable license
* terms, then you may not retain, install, activate or otherwise use the software.
*/

#include "events_init.h"
#include "board.h"
#include <stdio.h>
#include "lvgl.h"


static void screen_img_1_event_handler (lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);

	switch (code) {
	case LV_EVENT_CLICKED:
	{
		//Write the load screen code.
	    lv_obj_t * act_scr = lv_scr_act();
	    	    if(act_scr == guider_ui.screen1 || act_scr == guider_ui.screen_1){
	    	    			if(Temp - curr_temp > 3 || Temp - curr_temp < 3 || Humidity - curr_hum > 10 || Humidity - curr_hum < 10){
	    	    				USER_FAN_ON();
	    	    			}else USER_FAN_OFF();
	    	    		}else if(act_scr == guider_ui.screen2 || act_scr == guider_ui.screen_2){
	    	    			if(Temp2 - curr_temp > 3 || Temp2 - curr_temp < 3 || Humidity2 - curr_hum > 10 || Humidity2 - curr_hum < 10){
	    	    				USER_FAN_ON();
	    	    			}else USER_FAN_OFF();
	    	    		}else if(act_scr == guider_ui.screen3 || act_scr == guider_ui.screen_3){
	    	    			if(Temp3 - curr_temp > 3 || Temp3 - curr_temp < 3 || Humidity3 - curr_hum > 10 || Humidity3 - curr_hum < 10){
	    	    				USER_FAN_ON();
	    	    			}else USER_FAN_OFF();
	    	    		}
	    lv_disp_t * d = lv_obj_get_disp(act_scr);
	    if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr)) {
	        if (guider_ui.screen1_del == true) {
	          setup_scr_screen1(&guider_ui);
	        }
	        lv_scr_load_anim(guider_ui.screen1, LV_SCR_LOAD_ANIM_NONE, 200, 200, true);
	        guider_ui.screen1_del = true;
	    }
		sprintf(hum,  "%d %%" , Humidity);
		sprintf(curr_h, "%d", curr_hum);
	lv_label_set_text(guider_ui.screen1_H1, curr_h);
	
	sprintf(tem,  "%d" , Temp);
	sprintf(curr_t, "%d", curr_temp);
	lv_label_set_text(guider_ui.screen1_T1, curr_t);
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

	    	    if(act_scr == guider_ui.screen1 || act_scr == guider_ui.screen_1){
	    	    			if(Temp - curr_temp > 3 || Temp - curr_temp < 3 || Humidity - curr_hum > 10 || Humidity - curr_hum < 10){
	    	    				USER_FAN_ON();
	    	    			}else USER_FAN_OFF();
	    	    		}else if(act_scr == guider_ui.screen2 || act_scr == guider_ui.screen_2){
	    	    			if(Temp2 - curr_temp > 3 || Temp2 - curr_temp < 3 || Humidity2 - curr_hum > 10 || Humidity2 - curr_hum < 10){
	    	    				USER_FAN_ON();
	    	    			}else USER_FAN_OFF();
	    	    		}else if(act_scr == guider_ui.screen3 || act_scr == guider_ui.screen_3){
	    	    			if(Temp3 - curr_temp > 3 || Temp3 - curr_temp < 3 || Humidity3 - curr_hum > 10 || Humidity3 - curr_hum < 10){
	    	    				USER_FAN_ON();
	    	    			}else USER_FAN_OFF();
	    	    		}
	    lv_disp_t * d = lv_obj_get_disp(act_scr);
	    if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr)) {
	        if (guider_ui.screen2_del == true) {
	          setup_scr_screen2(&guider_ui);
	        }
	        lv_scr_load_anim(guider_ui.screen2, LV_SCR_LOAD_ANIM_NONE, 200, 200, true);
	        guider_ui.screen2_del = true;
	    }
		sprintf(hum2,  "%d %%" , Humidity2);
		sprintf(curr_h, "%d", curr_hum);
	lv_label_set_text(guider_ui.screen2_H2, curr_h);
	
	sprintf(tem2,  "%d" , Temp2);
	sprintf(curr_t, "%d", curr_temp);
	lv_label_set_text(guider_ui.screen2_T2, curr_t);
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

	    	    if(act_scr == guider_ui.screen1 || act_scr == guider_ui.screen_1){
	    	    			if(Temp - curr_temp > 3 || Temp - curr_temp < 3 || Humidity - curr_hum > 10 || Humidity - curr_hum < 10){
	    	    				USER_FAN_ON();
	    	    			}else USER_FAN_OFF();
	    	    		}else if(act_scr == guider_ui.screen2 || act_scr == guider_ui.screen_2){
	    	    			if(Temp2 - curr_temp > 3 || Temp2 - curr_temp < 3 || Humidity2 - curr_hum > 10 || Humidity2 - curr_hum < 10){
	    	    				USER_FAN_ON();
	    	    			}else USER_FAN_OFF();
	    	    		}else if(act_scr == guider_ui.screen3 || act_scr == guider_ui.screen_3){
	    	    			if(Temp3 - curr_temp > 3 || Temp3 - curr_temp < 3 || Humidity3 - curr_hum > 10 || Humidity3 - curr_hum < 10){
	    	    				USER_FAN_ON();
	    	    			}else USER_FAN_OFF();
	    	    		}
	    lv_disp_t * d = lv_obj_get_disp(act_scr);
	    if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr)) {
	        if (guider_ui.screen3_del == true) {
	          setup_scr_screen3(&guider_ui);
	        }
	        lv_scr_load_anim(guider_ui.screen3, LV_SCR_LOAD_ANIM_NONE, 200, 200, true);
	        guider_ui.screen3_del = true;
	    }
		sprintf(hum3,  "%d %%" , Humidity3);
		sprintf(curr_h, "%d", curr_hum);
	lv_label_set_text(guider_ui.screen3_H3, curr_h);
	
	sprintf(tem3,  "%d" , Temp3);
	sprintf(curr_t, "%d", curr_temp);
	lv_label_set_text(guider_ui.screen3_T3, curr_t);
		break;
	}
	default:
		break;
	}
}
static void screen_btn_1_event_handler (lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);

	switch (code) {
	case LV_EVENT_CLICKED:
	{
		//Write the load screen code.
	    lv_obj_t * act_scr = lv_scr_act();

	    	    if(act_scr == guider_ui.screen1 || act_scr == guider_ui.screen_1){
	    	    			if(Temp - curr_temp > 3 || Temp - curr_temp < 3 || Humidity - curr_hum > 10 || Humidity - curr_hum < 10){
	    	    				USER_FAN_ON();
	    	    			}else USER_FAN_OFF();
	    	    		}else if(act_scr == guider_ui.screen2 || act_scr == guider_ui.screen_2){
	    	    			if(Temp2 - curr_temp > 3 || Temp2 - curr_temp < 3 || Humidity2 - curr_hum > 10 || Humidity2 - curr_hum < 10){
	    	    				USER_FAN_ON();
	    	    			}else USER_FAN_OFF();
	    	    		}else if(act_scr == guider_ui.screen3 || act_scr == guider_ui.screen_3){
	    	    			if(Temp3 - curr_temp > 3 || Temp3 - curr_temp < 3 || Humidity3 - curr_hum > 10 || Humidity3 - curr_hum < 10){
	    	    				USER_FAN_ON();
	    	    			}else USER_FAN_OFF();
	    	    		}
	    lv_disp_t * d = lv_obj_get_disp(act_scr);
	    if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr)) {
	        if (guider_ui.add_del == true) {
	          setup_scr_add(&guider_ui);
	        }
	        lv_scr_load_anim(guider_ui.add, LV_SCR_LOAD_ANIM_NONE, 200, 200, true);
	        guider_ui.add_del = true;
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
	lv_obj_add_event_cb(ui->screen_btn_1, screen_btn_1_event_handler, LV_EVENT_ALL, NULL);
}
static void screen1_Menu_event_handler (lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);

	switch (code) {
	case LV_EVENT_CLICKED:
	{
		//Write the load screen code.
	    lv_obj_t * act_scr = lv_scr_act();

	    	    if(act_scr == guider_ui.screen1 || act_scr == guider_ui.screen_1){
	    	    			if(Temp - curr_temp > 3 || Temp - curr_temp < 3 || Humidity - curr_hum > 10 || Humidity - curr_hum < 10){
	    	    				USER_FAN_ON();
	    	    			}else USER_FAN_OFF();
	    	    		}else if(act_scr == guider_ui.screen2 || act_scr == guider_ui.screen_2){
	    	    			if(Temp2 - curr_temp > 3 || Temp2 - curr_temp < 3 || Humidity2 - curr_hum > 10 || Humidity2 - curr_hum < 10){
	    	    				USER_FAN_ON();
	    	    			}else USER_FAN_OFF();
	    	    		}else if(act_scr == guider_ui.screen3 || act_scr == guider_ui.screen_3){
	    	    			if(Temp3 - curr_temp > 3 || Temp3 - curr_temp < 3 || Humidity3 - curr_hum > 10 || Humidity3 - curr_hum < 10){
	    	    				USER_FAN_ON();
	    	    			}else USER_FAN_OFF();
	    	    		}
	    lv_disp_t * d = lv_obj_get_disp(act_scr);
	    if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr)) {
	        if (guider_ui.screen_del == true) {
	          setup_scr_screen(&guider_ui);
	        }
	        lv_scr_load_anim(guider_ui.screen, LV_SCR_LOAD_ANIM_NONE, 200, 200, true);
	        guider_ui.screen_del = true;
	    }
		break;
	}
	default:
		break;
	}
}
static void screen1_btn_1_event_handler (lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);

	switch (code) {
	case LV_EVENT_CLICKED:
	{
		//Write the load screen code.
	    lv_obj_t * act_scr = lv_scr_act();

	    if(act_scr == guider_ui.screen1 || act_scr == guider_ui.screen_1){
			if(Temp - curr_temp > 3 || Temp - curr_temp < 3 || Humidity - curr_hum > 10 || Humidity - curr_hum < 10){
				USER_FAN_ON();
			}else USER_FAN_OFF();
		}else if(act_scr == guider_ui.screen2 || act_scr == guider_ui.screen_2){
			if(Temp2 - curr_temp > 3 || Temp2 - curr_temp < 3 || Humidity2 - curr_hum > 10 || Humidity2 - curr_hum < 10){
				USER_FAN_ON();
			}else USER_FAN_OFF();
		}else if(act_scr == guider_ui.screen3 || act_scr == guider_ui.screen_3){
			if(Temp3 - curr_temp > 3 || Temp3 - curr_temp < 3 || Humidity3 - curr_hum > 10 || Humidity3 - curr_hum < 10){
				USER_FAN_ON();
			}else USER_FAN_OFF();
		}
	    lv_disp_t * d = lv_obj_get_disp(act_scr);
	    if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr)) {
	        if (guider_ui.screen_1_del == true) {
	          setup_scr_screen_1(&guider_ui);
	        }
	        lv_scr_load_anim(guider_ui.screen_1, LV_SCR_LOAD_ANIM_NONE, 200, 200, true);
	        guider_ui.screen_1_del = true;
	    }
		sprintf(hum,  "%d %%" , Humidity);
	lv_label_set_text(guider_ui.screen_1_Humidity, hum);
	
	sprintf(tem,  "%d" , Temp);
	lv_label_set_text(guider_ui.screen_1_Temp, tem);
		break;
	}
	default:
		break;
	}
}
void events_init_screen1(lv_ui *ui)
{
	lv_obj_add_event_cb(ui->screen1_Menu, screen1_Menu_event_handler, LV_EVENT_ALL, NULL);
	lv_obj_add_event_cb(ui->screen1_btn_1, screen1_btn_1_event_handler, LV_EVENT_ALL, NULL);
}
static void screen2_Menu_event_handler (lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);

	switch (code) {
	case LV_EVENT_CLICKED:
	{
		//Write the load screen code.
	    lv_obj_t * act_scr = lv_scr_act();
	    if(act_scr == guider_ui.screen1 || act_scr == guider_ui.screen_1){
			if(Temp - curr_temp > 3 || Temp - curr_temp < 3 || Humidity - curr_hum > 10 || Humidity - curr_hum < 10){
				USER_FAN_ON();
			}else USER_FAN_OFF();
		}else if(act_scr == guider_ui.screen2 || act_scr == guider_ui.screen_2){
			if(Temp2 - curr_temp > 3 || Temp2 - curr_temp < 3 || Humidity2 - curr_hum > 10 || Humidity2 - curr_hum < 10){
				USER_FAN_ON();
			}else USER_FAN_OFF();
		}else if(act_scr == guider_ui.screen3 || act_scr == guider_ui.screen_3){
			if(Temp3 - curr_temp > 3 || Temp3 - curr_temp < 3 || Humidity3 - curr_hum > 10 || Humidity3 - curr_hum < 10){
				USER_FAN_ON();
			}else USER_FAN_OFF();
		}
	    lv_disp_t * d = lv_obj_get_disp(act_scr);
	    if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr)) {
	        if (guider_ui.screen_del == true) {
	          setup_scr_screen(&guider_ui);
	        }
	        lv_scr_load_anim(guider_ui.screen, LV_SCR_LOAD_ANIM_NONE, 200, 200, true);
	        guider_ui.screen_del = true;
	    }
		break;
	}
	default:
		break;
	}
}
static void screen2_btn_1_event_handler (lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);

	switch (code) {
	case LV_EVENT_CLICKED:
	{
		//Write the load screen code.
	    lv_obj_t * act_scr = lv_scr_act();
	    if(act_scr == guider_ui.screen1 || act_scr == guider_ui.screen_1){
	    			if(Temp - curr_temp > 3 || Temp - curr_temp < 3 || Humidity - curr_hum > 10 || Humidity - curr_hum < 10){
	    				USER_FAN_ON();
	    			}else USER_FAN_OFF();
	    		}else if(act_scr == guider_ui.screen2 || act_scr == guider_ui.screen_2){
	    			if(Temp2 - curr_temp > 3 || Temp2 - curr_temp < 3 || Humidity2 - curr_hum > 10 || Humidity2 - curr_hum < 10){
	    				USER_FAN_ON();
	    			}else USER_FAN_OFF();
	    		}else if(act_scr == guider_ui.screen3 || act_scr == guider_ui.screen_3){
	    			if(Temp3 - curr_temp > 3 || Temp3 - curr_temp < 3 || Humidity3 - curr_hum > 10 || Humidity3 - curr_hum < 10){
	    				USER_FAN_ON();
	    			}else USER_FAN_OFF();
	    		}
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
void events_init_screen2(lv_ui *ui)
{
	lv_obj_add_event_cb(ui->screen2_Menu, screen2_Menu_event_handler, LV_EVENT_ALL, NULL);
	lv_obj_add_event_cb(ui->screen2_btn_1, screen2_btn_1_event_handler, LV_EVENT_ALL, NULL);
}
static void screen3_Menu_event_handler (lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);

	switch (code) {
	case LV_EVENT_CLICKED:
	{
		//Write the load screen code.
	    lv_obj_t * act_scr = lv_scr_act();
	    if(act_scr == guider_ui.screen1 || act_scr == guider_ui.screen_1){
	    			if(Temp - curr_temp > 3 || Temp - curr_temp < 3 || Humidity - curr_hum > 10 || Humidity - curr_hum < 10){
	    				USER_FAN_ON();
	    			}else USER_FAN_OFF();
	    		}else if(act_scr == guider_ui.screen2 || act_scr == guider_ui.screen_2){
	    			if(Temp2 - curr_temp > 3 || Temp2 - curr_temp < 3 || Humidity2 - curr_hum > 10 || Humidity2 - curr_hum < 10){
	    				USER_FAN_ON();
	    			}else USER_FAN_OFF();
	    		}else if(act_scr == guider_ui.screen3 || act_scr == guider_ui.screen_3){
	    			if(Temp3 - curr_temp > 3 || Temp3 - curr_temp < 3 || Humidity3 - curr_hum > 10 || Humidity3 - curr_hum < 10){
	    				USER_FAN_ON();
	    			}else USER_FAN_OFF();
	    		}
	    lv_disp_t * d = lv_obj_get_disp(act_scr);
	    if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr)) {
	        if (guider_ui.screen_del == true) {
	          setup_scr_screen(&guider_ui);
	        }
	        lv_scr_load_anim(guider_ui.screen, LV_SCR_LOAD_ANIM_NONE, 200, 200, true);
	        guider_ui.screen_del = true;
	    }
		sprintf(hum3,  "%d %%" , Humidity3);
		sprintf(curr_h, "%d", curr_hum);
	lv_label_set_text(guider_ui.screen3_H3, curr_h);
	
	sprintf(tem3,  "%d" , Temp3);
	sprintf(curr_t, "%d", curr_temp);
	lv_label_set_text(guider_ui.screen3_T3, curr_t);
		break;
	}
	default:
		break;
	}
}
static void screen3_btn_1_event_handler (lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);

	switch (code) {
	case LV_EVENT_CLICKED:
	{
		//Write the load screen code.
	    lv_obj_t * act_scr = lv_scr_act();
	    if(act_scr == guider_ui.screen1 || act_scr == guider_ui.screen_1){
	    			if(Temp - curr_temp > 3 || Temp - curr_temp < 3 || Humidity - curr_hum > 10 || Humidity - curr_hum < 10){
	    				USER_FAN_ON();
	    			}else USER_FAN_OFF();
	    		}else if(act_scr == guider_ui.screen2 || act_scr == guider_ui.screen_2){
	    			if(Temp2 - curr_temp > 3 || Temp2 - curr_temp < 3 || Humidity2 - curr_hum > 10 || Humidity2 - curr_hum < 10){
	    				USER_FAN_ON();
	    			}else USER_FAN_OFF();
	    		}else if(act_scr == guider_ui.screen3 || act_scr == guider_ui.screen_3){
	    			if(Temp3 - curr_temp > 3 || Temp3 - curr_temp < 3 || Humidity3 - curr_hum > 10 || Humidity3 - curr_hum < 10){
	    				USER_FAN_ON();
	    			}else USER_FAN_OFF();
	    		}
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
void events_init_screen3(lv_ui *ui)
{
	lv_obj_add_event_cb(ui->screen3_Menu, screen3_Menu_event_handler, LV_EVENT_ALL, NULL);
	lv_obj_add_event_cb(ui->screen3_btn_1, screen3_btn_1_event_handler, LV_EVENT_ALL, NULL);
}
static void screen_1_back_event_handler (lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);

	switch (code) {
	case LV_EVENT_CLICKED:
	{
		//Write the load screen code.
	    lv_obj_t * act_scr = lv_scr_act();
	    if(act_scr == guider_ui.screen1 || act_scr == guider_ui.screen_1){
	    			if(Temp - curr_temp > 3 || Temp - curr_temp < 3 || Humidity - curr_hum > 10 || Humidity - curr_hum < 10){
	    				USER_FAN_ON();
	    			}else USER_FAN_OFF();
	    		}else if(act_scr == guider_ui.screen2 || act_scr == guider_ui.screen_2){
	    			if(Temp2 - curr_temp > 3 || Temp2 - curr_temp < 3 || Humidity2 - curr_hum > 10 || Humidity2 - curr_hum < 10){
	    				USER_FAN_ON();
	    			}else USER_FAN_OFF();
	    		}else if(act_scr == guider_ui.screen3 || act_scr == guider_ui.screen_3){
	    			if(Temp3 - curr_temp > 3 || Temp3 - curr_temp < 3 || Humidity3 - curr_hum > 10 || Humidity3 - curr_hum < 10){
	    				USER_FAN_ON();
	    			}else USER_FAN_OFF();
	    		}
	    lv_disp_t * d = lv_obj_get_disp(act_scr);
	    if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr)) {
	        if (guider_ui.screen1_del == true) {
	          setup_scr_screen1(&guider_ui);
	        }
	        lv_scr_load_anim(guider_ui.screen1, LV_SCR_LOAD_ANIM_NONE, 200, 200, true);
	        guider_ui.screen1_del = true;
	    }
		sprintf(hum,  "%d %%" , Humidity);
		sprintf(curr_h, "%d", curr_hum);
	lv_label_set_text(guider_ui.screen1_H1, curr_h);
	
	sprintf(tem,  "%d" , Temp);
	sprintf(curr_t, "%d", curr_temp);
	lv_label_set_text(guider_ui.screen1_T1, curr_t);
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
	lv_obj_t * act_scr = lv_scr_act();
		    if(act_scr == guider_ui.screen1 || act_scr == guider_ui.screen_1){
		    			if(Temp - curr_temp > 3 || Temp - curr_temp < 3 || Humidity - curr_hum > 10 || Humidity - curr_hum < 10){
		    				USER_FAN_ON();
		    			}else USER_FAN_OFF();
		    		}else if(act_scr == guider_ui.screen2 || act_scr == guider_ui.screen_2){
		    			if(Temp2 - curr_temp > 3 || Temp2 - curr_temp < 3 || Humidity2 - curr_hum > 10 || Humidity2 - curr_hum < 10){
		    				USER_FAN_ON();
		    			}else USER_FAN_OFF();
		    		}else if(act_scr == guider_ui.screen3 || act_scr == guider_ui.screen_3){
		    			if(Temp3 - curr_temp > 3 || Temp3 - curr_temp < 3 || Humidity3 - curr_hum > 10 || Humidity3 - curr_hum < 10){
		    				USER_FAN_ON();
		    			}else USER_FAN_OFF();
		    		}
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
	lv_obj_t * act_scr = lv_scr_act();
		    if(act_scr == guider_ui.screen1 || act_scr == guider_ui.screen_1){
		    			if(Temp - curr_temp > 3 || Temp - curr_temp < 3 || Humidity - curr_hum > 10 || Humidity - curr_hum < 10){
		    				USER_FAN_ON();
		    			}else USER_FAN_OFF();
		    		}else if(act_scr == guider_ui.screen2 || act_scr == guider_ui.screen_2){
		    			if(Temp2 - curr_temp > 3 || Temp2 - curr_temp < 3 || Humidity2 - curr_hum > 10 || Humidity2 - curr_hum < 10){
		    				USER_FAN_ON();
		    			}else USER_FAN_OFF();
		    		}else if(act_scr == guider_ui.screen3 || act_scr == guider_ui.screen_3){
		    			if(Temp3 - curr_temp > 3 || Temp3 - curr_temp < 3 || Humidity3 - curr_hum > 10 || Humidity3 - curr_hum < 10){
		    				USER_FAN_ON();
		    			}else USER_FAN_OFF();
		    		}
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
	lv_obj_t * act_scr = lv_scr_act();
		    if(act_scr == guider_ui.screen1 || act_scr == guider_ui.screen_1){
		    			if(Temp - curr_temp > 3 || Temp - curr_temp < 3 || Humidity - curr_hum > 10 || Humidity - curr_hum < 10){
		    				USER_FAN_ON();
		    			}else USER_FAN_OFF();
		    		}else if(act_scr == guider_ui.screen2 || act_scr == guider_ui.screen_2){
		    			if(Temp2 - curr_temp > 3 || Temp2 - curr_temp < 3 || Humidity2 - curr_hum > 10 || Humidity2 - curr_hum < 10){
		    				USER_FAN_ON();
		    			}else USER_FAN_OFF();
		    		}else if(act_scr == guider_ui.screen3 || act_scr == guider_ui.screen_3){
		    			if(Temp3 - curr_temp > 3 || Temp3 - curr_temp < 3 || Humidity3 - curr_hum > 10 || Humidity3 - curr_hum < 10){
		    				USER_FAN_ON();
		    			}else USER_FAN_OFF();
		    		}
	
		break;
	}
	default:
		break;
	}
}
static void screen_1_Reset_T_event_handler (lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);

	switch (code) {
	case LV_EVENT_CLICKED:
	{
		Temp = 25;
	sprintf(tem,"%d",Temp);
	lv_label_set_text(guider_ui.screen_1_Temp, tem);
	lv_obj_t * act_scr = lv_scr_act();
		    if(act_scr == guider_ui.screen1 || act_scr == guider_ui.screen_1){
		    			if(Temp - curr_temp > 3 || Temp - curr_temp < 3 || Humidity - curr_hum > 10 || Humidity - curr_hum < 10){
		    				USER_FAN_ON();
		    			}else USER_FAN_OFF();
		    		}else if(act_scr == guider_ui.screen2 || act_scr == guider_ui.screen_2){
		    			if(Temp2 - curr_temp > 3 || Temp2 - curr_temp < 3 || Humidity2 - curr_hum > 10 || Humidity2 - curr_hum < 10){
		    				USER_FAN_ON();
		    			}else USER_FAN_OFF();
		    		}else if(act_scr == guider_ui.screen3 || act_scr == guider_ui.screen_3){
		    			if(Temp3 - curr_temp > 3 || Temp3 - curr_temp < 3 || Humidity3 - curr_hum > 10 || Humidity3 - curr_hum < 10){
		    				USER_FAN_ON();
		    			}else USER_FAN_OFF();
		    		}
		break;
	}
	default:
		break;
	}
}
static void screen_1_Reset_H_event_handler (lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);

	switch (code) {
	case LV_EVENT_CLICKED:
	{
		Humidity = 40;
	sprintf(hum,"%d %%", Humidity);
	lv_label_set_text(guider_ui.screen_1_Humidity, hum);
	lv_obj_t * act_scr = lv_scr_act();
		    if(act_scr == guider_ui.screen1 || act_scr == guider_ui.screen_1){
		    			if(Temp - curr_temp > 3 || Temp - curr_temp < 3 || Humidity - curr_hum > 10 || Humidity - curr_hum < 10){
		    				USER_FAN_ON();
		    			}else USER_FAN_OFF();
		    		}else if(act_scr == guider_ui.screen2 || act_scr == guider_ui.screen_2){
		    			if(Temp2 - curr_temp > 3 || Temp2 - curr_temp < 3 || Humidity2 - curr_hum > 10 || Humidity2 - curr_hum < 10){
		    				USER_FAN_ON();
		    			}else USER_FAN_OFF();
		    		}else if(act_scr == guider_ui.screen3 || act_scr == guider_ui.screen_3){
		    			if(Temp3 - curr_temp > 3 || Temp3 - curr_temp < 3 || Humidity3 - curr_hum > 10 || Humidity3 - curr_hum < 10){
		    				USER_FAN_ON();
		    			}else USER_FAN_OFF();
		    		}
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
	lv_obj_add_event_cb(ui->screen_1_Reset_T, screen_1_Reset_T_event_handler, LV_EVENT_ALL, NULL);
	lv_obj_add_event_cb(ui->screen_1_Reset_H, screen_1_Reset_H_event_handler, LV_EVENT_ALL, NULL);
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
	        if (guider_ui.screen2_del == true) {
	          setup_scr_screen2(&guider_ui);
	        }
	        lv_scr_load_anim(guider_ui.screen2, LV_SCR_LOAD_ANIM_NONE, 200, 200, true);
	        guider_ui.screen2_del = true;
	    }
		sprintf(hum2,  "%d %%" , Humidity2);
		sprintf(curr_h, "%d", curr_hum);
	lv_label_set_text(guider_ui.screen2_H2, curr_h);
	
	sprintf(tem2,  "%d" , Temp2);
	sprintf(curr_t, "%d", curr_temp);
	lv_label_set_text(guider_ui.screen2_T2, curr_t);
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
		Temp2++;
	sprintf(tem2,  "%d" , Temp2);
	lv_label_set_text(guider_ui.screen_2_Temp2, tem2);
	lv_obj_t * act_scr = lv_scr_act();
		    if(act_scr == guider_ui.screen1 || act_scr == guider_ui.screen_1){
		    			if(Temp - curr_temp > 3 || Temp - curr_temp < 3 || Humidity - curr_hum > 10 || Humidity - curr_hum < 10){
		    				USER_FAN_ON();
		    			}else USER_FAN_OFF();
		    		}else if(act_scr == guider_ui.screen2 || act_scr == guider_ui.screen_2){
		    			if(Temp2 - curr_temp > 3 || Temp2 - curr_temp < 3 || Humidity2 - curr_hum > 10 || Humidity2 - curr_hum < 10){
		    				USER_FAN_ON();
		    			}else USER_FAN_OFF();
		    		}else if(act_scr == guider_ui.screen3 || act_scr == guider_ui.screen_3){
		    			if(Temp3 - curr_temp > 3 || Temp3 - curr_temp < 3 || Humidity3 - curr_hum > 10 || Humidity3 - curr_hum < 10){
		    				USER_FAN_ON();
		    			}else USER_FAN_OFF();
		    		}
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
		Temp2--;
	sprintf(tem2,  "%d" , Temp2);
	lv_label_set_text(guider_ui.screen_2_Temp2, tem2);
	lv_obj_t * act_scr = lv_scr_act();
		    if(act_scr == guider_ui.screen1 || act_scr == guider_ui.screen_1){
		    			if(Temp - curr_temp > 3 || Temp - curr_temp < 3 || Humidity - curr_hum > 10 || Humidity - curr_hum < 10){
		    				USER_FAN_ON();
		    			}else USER_FAN_OFF();
		    		}else if(act_scr == guider_ui.screen2 || act_scr == guider_ui.screen_2){
		    			if(Temp2 - curr_temp > 3 || Temp2 - curr_temp < 3 || Humidity2 - curr_hum > 10 || Humidity2 - curr_hum < 10){
		    				USER_FAN_ON();
		    			}else USER_FAN_OFF();
		    		}else if(act_scr == guider_ui.screen3 || act_scr == guider_ui.screen_3){
		    			if(Temp3 - curr_temp > 3 || Temp3 - curr_temp < 3 || Humidity3 - curr_hum > 10 || Humidity3 - curr_hum < 10){
		    				USER_FAN_ON();
		    			}else USER_FAN_OFF();
		    		}
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
		if(Humidity2<=0){
	  break;
	}
	else{
	  Humidity2--;
	  sprintf(hum2,  "%d %%" , Humidity2);
	  lv_label_set_text(guider_ui.screen_2_Humidity2, hum2);
	  lv_obj_t * act_scr = lv_scr_act();
	  	    if(act_scr == guider_ui.screen1 || act_scr == guider_ui.screen_1){
	  	    			if(Temp - curr_temp > 3 || Temp - curr_temp < 3 || Humidity - curr_hum > 10 || Humidity - curr_hum < 10){
	  	    				USER_FAN_ON();
	  	    			}else USER_FAN_OFF();
	  	    		}else if(act_scr == guider_ui.screen2 || act_scr == guider_ui.screen_2){
	  	    			if(Temp2 - curr_temp > 3 || Temp2 - curr_temp < 3 || Humidity2 - curr_hum > 10 || Humidity2 - curr_hum < 10){
	  	    				USER_FAN_ON();
	  	    			}else USER_FAN_OFF();
	  	    		}else if(act_scr == guider_ui.screen3 || act_scr == guider_ui.screen_3){
	  	    			if(Temp3 - curr_temp > 3 || Temp3 - curr_temp < 3 || Humidity3 - curr_hum > 10 || Humidity3 - curr_hum < 10){
	  	    				USER_FAN_ON();
	  	    			}else USER_FAN_OFF();
	  	    		}
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
		Humidity2++;
	sprintf(hum2,  "%d %%" , Humidity2);
	lv_label_set_text(guider_ui.screen_2_Humidity2, hum2);
	lv_obj_t * act_scr = lv_scr_act();
		    if(act_scr == guider_ui.screen1 || act_scr == guider_ui.screen_1){
		    			if(Temp - curr_temp > 3 || Temp - curr_temp < 3 || Humidity - curr_hum > 10 || Humidity - curr_hum < 10){
		    				USER_FAN_ON();
		    			}else USER_FAN_OFF();
		    		}else if(act_scr == guider_ui.screen2 || act_scr == guider_ui.screen_2){
		    			if(Temp2 - curr_temp > 3 || Temp2 - curr_temp < 3 || Humidity2 - curr_hum > 10 || Humidity2 - curr_hum < 10){
		    				USER_FAN_ON();
		    			}else USER_FAN_OFF();
		    		}else if(act_scr == guider_ui.screen3 || act_scr == guider_ui.screen_3){
		    			if(Temp3 - curr_temp > 3 || Temp3 - curr_temp < 3 || Humidity3 - curr_hum > 10 || Humidity3 - curr_hum < 10){
		    				USER_FAN_ON();
		    			}else USER_FAN_OFF();
		    		}
	
		break;
	}
	default:
		break;
	}
}
static void screen_2_btn_2_event_handler (lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);

	switch (code) {
	case LV_EVENT_CLICKED:
	{
		Humidity2 = 40;
	sprintf(hum2,"%d %%", Humidity2);
	lv_label_set_text(guider_ui.screen_2_Humidity2, hum2);
	lv_obj_t * act_scr = lv_scr_act();
		    if(act_scr == guider_ui.screen1 || act_scr == guider_ui.screen_1){
		    			if(Temp - curr_temp > 3 || Temp - curr_temp < 3 || Humidity - curr_hum > 10 || Humidity - curr_hum < 10){
		    				USER_FAN_ON();
		    			}else USER_FAN_OFF();
		    		}else if(act_scr == guider_ui.screen2 || act_scr == guider_ui.screen_2){
		    			if(Temp2 - curr_temp > 3 || Temp2 - curr_temp < 3 || Humidity2 - curr_hum > 10 || Humidity2 - curr_hum < 10){
		    				USER_FAN_ON();
		    			}else USER_FAN_OFF();
		    		}else if(act_scr == guider_ui.screen3 || act_scr == guider_ui.screen_3){
		    			if(Temp3 - curr_temp > 3 || Temp3 - curr_temp < 3 || Humidity3 - curr_hum > 10 || Humidity3 - curr_hum < 10){
		    				USER_FAN_ON();
		    			}else USER_FAN_OFF();
		    		}
		break;
	}
	default:
		break;
	}
}
static void screen_2_btn_1_event_handler (lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);

	switch (code) {
	case LV_EVENT_CLICKED:
	{
		Temp2 = 25;
	sprintf(tem2,"%d",Temp2);
	lv_label_set_text(guider_ui.screen_2_Temp2, tem2);
	lv_obj_t * act_scr = lv_scr_act();
		    if(act_scr == guider_ui.screen1 || act_scr == guider_ui.screen_1){
		    			if(Temp - curr_temp > 3 || Temp - curr_temp < 3 || Humidity - curr_hum > 10 || Humidity - curr_hum < 10){
		    				USER_FAN_ON();
		    			}else USER_FAN_OFF();
		    		}else if(act_scr == guider_ui.screen2 || act_scr == guider_ui.screen_2){
		    			if(Temp2 - curr_temp > 3 || Temp2 - curr_temp < 3 || Humidity2 - curr_hum > 10 || Humidity2 - curr_hum < 10){
		    				USER_FAN_ON();
		    			}else USER_FAN_OFF();
		    		}else if(act_scr == guider_ui.screen3 || act_scr == guider_ui.screen_3){
		    			if(Temp3 - curr_temp > 3 || Temp3 - curr_temp < 3 || Humidity3 - curr_hum > 10 || Humidity3 - curr_hum < 10){
		    				USER_FAN_ON();
		    			}else USER_FAN_OFF();
		    		}
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
	lv_obj_add_event_cb(ui->screen_2_btn_2, screen_2_btn_2_event_handler, LV_EVENT_ALL, NULL);
	lv_obj_add_event_cb(ui->screen_2_btn_1, screen_2_btn_1_event_handler, LV_EVENT_ALL, NULL);
}
static void screen_3_back_event_handler (lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);

	switch (code) {
	case LV_EVENT_CLICKED:
	{
		//Write the load screen code.
	    lv_obj_t * act_scr = lv_scr_act();

	    	    if(act_scr == guider_ui.screen1 || act_scr == guider_ui.screen_1){
	    	    			if(Temp - curr_temp > 3 || Temp - curr_temp < 3 || Humidity - curr_hum > 10 || Humidity - curr_hum < 10){
	    	    				USER_FAN_ON();
	    	    			}else USER_FAN_OFF();
	    	    		}else if(act_scr == guider_ui.screen2 || act_scr == guider_ui.screen_2){
	    	    			if(Temp2 - curr_temp > 3 || Temp2 - curr_temp < 3 || Humidity2 - curr_hum > 10 || Humidity2 - curr_hum < 10){
	    	    				USER_FAN_ON();
	    	    			}else USER_FAN_OFF();
	    	    		}else if(act_scr == guider_ui.screen3 || act_scr == guider_ui.screen_3){
	    	    			if(Temp3 - curr_temp > 3 || Temp3 - curr_temp < 3 || Humidity3 - curr_hum > 10 || Humidity3 - curr_hum < 10){
	    	    				USER_FAN_ON();
	    	    			}else USER_FAN_OFF();
	    	    		}
	    lv_disp_t * d = lv_obj_get_disp(act_scr);
	    if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr)) {
	        if (guider_ui.screen3_del == true) {
	          setup_scr_screen3(&guider_ui);
	        }
	        lv_scr_load_anim(guider_ui.screen3, LV_SCR_LOAD_ANIM_NONE, 200, 200, true);
	        guider_ui.screen3_del = true;
	    }
		sprintf(hum3,  "%d %%" , Humidity3);
		sprintf(curr_h, "%d", curr_hum);
	lv_label_set_text(guider_ui.screen3_H3, curr_h);
	
	sprintf(tem3,  "%d" , Temp3);
	sprintf(curr_t, "%d", curr_temp);
	lv_label_set_text(guider_ui.screen3_T3, curr_t);
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
		Temp3++;
	sprintf(tem3,  "%d" , Temp3);
	lv_label_set_text(guider_ui.screen_3_Temp3, tem3);
	lv_obj_t * act_scr = lv_scr_act();
		    if(act_scr == guider_ui.screen1 || act_scr == guider_ui.screen_1){
		    			if(Temp - curr_temp > 3 || Temp - curr_temp < 3 || Humidity - curr_hum > 10 || Humidity - curr_hum < 10){
		    				USER_FAN_ON();
		    			}else USER_FAN_OFF();
		    		}else if(act_scr == guider_ui.screen2 || act_scr == guider_ui.screen_2){
		    			if(Temp2 - curr_temp > 3 || Temp2 - curr_temp < 3 || Humidity2 - curr_hum > 10 || Humidity2 - curr_hum < 10){
		    				USER_FAN_ON();
		    			}else USER_FAN_OFF();
		    		}else if(act_scr == guider_ui.screen3 || act_scr == guider_ui.screen_3){
		    			if(Temp3 - curr_temp > 3 || Temp3 - curr_temp < 3 || Humidity3 - curr_hum > 10 || Humidity3 - curr_hum < 10){
		    				USER_FAN_ON();
		    			}else USER_FAN_OFF();
		    		}
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
		Temp3--;
	sprintf(tem3,  "%d" , Temp3);
	lv_label_set_text(guider_ui.screen_3_Temp3, tem3);
	lv_obj_t * act_scr = lv_scr_act();
		    if(act_scr == guider_ui.screen1 || act_scr == guider_ui.screen_1){
		    			if(Temp - curr_temp > 3 || Temp - curr_temp < 3 || Humidity - curr_hum > 10 || Humidity - curr_hum < 10){
		    				USER_FAN_ON();
		    			}else USER_FAN_OFF();
		    		}else if(act_scr == guider_ui.screen2 || act_scr == guider_ui.screen_2){
		    			if(Temp2 - curr_temp > 3 || Temp2 - curr_temp < 3 || Humidity2 - curr_hum > 10 || Humidity2 - curr_hum < 10){
		    				USER_FAN_ON();
		    			}else USER_FAN_OFF();
		    		}else if(act_scr == guider_ui.screen3 || act_scr == guider_ui.screen_3){
		    			if(Temp3 - curr_temp > 3 || Temp3 - curr_temp < 3 || Humidity3 - curr_hum > 10 || Humidity3 - curr_hum < 10){
		    				USER_FAN_ON();
		    			}else USER_FAN_OFF();
		    		}
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
		if(Humidity3<=0){
	  break;
	}
	else{
	  Humidity3--;
	  sprintf(hum3,  "%d %%" , Humidity3);
	  lv_label_set_text(guider_ui.screen_3_Humidity3, hum3);
	  lv_obj_t * act_scr = lv_scr_act();
	  	    if(act_scr == guider_ui.screen1 || act_scr == guider_ui.screen_1){
	  	    			if(Temp - curr_temp > 3 || Temp - curr_temp < 3 || Humidity - curr_hum > 10 || Humidity - curr_hum < 10){
	  	    				USER_FAN_ON();
	  	    			}else USER_FAN_OFF();
	  	    		}else if(act_scr == guider_ui.screen2 || act_scr == guider_ui.screen_2){
	  	    			if(Temp2 - curr_temp > 3 || Temp2 - curr_temp < 3 || Humidity2 - curr_hum > 10 || Humidity2 - curr_hum < 10){
	  	    				USER_FAN_ON();
	  	    			}else USER_FAN_OFF();
	  	    		}else if(act_scr == guider_ui.screen3 || act_scr == guider_ui.screen_3){
	  	    			if(Temp3 - curr_temp > 3 || Temp3 - curr_temp < 3 || Humidity3 - curr_hum > 10 || Humidity3 - curr_hum < 10){
	  	    				USER_FAN_ON();
	  	    			}else USER_FAN_OFF();
	  	    		}
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
		Humidity3++;
	sprintf(hum3,  "%d %%" , Humidity3);
	lv_label_set_text(guider_ui.screen_3_Humidity3, hum3);
	lv_obj_t * act_scr = lv_scr_act();
		    if(act_scr == guider_ui.screen1 || act_scr == guider_ui.screen_1){
		    			if(Temp - curr_temp > 3 || Temp - curr_temp < 3 || Humidity - curr_hum > 10 || Humidity - curr_hum < 10){
		    				USER_FAN_ON();
		    			}else USER_FAN_OFF();
		    		}else if(act_scr == guider_ui.screen2 || act_scr == guider_ui.screen_2){
		    			if(Temp2 - curr_temp > 3 || Temp2 - curr_temp < 3 || Humidity2 - curr_hum > 10 || Humidity2 - curr_hum < 10){
		    				USER_FAN_ON();
		    			}else USER_FAN_OFF();
		    		}else if(act_scr == guider_ui.screen3 || act_scr == guider_ui.screen_3){
		    			if(Temp3 - curr_temp > 3 || Temp3 - curr_temp < 3 || Humidity3 - curr_hum > 10 || Humidity3 - curr_hum < 10){
		    				USER_FAN_ON();
		    			}else USER_FAN_OFF();
		    		}
	
		break;
	}
	default:
		break;
	}
}
static void screen_3_btn_2_event_handler (lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);

	switch (code) {
	case LV_EVENT_CLICKED:
	{
		Humidity3 = 40;
	sprintf(hum3,"%d %%", Humidity3);
	lv_label_set_text(guider_ui.screen_3_Humidity3, hum3);
	lv_obj_t * act_scr = lv_scr_act();
		    if(act_scr == guider_ui.screen1 || act_scr == guider_ui.screen_1){
		    			if(Temp - curr_temp > 3 || Temp - curr_temp < 3 || Humidity - curr_hum > 10 || Humidity - curr_hum < 10){
		    				USER_FAN_ON();
		    			}else USER_FAN_OFF();
		    		}else if(act_scr == guider_ui.screen2 || act_scr == guider_ui.screen_2){
		    			if(Temp2 - curr_temp > 3 || Temp2 - curr_temp < 3 || Humidity2 - curr_hum > 10 || Humidity2 - curr_hum < 10){
		    				USER_FAN_ON();
		    			}else USER_FAN_OFF();
		    		}else if(act_scr == guider_ui.screen3 || act_scr == guider_ui.screen_3){
		    			if(Temp3 - curr_temp > 3 || Temp3 - curr_temp < 3 || Humidity3 - curr_hum > 10 || Humidity3 - curr_hum < 10){
		    				USER_FAN_ON();
		    			}else USER_FAN_OFF();
		    		}
		break;
	}
	default:
		break;
	}
}
static void screen_3_btn_1_event_handler (lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);

	switch (code) {
	case LV_EVENT_CLICKED:
	{
		Temp3 = 25;
	sprintf(tem3,"%d",Temp3);
	lv_label_set_text(guider_ui.screen_3_Temp3, tem3);
	lv_obj_t * act_scr = lv_scr_act();
		    if(act_scr == guider_ui.screen1 || act_scr == guider_ui.screen_1){
		    			if(Temp - curr_temp > 3 || Temp - curr_temp < 3 || Humidity - curr_hum > 10 || Humidity - curr_hum < 10){
		    				USER_FAN_ON();
		    			}else USER_FAN_OFF();
		    		}else if(act_scr == guider_ui.screen2 || act_scr == guider_ui.screen_2){
		    			if(Temp2 - curr_temp > 3 || Temp2 - curr_temp < 3 || Humidity2 - curr_hum > 10 || Humidity2 - curr_hum < 10){
		    				USER_FAN_ON();
		    			}else USER_FAN_OFF();
		    		}else if(act_scr == guider_ui.screen3 || act_scr == guider_ui.screen_3){
		    			if(Temp3 - curr_temp > 3 || Temp3 - curr_temp < 3 || Humidity3 - curr_hum > 10 || Humidity3 - curr_hum < 10){
		    				USER_FAN_ON();
		    			}else USER_FAN_OFF();
		    		}
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
	lv_obj_add_event_cb(ui->screen_3_btn_2, screen_3_btn_2_event_handler, LV_EVENT_ALL, NULL);
	lv_obj_add_event_cb(ui->screen_3_btn_1, screen_3_btn_1_event_handler, LV_EVENT_ALL, NULL);
}
static void add_btn_1_event_handler (lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);

	switch (code) {
	case LV_EVENT_CLICKED:
	{
		//Write the load screen code.
	    lv_obj_t * act_scr = lv_scr_act();

	    	    if(act_scr == guider_ui.screen1 || act_scr == guider_ui.screen_1){
	    	    			if(Temp - curr_temp > 3 || Temp - curr_temp < 3 || Humidity - curr_hum > 10 || Humidity - curr_hum < 10){
	    	    				USER_FAN_ON();
	    	    			}else USER_FAN_OFF();
	    	    		}else if(act_scr == guider_ui.screen2 || act_scr == guider_ui.screen_2){
	    	    			if(Temp2 - curr_temp > 3 || Temp2 - curr_temp < 3 || Humidity2 - curr_hum > 10 || Humidity2 - curr_hum < 10){
	    	    				USER_FAN_ON();
	    	    			}else USER_FAN_OFF();
	    	    		}else if(act_scr == guider_ui.screen3 || act_scr == guider_ui.screen_3){
	    	    			if(Temp3 - curr_temp > 3 || Temp3 - curr_temp < 3 || Humidity3 - curr_hum > 10 || Humidity3 - curr_hum < 10){
	    	    				USER_FAN_ON();
	    	    			}else USER_FAN_OFF();
	    	    		}
	    lv_disp_t * d = lv_obj_get_disp(act_scr);
	    if (d->prev_scr == NULL && (d->scr_to_load == NULL || d->scr_to_load == act_scr)) {
	        if (guider_ui.screen_del == true) {
	          setup_scr_screen(&guider_ui);
	        }
	        lv_scr_load_anim(guider_ui.screen, LV_SCR_LOAD_ANIM_NONE, 200, 200, true);
	        guider_ui.screen_del = true;
	    }
		break;
	}
	default:
		break;
	}
}
void events_init_add(lv_ui *ui)
{
	lv_obj_add_event_cb(ui->add_btn_1, add_btn_1_event_handler, LV_EVENT_ALL, NULL);
}

void events_init(lv_ui *ui)
{

}
