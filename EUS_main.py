#!/usr/bin/python3
# coding: utf-8
import draw_train as draw
import event_weekday as weekday
from time import sleep
import time_count as tc
import train as tr
import sys


stationid =[0 for i in range(42)]
#江ノ島留置線の配列(将来的には4になる)
enoid = [0 for i in range(3)]
#検車区の配列（こっちは15編成ぶん用意しておくが、サイズは動的に確保するものとする）
depotid = [0 for i in range(15)]

#車両の配列　車両番号と、車両番号の文字列と、車両が車庫に入っているかどうか、1で入庫中
#carid = [[305, 1001, 1002, 1101, 1201, 1501, 1502, 2001, 2002, 2003, 10, 21, 22, 501, 502],[" 305", "1001", "1002", "1101", "1201", "1501", "1502", "2001", "2002", "2003", " 10 ", " 21 ", " 22 ", " 501", " 502"],[1 for i in range(15)]]


hour = 5
min = 0

'''
# シミュレーション開始時間の設定(車両を出庫するコマンドを実行していないため、9時とかに設定しても電車が動かない不良アリ。)
if int(sys.argv[1])>4 and int(sys.argv[1])<24:
    hour = int(sys.argv[1])
    if int(sys.argv[2])>=0 and int(sys.argv[2])<60:
        min = int(sys.argv[2])
'''


if __name__ == '__main__':
    tr.un1 = tr.UnyouClass(2003, 0, 20, 1)
    tr.un2 = tr.UnyouClass(1001,0, 5, 2)
    tr.un3 = tr.UnyouClass(2002,1502, 5, 3)
    tr.un4 = tr.UnyouClass( 22 ,0, 26, 4)
    tr.un5 = tr.UnyouClass( 21 ,1501, 10, 5)
    tr.un6 = tr.UnyouClass(1002, 305, 21, 6)
    tr.un7 = tr.UnyouClass(1501, 502, 21, 6)   
    tr.testrun = tr.UnyouClass(0, 0, 21, 6)  

'''
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
'''

sleep_time = 0.2 
    
while hour < 6:
    #始発列車の発車処理関数をここで6運用分入れる　移設
    #入庫列車を線路上から運用ごとに除去する
    #両数の変更は車両交換で行うこと。江ノ島留置に重連突っ込もうとしたときにどういう処理を出すかはいまのところ考えてない
    #平日の運用で車両交換を行う

    weekday.run_train(hour, min, stationid)

    #指定時間前は描画処理をパスする
    if int(sys.argv[1]) <= hour:
        draw.draw_train(hour,min,stationid)
        sleep(sleep_time)

    tr.startingsignal_sta_morning(hour,min,stationid)
    hour, min = tc.time_counter(hour, min)


while hour <= 21:
    #始発列車の発車処理関数をここで6運用分入れる
    #入庫列車を線路上から各運用で除去する
    weekday.run_train(hour, min, stationid)


    if int(sys.argv[1]) <= hour:
        draw.draw_train(hour,min,stationid)
        sleep(sleep_time)
    tr.startingsignal_sta_pattern(hour,min,stationid)
    hour, min = tc.time_counter(hour, min)

while hour <= 24:
    #始発列車の発車処理関数をここで6運用分入れる
    #入庫列車を線路上から各運用で除去する
    weekday.run_train(hour, min, stationid)

    if int(sys.argv[1]) <= hour:
        draw.draw_train(hour,min,stationid)
        sleep(sleep_time)
        
    tr.startingsignal_sta_night(hour,min,stationid)
    hour, min = tc.time_counter(hour, min)

