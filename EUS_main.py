#!/usr/bin/python3
# coding: utf-8
import draw_train as draw
from time import sleep
import time_count as tc
import train as tr

stationid =[0 for i in range(32)]


hour = 5
sec = 0

    
while hour < 6:
    #始発列車の発車処理関数をここで6運用分入れる
    #入庫列車を線路上から各運用で除去する
    if tc.alarm(5,43, hour, sec) == True:
        un1 = tr.UnyouClass(" 501","", 0, 1)
        tr.UnyouClass.set_train(un1,stationid)
        
    if tc.alarm(5,22, hour, sec) == True:
        un2= tr.UnyouClass(" 10 ","1001", 5, 2)
        tr.UnyouClass.set_train(un2,stationid)
    if tc.alarm(5,9, hour, sec) == True:
        un3= tr.UnyouClass("2002","1502", 5, 3)
        tr.UnyouClass.set_train(un3,stationid)
    if tc.alarm(5,10, hour, sec) == True:
        un4= tr.UnyouClass("1101"," 22 ", 26, 4)
        tr.UnyouClass.set_train(un4,stationid)
    if tc.alarm(6,11, hour, sec) == True:
        un5= tr.UnyouClass(" 21 ","1501", 11, 5)
        tr.UnyouClass.set_train(un5,stationid)
    if tc.alarm(5,22, hour, sec) == True:
        un6= tr.UnyouClass("1002"," 305", 21, 6)
        tr.UnyouClass.set_train(un6,stationid)


    draw.draw_train(hour,sec,stationid)
    sleep(0.3)
    tr.startingsignal_sta_morning(hour,sec,stationid)
    hour, sec = tc.time_counter(hour, sec)

while hour <= 21:
    #始発列車の発車処理関数をここで6運用分入れる
    #入庫列車を線路上から各運用で除去する

    draw.draw_train(hour,sec,stationid)
    sleep(1)
    tr.startingsignal_sta_pattern(hour,sec,stationid)
    hour, sec = tc.time_counter(hour, sec)


