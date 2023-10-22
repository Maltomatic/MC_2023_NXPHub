/*
* Copyright 2023 NXP
* NXP Confidential and Proprietary. This software is owned or controlled by NXP and may only be used strictly in
* accordance with the applicable license terms. By expressly accepting such terms or by downloading, installing,
* activating and/or otherwise using the software, you are agreeing that you have read, and that you agree to
* comply with and are bound by, such license terms.  If you do not agree to be bound by the applicable license
* terms, then you may not retain, install, activate or otherwise use the software.
*/


#ifndef EVENTS_INIT_H_
#define EVENTS_INIT_H_
#ifdef __cplusplus
extern "C" {
#endif

#include "gui_guider.h"

void events_init(lv_ui *ui);

void events_init_screen(lv_ui *ui);
void events_init_screen1(lv_ui *ui);
void events_init_screen2(lv_ui *ui);
void events_init_screen3(lv_ui *ui);
void events_init_screen_1(lv_ui *ui);
void events_init_screen_2(lv_ui *ui);
void events_init_screen_3(lv_ui *ui);
void events_init_add(lv_ui *ui);


static unsigned int curr_temp = 28;
static char curr_t[3];
static unsigned int curr_hum = 55;
static char curr_h[3];

static unsigned int Temp = 25;
static char tem[3];
static unsigned int Humidity = 40;
static char hum[3];
static unsigned int Temp2 = 25;
static char tem2[3];
static char nothing[3] = "0";
static unsigned int Humidity2 = 40;
static char hum2[3];
static unsigned int Temp3 = 0;
static char tem3[3];
static unsigned int Humidity3 = 0;
static char hum3[3];

#ifdef __cplusplus
}
#endif
#endif /* EVENT_CB_H_ */
