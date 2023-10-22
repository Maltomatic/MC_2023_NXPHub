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

def screen1_ta_event_cb(e,kb):
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

def screen2_ta_event_cb(e,kb):
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

def screen3_ta_event_cb(e,kb):
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

def add_ta_event_cb(e,kb):
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
screen.set_style_bg_opa(72, lv.PART.MAIN|lv.STATE.DEFAULT)
screen.set_style_bg_color(lv.color_hex(0xff9d00), lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_img_1
screen_img_1 = lv.img(screen)
screen_img_1.set_src(load_image(r"C:\Users\justi\Documents\MCUXpressoIDE_11.8.0_1165\practice\scratch\generated\MicroPython\OIP_181_110.png"))
screen_img_1.add_flag(lv.obj.FLAG.CLICKABLE)
screen_img_1.set_pivot(50,50)
screen_img_1.set_angle(0)
screen_img_1.set_pos(36, 17)
screen_img_1.set_size(181, 110)
screen_img_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_img_1, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_img_1.set_style_img_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_img_2
screen_img_2 = lv.img(screen)
screen_img_2.set_src(load_image(r"C:\Users\justi\Documents\MCUXpressoIDE_11.8.0_1165\practice\scratch\generated\MicroPython\photo_6168027389217584763_y_176_122.png"))
screen_img_2.add_flag(lv.obj.FLAG.CLICKABLE)
screen_img_2.set_pivot(50,50)
screen_img_2.set_angle(0)
screen_img_2.set_pos(41, 139)
screen_img_2.set_size(176, 122)
screen_img_2.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_img_2, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_img_2.set_style_img_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_img_3
screen_img_3 = lv.img(screen)
screen_img_3.set_src(load_image(r"C:\Users\justi\Documents\MCUXpressoIDE_11.8.0_1165\practice\scratch\generated\MicroPython\R_180_115.png"))
screen_img_3.add_flag(lv.obj.FLAG.CLICKABLE)
screen_img_3.set_pivot(50,50)
screen_img_3.set_angle(0)
screen_img_3.set_pos(246, 79)
screen_img_3.set_size(180, 115)
screen_img_3.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_img_3, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_img_3.set_style_img_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_btn_1
screen_btn_1 = lv.btn(screen)
screen_btn_1_label = lv.label(screen_btn_1)
screen_btn_1_label.set_text("+")
screen_btn_1_label.set_long_mode(lv.label.LONG.WRAP)
screen_btn_1_label.align(lv.ALIGN.CENTER, 0, 0)
screen_btn_1.set_style_pad_all(0, lv.STATE.DEFAULT)
screen_btn_1.set_pos(406, 215)
screen_btn_1.set_size(40, 40)
screen_btn_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_btn_1, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_btn_1.set_style_bg_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_btn_1.set_style_bg_color(lv.color_hex(0x009ea9), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_btn_1.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_btn_1.set_style_radius(25, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_btn_1.set_style_shadow_width(3, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_btn_1.set_style_shadow_color(lv.color_hex(0x0d4b3b), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_btn_1.set_style_shadow_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_btn_1.set_style_shadow_spread(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_btn_1.set_style_shadow_ofs_x(1, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_btn_1.set_style_shadow_ofs_y(2, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_btn_1.set_style_text_color(lv.color_hex(0xffffff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_btn_1.set_style_text_font(test_font("Acme_Regular", 30), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_btn_1.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)

screen.update_layout()
# Create screen1
screen1 = lv.obj()
screen1.set_size(480, 272)
screen1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen1, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen1.set_style_bg_opa(0, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen1_img_1
screen1_img_1 = lv.img(screen1)
screen1_img_1.set_src(load_image(r"C:\Users\justi\Documents\MCUXpressoIDE_11.8.0_1165\practice\scratch\generated\MicroPython\OIP_486_276.png"))
screen1_img_1.add_flag(lv.obj.FLAG.CLICKABLE)
screen1_img_1.set_pivot(50,50)
screen1_img_1.set_angle(0)
screen1_img_1.set_pos(-5, -3)
screen1_img_1.set_size(486, 276)
screen1_img_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen1_img_1, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen1_img_1.set_style_img_opa(144, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen1_label_2
screen1_label_2 = lv.label(screen1)
screen1_label_2.set_text(" Fan")
screen1_label_2.set_long_mode(lv.label.LONG.WRAP)
screen1_label_2.set_pos(173, 212)
screen1_label_2.set_size(127, 17)
screen1_label_2.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen1_label_2, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen1_label_2.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_label_2.set_style_radius(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_label_2.set_style_text_color(lv.color_hex(0x000000), lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_label_2.set_style_text_font(test_font("Alatsi_Regular", 16), lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_label_2.set_style_text_letter_space(2, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_label_2.set_style_text_line_space(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_label_2.set_style_text_align(lv.TEXT_ALIGN.LEFT, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_label_2.set_style_bg_opa(165, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_label_2.set_style_bg_color(lv.color_hex(0xd9dbdb), lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_label_2.set_style_bg_grad_dir(lv.GRAD_DIR.HOR, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_label_2.set_style_bg_grad_color(lv.color_hex(0xa6ff00), lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_label_2.set_style_pad_top(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_label_2.set_style_pad_right(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_label_2.set_style_pad_bottom(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_label_2.set_style_pad_left(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_label_2.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen1_label_1
screen1_label_1 = lv.label(screen1)
screen1_label_1.set_text(" Camera ")
screen1_label_1.set_long_mode(lv.label.LONG.WRAP)
screen1_label_1.set_pos(173, 181)
screen1_label_1.set_size(127, 17)
screen1_label_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen1_label_1, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen1_label_1.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_label_1.set_style_radius(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_label_1.set_style_text_color(lv.color_hex(0x000000), lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_label_1.set_style_text_font(test_font("Alatsi_Regular", 16), lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_label_1.set_style_text_letter_space(2, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_label_1.set_style_text_line_space(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_label_1.set_style_text_align(lv.TEXT_ALIGN.LEFT, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_label_1.set_style_bg_opa(150, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_label_1.set_style_bg_color(lv.color_hex(0xf1f1f1), lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_label_1.set_style_bg_grad_dir(lv.GRAD_DIR.HOR, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_label_1.set_style_bg_grad_color(lv.color_hex(0x0078f1), lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_label_1.set_style_pad_top(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_label_1.set_style_pad_right(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_label_1.set_style_pad_bottom(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_label_1.set_style_pad_left(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_label_1.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen1_Menu
screen1_Menu = lv.btn(screen1)
screen1_Menu_label = lv.label(screen1_Menu)
screen1_Menu_label.set_text("Menu")
screen1_Menu_label.set_long_mode(lv.label.LONG.WRAP)
screen1_Menu_label.align(lv.ALIGN.CENTER, 0, 0)
screen1_Menu.set_style_pad_all(0, lv.STATE.DEFAULT)
screen1_Menu.set_pos(25, 19)
screen1_Menu.set_size(100, 36)
screen1_Menu.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen1_Menu, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen1_Menu.set_style_bg_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_Menu.set_style_bg_color(lv.color_hex(0x37abf5), lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_Menu.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_Menu.set_style_radius(5, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_Menu.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_Menu.set_style_text_color(lv.color_hex(0xffffff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_Menu.set_style_text_font(test_font("montserratMedium", 16), lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_Menu.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen1_btn_1
screen1_btn_1 = lv.btn(screen1)
screen1_btn_1_label = lv.label(screen1_btn_1)
screen1_btn_1_label.set_text("Temperature\n& Humidity")
screen1_btn_1_label.set_long_mode(lv.label.LONG.WRAP)
screen1_btn_1_label.align(lv.ALIGN.CENTER, 0, 0)
screen1_btn_1.set_style_pad_all(0, lv.STATE.DEFAULT)
screen1_btn_1.set_pos(25, 177)
screen1_btn_1.set_size(107, 53)
screen1_btn_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen1_btn_1, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen1_btn_1.set_style_bg_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_btn_1.set_style_bg_color(lv.color_hex(0x07624a), lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_btn_1.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_btn_1.set_style_radius(5, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_btn_1.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_btn_1.set_style_text_color(lv.color_hex(0xffffff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_btn_1.set_style_text_font(test_font("simsun", 16), lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_btn_1.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen1_sw_1
screen1_sw_1 = lv.switch(screen1)
screen1_sw_1.set_pos(264, 181)
screen1_sw_1.set_size(40, 20)
screen1_sw_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen1_sw_1, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen1_sw_1.set_style_bg_opa(165, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_sw_1.set_style_bg_color(lv.color_hex(0x2F92DA), lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_sw_1.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_sw_1.set_style_radius(10, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_sw_1.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)

# Set style for screen1_sw_1, Part: lv.PART.INDICATOR, State: lv.STATE.CHECKED.
screen1_sw_1.set_style_bg_opa(255, lv.PART.INDICATOR|lv.STATE.CHECKED)
screen1_sw_1.set_style_bg_color(lv.color_hex(0x2195f6), lv.PART.INDICATOR|lv.STATE.CHECKED)
screen1_sw_1.set_style_border_width(0, lv.PART.INDICATOR|lv.STATE.CHECKED)

# Set style for screen1_sw_1, Part: lv.PART.KNOB, State: lv.STATE.DEFAULT.
screen1_sw_1.set_style_bg_opa(255, lv.PART.KNOB|lv.STATE.DEFAULT)
screen1_sw_1.set_style_bg_color(lv.color_hex(0xffffff), lv.PART.KNOB|lv.STATE.DEFAULT)
screen1_sw_1.set_style_border_width(0, lv.PART.KNOB|lv.STATE.DEFAULT)
screen1_sw_1.set_style_radius(100, lv.PART.KNOB|lv.STATE.DEFAULT)

# Create screen1_sw_2
screen1_sw_2 = lv.switch(screen1)
screen1_sw_2.set_pos(264, 209)
screen1_sw_2.set_size(40, 20)
screen1_sw_2.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen1_sw_2, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen1_sw_2.set_style_bg_opa(165, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_sw_2.set_style_bg_color(lv.color_hex(0xbcd202), lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_sw_2.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_sw_2.set_style_radius(10, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_sw_2.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)

# Set style for screen1_sw_2, Part: lv.PART.INDICATOR, State: lv.STATE.CHECKED.
screen1_sw_2.set_style_bg_opa(255, lv.PART.INDICATOR|lv.STATE.CHECKED)
screen1_sw_2.set_style_bg_color(lv.color_hex(0x2195f6), lv.PART.INDICATOR|lv.STATE.CHECKED)
screen1_sw_2.set_style_border_width(0, lv.PART.INDICATOR|lv.STATE.CHECKED)

# Set style for screen1_sw_2, Part: lv.PART.KNOB, State: lv.STATE.DEFAULT.
screen1_sw_2.set_style_bg_opa(255, lv.PART.KNOB|lv.STATE.DEFAULT)
screen1_sw_2.set_style_bg_color(lv.color_hex(0xffffff), lv.PART.KNOB|lv.STATE.DEFAULT)
screen1_sw_2.set_style_border_width(0, lv.PART.KNOB|lv.STATE.DEFAULT)
screen1_sw_2.set_style_radius(100, lv.PART.KNOB|lv.STATE.DEFAULT)

# Create screen1_btn_2
screen1_btn_2 = lv.btn(screen1)
screen1_btn_2_label = lv.label(screen1_btn_2)
screen1_btn_2_label.set_text("Baby\nAlarm")
screen1_btn_2_label.set_long_mode(lv.label.LONG.WRAP)
screen1_btn_2_label.align(lv.ALIGN.CENTER, 0, 0)
screen1_btn_2.set_style_pad_all(0, lv.STATE.DEFAULT)
screen1_btn_2.set_pos(348, 176)
screen1_btn_2.set_size(107, 53)
screen1_btn_2.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen1_btn_2, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen1_btn_2.set_style_bg_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_btn_2.set_style_bg_color(lv.color_hex(0xd60025), lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_btn_2.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_btn_2.set_style_radius(5, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_btn_2.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_btn_2.set_style_text_color(lv.color_hex(0xffffff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_btn_2.set_style_text_font(test_font("simsun", 16), lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_btn_2.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen1_T1
screen1_T1 = lv.label(screen1)
screen1_T1.set_text("T")
screen1_T1.set_long_mode(lv.label.LONG.WRAP)
screen1_T1.set_pos(186, 42)
screen1_T1.set_size(109, 17)
screen1_T1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen1_T1, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen1_T1.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_T1.set_style_radius(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_T1.set_style_text_color(lv.color_hex(0x000000), lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_T1.set_style_text_font(test_font("Amiko_Regular", 16), lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_T1.set_style_text_letter_space(2, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_T1.set_style_text_line_space(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_T1.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_T1.set_style_bg_opa(172, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_T1.set_style_bg_color(lv.color_hex(0x585df6), lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_T1.set_style_bg_grad_dir(lv.GRAD_DIR.HOR, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_T1.set_style_bg_grad_color(lv.color_hex(0xee80fe), lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_T1.set_style_pad_top(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_T1.set_style_pad_right(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_T1.set_style_pad_bottom(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_T1.set_style_pad_left(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_T1.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen1_H1
screen1_H1 = lv.label(screen1)
screen1_H1.set_text("H")
screen1_H1.set_long_mode(lv.label.LONG.WRAP)
screen1_H1.set_pos(348, 42)
screen1_H1.set_size(92, 18)
screen1_H1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen1_H1, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen1_H1.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_H1.set_style_radius(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_H1.set_style_text_color(lv.color_hex(0x000000), lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_H1.set_style_text_font(test_font("Amiko_Regular", 16), lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_H1.set_style_text_letter_space(2, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_H1.set_style_text_line_space(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_H1.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_H1.set_style_bg_opa(120, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_H1.set_style_bg_color(lv.color_hex(0x0dcb75), lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_H1.set_style_bg_grad_dir(lv.GRAD_DIR.HOR, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_H1.set_style_bg_grad_color(lv.color_hex(0x3cb6f6), lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_H1.set_style_pad_top(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_H1.set_style_pad_right(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_H1.set_style_pad_bottom(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_H1.set_style_pad_left(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_H1.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen1_label_3
screen1_label_3 = lv.label(screen1)
screen1_label_3.set_text("Humidity")
screen1_label_3.set_long_mode(lv.label.LONG.WRAP)
screen1_label_3.set_pos(348, 19)
screen1_label_3.set_size(93, 23)
screen1_label_3.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen1_label_3, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen1_label_3.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_label_3.set_style_radius(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_label_3.set_style_text_color(lv.color_hex(0x000000), lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_label_3.set_style_text_font(test_font("Adventpro_regular", 20), lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_label_3.set_style_text_letter_space(2, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_label_3.set_style_text_line_space(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_label_3.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_label_3.set_style_bg_opa(134, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_label_3.set_style_bg_color(lv.color_hex(0xffffff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_label_3.set_style_pad_top(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_label_3.set_style_pad_right(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_label_3.set_style_pad_bottom(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_label_3.set_style_pad_left(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_label_3.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen1_label_4
screen1_label_4 = lv.label(screen1)
screen1_label_4.set_text("Temperature")
screen1_label_4.set_long_mode(lv.label.LONG.WRAP)
screen1_label_4.set_pos(184, 19)
screen1_label_4.set_size(112, 23)
screen1_label_4.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen1_label_4, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen1_label_4.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_label_4.set_style_radius(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_label_4.set_style_text_color(lv.color_hex(0x000000), lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_label_4.set_style_text_font(test_font("Adventpro_regular", 20), lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_label_4.set_style_text_letter_space(2, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_label_4.set_style_text_line_space(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_label_4.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_label_4.set_style_bg_opa(134, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_label_4.set_style_bg_color(lv.color_hex(0xffffff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_label_4.set_style_pad_top(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_label_4.set_style_pad_right(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_label_4.set_style_pad_bottom(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_label_4.set_style_pad_left(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen1_label_4.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)

screen1.update_layout()
# Create screen2
screen2 = lv.obj()
screen2.set_size(480, 272)
screen2.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen2, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen2.set_style_bg_opa(0, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen2_img_1
screen2_img_1 = lv.img(screen2)
screen2_img_1.set_src(load_image(r"C:\Users\justi\Documents\MCUXpressoIDE_11.8.0_1165\practice\scratch\generated\MicroPython\photo_6168027389217584763_y_482_300.png"))
screen2_img_1.add_flag(lv.obj.FLAG.CLICKABLE)
screen2_img_1.set_pivot(50,50)
screen2_img_1.set_angle(0)
screen2_img_1.set_pos(-1, -22)
screen2_img_1.set_size(482, 300)
screen2_img_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen2_img_1, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen2_img_1.set_style_img_opa(144, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen2_label_7
screen2_label_7 = lv.label(screen2)
screen2_label_7.set_text(" Camera ")
screen2_label_7.set_long_mode(lv.label.LONG.WRAP)
screen2_label_7.set_pos(255, 196)
screen2_label_7.set_size(127, 17)
screen2_label_7.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen2_label_7, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen2_label_7.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_label_7.set_style_radius(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_label_7.set_style_text_color(lv.color_hex(0x000000), lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_label_7.set_style_text_font(test_font("Alatsi_Regular", 16), lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_label_7.set_style_text_letter_space(2, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_label_7.set_style_text_line_space(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_label_7.set_style_text_align(lv.TEXT_ALIGN.LEFT, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_label_7.set_style_bg_opa(150, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_label_7.set_style_bg_color(lv.color_hex(0xf1f1f1), lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_label_7.set_style_bg_grad_dir(lv.GRAD_DIR.HOR, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_label_7.set_style_bg_grad_color(lv.color_hex(0x0078f1), lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_label_7.set_style_pad_top(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_label_7.set_style_pad_right(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_label_7.set_style_pad_bottom(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_label_7.set_style_pad_left(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_label_7.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen2_label_6
screen2_label_6 = lv.label(screen2)
screen2_label_6.set_text(" Fan")
screen2_label_6.set_long_mode(lv.label.LONG.WRAP)
screen2_label_6.set_pos(255, 224)
screen2_label_6.set_size(127, 17)
screen2_label_6.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen2_label_6, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen2_label_6.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_label_6.set_style_radius(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_label_6.set_style_text_color(lv.color_hex(0x000000), lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_label_6.set_style_text_font(test_font("Alatsi_Regular", 16), lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_label_6.set_style_text_letter_space(2, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_label_6.set_style_text_line_space(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_label_6.set_style_text_align(lv.TEXT_ALIGN.LEFT, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_label_6.set_style_bg_opa(165, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_label_6.set_style_bg_color(lv.color_hex(0xd9dbdb), lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_label_6.set_style_bg_grad_dir(lv.GRAD_DIR.HOR, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_label_6.set_style_bg_grad_color(lv.color_hex(0xa6ff00), lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_label_6.set_style_pad_top(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_label_6.set_style_pad_right(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_label_6.set_style_pad_bottom(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_label_6.set_style_pad_left(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_label_6.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen2_Menu
screen2_Menu = lv.btn(screen2)
screen2_Menu_label = lv.label(screen2_Menu)
screen2_Menu_label.set_text("Menu")
screen2_Menu_label.set_long_mode(lv.label.LONG.WRAP)
screen2_Menu_label.align(lv.ALIGN.CENTER, 0, 0)
screen2_Menu.set_style_pad_all(0, lv.STATE.DEFAULT)
screen2_Menu.set_pos(25, 16)
screen2_Menu.set_size(100, 36)
screen2_Menu.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen2_Menu, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen2_Menu.set_style_bg_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_Menu.set_style_bg_color(lv.color_hex(0x08c3e4), lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_Menu.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_Menu.set_style_radius(5, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_Menu.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_Menu.set_style_text_color(lv.color_hex(0xffffff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_Menu.set_style_text_font(test_font("montserratMedium", 16), lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_Menu.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen2_btn_1
screen2_btn_1 = lv.btn(screen2)
screen2_btn_1_label = lv.label(screen2_btn_1)
screen2_btn_1_label.set_text("Temperature\n& Humidity")
screen2_btn_1_label.set_long_mode(lv.label.LONG.WRAP)
screen2_btn_1_label.align(lv.ALIGN.CENTER, 0, 0)
screen2_btn_1.set_style_pad_all(0, lv.STATE.DEFAULT)
screen2_btn_1.set_pos(106, 194)
screen2_btn_1.set_size(107, 53)
screen2_btn_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen2_btn_1, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen2_btn_1.set_style_bg_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_btn_1.set_style_bg_color(lv.color_hex(0x07624a), lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_btn_1.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_btn_1.set_style_radius(5, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_btn_1.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_btn_1.set_style_text_color(lv.color_hex(0xffffff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_btn_1.set_style_text_font(test_font("simsun", 16), lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_btn_1.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen2_sw_1
screen2_sw_1 = lv.switch(screen2)
screen2_sw_1.set_pos(346, 193)
screen2_sw_1.set_size(40, 20)
screen2_sw_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen2_sw_1, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen2_sw_1.set_style_bg_opa(165, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_sw_1.set_style_bg_color(lv.color_hex(0x2F92DA), lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_sw_1.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_sw_1.set_style_radius(10, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_sw_1.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)

# Set style for screen2_sw_1, Part: lv.PART.INDICATOR, State: lv.STATE.CHECKED.
screen2_sw_1.set_style_bg_opa(255, lv.PART.INDICATOR|lv.STATE.CHECKED)
screen2_sw_1.set_style_bg_color(lv.color_hex(0x2195f6), lv.PART.INDICATOR|lv.STATE.CHECKED)
screen2_sw_1.set_style_border_width(0, lv.PART.INDICATOR|lv.STATE.CHECKED)

# Set style for screen2_sw_1, Part: lv.PART.KNOB, State: lv.STATE.DEFAULT.
screen2_sw_1.set_style_bg_opa(255, lv.PART.KNOB|lv.STATE.DEFAULT)
screen2_sw_1.set_style_bg_color(lv.color_hex(0xffffff), lv.PART.KNOB|lv.STATE.DEFAULT)
screen2_sw_1.set_style_border_width(0, lv.PART.KNOB|lv.STATE.DEFAULT)
screen2_sw_1.set_style_radius(100, lv.PART.KNOB|lv.STATE.DEFAULT)

# Create screen2_sw_2
screen2_sw_2 = lv.switch(screen2)
screen2_sw_2.set_pos(346, 221)
screen2_sw_2.set_size(40, 20)
screen2_sw_2.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen2_sw_2, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen2_sw_2.set_style_bg_opa(165, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_sw_2.set_style_bg_color(lv.color_hex(0xbcd202), lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_sw_2.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_sw_2.set_style_radius(10, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_sw_2.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)

# Set style for screen2_sw_2, Part: lv.PART.INDICATOR, State: lv.STATE.CHECKED.
screen2_sw_2.set_style_bg_opa(255, lv.PART.INDICATOR|lv.STATE.CHECKED)
screen2_sw_2.set_style_bg_color(lv.color_hex(0x2195f6), lv.PART.INDICATOR|lv.STATE.CHECKED)
screen2_sw_2.set_style_border_width(0, lv.PART.INDICATOR|lv.STATE.CHECKED)

# Set style for screen2_sw_2, Part: lv.PART.KNOB, State: lv.STATE.DEFAULT.
screen2_sw_2.set_style_bg_opa(255, lv.PART.KNOB|lv.STATE.DEFAULT)
screen2_sw_2.set_style_bg_color(lv.color_hex(0xffffff), lv.PART.KNOB|lv.STATE.DEFAULT)
screen2_sw_2.set_style_border_width(0, lv.PART.KNOB|lv.STATE.DEFAULT)
screen2_sw_2.set_style_radius(100, lv.PART.KNOB|lv.STATE.DEFAULT)

# Create screen2_H2
screen2_H2 = lv.label(screen2)
screen2_H2.set_text("H")
screen2_H2.set_long_mode(lv.label.LONG.WRAP)
screen2_H2.set_pos(348, 42)
screen2_H2.set_size(92, 18)
screen2_H2.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen2_H2, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen2_H2.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_H2.set_style_radius(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_H2.set_style_text_color(lv.color_hex(0x000000), lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_H2.set_style_text_font(test_font("Amiko_Regular", 16), lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_H2.set_style_text_letter_space(2, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_H2.set_style_text_line_space(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_H2.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_H2.set_style_bg_opa(120, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_H2.set_style_bg_color(lv.color_hex(0x00c894), lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_H2.set_style_bg_grad_dir(lv.GRAD_DIR.HOR, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_H2.set_style_bg_grad_color(lv.color_hex(0x2195f6), lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_H2.set_style_pad_top(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_H2.set_style_pad_right(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_H2.set_style_pad_bottom(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_H2.set_style_pad_left(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_H2.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen2_label_5
screen2_label_5 = lv.label(screen2)
screen2_label_5.set_text("Humidity")
screen2_label_5.set_long_mode(lv.label.LONG.WRAP)
screen2_label_5.set_pos(348, 19)
screen2_label_5.set_size(93, 23)
screen2_label_5.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen2_label_5, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen2_label_5.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_label_5.set_style_radius(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_label_5.set_style_text_color(lv.color_hex(0x000000), lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_label_5.set_style_text_font(test_font("Adventpro_regular", 20), lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_label_5.set_style_text_letter_space(2, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_label_5.set_style_text_line_space(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_label_5.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_label_5.set_style_bg_opa(134, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_label_5.set_style_bg_color(lv.color_hex(0xffffff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_label_5.set_style_pad_top(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_label_5.set_style_pad_right(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_label_5.set_style_pad_bottom(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_label_5.set_style_pad_left(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_label_5.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen2_T2
screen2_T2 = lv.label(screen2)
screen2_T2.set_text("T")
screen2_T2.set_long_mode(lv.label.LONG.WRAP)
screen2_T2.set_pos(186, 42)
screen2_T2.set_size(109, 17)
screen2_T2.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen2_T2, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen2_T2.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_T2.set_style_radius(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_T2.set_style_text_color(lv.color_hex(0x000000), lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_T2.set_style_text_font(test_font("Amiko_Regular", 16), lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_T2.set_style_text_letter_space(2, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_T2.set_style_text_line_space(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_T2.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_T2.set_style_bg_opa(115, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_T2.set_style_bg_color(lv.color_hex(0xff00db), lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_T2.set_style_bg_grad_dir(lv.GRAD_DIR.HOR, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_T2.set_style_bg_grad_color(lv.color_hex(0x2195f6), lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_T2.set_style_pad_top(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_T2.set_style_pad_right(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_T2.set_style_pad_bottom(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_T2.set_style_pad_left(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_T2.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen2_label_3
screen2_label_3 = lv.label(screen2)
screen2_label_3.set_text("Temperature")
screen2_label_3.set_long_mode(lv.label.LONG.WRAP)
screen2_label_3.set_pos(184, 19)
screen2_label_3.set_size(112, 23)
screen2_label_3.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen2_label_3, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen2_label_3.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_label_3.set_style_radius(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_label_3.set_style_text_color(lv.color_hex(0x000000), lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_label_3.set_style_text_font(test_font("Adventpro_regular", 20), lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_label_3.set_style_text_letter_space(2, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_label_3.set_style_text_line_space(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_label_3.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_label_3.set_style_bg_opa(134, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_label_3.set_style_bg_color(lv.color_hex(0xffffff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_label_3.set_style_pad_top(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_label_3.set_style_pad_right(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_label_3.set_style_pad_bottom(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_label_3.set_style_pad_left(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen2_label_3.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)

screen2.update_layout()
# Create screen3
screen3 = lv.obj()
screen3.set_size(480, 272)
screen3.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen3, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen3.set_style_bg_opa(0, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen3_img_1
screen3_img_1 = lv.img(screen3)
screen3_img_1.set_src(load_image(r"C:\Users\justi\Documents\MCUXpressoIDE_11.8.0_1165\practice\scratch\generated\MicroPython\R_483_285.png"))
screen3_img_1.add_flag(lv.obj.FLAG.CLICKABLE)
screen3_img_1.set_pivot(50,50)
screen3_img_1.set_angle(0)
screen3_img_1.set_pos(-1, 0)
screen3_img_1.set_size(483, 285)
screen3_img_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen3_img_1, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen3_img_1.set_style_img_opa(160, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen3_Menu
screen3_Menu = lv.btn(screen3)
screen3_Menu_label = lv.label(screen3_Menu)
screen3_Menu_label.set_text("Menu")
screen3_Menu_label.set_long_mode(lv.label.LONG.WRAP)
screen3_Menu_label.align(lv.ALIGN.CENTER, 0, 0)
screen3_Menu.set_style_pad_all(0, lv.STATE.DEFAULT)
screen3_Menu.set_pos(25, 16)
screen3_Menu.set_size(100, 36)
screen3_Menu.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen3_Menu, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen3_Menu.set_style_bg_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_Menu.set_style_bg_color(lv.color_hex(0x00b7e7), lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_Menu.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_Menu.set_style_radius(5, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_Menu.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_Menu.set_style_text_color(lv.color_hex(0xffffff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_Menu.set_style_text_font(test_font("montserratMedium", 16), lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_Menu.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen3_btn_1
screen3_btn_1 = lv.btn(screen3)
screen3_btn_1_label = lv.label(screen3_btn_1)
screen3_btn_1_label.set_text("Temperature\n& Humidity")
screen3_btn_1_label.set_long_mode(lv.label.LONG.WRAP)
screen3_btn_1_label.align(lv.ALIGN.CENTER, 0, 0)
screen3_btn_1.set_style_pad_all(0, lv.STATE.DEFAULT)
screen3_btn_1.set_pos(95, 193)
screen3_btn_1.set_size(107, 53)
screen3_btn_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen3_btn_1, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen3_btn_1.set_style_bg_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_btn_1.set_style_bg_color(lv.color_hex(0x07624a), lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_btn_1.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_btn_1.set_style_radius(5, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_btn_1.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_btn_1.set_style_text_color(lv.color_hex(0xffffff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_btn_1.set_style_text_font(test_font("simsun", 16), lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_btn_1.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen3_H3
screen3_H3 = lv.label(screen3)
screen3_H3.set_text("H")
screen3_H3.set_long_mode(lv.label.LONG.WRAP)
screen3_H3.set_pos(348, 42)
screen3_H3.set_size(92, 18)
screen3_H3.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen3_H3, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen3_H3.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_H3.set_style_radius(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_H3.set_style_text_color(lv.color_hex(0x000000), lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_H3.set_style_text_font(test_font("Amiko_Regular", 16), lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_H3.set_style_text_letter_space(2, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_H3.set_style_text_line_space(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_H3.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_H3.set_style_bg_opa(145, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_H3.set_style_bg_color(lv.color_hex(0x00ffbd), lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_H3.set_style_bg_grad_dir(lv.GRAD_DIR.HOR, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_H3.set_style_bg_grad_color(lv.color_hex(0x2195f6), lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_H3.set_style_pad_top(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_H3.set_style_pad_right(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_H3.set_style_pad_bottom(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_H3.set_style_pad_left(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_H3.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen3_label_5
screen3_label_5 = lv.label(screen3)
screen3_label_5.set_text("Humidity")
screen3_label_5.set_long_mode(lv.label.LONG.WRAP)
screen3_label_5.set_pos(348, 19)
screen3_label_5.set_size(93, 23)
screen3_label_5.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen3_label_5, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen3_label_5.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_label_5.set_style_radius(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_label_5.set_style_text_color(lv.color_hex(0x000000), lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_label_5.set_style_text_font(test_font("Adventpro_regular", 20), lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_label_5.set_style_text_letter_space(2, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_label_5.set_style_text_line_space(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_label_5.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_label_5.set_style_bg_opa(134, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_label_5.set_style_bg_color(lv.color_hex(0xffffff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_label_5.set_style_pad_top(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_label_5.set_style_pad_right(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_label_5.set_style_pad_bottom(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_label_5.set_style_pad_left(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_label_5.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen3_T3
screen3_T3 = lv.label(screen3)
screen3_T3.set_text("T")
screen3_T3.set_long_mode(lv.label.LONG.WRAP)
screen3_T3.set_pos(186, 42)
screen3_T3.set_size(109, 17)
screen3_T3.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen3_T3, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen3_T3.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_T3.set_style_radius(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_T3.set_style_text_color(lv.color_hex(0x000000), lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_T3.set_style_text_font(test_font("Amiko_Regular", 16), lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_T3.set_style_text_letter_space(2, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_T3.set_style_text_line_space(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_T3.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_T3.set_style_bg_opa(129, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_T3.set_style_bg_color(lv.color_hex(0xffabec), lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_T3.set_style_bg_grad_dir(lv.GRAD_DIR.HOR, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_T3.set_style_bg_grad_color(lv.color_hex(0x7f80ff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_T3.set_style_pad_top(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_T3.set_style_pad_right(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_T3.set_style_pad_bottom(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_T3.set_style_pad_left(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_T3.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen3_label_3
screen3_label_3 = lv.label(screen3)
screen3_label_3.set_text("Temperature")
screen3_label_3.set_long_mode(lv.label.LONG.WRAP)
screen3_label_3.set_pos(184, 19)
screen3_label_3.set_size(112, 23)
screen3_label_3.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen3_label_3, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen3_label_3.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_label_3.set_style_radius(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_label_3.set_style_text_color(lv.color_hex(0x000000), lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_label_3.set_style_text_font(test_font("Adventpro_regular", 20), lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_label_3.set_style_text_letter_space(2, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_label_3.set_style_text_line_space(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_label_3.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_label_3.set_style_bg_opa(134, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_label_3.set_style_bg_color(lv.color_hex(0xffffff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_label_3.set_style_pad_top(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_label_3.set_style_pad_right(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_label_3.set_style_pad_bottom(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_label_3.set_style_pad_left(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_label_3.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen3_label_7
screen3_label_7 = lv.label(screen3)
screen3_label_7.set_text(" Fan")
screen3_label_7.set_long_mode(lv.label.LONG.WRAP)
screen3_label_7.set_pos(255, 224)
screen3_label_7.set_size(127, 17)
screen3_label_7.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen3_label_7, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen3_label_7.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_label_7.set_style_radius(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_label_7.set_style_text_color(lv.color_hex(0x000000), lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_label_7.set_style_text_font(test_font("Alatsi_Regular", 16), lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_label_7.set_style_text_letter_space(2, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_label_7.set_style_text_line_space(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_label_7.set_style_text_align(lv.TEXT_ALIGN.LEFT, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_label_7.set_style_bg_opa(165, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_label_7.set_style_bg_color(lv.color_hex(0xd9dbdb), lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_label_7.set_style_bg_grad_dir(lv.GRAD_DIR.HOR, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_label_7.set_style_bg_grad_color(lv.color_hex(0xa6ff00), lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_label_7.set_style_pad_top(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_label_7.set_style_pad_right(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_label_7.set_style_pad_bottom(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_label_7.set_style_pad_left(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_label_7.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen3_label_6
screen3_label_6 = lv.label(screen3)
screen3_label_6.set_text(" Camera ")
screen3_label_6.set_long_mode(lv.label.LONG.WRAP)
screen3_label_6.set_pos(255, 196)
screen3_label_6.set_size(127, 17)
screen3_label_6.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen3_label_6, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen3_label_6.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_label_6.set_style_radius(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_label_6.set_style_text_color(lv.color_hex(0x000000), lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_label_6.set_style_text_font(test_font("Alatsi_Regular", 16), lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_label_6.set_style_text_letter_space(2, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_label_6.set_style_text_line_space(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_label_6.set_style_text_align(lv.TEXT_ALIGN.LEFT, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_label_6.set_style_bg_opa(150, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_label_6.set_style_bg_color(lv.color_hex(0xf1f1f1), lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_label_6.set_style_bg_grad_dir(lv.GRAD_DIR.HOR, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_label_6.set_style_bg_grad_color(lv.color_hex(0x0078f1), lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_label_6.set_style_pad_top(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_label_6.set_style_pad_right(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_label_6.set_style_pad_bottom(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_label_6.set_style_pad_left(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_label_6.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen3_sw_1
screen3_sw_1 = lv.switch(screen3)
screen3_sw_1.set_pos(348, 193)
screen3_sw_1.set_size(40, 20)
screen3_sw_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen3_sw_1, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen3_sw_1.set_style_bg_opa(165, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_sw_1.set_style_bg_color(lv.color_hex(0x2F92DA), lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_sw_1.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_sw_1.set_style_radius(10, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_sw_1.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)

# Set style for screen3_sw_1, Part: lv.PART.INDICATOR, State: lv.STATE.CHECKED.
screen3_sw_1.set_style_bg_opa(255, lv.PART.INDICATOR|lv.STATE.CHECKED)
screen3_sw_1.set_style_bg_color(lv.color_hex(0x2195f6), lv.PART.INDICATOR|lv.STATE.CHECKED)
screen3_sw_1.set_style_border_width(0, lv.PART.INDICATOR|lv.STATE.CHECKED)

# Set style for screen3_sw_1, Part: lv.PART.KNOB, State: lv.STATE.DEFAULT.
screen3_sw_1.set_style_bg_opa(255, lv.PART.KNOB|lv.STATE.DEFAULT)
screen3_sw_1.set_style_bg_color(lv.color_hex(0xffffff), lv.PART.KNOB|lv.STATE.DEFAULT)
screen3_sw_1.set_style_border_width(0, lv.PART.KNOB|lv.STATE.DEFAULT)
screen3_sw_1.set_style_radius(100, lv.PART.KNOB|lv.STATE.DEFAULT)

# Create screen3_sw_2
screen3_sw_2 = lv.switch(screen3)
screen3_sw_2.set_pos(348, 222)
screen3_sw_2.set_size(40, 19)
screen3_sw_2.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen3_sw_2, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen3_sw_2.set_style_bg_opa(165, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_sw_2.set_style_bg_color(lv.color_hex(0xbcd202), lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_sw_2.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_sw_2.set_style_radius(10, lv.PART.MAIN|lv.STATE.DEFAULT)
screen3_sw_2.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)

# Set style for screen3_sw_2, Part: lv.PART.INDICATOR, State: lv.STATE.CHECKED.
screen3_sw_2.set_style_bg_opa(255, lv.PART.INDICATOR|lv.STATE.CHECKED)
screen3_sw_2.set_style_bg_color(lv.color_hex(0x2195f6), lv.PART.INDICATOR|lv.STATE.CHECKED)
screen3_sw_2.set_style_border_width(0, lv.PART.INDICATOR|lv.STATE.CHECKED)

# Set style for screen3_sw_2, Part: lv.PART.KNOB, State: lv.STATE.DEFAULT.
screen3_sw_2.set_style_bg_opa(255, lv.PART.KNOB|lv.STATE.DEFAULT)
screen3_sw_2.set_style_bg_color(lv.color_hex(0xffffff), lv.PART.KNOB|lv.STATE.DEFAULT)
screen3_sw_2.set_style_border_width(0, lv.PART.KNOB|lv.STATE.DEFAULT)
screen3_sw_2.set_style_radius(100, lv.PART.KNOB|lv.STATE.DEFAULT)

screen3.update_layout()
# Create screen_1
screen_1 = lv.obj()
screen_1.set_size(480, 272)
screen_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_1, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_1.set_style_bg_opa(0, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_1_img_2
screen_1_img_2 = lv.img(screen_1)
screen_1_img_2.set_src(load_image(r"C:\Users\justi\Documents\MCUXpressoIDE_11.8.0_1165\practice\scratch\generated\MicroPython\OIP_486_276.png"))
screen_1_img_2.add_flag(lv.obj.FLAG.CLICKABLE)
screen_1_img_2.set_pivot(50,50)
screen_1_img_2.set_angle(0)
screen_1_img_2.set_pos(-5, -3)
screen_1_img_2.set_size(486, 276)
screen_1_img_2.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_1_img_2, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_1_img_2.set_style_img_opa(141, lv.PART.MAIN|lv.STATE.DEFAULT)

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
screen_1_Temp.set_pos(191, 145)
screen_1_Temp.set_size(37, 20)
screen_1_Temp.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_1_Temp, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_1_Temp.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Temp.set_style_radius(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Temp.set_style_text_color(lv.color_hex(0x000000), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Temp.set_style_text_font(test_font("montserratMedium", 16), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Temp.set_style_text_letter_space(2, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Temp.set_style_text_line_space(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Temp.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Temp.set_style_bg_opa(181, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Temp.set_style_bg_color(lv.color_hex(0xffffff), lv.PART.MAIN|lv.STATE.DEFAULT)
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
screen_1_T_plus.set_pos(26, 107)
screen_1_T_plus.set_size(40, 40)
screen_1_T_plus.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_1_T_plus, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_1_T_plus.set_style_bg_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_T_plus.set_style_bg_color(lv.color_hex(0x009ea9), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_T_plus.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_T_plus.set_style_radius(25, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_T_plus.set_style_shadow_width(3, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_T_plus.set_style_shadow_color(lv.color_hex(0x0d4b3b), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_T_plus.set_style_shadow_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_T_plus.set_style_shadow_spread(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_T_plus.set_style_shadow_ofs_x(1, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_T_plus.set_style_shadow_ofs_y(2, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_T_plus.set_style_text_color(lv.color_hex(0xffffff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_T_plus.set_style_text_font(test_font("Acme_Regular", 30), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_T_plus.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_1_T_minus
screen_1_T_minus = lv.btn(screen_1)
screen_1_T_minus_label = lv.label(screen_1_T_minus)
screen_1_T_minus_label.set_text("-")
screen_1_T_minus_label.set_long_mode(lv.label.LONG.WRAP)
screen_1_T_minus_label.align(lv.ALIGN.CENTER, 0, 0)
screen_1_T_minus.set_style_pad_all(0, lv.STATE.DEFAULT)
screen_1_T_minus.set_pos(26, 158)
screen_1_T_minus.set_size(42, 42)
screen_1_T_minus.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_1_T_minus, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_1_T_minus.set_style_bg_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_T_minus.set_style_bg_color(lv.color_hex(0x009ea9), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_T_minus.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_T_minus.set_style_radius(25, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_T_minus.set_style_shadow_width(3, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_T_minus.set_style_shadow_color(lv.color_hex(0x0d4b3b), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_T_minus.set_style_shadow_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_T_minus.set_style_shadow_spread(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_T_minus.set_style_shadow_ofs_x(1, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_T_minus.set_style_shadow_ofs_y(2, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_T_minus.set_style_text_color(lv.color_hex(0xffffff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_T_minus.set_style_text_font(test_font("Alatsi_Regular", 30), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_T_minus.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_1_H_minus
screen_1_H_minus = lv.btn(screen_1)
screen_1_H_minus_label = lv.label(screen_1_H_minus)
screen_1_H_minus_label.set_text("-")
screen_1_H_minus_label.set_long_mode(lv.label.LONG.WRAP)
screen_1_H_minus_label.align(lv.ALIGN.CENTER, 0, 0)
screen_1_H_minus.set_style_pad_all(0, lv.STATE.DEFAULT)
screen_1_H_minus.set_pos(407, 165)
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
screen_1_H_plus.set_pos(407, 112)
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
screen_1_Humidity.set_pos(345, 147)
screen_1_Humidity.set_size(51, 21)
screen_1_Humidity.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_1_Humidity, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_1_Humidity.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Humidity.set_style_radius(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Humidity.set_style_text_color(lv.color_hex(0x000000), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Humidity.set_style_text_font(test_font("montserratMedium", 16), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Humidity.set_style_text_letter_space(2, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Humidity.set_style_text_line_space(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Humidity.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Humidity.set_style_bg_opa(123, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Humidity.set_style_bg_color(lv.color_hex(0xfcfcfc), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Humidity.set_style_pad_top(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Humidity.set_style_pad_right(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Humidity.set_style_pad_bottom(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Humidity.set_style_pad_left(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Humidity.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_1_Reset_T
screen_1_Reset_T = lv.btn(screen_1)
screen_1_Reset_T_label = lv.label(screen_1_Reset_T)
screen_1_Reset_T_label.set_text("Reset")
screen_1_Reset_T_label.set_long_mode(lv.label.LONG.WRAP)
screen_1_Reset_T_label.align(lv.ALIGN.CENTER, 0, 0)
screen_1_Reset_T.set_style_pad_all(0, lv.STATE.DEFAULT)
screen_1_Reset_T.set_pos(26, 215)
screen_1_Reset_T.set_size(74, 37)
screen_1_Reset_T.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_1_Reset_T, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_1_Reset_T.set_style_bg_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Reset_T.set_style_bg_color(lv.color_hex(0x292929), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Reset_T.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Reset_T.set_style_radius(5, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Reset_T.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Reset_T.set_style_text_color(lv.color_hex(0xffffff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Reset_T.set_style_text_font(test_font("simsun", 18), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Reset_T.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_1_Reset_H
screen_1_Reset_H = lv.btn(screen_1)
screen_1_Reset_H_label = lv.label(screen_1_Reset_H)
screen_1_Reset_H_label.set_text("Reset")
screen_1_Reset_H_label.set_long_mode(lv.label.LONG.WRAP)
screen_1_Reset_H_label.align(lv.ALIGN.CENTER, 0, 0)
screen_1_Reset_H.set_style_pad_all(0, lv.STATE.DEFAULT)
screen_1_Reset_H.set_pos(374, 215)
screen_1_Reset_H.set_size(74, 37)
screen_1_Reset_H.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_1_Reset_H, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_1_Reset_H.set_style_bg_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Reset_H.set_style_bg_color(lv.color_hex(0x292929), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Reset_H.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Reset_H.set_style_radius(5, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Reset_H.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Reset_H.set_style_text_color(lv.color_hex(0xffffff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Reset_H.set_style_text_font(test_font("simsun", 18), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_Reset_H.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_1_label_1
screen_1_label_1 = lv.label(screen_1)
screen_1_label_1.set_text("Temperature")
screen_1_label_1.set_long_mode(lv.label.LONG.WRAP)
screen_1_label_1.set_pos(79, 145)
screen_1_label_1.set_size(112, 23)
screen_1_label_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_1_label_1, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_1_label_1.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_label_1.set_style_radius(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_label_1.set_style_text_color(lv.color_hex(0x000000), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_label_1.set_style_text_font(test_font("Adventpro_regular", 20), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_label_1.set_style_text_letter_space(2, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_label_1.set_style_text_line_space(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_label_1.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_label_1.set_style_bg_opa(134, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_label_1.set_style_bg_color(lv.color_hex(0xffffff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_label_1.set_style_pad_top(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_label_1.set_style_pad_right(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_label_1.set_style_pad_bottom(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_label_1.set_style_pad_left(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_label_1.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_1_label_2
screen_1_label_2 = lv.label(screen_1)
screen_1_label_2.set_text("Humidity")
screen_1_label_2.set_long_mode(lv.label.LONG.WRAP)
screen_1_label_2.set_pos(251, 145)
screen_1_label_2.set_size(93, 23)
screen_1_label_2.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_1_label_2, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_1_label_2.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_label_2.set_style_radius(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_label_2.set_style_text_color(lv.color_hex(0x000000), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_label_2.set_style_text_font(test_font("Adventpro_regular", 20), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_label_2.set_style_text_letter_space(2, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_label_2.set_style_text_line_space(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_label_2.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_label_2.set_style_bg_opa(134, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_label_2.set_style_bg_color(lv.color_hex(0xffffff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_label_2.set_style_pad_top(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_label_2.set_style_pad_right(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_label_2.set_style_pad_bottom(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_label_2.set_style_pad_left(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_1_label_2.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)

screen_1.update_layout()
# Create screen_2
screen_2 = lv.obj()
screen_2.set_size(480, 272)
screen_2.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_2, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_2.set_style_bg_opa(0, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_2_img_1
screen_2_img_1 = lv.img(screen_2)
screen_2_img_1.set_src(load_image(r"C:\Users\justi\Documents\MCUXpressoIDE_11.8.0_1165\practice\scratch\generated\MicroPython\photo_6168027389217584763_y_482_300.png"))
screen_2_img_1.add_flag(lv.obj.FLAG.CLICKABLE)
screen_2_img_1.set_pivot(50,50)
screen_2_img_1.set_angle(0)
screen_2_img_1.set_pos(-1, -21)
screen_2_img_1.set_size(482, 300)
screen_2_img_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_2_img_1, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_2_img_1.set_style_img_opa(144, lv.PART.MAIN|lv.STATE.DEFAULT)

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

# Create screen_2_Temp2
screen_2_Temp2 = lv.label(screen_2)
screen_2_Temp2.set_text("0")
screen_2_Temp2.set_long_mode(lv.label.LONG.WRAP)
screen_2_Temp2.set_pos(183, 148)
screen_2_Temp2.set_size(35, 21)
screen_2_Temp2.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_2_Temp2, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_2_Temp2.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_Temp2.set_style_radius(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_Temp2.set_style_text_color(lv.color_hex(0x000000), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_Temp2.set_style_text_font(test_font("montserratMedium", 16), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_Temp2.set_style_text_letter_space(2, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_Temp2.set_style_text_line_space(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_Temp2.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_Temp2.set_style_bg_opa(126, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_Temp2.set_style_bg_color(lv.color_hex(0xe7f9cb), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_Temp2.set_style_pad_top(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_Temp2.set_style_pad_right(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_Temp2.set_style_pad_bottom(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_Temp2.set_style_pad_left(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_Temp2.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_2_T_plus
screen_2_T_plus = lv.btn(screen_2)
screen_2_T_plus_label = lv.label(screen_2_T_plus)
screen_2_T_plus_label.set_text("+")
screen_2_T_plus_label.set_long_mode(lv.label.LONG.WRAP)
screen_2_T_plus_label.align(lv.ALIGN.CENTER, 0, 0)
screen_2_T_plus.set_style_pad_all(0, lv.STATE.DEFAULT)
screen_2_T_plus.set_pos(15, 108)
screen_2_T_plus.set_size(42, 41)
screen_2_T_plus.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_2_T_plus, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_2_T_plus.set_style_bg_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_T_plus.set_style_bg_color(lv.color_hex(0x009ea9), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_T_plus.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_T_plus.set_style_radius(25, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_T_plus.set_style_shadow_width(3, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_T_plus.set_style_shadow_color(lv.color_hex(0x0d4b3b), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_T_plus.set_style_shadow_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_T_plus.set_style_shadow_spread(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_T_plus.set_style_shadow_ofs_x(1, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_T_plus.set_style_shadow_ofs_y(2, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_T_plus.set_style_text_color(lv.color_hex(0xffffff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_T_plus.set_style_text_font(test_font("Alatsi_Regular", 30), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_T_plus.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_2_T_minus
screen_2_T_minus = lv.btn(screen_2)
screen_2_T_minus_label = lv.label(screen_2_T_minus)
screen_2_T_minus_label.set_text("-")
screen_2_T_minus_label.set_long_mode(lv.label.LONG.WRAP)
screen_2_T_minus_label.align(lv.ALIGN.CENTER, 0, 0)
screen_2_T_minus.set_style_pad_all(0, lv.STATE.DEFAULT)
screen_2_T_minus.set_pos(15, 160)
screen_2_T_minus.set_size(42, 42)
screen_2_T_minus.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_2_T_minus, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_2_T_minus.set_style_bg_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_T_minus.set_style_bg_color(lv.color_hex(0x009ea9), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_T_minus.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_T_minus.set_style_radius(25, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_T_minus.set_style_shadow_width(3, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_T_minus.set_style_shadow_color(lv.color_hex(0x0d4b3b), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_T_minus.set_style_shadow_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_T_minus.set_style_shadow_spread(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_T_minus.set_style_shadow_ofs_x(1, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_T_minus.set_style_shadow_ofs_y(2, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_T_minus.set_style_text_color(lv.color_hex(0xffffff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_T_minus.set_style_text_font(test_font("Alatsi_Regular", 32), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_T_minus.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_2_H_minus
screen_2_H_minus = lv.btn(screen_2)
screen_2_H_minus_label = lv.label(screen_2_H_minus)
screen_2_H_minus_label.set_text("-")
screen_2_H_minus_label.set_long_mode(lv.label.LONG.WRAP)
screen_2_H_minus_label.align(lv.ALIGN.CENTER, 0, 0)
screen_2_H_minus.set_style_pad_all(0, lv.STATE.DEFAULT)
screen_2_H_minus.set_pos(408, 160)
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
screen_2_H_plus.set_pos(408, 114)
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

# Create screen_2_Humidity2
screen_2_Humidity2 = lv.label(screen_2)
screen_2_Humidity2.set_text("0 %")
screen_2_Humidity2.set_long_mode(lv.label.LONG.WRAP)
screen_2_Humidity2.set_pos(345, 146)
screen_2_Humidity2.set_size(43, 23)
screen_2_Humidity2.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_2_Humidity2, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_2_Humidity2.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_Humidity2.set_style_radius(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_Humidity2.set_style_text_color(lv.color_hex(0x000000), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_Humidity2.set_style_text_font(test_font("montserratMedium", 16), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_Humidity2.set_style_text_letter_space(2, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_Humidity2.set_style_text_line_space(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_Humidity2.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_Humidity2.set_style_bg_opa(118, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_Humidity2.set_style_bg_color(lv.color_hex(0xf4fbd4), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_Humidity2.set_style_pad_top(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_Humidity2.set_style_pad_right(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_Humidity2.set_style_pad_bottom(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_Humidity2.set_style_pad_left(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_Humidity2.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_2_btn_2
screen_2_btn_2 = lv.btn(screen_2)
screen_2_btn_2_label = lv.label(screen_2_btn_2)
screen_2_btn_2_label.set_text("Reset")
screen_2_btn_2_label.set_long_mode(lv.label.LONG.WRAP)
screen_2_btn_2_label.align(lv.ALIGN.CENTER, 0, 0)
screen_2_btn_2.set_style_pad_all(0, lv.STATE.DEFAULT)
screen_2_btn_2.set_pos(375, 217)
screen_2_btn_2.set_size(74, 37)
screen_2_btn_2.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_2_btn_2, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_2_btn_2.set_style_bg_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_btn_2.set_style_bg_color(lv.color_hex(0x292929), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_btn_2.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_btn_2.set_style_radius(5, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_btn_2.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_btn_2.set_style_text_color(lv.color_hex(0xffffff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_btn_2.set_style_text_font(test_font("simsun", 18), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_btn_2.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_2_btn_1
screen_2_btn_1 = lv.btn(screen_2)
screen_2_btn_1_label = lv.label(screen_2_btn_1)
screen_2_btn_1_label.set_text("Reset")
screen_2_btn_1_label.set_long_mode(lv.label.LONG.WRAP)
screen_2_btn_1_label.align(lv.ALIGN.CENTER, 0, 0)
screen_2_btn_1.set_style_pad_all(0, lv.STATE.DEFAULT)
screen_2_btn_1.set_pos(16, 217)
screen_2_btn_1.set_size(74, 37)
screen_2_btn_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_2_btn_1, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_2_btn_1.set_style_bg_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_btn_1.set_style_bg_color(lv.color_hex(0x292929), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_btn_1.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_btn_1.set_style_radius(5, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_btn_1.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_btn_1.set_style_text_color(lv.color_hex(0xffffff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_btn_1.set_style_text_font(test_font("simsun", 18), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_btn_1.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_2_label_1
screen_2_label_1 = lv.label(screen_2)
screen_2_label_1.set_text("Temperature")
screen_2_label_1.set_long_mode(lv.label.LONG.WRAP)
screen_2_label_1.set_pos(71, 146)
screen_2_label_1.set_size(112, 23)
screen_2_label_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_2_label_1, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_2_label_1.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_label_1.set_style_radius(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_label_1.set_style_text_color(lv.color_hex(0x000000), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_label_1.set_style_text_font(test_font("Adventpro_regular", 20), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_label_1.set_style_text_letter_space(2, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_label_1.set_style_text_line_space(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_label_1.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_label_1.set_style_bg_opa(134, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_label_1.set_style_bg_color(lv.color_hex(0xffffff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_label_1.set_style_pad_top(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_label_1.set_style_pad_right(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_label_1.set_style_pad_bottom(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_label_1.set_style_pad_left(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_label_1.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_2_label_2
screen_2_label_2 = lv.label(screen_2)
screen_2_label_2.set_text("Humidity")
screen_2_label_2.set_long_mode(lv.label.LONG.WRAP)
screen_2_label_2.set_pos(252, 146)
screen_2_label_2.set_size(93, 23)
screen_2_label_2.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_2_label_2, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_2_label_2.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_label_2.set_style_radius(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_label_2.set_style_text_color(lv.color_hex(0x000000), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_label_2.set_style_text_font(test_font("Adventpro_regular", 20), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_label_2.set_style_text_letter_space(2, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_label_2.set_style_text_line_space(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_label_2.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_label_2.set_style_bg_opa(134, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_label_2.set_style_bg_color(lv.color_hex(0xffffff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_label_2.set_style_pad_top(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_label_2.set_style_pad_right(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_label_2.set_style_pad_bottom(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_label_2.set_style_pad_left(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_2_label_2.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)

screen_2.update_layout()
# Create screen_3
screen_3 = lv.obj()
screen_3.set_size(480, 272)
screen_3.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_3, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_3.set_style_bg_opa(0, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_3_img_1
screen_3_img_1 = lv.img(screen_3)
screen_3_img_1.set_src(load_image(r"C:\Users\justi\Documents\MCUXpressoIDE_11.8.0_1165\practice\scratch\generated\MicroPython\R_483_285.png"))
screen_3_img_1.add_flag(lv.obj.FLAG.CLICKABLE)
screen_3_img_1.set_pivot(50,50)
screen_3_img_1.set_angle(0)
screen_3_img_1.set_pos(-1, 0)
screen_3_img_1.set_size(483, 285)
screen_3_img_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_3_img_1, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_3_img_1.set_style_img_opa(160, lv.PART.MAIN|lv.STATE.DEFAULT)

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

# Create screen_3_Temp3
screen_3_Temp3 = lv.label(screen_3)
screen_3_Temp3.set_text("0")
screen_3_Temp3.set_long_mode(lv.label.LONG.WRAP)
screen_3_Temp3.set_pos(191, 146)
screen_3_Temp3.set_size(37, 21)
screen_3_Temp3.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_3_Temp3, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_3_Temp3.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_Temp3.set_style_radius(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_Temp3.set_style_text_color(lv.color_hex(0x000000), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_Temp3.set_style_text_font(test_font("montserratMedium", 16), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_Temp3.set_style_text_letter_space(2, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_Temp3.set_style_text_line_space(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_Temp3.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_Temp3.set_style_bg_opa(129, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_Temp3.set_style_bg_color(lv.color_hex(0xf9eaf7), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_Temp3.set_style_pad_top(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_Temp3.set_style_pad_right(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_Temp3.set_style_pad_bottom(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_Temp3.set_style_pad_left(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_Temp3.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_3_T_plus
screen_3_T_plus = lv.btn(screen_3)
screen_3_T_plus_label = lv.label(screen_3_T_plus)
screen_3_T_plus_label.set_text("+")
screen_3_T_plus_label.set_long_mode(lv.label.LONG.WRAP)
screen_3_T_plus_label.align(lv.ALIGN.CENTER, 0, 0)
screen_3_T_plus.set_style_pad_all(0, lv.STATE.DEFAULT)
screen_3_T_plus.set_pos(27, 115)
screen_3_T_plus.set_size(43, 42)
screen_3_T_plus.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_3_T_plus, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_3_T_plus.set_style_bg_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_T_plus.set_style_bg_color(lv.color_hex(0x009ea9), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_T_plus.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_T_plus.set_style_radius(25, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_T_plus.set_style_shadow_width(3, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_T_plus.set_style_shadow_color(lv.color_hex(0x0d4b3b), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_T_plus.set_style_shadow_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_T_plus.set_style_shadow_spread(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_T_plus.set_style_shadow_ofs_x(1, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_T_plus.set_style_shadow_ofs_y(2, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_T_plus.set_style_text_color(lv.color_hex(0xffffff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_T_plus.set_style_text_font(test_font("Acme_Regular", 30), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_T_plus.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_3_T_minus
screen_3_T_minus = lv.btn(screen_3)
screen_3_T_minus_label = lv.label(screen_3_T_minus)
screen_3_T_minus_label.set_text("-")
screen_3_T_minus_label.set_long_mode(lv.label.LONG.WRAP)
screen_3_T_minus_label.align(lv.ALIGN.CENTER, 0, 0)
screen_3_T_minus.set_style_pad_all(0, lv.STATE.DEFAULT)
screen_3_T_minus.set_pos(27, 167)
screen_3_T_minus.set_size(42, 42)
screen_3_T_minus.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_3_T_minus, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_3_T_minus.set_style_bg_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_T_minus.set_style_bg_color(lv.color_hex(0x009ea9), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_T_minus.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_T_minus.set_style_radius(25, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_T_minus.set_style_shadow_width(3, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_T_minus.set_style_shadow_color(lv.color_hex(0x0d4b3b), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_T_minus.set_style_shadow_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_T_minus.set_style_shadow_spread(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_T_minus.set_style_shadow_ofs_x(1, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_T_minus.set_style_shadow_ofs_y(2, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_T_minus.set_style_text_color(lv.color_hex(0xffffff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_T_minus.set_style_text_font(test_font("Alatsi_Regular", 30), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_T_minus.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_3_H_minus
screen_3_H_minus = lv.btn(screen_3)
screen_3_H_minus_label = lv.label(screen_3_H_minus)
screen_3_H_minus_label.set_text("-")
screen_3_H_minus_label.set_long_mode(lv.label.LONG.WRAP)
screen_3_H_minus_label.align(lv.ALIGN.CENTER, 0, 0)
screen_3_H_minus.set_style_pad_all(0, lv.STATE.DEFAULT)
screen_3_H_minus.set_pos(408, 167)
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
screen_3_H_plus.set_pos(408, 119)
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

# Create screen_3_Humidity3
screen_3_Humidity3 = lv.label(screen_3)
screen_3_Humidity3.set_text("0 %")
screen_3_Humidity3.set_long_mode(lv.label.LONG.WRAP)
screen_3_Humidity3.set_pos(343, 145)
screen_3_Humidity3.set_size(46, 23)
screen_3_Humidity3.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_3_Humidity3, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_3_Humidity3.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_Humidity3.set_style_radius(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_Humidity3.set_style_text_color(lv.color_hex(0x000000), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_Humidity3.set_style_text_font(test_font("montserratMedium", 16), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_Humidity3.set_style_text_letter_space(2, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_Humidity3.set_style_text_line_space(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_Humidity3.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_Humidity3.set_style_bg_opa(97, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_Humidity3.set_style_bg_color(lv.color_hex(0xfdf7fc), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_Humidity3.set_style_pad_top(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_Humidity3.set_style_pad_right(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_Humidity3.set_style_pad_bottom(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_Humidity3.set_style_pad_left(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_Humidity3.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_3_btn_2
screen_3_btn_2 = lv.btn(screen_3)
screen_3_btn_2_label = lv.label(screen_3_btn_2)
screen_3_btn_2_label.set_text("Reset")
screen_3_btn_2_label.set_long_mode(lv.label.LONG.WRAP)
screen_3_btn_2_label.align(lv.ALIGN.CENTER, 0, 0)
screen_3_btn_2.set_style_pad_all(0, lv.STATE.DEFAULT)
screen_3_btn_2.set_pos(382, 217)
screen_3_btn_2.set_size(74, 37)
screen_3_btn_2.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_3_btn_2, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_3_btn_2.set_style_bg_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_btn_2.set_style_bg_color(lv.color_hex(0x292929), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_btn_2.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_btn_2.set_style_radius(5, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_btn_2.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_btn_2.set_style_text_color(lv.color_hex(0xffffff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_btn_2.set_style_text_font(test_font("simsun", 18), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_btn_2.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_3_btn_1
screen_3_btn_1 = lv.btn(screen_3)
screen_3_btn_1_label = lv.label(screen_3_btn_1)
screen_3_btn_1_label.set_text("Reset")
screen_3_btn_1_label.set_long_mode(lv.label.LONG.WRAP)
screen_3_btn_1_label.align(lv.ALIGN.CENTER, 0, 0)
screen_3_btn_1.set_style_pad_all(0, lv.STATE.DEFAULT)
screen_3_btn_1.set_pos(27, 217)
screen_3_btn_1.set_size(74, 37)
screen_3_btn_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_3_btn_1, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_3_btn_1.set_style_bg_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_btn_1.set_style_bg_color(lv.color_hex(0x292929), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_btn_1.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_btn_1.set_style_radius(5, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_btn_1.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_btn_1.set_style_text_color(lv.color_hex(0xffffff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_btn_1.set_style_text_font(test_font("simsun", 18), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_btn_1.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_3_label_1
screen_3_label_1 = lv.label(screen_3)
screen_3_label_1.set_text("Temperature")
screen_3_label_1.set_long_mode(lv.label.LONG.WRAP)
screen_3_label_1.set_pos(79, 145)
screen_3_label_1.set_size(112, 23)
screen_3_label_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_3_label_1, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_3_label_1.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_label_1.set_style_radius(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_label_1.set_style_text_color(lv.color_hex(0x000000), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_label_1.set_style_text_font(test_font("Adventpro_regular", 20), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_label_1.set_style_text_letter_space(2, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_label_1.set_style_text_line_space(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_label_1.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_label_1.set_style_bg_opa(134, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_label_1.set_style_bg_color(lv.color_hex(0xffffff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_label_1.set_style_pad_top(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_label_1.set_style_pad_right(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_label_1.set_style_pad_bottom(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_label_1.set_style_pad_left(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_label_1.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_3_label_2
screen_3_label_2 = lv.label(screen_3)
screen_3_label_2.set_text("Humidity")
screen_3_label_2.set_long_mode(lv.label.LONG.WRAP)
screen_3_label_2.set_pos(252, 145)
screen_3_label_2.set_size(93, 23)
screen_3_label_2.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen_3_label_2, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_3_label_2.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_label_2.set_style_radius(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_label_2.set_style_text_color(lv.color_hex(0x000000), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_label_2.set_style_text_font(test_font("Adventpro_regular", 20), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_label_2.set_style_text_letter_space(2, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_label_2.set_style_text_line_space(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_label_2.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_label_2.set_style_bg_opa(134, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_label_2.set_style_bg_color(lv.color_hex(0xffffff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_label_2.set_style_pad_top(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_label_2.set_style_pad_right(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_label_2.set_style_pad_bottom(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_label_2.set_style_pad_left(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_3_label_2.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)

screen_3.update_layout()
# Create add
add = lv.obj()
add.set_size(480, 272)
add.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for add, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
add.set_style_bg_opa(0, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create add_label_1
add_label_1 = lv.label(add)
add_label_1.set_text("Add Profile")
add_label_1.set_long_mode(lv.label.LONG.WRAP)
add_label_1.set_pos(69, 26)
add_label_1.set_size(342, 35)
add_label_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for add_label_1, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
add_label_1.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
add_label_1.set_style_radius(0, lv.PART.MAIN|lv.STATE.DEFAULT)
add_label_1.set_style_text_color(lv.color_hex(0x000000), lv.PART.MAIN|lv.STATE.DEFAULT)
add_label_1.set_style_text_font(test_font("Acme_Regular", 30), lv.PART.MAIN|lv.STATE.DEFAULT)
add_label_1.set_style_text_letter_space(2, lv.PART.MAIN|lv.STATE.DEFAULT)
add_label_1.set_style_text_line_space(0, lv.PART.MAIN|lv.STATE.DEFAULT)
add_label_1.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)
add_label_1.set_style_bg_opa(0, lv.PART.MAIN|lv.STATE.DEFAULT)
add_label_1.set_style_pad_top(0, lv.PART.MAIN|lv.STATE.DEFAULT)
add_label_1.set_style_pad_right(0, lv.PART.MAIN|lv.STATE.DEFAULT)
add_label_1.set_style_pad_bottom(0, lv.PART.MAIN|lv.STATE.DEFAULT)
add_label_1.set_style_pad_left(0, lv.PART.MAIN|lv.STATE.DEFAULT)
add_label_1.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create add_btn_1
add_btn_1 = lv.btn(add)
add_btn_1_label = lv.label(add_btn_1)
add_btn_1_label.set_text("Menu")
add_btn_1_label.set_long_mode(lv.label.LONG.WRAP)
add_btn_1_label.align(lv.ALIGN.CENTER, 0, 0)
add_btn_1.set_style_pad_all(0, lv.STATE.DEFAULT)
add_btn_1.set_pos(366, 223)
add_btn_1.set_size(100, 36)
add_btn_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for add_btn_1, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
add_btn_1.set_style_bg_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)
add_btn_1.set_style_bg_color(lv.color_hex(0x08c3e4), lv.PART.MAIN|lv.STATE.DEFAULT)
add_btn_1.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
add_btn_1.set_style_radius(5, lv.PART.MAIN|lv.STATE.DEFAULT)
add_btn_1.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
add_btn_1.set_style_text_color(lv.color_hex(0xffffff), lv.PART.MAIN|lv.STATE.DEFAULT)
add_btn_1.set_style_text_font(test_font("montserratMedium", 16), lv.PART.MAIN|lv.STATE.DEFAULT)
add_btn_1.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)

add.update_layout()

def screen_img_1_event_handler(e):
    code = e.get_code()
    if (code == lv.EVENT.CLICKED):
        lv.scr_load_anim(screen1, lv.SCR_LOAD_ANIM.NONE, 200, 200, False)

screen_img_1.add_event_cb(lambda e: screen_img_1_event_handler(e), lv.EVENT.ALL, None)

def screen_img_2_event_handler(e):
    code = e.get_code()
    if (code == lv.EVENT.CLICKED):
        lv.scr_load_anim(screen2, lv.SCR_LOAD_ANIM.NONE, 200, 200, False)

screen_img_2.add_event_cb(lambda e: screen_img_2_event_handler(e), lv.EVENT.ALL, None)

def screen_img_3_event_handler(e):
    code = e.get_code()
    if (code == lv.EVENT.CLICKED):
        lv.scr_load_anim(screen3, lv.SCR_LOAD_ANIM.NONE, 200, 200, False)

screen_img_3.add_event_cb(lambda e: screen_img_3_event_handler(e), lv.EVENT.ALL, None)

def screen_btn_1_event_handler(e):
    code = e.get_code()
    if (code == lv.EVENT.CLICKED):
        lv.scr_load_anim(add, lv.SCR_LOAD_ANIM.NONE, 200, 200, False)

screen_btn_1.add_event_cb(lambda e: screen_btn_1_event_handler(e), lv.EVENT.ALL, None)

def screen1_Menu_event_handler(e):
    code = e.get_code()
    if (code == lv.EVENT.CLICKED):
        lv.scr_load_anim(screen, lv.SCR_LOAD_ANIM.NONE, 200, 200, False)

screen1_Menu.add_event_cb(lambda e: screen1_Menu_event_handler(e), lv.EVENT.ALL, None)

def screen1_btn_1_event_handler(e):
    code = e.get_code()
    if (code == lv.EVENT.CLICKED):
        lv.scr_load_anim(screen_1, lv.SCR_LOAD_ANIM.NONE, 200, 200, False)

screen1_btn_1.add_event_cb(lambda e: screen1_btn_1_event_handler(e), lv.EVENT.ALL, None)

def screen2_Menu_event_handler(e):
    code = e.get_code()
    if (code == lv.EVENT.CLICKED):
        lv.scr_load_anim(screen, lv.SCR_LOAD_ANIM.NONE, 200, 200, False)

screen2_Menu.add_event_cb(lambda e: screen2_Menu_event_handler(e), lv.EVENT.ALL, None)

def screen2_btn_1_event_handler(e):
    code = e.get_code()
    if (code == lv.EVENT.CLICKED):
        lv.scr_load_anim(screen_2, lv.SCR_LOAD_ANIM.NONE, 200, 200, False)

screen2_btn_1.add_event_cb(lambda e: screen2_btn_1_event_handler(e), lv.EVENT.ALL, None)

def screen3_Menu_event_handler(e):
    code = e.get_code()
    if (code == lv.EVENT.CLICKED):
        lv.scr_load_anim(screen, lv.SCR_LOAD_ANIM.NONE, 200, 200, False)

screen3_Menu.add_event_cb(lambda e: screen3_Menu_event_handler(e), lv.EVENT.ALL, None)

def screen3_btn_1_event_handler(e):
    code = e.get_code()
    if (code == lv.EVENT.CLICKED):
        lv.scr_load_anim(screen_3, lv.SCR_LOAD_ANIM.NONE, 200, 200, False)

screen3_btn_1.add_event_cb(lambda e: screen3_btn_1_event_handler(e), lv.EVENT.ALL, None)

def screen_1_back_event_handler(e):
    code = e.get_code()
    if (code == lv.EVENT.CLICKED):
        lv.scr_load_anim(screen1, lv.SCR_LOAD_ANIM.NONE, 200, 200, False)

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

def screen_1_Reset_T_event_handler(e):
    code = e.get_code()

screen_1_Reset_T.add_event_cb(lambda e: screen_1_Reset_T_event_handler(e), lv.EVENT.ALL, None)

def screen_1_Reset_H_event_handler(e):
    code = e.get_code()

screen_1_Reset_H.add_event_cb(lambda e: screen_1_Reset_H_event_handler(e), lv.EVENT.ALL, None)

def screen_2_back_event_handler(e):
    code = e.get_code()
    if (code == lv.EVENT.CLICKED):
        lv.scr_load_anim(screen2, lv.SCR_LOAD_ANIM.NONE, 200, 200, False)

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

def screen_2_btn_2_event_handler(e):
    code = e.get_code()

screen_2_btn_2.add_event_cb(lambda e: screen_2_btn_2_event_handler(e), lv.EVENT.ALL, None)

def screen_2_btn_1_event_handler(e):
    code = e.get_code()

screen_2_btn_1.add_event_cb(lambda e: screen_2_btn_1_event_handler(e), lv.EVENT.ALL, None)

def screen_3_back_event_handler(e):
    code = e.get_code()
    if (code == lv.EVENT.CLICKED):
        lv.scr_load_anim(screen3, lv.SCR_LOAD_ANIM.NONE, 200, 200, False)

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

def screen_3_btn_2_event_handler(e):
    code = e.get_code()

screen_3_btn_2.add_event_cb(lambda e: screen_3_btn_2_event_handler(e), lv.EVENT.ALL, None)

def screen_3_btn_1_event_handler(e):
    code = e.get_code()

screen_3_btn_1.add_event_cb(lambda e: screen_3_btn_1_event_handler(e), lv.EVENT.ALL, None)

def add_btn_1_event_handler(e):
    code = e.get_code()
    if (code == lv.EVENT.CLICKED):
        lv.scr_load_anim(screen, lv.SCR_LOAD_ANIM.NONE, 200, 200, False)

add_btn_1.add_event_cb(lambda e: add_btn_1_event_handler(e), lv.EVENT.ALL, None)

# content from custom.py

# Load the default screen
lv.scr_load(screen)

while SDL.check():
    time.sleep_ms(5)

