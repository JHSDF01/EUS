#!/usr/bin/python3
# coding: utf-8
import draw_train as draw
from time import sleep
import time_count as tc
import train as tr

stationid =[0 for i in range(42)]
hour = 5
min = 0

if __name__ == '__main__':
    tr.un1 = tr.UnyouClass(" 501","2003", 20, 1)
    tr.un2 = tr.UnyouClass(" 10 ","1001", 5, 2)
    tr.un3 = tr.UnyouClass("2002","1502", 5, 3)
    tr.un4 = tr.UnyouClass("1101"," 22 ", 26, 4)
    tr.un5 = tr.UnyouClass(" 21 ","1501", 10, 5)
    tr.un6 = tr.UnyouClass("1002"," 305", 21, 6)


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

    if tc.timesig(9, 7, hour, min) == True:
        tr.un6.change_all_cars(20, " 10 ", stationid)

    if tc.timesig(9, 24, hour, min) == True:
        tr.un6.add_cars(26, " 502", stationid)
    """
    if tc.timesig(9, 25, hour, min) == True:
        tr.un4.parge_cars(11, stationid)


    if tc.timesig(7,23, hour, min) == True:
        tr.un1.out_train(stationid,26)
    if tc.timesig(7,25, hour, min) == True:
        tr.un2.out_train(stationid,11)
    """
    
    
while hour < 6:
    #始発列車の発車処理関数をここで6運用分入れる　移設
    #入庫列車を線路上から運用ごとに除去する
    #両数の変更は車両交換で行うこと。江ノ島留置に重連突っ込もうとしたときにどういう処理を出すかはいまのところ考えてない
    run_train(hour, min, stationid)

    draw.draw_train(hour,min,stationid)
    sleep(0.2)
    tr.startingsignal_sta_morning(hour,min,stationid)
    hour, min = tc.time_counter(hour, min)

while hour <= 21:
    #始発列車の発車処理関数をここで6運用分入れる
    #入庫列車を線路上から各運用で除去する
    run_train(hour, min, stationid)

    draw.draw_train(hour,min,stationid)
    sleep(0.2)
    tr.startingsignal_sta_pattern(hour,min,stationid)
    hour, min = tc.time_counter(hour, min)


