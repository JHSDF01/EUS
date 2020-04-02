#!/usr/bin/python3
# coding: utf-8

from time import sleep
import time_count as tc
import train as tr


def run_train(hour,min, stationid):
    if tc.timesig(5,43, hour, min) == True:
        tr.un1.set_train(stationid) 
    if tc.timesig(5,22, hour, min) == True:
        tr.un2.set_train(stationid)
    if tc.timesig(5,9, hour, min) == True:
        tr.un3.set_train(stationid)
    if tc.timesig(5,10, hour, min) == True:
        tr.un4.set_train(stationid)
    if tc.timesig(6,11, hour, min) == True:
        tr.un5.set_train(stationid)
    if tc.timesig(5,22, hour, min) == True:
        tr.un6.set_train(stationid)

    if tc.timesig(6, 00, hour, min) == True:
        tr.un1.add_cars(26, 501, stationid)

    if tc.timesig(5, 55, hour, min) == True:
        tr.un2.add_cars(20,  10, stationid)

    if tc.timesig(6, 18, hour, min) == True:
        tr.un4.add_cars(20,1101, stationid)


    if tc.timesig(9, 7, hour, min) == True:
        tr.un6.change_all_cars(20, 1201, stationid)

    if tc.timesig(9, 24, hour, min) == True:
        tr.un6.add_cars(26, 502, stationid)

    if tc.timesig(17, 50, hour, min) == True:
        tr.un3.parge_cars(11, stationid)

    if tc.timesig(18,  2, hour, min) == True:
        tr.un5.parge_cars(11, stationid)

    if tc.timesig(19,  0, hour, min) == True:
        tr.un6.parge_cars(26, stationid)

    if tc.timesig(18, 38, hour, min) == True:
        tr.un1.parge_cars(11, stationid)

    if tc.timesig(22,16, hour, min) == True:
        tr.un1.out_train(stationid,11)
    if tc.timesig(24,0, hour, min) == True:
        tr.un2.out_train(stationid,21)
    if tc.timesig(22,0, hour, min) == True:
        tr.un3.out_train(stationid,26)
    if tc.timesig(23,50, hour, min) == True:
        tr.un4.out_train(stationid,5)
    if tc.timesig(22,25, hour, min) == True:
        tr.un5.out_train(stationid,26)
    if tc.timesig(23,49, hour, min) == True:
        tr.un6.out_train(stationid,26)


    """
    if tc.timesig(9, 25, hour, min) == True:
        tr.un4.parge_cars(11, stationid)


    if tc.timesig(7,23, hour, min) == True:
        tr.un1.out_train(stationid,26)
    if tc.timesig(7,25, hour, min) == True:
        tr.un2.out_train(stationid,11)
    """