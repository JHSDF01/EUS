#!/usr/bin/python3
# coding: utf-8

from time import sleep
import time_count as tc
import train as tr
import depot as dp

def set_depot():
    dp.E01 = dp.depotClass(501)
    dp.E02 = dp.depotClass(0)
    dp.E03 = dp.depotClass(1001)
    dp.E04A = dp.depotClass(0)
    dp.E04B = dp.depotClass(502)
    dp.T05A = dp.depotClass(2002)
    dp.T05B = dp.depotClass(1502)
    dp.T26A = dp.depotClass(22)
    dp.T26B = dp.depotClass(0)
    dp.T21A = dp.depotClass(1002)
    dp.T21B = dp.depotClass(305)
    dp.Gtemp = dp.depotClass(0)
    dp.goku = dp.templeClass([2003,10,21,1501,1101,1201,2001])

def set_unyou():
    tr.un1 = tr.UnyouClass(dp.goku.desc_cars()[0], 0, 20, 1)
    tr.un2 = tr.UnyouClass(dp.E03.desc_car(),0, 5, 2)
    tr.un3 = tr.UnyouClass(dp.T05A.desc_car(),dp.T05B.desc_car(), 5, 3)
    tr.un4 = tr.UnyouClass(dp.T26A.desc_car(),dp.T26B.desc_car(), 26, 4)
    tr.un5 = tr.UnyouClass(dp.goku.desc_cars()[2],dp.goku.desc_cars()[3], 10, 5)
    tr.un6 = tr.UnyouClass(dp.T21A.desc_car(),dp.T21B.desc_car(), 21, 6)
    tr.un7 = tr.UnyouClass(0, 0, 21, 6)   
    tr.testrun = tr.UnyouClass(0, 0, 20, 6) 

def run_train(hour,min, stationid):
    
    if tc.timesig(5,43, hour, min) == True:
        del tr.un1
        tr.un1 = tr.UnyouClass(dp.goku.pull_car(), 0, 20, 1)
        tr.un1.set_train(stationid) 
    if tc.timesig(5,22, hour, min) == True:
        del tr.un2
        tr.un2 = tr.UnyouClass(dp.E03.pull_car(),0, 5, 2)
        tr.un2.set_train(stationid)
    if tc.timesig(5,9, hour, min) == True:
        del tr.un3
        tr.un3 = tr.UnyouClass(dp.T05A.pull_car(),dp.T05B.pull_car(), 5, 3)
        tr.un3.set_train(stationid)
    if tc.timesig(5,10, hour, min) == True:
        del tr.un4
        tr.un4 = tr.UnyouClass(dp.T26A.pull_car(),dp.T26B.pull_car(), 26, 4)
        tr.un4.set_train(stationid)
    if tc.timesig(6,11, hour, min) == True:
        del tr.un5
        tr.un5 = tr.UnyouClass(dp.goku.pull_car(),dp.goku.pull_car(), 10, 5)
        tr.un5.set_train(stationid)
    if tc.timesig(5,22, hour, min) == True:
        del tr.un6
        tr.un6 = tr.UnyouClass(dp.T21A.pull_car(),dp.T21B.pull_car(), 21, 6)
        tr.un6.set_train(stationid)

    if tc.timesig(6, 00, hour, min) == True:
        tr.un1.add_cars(26, dp.E01.pull_car(), stationid)

    if tc.timesig(5, 55, hour, min) == True:
        tr.un2.add_cars(20,dp.goku.pull_car(), stationid)

    if tc.timesig(6, 18, hour, min) == True:
        tr.un4.add_cars(20,dp.goku.pull_car(), stationid)


    if tc.timesig(9, 7, hour, min) == True:
        dp.goku.push_cars(tr.un6.change_all_cars(20, dp.goku.pull_car(), stationid))

    if tc.timesig(9, 24, hour, min) == True:
        tr.un6.add_cars(26, dp.E04B.pull_car(), stationid)

    if tc.timesig(17, 50, hour, min) == True:
        dp.goku.push_car(tr.un3.parge_cars(11, stationid))

    if tc.timesig(18,  14, hour, min) == True:
        dp.goku.push_car(tr.un5.parge_cars(11, stationid))

    if tc.timesig(19,  0, hour, min) == True:
        dp.E04B.push_car(tr.un6.parge_cars(26, stationid))

    if tc.timesig(18, 38, hour, min) == True:
        dp.goku.push_car(tr.un1.parge_cars(11, stationid))
    #32 1  33 2  34 3 35 4A 36 4B  
    if tc.timesig(22,16, hour, min) == True:
        tr.un1.out_train(stationid,11,dp.goku,dp.goku)
    if tc.timesig(24,0, hour, min) == True:
        tr.un2.out_train(stationid,21,dp.T21A,dp.T21B)
    if tc.timesig(22,0, hour, min) == True:
        tr.un3.out_train(stationid,26,dp.E03,'')
    if tc.timesig(23,50, hour, min) == True:
        tr.un4.out_train(stationid,5,dp.T05A,dp.T05B)
    if tc.timesig(22,25, hour, min) == True:
        tr.un5.out_train(stationid,26,dp.E01,'')
    if tc.timesig(23,49, hour, min) == True:
        tr.un6.out_train(stationid,26,dp.T26A,dp.T26B)


    """
    if tc.timesig(9, 25, hour, min) == True:
        tr.un4.parge_cars(11, stationid)


    if tc.timesig(7,23, hour, min) == True:
        tr.un1.out_train(stationid,26)
    if tc.timesig(7,25, hour, min) == True:
        tr.un2.out_train(stationid,11)
    """