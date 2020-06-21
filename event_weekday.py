#!/usr/bin/python3
# coding: utf-8

from time import sleep
import time_count as tc
import train as tr
import depot as dp
import save_depot as save
import json

def set_depot():
    depot_morning = save.EUS_load()
    dp.E01 = dp.depotClass(depot_morning["E01"])
    dp.E02 = dp.depotClass(depot_morning["E02"])
    dp.E03 = dp.depotClass(depot_morning["E03"])
    dp.E04A = dp.depotClass(depot_morning["E04A"])
    dp.E04B = dp.depotClass(depot_morning["E04B"])
    dp.T05A = dp.depotClass(depot_morning["5A"])
    dp.T05B = dp.depotClass(depot_morning["5B"])
    dp.T26A = dp.depotClass(depot_morning["26A"])
    dp.T26B = dp.depotClass(depot_morning["26B"])
    dp.T21A = dp.depotClass(depot_morning["21A"])
    dp.T21B = dp.depotClass(depot_morning["21B"])
    dp.Gtemp = dp.depotClass(depot_morning["Gtemp"])
    dp.goku = dp.templeClass(depot_morning["goku"])

def set_unyou():
    tr.un1 = tr.UnyouClass(dp.goku.desc_cars()[0], 0, 20, 1)
    tr.un2 = tr.UnyouClass(dp.E03.desc_car(),0, 5, 2)
    tr.un3 = tr.UnyouClass(dp.T05A.desc_car(),dp.T05B.desc_car(), 5, 3)
    tr.un4 = tr.UnyouClass(dp.T26A.desc_car(),dp.T26B.desc_car(), 26, 4)
    tr.un5 = tr.UnyouClass(dp.goku.desc_cars()[2],dp.goku.desc_cars()[3], 10, 5)
    tr.un6 = tr.UnyouClass(dp.T21A.desc_car(),dp.T21B.desc_car(), 21, 6)
    tr.un7 = tr.UnyouClass(0, 0, 21, 6)   
    tr.testrun = tr.UnyouClass(0, 0, 20, 6) 

def delete_depot():
    depot_midnight = {"E01": dp.E01.desc_car(),"E02": dp.E02.desc_car(),"E03": dp.E03.desc_car(),"E04A": dp.E04A.desc_car(),"E04B": dp.E04B.desc_car(),
        "Gtemp": 0, "goku": dp.goku.desc_cars(),
        "5A": dp.T05A.desc_car(),"5B": dp.T05B.desc_car(),"26A": dp.T26A.desc_car(),"26B": dp.T26B.desc_car(),"21A": dp.T21A.desc_car(),"21B": dp.T21B.desc_car()}
    save.EUS_save(depot_midnight)


def input_unyou():
    with open('save/unyo.json') as uload:
        noon = json.load(uload)
        tr.un1 = tr.UnyouClass(noon["[1]"][0], noon["[1]"][1], 0, 1)
        tr.un2 = tr.UnyouClass(noon["[2]"][0], noon["[2]"][1], 5, 2)
        tr.un3 = tr.UnyouClass(noon["[3]"][0], noon["[3]"][1], 10, 3)
        tr.un4 = tr.UnyouClass(noon["[4]"][0], noon["[4]"][1], 16, 4)
        tr.un5 = tr.UnyouClass(noon["[5]"][0], noon["[5]"][1], 21, 5)
        tr.un6 = tr.UnyouClass(noon["[6]"][0], noon["[6]"][1], 26, 6)

    
def output_unyo():
    output =str(str(tr.un1.desc_train())
        +"\n"+ str(tr.un2.desc_train())
        +"\n"+ str(tr.un3.desc_train())
        +"\n"+ str(tr.un4.desc_train())
        +"\n"+ str(tr.un5.desc_train())
        +"\n"+ str(tr.un6.desc_train())
        +"\ngoku"+ str(dp.goku.desc_cars())
    )
    with open('save/unyo.txt', 'w') as fsave:
       fsave.write(output)



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
        delete_depot()
 
    if tc.timesig(24,0, hour, min) == True:
        delete_depot()


    if tc.timesig(11, 00, hour, min) == True:
        # 1から6までの運用を出力する。
        output_unyo()
        pass

    """
    if tc.timesig(9, 25, hour, min) == True:
        tr.un4.parge_cars(11, stationid)


    if tc.timesig(7,23, hour, min) == True:
        tr.un1.out_train(stationid,26)
    if tc.timesig(7,25, hour, min) == True:
        tr.un2.out_train(stationid,11)
    """