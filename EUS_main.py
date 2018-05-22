#!/usr/bin/python3
# coding: utf-8
import draw_train as draw
from time import sleep
import time_count as tc
import train as tr

stationid =[0 for i in range(32)]


hour = 5
min = 0

def run_train(hour,min):
    if tc.timesig(5,43, hour, min) == True:
        un1 = tr.UnyouClass(" 501","", 20, 1)
        tr.UnyouClass.set_train(un1,stationid) 
    if tc.timesig(5,22, hour, min) == True:
        un2= tr.UnyouClass(" 10 ","1001", 5, 2)
        tr.UnyouClass.set_train(un2,stationid)
    if tc.timesig(5,9, hour, min) == True:
        un3= tr.UnyouClass("2002","1502", 5, 3)
        tr.UnyouClass.set_train(un3,stationid)
    if tc.timesig(5,10, hour, min) == True:
        un4= tr.UnyouClass("1101"," 22 ", 26, 4)
        tr.UnyouClass.set_train(un4,stationid)
    if tc.timesig(6,11, hour, min) == True:
        un5= tr.UnyouClass(" 21 ","1501", 10, 5)
        tr.UnyouClass.set_train(un5,stationid)
    if tc.timesig(5,22, hour, min) == True:
        un6= tr.UnyouClass("1002"," 305", 21, 6)
        tr.UnyouClass.set_train(un6,stationid)

    
while hour < 6:
    #始発列車の発車処理関数をここで6運用分入れる
    #入庫列車を線路上から各運用で除去する
    run_train(hour, min)

    draw.draw_train(hour,min,stationid)
    sleep(0.2)
    tr.startingsignal_sta_morning(hour,min,stationid)
    hour, min = tc.time_counter(hour, min)

while hour <= 21:
    #始発列車の発車処理関数をここで6運用分入れる
    #入庫列車を線路上から各運用で除去する
    run_train(hour, min)

    draw.draw_train(hour,min,stationid)
    sleep(0.2)
    tr.startingsignal_sta_pattern(hour,min,stationid)
    hour, min = tc.time_counter(hour, min)


