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