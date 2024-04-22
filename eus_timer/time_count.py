#!/usr/bin/python3
# -*- coding: UTF-8 -*-

def time_counter(hour, min):
    min += 1
    if min == 60:
        hour += 1
        min = 0
    return hour,min

if __name__ == '__main__':
    hour = ""
    min = ""

def timesig(timesighour, timesigmin, hour, min):
    if timesighour == hour and timesigmin == min:
        return True
    else:
        return False

#藤沢7時を基準にした14分間隔からの余りを吸収        
def calc_reminder_14_pattern(hour, min):
    reminder_hour = (hour + 7) % 7
    reminder_min = ((reminder_hour * 60) + min) % 14
    return reminder_min