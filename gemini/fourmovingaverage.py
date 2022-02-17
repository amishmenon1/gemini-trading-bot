import gemini.emailreader as emailreader
import time

entry_ema = 0
fast_ema = 0
medium_ema = 0
slow_ema = 0


def set_ema_values(subject_string):
    global entry_ema
    global fast_ema
    global medium_ema
    global slow_ema

    time.sleep(2)
    ema_values = subject_string.split(',')
    entry_ema = rounded_float(ema_values[0])
    fast_ema = rounded_float(ema_values[1])
    medium_ema = rounded_float(ema_values[2])
    slow_ema = rounded_float(ema_values[3])


def rounded_float(num_string):
    return float('%.2f' % float(num_string))


def get_entry_ema():
    global entry_ema
    return entry_ema


def get_fast_ema():
    global fast_ema
    return fast_ema


def get_medium_ema():
    global medium_ema
    return medium_ema


def get_slow_ema():
    global slow_ema
    return slow_ema


def is_moving_up():
    global entry_ema
    global fast_ema
    global medium_ema
    global slow_ema

    gap_threshold = 4
    upward_movement = entry_ema > fast_ema > medium_ema > slow_ema
    small_gaps = (entry_ema - fast_ema <= gap_threshold) and (fast_ema - medium_ema <= gap_threshold) and (medium_ema - slow_ema <= gap_threshold)

    return upward_movement and small_gaps


def set_ema_values_from_email():
    email_subject = emailreader.get_latest_email_subject()
    ema_values_string = email_subject.split(':')[3]
    set_ema_values(ema_values_string)
