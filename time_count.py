#!/usr/bin/python3
# -*- coding: UTF-8 -*-

def time_counter(hour, sec):
    sec += 1
    if sec == 60:
        hour += 1
        sec = 0
    return hour,sec

if __name__ == '__main__':
    hour = ""
    sec = ""

def alarm(alarmhour, alarmsec, hour, sec):
    if alarmhour == hour and alarmsec == sec:
        return True
    else:
        return False 