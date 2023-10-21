# Copyright 2023 NXP
# NXP Confidential and Proprietary. This software is owned or controlled by NXP and may only be used strictly in
# accordance with the applicable license terms. By expressly accepting such terms or by downloading, installing,
# activating and/or otherwise using the software, you are agreeing that you have read, and that you agree to
# comply with and are bound by, such license terms.  If you do not agree to be bound by the applicable license
# terms, then you may not retain, install, activate or otherwise use the software.

import SDL
import utime as time
import usys as sys
import lvgl as lv
import lodepng as png
import ustruct
import fs_driver

lv.init()
SDL.init(w=480,h=272)

# Register SDL display driver.
disp_buf1 = lv.disp_draw_buf_t()
buf1_1 = bytearray(480*10)
disp_buf1.init(buf1_1, None, len(buf1_1)//4)
disp_drv = lv.disp_drv_t()
disp_drv.init()
disp_drv.draw_buf = disp_buf1
disp_drv.flush_cb = SDL.monitor_flush
disp_drv.hor_res = 480
disp_drv.ver_res = 272
disp_drv.register()

# Regsiter SDL mouse driver
indev_drv = lv.indev_drv_t()
indev_drv.init()
indev_drv.type = lv.INDEV_TYPE.POINTER
indev_drv.read_cb = SDL.mouse_read
indev_drv.register()

fs_drv = lv.fs_drv_t()
fs_driver.fs_register(fs_drv, 'Z')

# Below: Taken from https://github.com/lvgl/lv_binding_micropython/blob/master/driver/js/imagetools.py#L22-L94

COLOR_SIZE = lv.color_t.__SIZE__
COLOR_IS_SWAPPED = hasattr(lv.color_t().ch,'green_h')

class lodepng_error(RuntimeError):
    def __init__(self, err):
        if type(err) is int:
            super().__init__(png.error_text(err))
        else:
            super().__init__(err)

# Parse PNG file header
# Taken from https://github.com/shibukawa/imagesize_py/blob/ffef30c1a4715c5acf90e8945ceb77f4a2ed2d45/imagesize.py#L63-L85

def get_png_info(decoder, src, header):
    # Only handle variable image types

    if lv.img.src_get_type(src) != lv.img.SRC.VARIABLE:
        return lv.RES.INV

    data = lv.img_dsc_t.__cast__(src).data
    if data == None:
        return lv.RES.INV

    png_header = bytes(data.__dereference__(24))

    if png_header.startswith(b'\211PNG\r\n\032\n'):
        if png_header[12:16] == b'IHDR':
            start = 16
        # Maybe this is for an older PNG version.
        else:
            start = 8
        try:
            width, height = ustruct.unpack(">LL", png_header[start:start+8])
        except ustruct.error:
            return lv.RES.INV
    else:
        return lv.RES.INV

    header.always_zero = 0
    header.w = width
    header.h = height
    header.cf = lv.img.CF.TRUE_COLOR_ALPHA

    return lv.RES.OK

def convert_rgba8888_to_bgra8888(img_view):
    for i in range(0, len(img_view), lv.color_t.__SIZE__):
        ch = lv.color_t.__cast__(img_view[i:i]).ch
        ch.red, ch.blue = ch.blue, ch.red

# Read and parse PNG file

def open_png(decoder, dsc):
    img_dsc = lv.img_dsc_t.__cast__(dsc.src)
    png_data = img_dsc.data
    png_size = img_dsc.data_size
    png_decoded = png.C_Pointer()
    png_width = png.C_Pointer()
    png_height = png.C_Pointer()
    error = png.decode32(png_decoded, png_width, png_height, png_data, png_size)
    if error:
        raise lodepng_error(error)
    img_size = png_width.int_val * png_height.int_val * 4
    img_data = png_decoded.ptr_val
    img_view = img_data.__dereference__(img_size)

    if COLOR_SIZE == 4:
        convert_rgba8888_to_bgra8888(img_view)
    else:
        raise lodepng_error("Error: Color mode not supported yet!")

    dsc.img_data = img_data
    return lv.RES.OK

# Above: Taken from https://github.com/lvgl/lv_binding_micropython/blob/master/driver/js/imagetools.py#L22-L94

decoder = lv.img.decoder_create()
decoder.info_cb = get_png_info
decoder.open_cb = open_png

def anim_x_cb(obj, v):
    obj.set_x(v)

def anim_y_cb(obj, v):
    obj.set_y(v)

def anim_width_cb(obj, v):
    obj.set_width(v)

def anim_height_cb(obj, v):
    obj.set_height(v)

def anim_img_zoom_cb(obj, v):
    obj.set_zoom(v)

def anim_img_rotate_cb(obj, v):
    obj.set_angle(v)

global_font_cache = {}
def test_font(font_family, font_size):
    global global_font_cache
    if font_family + str(font_size) in global_font_cache:
        return global_font_cache[font_family + str(font_size)]
    if font_size % 2:
        candidates = [
            (font_family, font_size),
            (font_family, font_size-font_size%2),
            (font_family, font_size+font_size%2),
            ("montserrat", font_size-font_size%2),
            ("montserrat", font_size+font_size%2),
            ("montserrat", 16)
        ]
    else:
        candidates = [
            (font_family, font_size),
            ("montserrat", font_size),
            ("montserrat", 16)
        ]
    for (family, size) in candidates:
        try:
            if eval(f'lv.font_{family}_{size}'):
                global_font_cache[font_family + str(font_size)] = eval(f'lv.font_{family}_{size}')
                if family != font_family or size != font_size:
                    print(f'WARNING: lv.font_{family}_{size} is used!')
                return eval(f'lv.font_{family}_{size}')
        except AttributeError:
            try:
                load_font = lv.font_load(f"Z:MicroPython/lv_font_{family}_{size}.fnt")
                global_font_cache[font_family + str(font_size)] = load_font
                return load_font
            except:
                if family == font_family and size == font_size:
                    print(f'WARNING: lv.font_{family}_{size} is NOT supported!')

global_image_cache = {}
def load_image(file):
    global global_image_cache
    if file in global_image_cache:
        return global_image_cache[file]
    try:
        with open(file,'rb') as f:
            data = f.read()
    except:
        print(f'Could not open {file}')
        sys.exit()

    img = lv.img_dsc_t({
        'data_size': len(data),
        'data': data
    })
    global_image_cache[file] = img
    return img

def calendar_event_handler(e,obj):
    code = e.get_code()

    if code == lv.EVENT.VALUE_CHANGED:
        source = e.get_current_target()
        date = lv.calendar_date_t()
        if source.get_pressed_date(date) == lv.RES.OK:
            source.set_highlighted_dates([date], 1)

def spinbox_increment_event_cb(e, obj):
    code = e.get_code()
    if code == lv.EVENT.SHORT_CLICKED or code == lv.EVENT.LONG_PRESSED_REPEAT:
        obj.increment()
def spinbox_decrement_event_cb(e, obj):
    code = e.get_code()
    if code == lv.EVENT.SHORT_CLICKED or code == lv.EVENT.LONG_PRESSED_REPEAT:
        obj.decrement()

def digital_clock_cb(timer, obj, current_time, show_second, use_ampm):
    hour = int(current_time[0])
    minute = int(current_time[1])
    second = int(current_time[2])
    ampm = current_time[3]
    second = second + 1
    if second == 60:
        second = 0
        minute = minute + 1
        if minute == 60:
            minute = 0
            hour = hour + 1
            if use_ampm:
                if hour == 12:
                    if ampm == 'AM':
                        ampm = 'PM'
                    elif ampm == 'PM':
                        ampm = 'AM'
                if hour > 12:
                    hour = hour % 12
    hour = hour % 24
    if use_ampm:
        if show_second:
            obj.set_text("%02d:%02d:%02d %s" %(hour, minute, second, ampm))
        else:
            obj.set_text("%02d:%02d %s" %(hour, minute, ampm))
    else:
        if show_second:
            obj.set_text("%02d:%02d:%02d" %(hour, minute, second))
        else:
            obj.set_text("%02d:%02d" %(hour, minute))
    current_time[0] = hour
    current_time[1] = minute
    current_time[2] = second
    current_time[3] = ampm

def analog_clock_cb(timer, obj):
    datetime = time.localtime()
    hour = datetime[3]
    if hour >= 12: hour = hour - 12
    obj.set_time(hour, datetime[4], datetime[5])

def datetext_event_handler(e, obj):
    code = e.get_code()
    target = e.get_target()
    if code == lv.EVENT.FOCUSED:
        if obj is None:
            bg = lv.layer_top()
            bg.add_flag(lv.obj.FLAG.CLICKABLE)
            obj = lv.calendar(bg)
            scr = target.get_screen()
            scr_height = scr.get_height()
            scr_width = scr.get_width()
            obj.set_size(int(scr_width * 0.8), int(scr_height * 0.8))
            datestring = target.get_text()
            year = int(datestring.split('/')[0])
            month = int(datestring.split('/')[1])
            day = int(datestring.split('/')[2])
            obj.set_showed_date(year, month)
            highlighted_days=[lv.calendar_date_t({'year':year, 'month':month, 'day':day})]
            obj.set_highlighted_dates(highlighted_days, 1)
            obj.align(lv.ALIGN.CENTER, 0, 0)
            lv.calendar_header_arrow(obj)
            obj.add_event_cb(lambda e: datetext_calendar_event_handler(e, target), lv.EVENT.ALL, None)
            scr.update_layout()

def datetext_calendar_event_handler(e, obj):
    code = e.get_code()
    target = e.get_current_target()
    if code == lv.EVENT.VALUE_CHANGED:
        date = lv.calendar_date_t()
        if target.get_pressed_date(date) == lv.RES.OK:
            obj.set_text(f"{date.year}/{date.month}/{date.day}")
            bg = lv.layer_top()
            bg.clear_flag(lv.obj.FLAG.CLICKABLE)
            bg.set_style_bg_opa(lv.OPA.TRANSP, 0)
            target.delete()

def screen_ta_event_cb(e,kb):
    code = e.get_code()
    ta = e.get_target()
    if code == lv.EVENT.FOCUSED:
        kb.set_textarea(ta)
        kb.move_foreground()
        kb.clear_flag(lv.obj.FLAG.HIDDEN)

    if code == lv.EVENT.DEFOCUSED:
        kb.set_textarea(None)
        kb.move_background()
        kb.add_flag(lv.obj.FLAG.HIDDEN)

def screen_1_ta_event_cb(e,kb):
    code = e.get_code()
    ta = e.get_target()
    if code == lv.EVENT.FOCUSED:
        kb.set_textarea(ta)
        kb.move_foreground()
        kb.clear_flag(lv.obj.FLAG.HIDDEN)

    if code == lv.EVENT.DEFOCUSED:
        kb.set_textarea(None)
        kb.move_background()
        kb.add_flag(lv.obj.FLAG.HIDDEN)

def screen_2_ta_event_cb(e,kb):
    code = e.get_code()
    ta = e.get_target()
    if code == lv.EVENT.FOCUSED:
        kb.set_textarea(ta)
        kb.move_foreground()
        kb.clear_flag(lv.obj.FLAG.HIDDEN)

    if code == lv.EVENT.DEFOCUSED:
        kb.set_textarea(None)
        kb.move_background()
        kb.add_flag(lv.obj.FLAG.HIDDEN)

def screen_3_ta_event_cb(e,kb):
    code = e.get_code()
    ta = e.get_target()
    if code == lv.EVENT.FOCUSED:
        kb.set_textarea(ta)
        kb.move_foreground()
        kb.clear_flag(lv.obj.FLAG.HIDDEN)

    if code == lv.EVENT.DEFOCUSED:
        kb.set_textarea(None)
        kb.move_background()
        kb.add_flag(lv.obj.FLAG.HIDDEN)

# Create screen
screen = lv.obj()
screen.set_size(480, 272)
screen.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen.set_style_bg_opa(0, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_img_1
screen_img_1 = lv.img(screen)
screen_img_1.set_src(load_image(r"C:\NXP\GUI-Guider-Projects\scratch\generated\MicroPython\_204_114.png"))
screen_img_1.add_flag(lv.obj.FLAG.CLICKABLE)
screen_img_1.set_pivot(50,50)
screen_img_1.set_angle(0)
screen_img_1.set_pos(22, 16)
screen_img_1.set_size(204, 114)
screen_img_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_img_1, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_img_1.set_style_img_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_img_2
screen_img_2 = lv.img(screen)
screen_img_2.set_src(load_image(r"C:\NXP\GUI-Guider-Projects\scratch\generated\MicroPython\_180_105.png"))
screen_img_2.add_flag(lv.obj.FLAG.CLICKABLE)
screen_img_2.set_pivot(50,50)
screen_img_2.set_angle(0)
screen_img_2.set_pos(255, 16)
screen_img_2.set_size(180, 105)
screen_img_2.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_img_2, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_img_2.set_style_img_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_img_3
screen_img_3 = lv.img(screen)
screen_img_3.set_src(load_image(r"C:\NXP\GUI-Guider-Projects\scratch\generated\MicroPython\_200_117.png"))
screen_img_3.add_flag(lv.obj.FLAG.CLICKABLE)
screen_img_3.set_pivot(50,50)
screen_img_3.set_angle(0)
screen_img_3.set_pos(26, 145)
screen_img_3.set_size(200, 117)
screen_img_3.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_img_3, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_img_3.set_style_img_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_ddlist_1
screen_ddlist_1 = lv.dropdown(screen)
screen_ddlist_1.set_options("list1\nlist2\nlist3")
screen_ddlist_1.set_pos(175, 121)
screen_ddlist_1.set_size(130, 30)
screen_ddlist_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_ddlist_1, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_ddlist_1.set_style_text_color(lv.color_hex(0x0D3055), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_ddlist_1.set_style_text_font(test_font("montserratMedium", 12), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_ddlist_1.set_style_border_width(1, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_ddlist_1.set_style_border_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_ddlist_1.set_style_border_color(lv.color_hex(0xe1e6ee), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_ddlist_1.set_style_pad_top(8, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_ddlist_1.set_style_pad_left(6, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_ddlist_1.set_style_pad_right(6, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_ddlist_1.set_style_radius(3, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_ddlist_1.set_style_bg_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_ddlist_1.set_style_bg_color(lv.color_hex(0xffffff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_ddlist_1.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)

# Set style for screen_ddlist_1, Part: lv.PART.SELECTED, State: lv.STATE.CHECKED.
style_screen_ddlist_1_extra_list_selected_checked = lv.style_t()
style_screen_ddlist_1_extra_list_selected_checked.init()
style_screen_ddlist_1_extra_list_selected_checked.set_text_color(lv.color_hex(0xffffff))
style_screen_ddlist_1_extra_list_selected_checked.set_text_font(test_font("montserratMedium", 12))
style_screen_ddlist_1_extra_list_selected_checked.set_border_width(1)
style_screen_ddlist_1_extra_list_selected_checked.set_border_opa(255)
style_screen_ddlist_1_extra_list_selected_checked.set_border_color(lv.color_hex(0xe1e6ee))
style_screen_ddlist_1_extra_list_selected_checked.set_radius(3)
style_screen_ddlist_1_extra_list_selected_checked.set_bg_opa(255)
style_screen_ddlist_1_extra_list_selected_checked.set_bg_color(lv.color_hex(0x00a1b5))
screen_ddlist_1.get_list().add_style(style_screen_ddlist_1_extra_list_selected_checked, lv.PART.SELECTED|lv.STATE.CHECKED)
# Set style for screen_ddlist_1, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
style_screen_ddlist_1_extra_list_main_default = lv.style_t()
style_screen_ddlist_1_extra_list_main_default.init()
style_screen_ddlist_1_extra_list_main_default.set_max_height(90)
style_screen_ddlist_1_extra_list_main_default.set_text_color(lv.color_hex(0x0D3055))
style_screen_ddlist_1_extra_list_main_default.set_text_font(test_font("montserratMedium", 12))
style_screen_ddlist_1_extra_list_main_default.set_border_width(1)
style_screen_ddlist_1_extra_list_main_default.set_border_opa(255)
style_screen_ddlist_1_extra_list_main_default.set_border_color(lv.color_hex(0xe1e6ee))
style_screen_ddlist_1_extra_list_main_default.set_radius(3)
style_screen_ddlist_1_extra_list_main_default.set_bg_opa(255)
style_screen_ddlist_1_extra_list_main_default.set_bg_color(lv.color_hex(0xffffff))
screen_ddlist_1.get_list().add_style(style_screen_ddlist_1_extra_list_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)
# Set style for screen_ddlist_1, Part: lv.PART.SCROLLBAR, State: lv.STATE.DEFAULT.
style_screen_ddlist_1_extra_list_scrollbar_default = lv.style_t()
style_screen_ddlist_1_extra_list_scrollbar_default.init()
style_screen_ddlist_1_extra_list_scrollbar_default.set_radius(3)
style_screen_ddlist_1_extra_list_scrollbar_default.set_bg_opa(255)
style_screen_ddlist_1_extra_list_scrollbar_default.set_bg_color(lv.color_hex(0x00ff00))
screen_ddlist_1.get_list().add_style(style_screen_ddlist_1_extra_list_scrollbar_default, lv.PART.SCROLLBAR|lv.STATE.DEFAULT)

screen.update_layout()
# Create screen_1
screen_1 = lv.obj()
screen_1.set_size(480, 272)
screen_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_1, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_1.set_style_bg_opa(0, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_1_img_1
screen_1_img_1 = lv.img(screen_1)
screen_1_img_1.set_src(load_image(r"C:\NXP\GUI-Guider-Projects\scratch\generated\MicroPython\_433_102.png"))
screen_1_img_1.add_flag(lv.obj.FLAG.CLICKABLE)
screen_1_img_1.set_pivot(50,50)
screen_1_img_1.set_angle(0)
screen_1_img_1.set_pos(25, 16)
screen_1_img_1.set_size(433, 102)
screen_1_img_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_1_img_1, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_1_img_1.set_style_img_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_1_back
screen_1_back = lv.btn(screen_1)
screen_1_back_label = lv.label(screen_1_back)
screen_1_back_label.set_text("Back")
screen_1_back_label.set_long_mode(lv.label.LONG.WRAP)
screen_1_back_label.align(lv.ALIGN.CENTER, 0, 0)
screen_1_back.set_style_pad_all(0, lv.STATE.DEFAULT)
screen_1_back.set_pos(25, 16)
screen_1_back.set_size(100, 36)
screen_1_back.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_1_back, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_1_back.set_style_bg_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_back.set_style_bg_color(lv.color_hex(0x2195f6), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_back.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_back.set_style_radius(5, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_back.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_back.set_style_text_color(lv.color_hex(0xffffff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_back.set_style_text_font(test_font("montserratMedium", 16), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_back.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_1_Temp
screen_1_Temp = lv.label(screen_1)
screen_1_Temp.set_text("0")
screen_1_Temp.set_long_mode(lv.label.LONG.WRAP)
screen_1_Temp.set_pos(62, 146)
screen_1_Temp.set_size(100, 32)
screen_1_Temp.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_1_Temp, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_1_Temp.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Temp.set_style_radius(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Temp.set_style_text_color(lv.color_hex(0x000000), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Temp.set_style_text_font(test_font("montserratMedium", 16), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Temp.set_style_text_letter_space(2, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Temp.set_style_text_line_space(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Temp.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Temp.set_style_bg_opa(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Temp.set_style_pad_top(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Temp.set_style_pad_right(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Temp.set_style_pad_bottom(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Temp.set_style_pad_left(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Temp.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_1_T_plus
screen_1_T_plus = lv.btn(screen_1)
screen_1_T_plus_label = lv.label(screen_1_T_plus)
screen_1_T_plus_label.set_text("+")
screen_1_T_plus_label.set_long_mode(lv.label.LONG.WRAP)
screen_1_T_plus_label.align(lv.ALIGN.CENTER, 0, 0)
screen_1_T_plus.set_style_pad_all(0, lv.STATE.DEFAULT)
screen_1_T_plus.set_pos(10, 119)
screen_1_T_plus.set_size(41, 35)
screen_1_T_plus.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_1_T_plus, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_1_T_plus.set_style_bg_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_T_plus.set_style_bg_color(lv.color_hex(0xD01FBB), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_T_plus.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_T_plus.set_style_radius(5, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_T_plus.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_T_plus.set_style_text_color(lv.color_hex(0xffffff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_T_plus.set_style_text_font(test_font("Alatsi_Regular", 33), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_T_plus.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_1_T_minus
screen_1_T_minus = lv.btn(screen_1)
screen_1_T_minus_label = lv.label(screen_1_T_minus)
screen_1_T_minus_label.set_text("-")
screen_1_T_minus_label.set_long_mode(lv.label.LONG.WRAP)
screen_1_T_minus_label.align(lv.ALIGN.CENTER, 0, 0)
screen_1_T_minus.set_style_pad_all(0, lv.STATE.DEFAULT)
screen_1_T_minus.set_pos(10, 167)
screen_1_T_minus.set_size(41, 35)
screen_1_T_minus.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_1_T_minus, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_1_T_minus.set_style_bg_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_T_minus.set_style_bg_color(lv.color_hex(0xD01FBB), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_T_minus.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_T_minus.set_style_radius(5, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_T_minus.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_T_minus.set_style_text_color(lv.color_hex(0xffffff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_T_minus.set_style_text_font(test_font("Alatsi_Regular", 33), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_T_minus.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_1_H_minus
screen_1_H_minus = lv.btn(screen_1)
screen_1_H_minus_label = lv.label(screen_1_H_minus)
screen_1_H_minus_label.set_text("-")
screen_1_H_minus_label.set_long_mode(lv.label.LONG.WRAP)
screen_1_H_minus_label.align(lv.ALIGN.CENTER, 0, 0)
screen_1_H_minus.set_style_pad_all(0, lv.STATE.DEFAULT)
screen_1_H_minus.set_pos(220, 167)
screen_1_H_minus.set_size(41, 35)
screen_1_H_minus.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_1_H_minus, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_1_H_minus.set_style_bg_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_H_minus.set_style_bg_color(lv.color_hex(0x00bdff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_H_minus.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_H_minus.set_style_radius(5, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_H_minus.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_H_minus.set_style_text_color(lv.color_hex(0xffffff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_H_minus.set_style_text_font(test_font("Alatsi_Regular", 33), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_H_minus.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_1_H_plus
screen_1_H_plus = lv.btn(screen_1)
screen_1_H_plus_label = lv.label(screen_1_H_plus)
screen_1_H_plus_label.set_text("+")
screen_1_H_plus_label.set_long_mode(lv.label.LONG.WRAP)
screen_1_H_plus_label.align(lv.ALIGN.CENTER, 0, 0)
screen_1_H_plus.set_style_pad_all(0, lv.STATE.DEFAULT)
screen_1_H_plus.set_pos(220, 114)
screen_1_H_plus.set_size(41, 35)
screen_1_H_plus.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_1_H_plus, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_1_H_plus.set_style_bg_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_H_plus.set_style_bg_color(lv.color_hex(0x00c4ff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_H_plus.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_H_plus.set_style_radius(5, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_H_plus.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_H_plus.set_style_text_color(lv.color_hex(0xffffff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_H_plus.set_style_text_font(test_font("Alatsi_Regular", 33), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_H_plus.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_1_Humidity
screen_1_Humidity = lv.label(screen_1)
screen_1_Humidity.set_text("0 %")
screen_1_Humidity.set_long_mode(lv.label.LONG.WRAP)
screen_1_Humidity.set_pos(292, 149)
screen_1_Humidity.set_size(100, 32)
screen_1_Humidity.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_1_Humidity, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_1_Humidity.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Humidity.set_style_radius(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Humidity.set_style_text_color(lv.color_hex(0x000000), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Humidity.set_style_text_font(test_font("montserratMedium", 16), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Humidity.set_style_text_letter_space(2, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Humidity.set_style_text_line_space(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Humidity.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Humidity.set_style_bg_opa(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Humidity.set_style_pad_top(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Humidity.set_style_pad_right(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Humidity.set_style_pad_bottom(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Humidity.set_style_pad_left(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Humidity.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)

screen_1.update_layout()
# Create screen_2
screen_2 = lv.obj()
screen_2.set_size(480, 272)
screen_2.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_2, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_2.set_style_bg_opa(0, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_2_img_1
screen_2_img_1 = lv.img(screen_2)
screen_2_img_1.set_src(load_image(r"C:\NXP\GUI-Guider-Projects\scratch\generated\MicroPython\_433_102.png"))
screen_2_img_1.add_flag(lv.obj.FLAG.CLICKABLE)
screen_2_img_1.set_pivot(50,50)
screen_2_img_1.set_angle(0)
screen_2_img_1.set_pos(25, 16)
screen_2_img_1.set_size(433, 102)
screen_2_img_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_2_img_1, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_2_img_1.set_style_img_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_2_back
screen_2_back = lv.btn(screen_2)
screen_2_back_label = lv.label(screen_2_back)
screen_2_back_label.set_text("Back")
screen_2_back_label.set_long_mode(lv.label.LONG.WRAP)
screen_2_back_label.align(lv.ALIGN.CENTER, 0, 0)
screen_2_back.set_style_pad_all(0, lv.STATE.DEFAULT)
screen_2_back.set_pos(25, 16)
screen_2_back.set_size(100, 36)
screen_2_back.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_2_back, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_2_back.set_style_bg_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_back.set_style_bg_color(lv.color_hex(0x2195f6), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_back.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_back.set_style_radius(5, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_back.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_back.set_style_text_color(lv.color_hex(0xffffff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_back.set_style_text_font(test_font("montserratMedium", 16), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_back.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_2_Temp
screen_2_Temp = lv.label(screen_2)
screen_2_Temp.set_text("0")
screen_2_Temp.set_long_mode(lv.label.LONG.WRAP)
screen_2_Temp.set_pos(62, 146)
screen_2_Temp.set_size(100, 32)
screen_2_Temp.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_2_Temp, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_2_Temp.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_Temp.set_style_radius(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_Temp.set_style_text_color(lv.color_hex(0x000000), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_Temp.set_style_text_font(test_font("montserratMedium", 16), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_Temp.set_style_text_letter_space(2, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_Temp.set_style_text_line_space(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_Temp.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_Temp.set_style_bg_opa(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_Temp.set_style_pad_top(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_Temp.set_style_pad_right(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_Temp.set_style_pad_bottom(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_Temp.set_style_pad_left(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_Temp.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_2_T_plus
screen_2_T_plus = lv.btn(screen_2)
screen_2_T_plus_label = lv.label(screen_2_T_plus)
screen_2_T_plus_label.set_text("+")
screen_2_T_plus_label.set_long_mode(lv.label.LONG.WRAP)
screen_2_T_plus_label.align(lv.ALIGN.CENTER, 0, 0)
screen_2_T_plus.set_style_pad_all(0, lv.STATE.DEFAULT)
screen_2_T_plus.set_pos(10, 119)
screen_2_T_plus.set_size(41, 35)
screen_2_T_plus.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_2_T_plus, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_2_T_plus.set_style_bg_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_T_plus.set_style_bg_color(lv.color_hex(0xD01FBB), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_T_plus.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_T_plus.set_style_radius(5, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_T_plus.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_T_plus.set_style_text_color(lv.color_hex(0xffffff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_T_plus.set_style_text_font(test_font("Alatsi_Regular", 33), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_T_plus.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_2_T_minus
screen_2_T_minus = lv.btn(screen_2)
screen_2_T_minus_label = lv.label(screen_2_T_minus)
screen_2_T_minus_label.set_text("-")
screen_2_T_minus_label.set_long_mode(lv.label.LONG.WRAP)
screen_2_T_minus_label.align(lv.ALIGN.CENTER, 0, 0)
screen_2_T_minus.set_style_pad_all(0, lv.STATE.DEFAULT)
screen_2_T_minus.set_pos(10, 167)
screen_2_T_minus.set_size(41, 35)
screen_2_T_minus.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_2_T_minus, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_2_T_minus.set_style_bg_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_T_minus.set_style_bg_color(lv.color_hex(0xD01FBB), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_T_minus.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_T_minus.set_style_radius(5, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_T_minus.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_T_minus.set_style_text_color(lv.color_hex(0xffffff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_T_minus.set_style_text_font(test_font("Alatsi_Regular", 33), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_T_minus.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_2_H_minus
screen_2_H_minus = lv.btn(screen_2)
screen_2_H_minus_label = lv.label(screen_2_H_minus)
screen_2_H_minus_label.set_text("-")
screen_2_H_minus_label.set_long_mode(lv.label.LONG.WRAP)
screen_2_H_minus_label.align(lv.ALIGN.CENTER, 0, 0)
screen_2_H_minus.set_style_pad_all(0, lv.STATE.DEFAULT)
screen_2_H_minus.set_pos(220, 167)
screen_2_H_minus.set_size(41, 35)
screen_2_H_minus.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_2_H_minus, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_2_H_minus.set_style_bg_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_H_minus.set_style_bg_color(lv.color_hex(0x00bdff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_H_minus.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_H_minus.set_style_radius(5, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_H_minus.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_H_minus.set_style_text_color(lv.color_hex(0xffffff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_H_minus.set_style_text_font(test_font("Alatsi_Regular", 33), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_H_minus.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_2_H_plus
screen_2_H_plus = lv.btn(screen_2)
screen_2_H_plus_label = lv.label(screen_2_H_plus)
screen_2_H_plus_label.set_text("+")
screen_2_H_plus_label.set_long_mode(lv.label.LONG.WRAP)
screen_2_H_plus_label.align(lv.ALIGN.CENTER, 0, 0)
screen_2_H_plus.set_style_pad_all(0, lv.STATE.DEFAULT)
screen_2_H_plus.set_pos(220, 114)
screen_2_H_plus.set_size(41, 35)
screen_2_H_plus.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_2_H_plus, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_2_H_plus.set_style_bg_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_H_plus.set_style_bg_color(lv.color_hex(0x00c4ff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_H_plus.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_H_plus.set_style_radius(5, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_H_plus.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_H_plus.set_style_text_color(lv.color_hex(0xffffff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_H_plus.set_style_text_font(test_font("Alatsi_Regular", 33), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_H_plus.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_2_Humidity
screen_2_Humidity = lv.label(screen_2)
screen_2_Humidity.set_text("0 %")
screen_2_Humidity.set_long_mode(lv.label.LONG.WRAP)
screen_2_Humidity.set_pos(292, 149)
screen_2_Humidity.set_size(100, 32)
screen_2_Humidity.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_2_Humidity, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_2_Humidity.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_Humidity.set_style_radius(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_Humidity.set_style_text_color(lv.color_hex(0x000000), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_Humidity.set_style_text_font(test_font("montserratMedium", 16), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_Humidity.set_style_text_letter_space(2, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_Humidity.set_style_text_line_space(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_Humidity.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_Humidity.set_style_bg_opa(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_Humidity.set_style_pad_top(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_Humidity.set_style_pad_right(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_Humidity.set_style_pad_bottom(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_Humidity.set_style_pad_left(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_Humidity.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)

screen_2.update_layout()
# Create screen_3
screen_3 = lv.obj()
screen_3.set_size(480, 272)
screen_3.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_3, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_3.set_style_bg_opa(0, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_3_img_1
screen_3_img_1 = lv.img(screen_3)
screen_3_img_1.set_src(load_image(r"C:\NXP\GUI-Guider-Projects\scratch\generated\MicroPython\_433_102.png"))
screen_3_img_1.add_flag(lv.obj.FLAG.CLICKABLE)
screen_3_img_1.set_pivot(50,50)
screen_3_img_1.set_angle(0)
screen_3_img_1.set_pos(25, 16)
screen_3_img_1.set_size(433, 102)
screen_3_img_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_3_img_1, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_3_img_1.set_style_img_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_3_back
screen_3_back = lv.btn(screen_3)
screen_3_back_label = lv.label(screen_3_back)
screen_3_back_label.set_text("Back")
screen_3_back_label.set_long_mode(lv.label.LONG.WRAP)
screen_3_back_label.align(lv.ALIGN.CENTER, 0, 0)
screen_3_back.set_style_pad_all(0, lv.STATE.DEFAULT)
screen_3_back.set_pos(25, 16)
screen_3_back.set_size(100, 36)
screen_3_back.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_3_back, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_3_back.set_style_bg_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_back.set_style_bg_color(lv.color_hex(0x2195f6), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_back.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_back.set_style_radius(5, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_back.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_back.set_style_text_color(lv.color_hex(0xffffff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_back.set_style_text_font(test_font("montserratMedium", 16), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_back.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_3_Temp
screen_3_Temp = lv.label(screen_3)
screen_3_Temp.set_text("0")
screen_3_Temp.set_long_mode(lv.label.LONG.WRAP)
screen_3_Temp.set_pos(62, 146)
screen_3_Temp.set_size(100, 32)
screen_3_Temp.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_3_Temp, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_3_Temp.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_Temp.set_style_radius(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_Temp.set_style_text_color(lv.color_hex(0x000000), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_Temp.set_style_text_font(test_font("montserratMedium", 16), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_Temp.set_style_text_letter_space(2, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_Temp.set_style_text_line_space(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_Temp.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_Temp.set_style_bg_opa(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_Temp.set_style_pad_top(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_Temp.set_style_pad_right(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_Temp.set_style_pad_bottom(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_Temp.set_style_pad_left(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_Temp.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_3_T_plus
screen_3_T_plus = lv.btn(screen_3)
screen_3_T_plus_label = lv.label(screen_3_T_plus)
screen_3_T_plus_label.set_text("+")
screen_3_T_plus_label.set_long_mode(lv.label.LONG.WRAP)
screen_3_T_plus_label.align(lv.ALIGN.CENTER, 0, 0)
screen_3_T_plus.set_style_pad_all(0, lv.STATE.DEFAULT)
screen_3_T_plus.set_pos(10, 119)
screen_3_T_plus.set_size(41, 35)
screen_3_T_plus.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_3_T_plus, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_3_T_plus.set_style_bg_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_T_plus.set_style_bg_color(lv.color_hex(0xD01FBB), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_T_plus.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_T_plus.set_style_radius(5, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_T_plus.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_T_plus.set_style_text_color(lv.color_hex(0xffffff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_T_plus.set_style_text_font(test_font("Alatsi_Regular", 33), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_T_plus.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_3_T_minus
screen_3_T_minus = lv.btn(screen_3)
screen_3_T_minus_label = lv.label(screen_3_T_minus)
screen_3_T_minus_label.set_text("-")
screen_3_T_minus_label.set_long_mode(lv.label.LONG.WRAP)
screen_3_T_minus_label.align(lv.ALIGN.CENTER, 0, 0)
screen_3_T_minus.set_style_pad_all(0, lv.STATE.DEFAULT)
screen_3_T_minus.set_pos(10, 167)
screen_3_T_minus.set_size(41, 35)
screen_3_T_minus.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_3_T_minus, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_3_T_minus.set_style_bg_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_T_minus.set_style_bg_color(lv.color_hex(0xD01FBB), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_T_minus.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_T_minus.set_style_radius(5, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_T_minus.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_T_minus.set_style_text_color(lv.color_hex(0xffffff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_T_minus.set_style_text_font(test_font("Alatsi_Regular", 33), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_T_minus.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_3_H_minus
screen_3_H_minus = lv.btn(screen_3)
screen_3_H_minus_label = lv.label(screen_3_H_minus)
screen_3_H_minus_label.set_text("-")
screen_3_H_minus_label.set_long_mode(lv.label.LONG.WRAP)
screen_3_H_minus_label.align(lv.ALIGN.CENTER, 0, 0)
screen_3_H_minus.set_style_pad_all(0, lv.STATE.DEFAULT)
screen_3_H_minus.set_pos(220, 167)
screen_3_H_minus.set_size(41, 35)
screen_3_H_minus.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_3_H_minus, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_3_H_minus.set_style_bg_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_H_minus.set_style_bg_color(lv.color_hex(0x00bdff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_H_minus.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_H_minus.set_style_radius(5, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_H_minus.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_H_minus.set_style_text_color(lv.color_hex(0xffffff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_H_minus.set_style_text_font(test_font("Alatsi_Regular", 33), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_H_minus.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_3_H_plus
screen_3_H_plus = lv.btn(screen_3)
screen_3_H_plus_label = lv.label(screen_3_H_plus)
screen_3_H_plus_label.set_text("+")
screen_3_H_plus_label.set_long_mode(lv.label.LONG.WRAP)
screen_3_H_plus_label.align(lv.ALIGN.CENTER, 0, 0)
screen_3_H_plus.set_style_pad_all(0, lv.STATE.DEFAULT)
screen_3_H_plus.set_pos(220, 114)
screen_3_H_plus.set_size(41, 35)
screen_3_H_plus.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_3_H_plus, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_3_H_plus.set_style_bg_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_H_plus.set_style_bg_color(lv.color_hex(0x00c4ff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_H_plus.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_H_plus.set_style_radius(5, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_H_plus.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_H_plus.set_style_text_color(lv.color_hex(0xffffff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_H_plus.set_style_text_font(test_font("Alatsi_Regular", 33), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_H_plus.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_3_Humidity
screen_3_Humidity = lv.label(screen_3)
screen_3_Humidity.set_text("0 %")
screen_3_Humidity.set_long_mode(lv.label.LONG.WRAP)
screen_3_Humidity.set_pos(292, 149)
screen_3_Humidity.set_size(100, 32)
screen_3_Humidity.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_3_Humidity, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_3_Humidity.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_Humidity.set_style_radius(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_Humidity.set_style_text_color(lv.color_hex(0x000000), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_Humidity.set_style_text_font(test_font("montserratMedium", 16), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_Humidity.set_style_text_letter_space(2, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_Humidity.set_style_text_line_space(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_Humidity.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_Humidity.set_style_bg_opa(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_Humidity.set_style_pad_top(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_Humidity.set_style_pad_right(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_Humidity.set_style_pad_bottom(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_Humidity.set_style_pad_left(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_Humidity.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)

screen_3.update_layout()

def screen_img_1_event_handler(e):
    code = e.get_code()
    if (code == lv.EVENT.CLICKED):
        lv.scr_load_anim(screen_1, lv.SCR_LOAD_ANIM.NONE, 200, 200, False)

screen_img_1.add_event_cb(lambda e: screen_img_1_event_handler(e), lv.EVENT.ALL, None)

def screen_img_2_event_handler(e):
    code = e.get_code()
    if (code == lv.EVENT.CLICKED):
        lv.scr_load_anim(screen_2, lv.SCR_LOAD_ANIM.NONE, 200, 200, False)

screen_img_2.add_event_cb(lambda e: screen_img_2_event_handler(e), lv.EVENT.ALL, None)

def screen_img_3_event_handler(e):
    code = e.get_code()
    if (code == lv.EVENT.CLICKED):
        lv.scr_load_anim(screen_3, lv.SCR_LOAD_ANIM.NONE, 200, 200, False)

screen_img_3.add_event_cb(lambda e: screen_img_3_event_handler(e), lv.EVENT.ALL, None)

def screen_1_back_event_handler(e):
    code = e.get_code()
    if (code == lv.EVENT.CLICKED):
        lv.scr_load_anim(screen, lv.SCR_LOAD_ANIM.NONE, 200, 200, False)

screen_1_back.add_event_cb(lambda e: screen_1_back_event_handler(e), lv.EVENT.ALL, None)

def screen_1_T_plus_event_handler(e):
    code = e.get_code()

screen_1_T_plus.add_event_cb(lambda e: screen_1_T_plus_event_handler(e), lv.EVENT.ALL, None)

def screen_1_T_minus_event_handler(e):
    code = e.get_code()

screen_1_T_minus.add_event_cb(lambda e: screen_1_T_minus_event_handler(e), lv.EVENT.ALL, None)

def screen_1_H_minus_event_handler(e):
    code = e.get_code()

screen_1_H_minus.add_event_cb(lambda e: screen_1_H_minus_event_handler(e), lv.EVENT.ALL, None)

def screen_1_H_plus_event_handler(e):
    code = e.get_code()

screen_1_H_plus.add_event_cb(lambda e: screen_1_H_plus_event_handler(e), lv.EVENT.ALL, None)

def screen_2_back_event_handler(e):
    code = e.get_code()
    if (code == lv.EVENT.CLICKED):
        lv.scr_load_anim(screen, lv.SCR_LOAD_ANIM.NONE, 200, 200, False)

screen_2_back.add_event_cb(lambda e: screen_2_back_event_handler(e), lv.EVENT.ALL, None)

def screen_2_T_plus_event_handler(e):
    code = e.get_code()

screen_2_T_plus.add_event_cb(lambda e: screen_2_T_plus_event_handler(e), lv.EVENT.ALL, None)

def screen_2_T_minus_event_handler(e):
    code = e.get_code()

screen_2_T_minus.add_event_cb(lambda e: screen_2_T_minus_event_handler(e), lv.EVENT.ALL, None)

def screen_2_H_minus_event_handler(e):
    code = e.get_code()

screen_2_H_minus.add_event_cb(lambda e: screen_2_H_minus_event_handler(e), lv.EVENT.ALL, None)

def screen_2_H_plus_event_handler(e):
    code = e.get_code()

screen_2_H_plus.add_event_cb(lambda e: screen_2_H_plus_event_handler(e), lv.EVENT.ALL, None)

def screen_3_back_event_handler(e):
    code = e.get_code()
    if (code == lv.EVENT.CLICKED):
        lv.scr_load_anim(screen, lv.SCR_LOAD_ANIM.NONE, 200, 200, False)

screen_3_back.add_event_cb(lambda e: screen_3_back_event_handler(e), lv.EVENT.ALL, None)

def screen_3_T_plus_event_handler(e):
    code = e.get_code()

screen_3_T_plus.add_event_cb(lambda e: screen_3_T_plus_event_handler(e), lv.EVENT.ALL, None)

def screen_3_T_minus_event_handler(e):
    code = e.get_code()

screen_3_T_minus.add_event_cb(lambda e: screen_3_T_minus_event_handler(e), lv.EVENT.ALL, None)

def screen_3_H_minus_event_handler(e):
    code = e.get_code()

screen_3_H_minus.add_event_cb(lambda e: screen_3_H_minus_event_handler(e), lv.EVENT.ALL, None)

def screen_3_H_plus_event_handler(e):
    code = e.get_code()

screen_3_H_plus.add_event_cb(lambda e: screen_3_H_plus_event_handler(e), lv.EVENT.ALL, None)

# content from custom.py

# Load the default screen
lv.scr_load(screen)

while SDL.check():
    time.sleep_ms(5)

