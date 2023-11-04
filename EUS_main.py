#!/usr/bin/python3
# coding: utf-8
'''
凡例 引数
sys argv
0 プログラム名（コレ）
1 開始時　デフォルトは5
2 終了時　デフォルトは24
3 描画間隔　デフォルトは0.2
4 平日・休日　0か1で制御 デフォルトは0

'''

import draw_train as draw
from time import sleep
from eus_timer import time_count as tc
import train as tr
import save_depot as save
import sys

sim_start_time = 5
sim_end_time = 24
sleep_time = 0.2
sim_day_mode = 0

print(len(sys.argv))
if len(sys.argv) >= 3:
    sim_start_time = int(sys.argv[1])
    sim_end_time = int(sys.argv[2])
    if len(sys.argv) >= 4:
        sleep_time = float(sys.argv[3])
        if len(sys.argv) == 5:
            sim_day_mode = int(sys.argv[4])

if sim_day_mode == 1:
    from eus_event import event_holiday as event
    day_mode_name = '土休日'
elif sim_day_mode == 2:
    from eus_event import event_holiday_calc as event
    day_mode_name = '平日(日中から計算)'
elif sim_day_mode == 3:
    from eus_event import event_holiday_calc as event
    day_mode_name = '土休日(日中から計算)'
else:
    # 0のとき
    from eus_event import event_weekday as event
    day_mode_name = '平日'


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
load
EUS_saveからファイルを読み取り、
saveデータを引っ張ってきて、配列に格納する。
格納した配列を定義で渡せるようにする。
'''
event.set_depot()

if __name__ == '__main__':

    # 車庫入りを定義し、運番を定義する。
    
    event.set_unyou()
    '''
    tr.un1 = tr.UnyouClass(2003, 0, 20, 1)
    tr.un2 = tr.UnyouClass(1001,0, 5, 2)
    tr.un3 = tr.UnyouClass(2002,1502, 5, 3)
    tr.un4 = tr.UnyouClass( 22 ,0, 26, 4)
    tr.un5 = tr.UnyouClass( 21 ,1501, 10, 5)
    tr.un6 = tr.UnyouClass(1002, 305, 21, 6)
    tr.un7 = tr.UnyouClass(0, 0, 21, 6)   
    tr.testrun = tr.UnyouClass(0, 0, 21, 6) 
    '''



    
while hour < 6:
    #始発列車の発車処理関数をここで6運用分入れる　移設
    #入庫列車を線路上から運用ごとに除去する
    #両数の変更は車両交換で行うこと。江ノ島留置に重連突っ込もうとしたときにどういう処理を出すかはいまのところ考えてない
    #平日の運用で車両交換を行う

    event.run_train(hour, min, stationid)

    #指定時間前は描画処理をパスする
    if int(sim_start_time) <= hour:
        draw.draw_train(hour,min,stationid,day_mode_name,event)
        sleep(sleep_time)
    if int(sim_end_time) <= hour:
        break
    tr.startingsignal_sta_morning(hour,min,stationid)
    hour, min = tc.time_counter(hour, min)


while hour <= 21:
    #始発列車の発車処理関数をここで6運用分入れる
    #入庫列車を線路上から各運用で除去する
    event.run_train(hour, min, stationid)


    if int(sim_start_time) <= hour:
        draw.draw_train(hour,min,stationid,day_mode_name,event)
        sleep(sleep_time)
    if int(sim_end_time) <= hour:
        break
    tr.startingsignal_sta_pattern(hour,min,stationid)
    hour, min = tc.time_counter(hour, min)

while hour <= 24:
    #始発列車の発車処理関数をここで6運用分入れる
    #入庫列車を線路上から各運用で除去する
    event.run_train(hour, min, stationid)

    if int(sim_start_time) <= hour:
        draw.draw_train(hour,min,stationid,day_mode_name,event)
        sleep(sleep_time)
    if int(sim_end_time) <= hour:
        break    
    tr.startingsignal_sta_night(hour,min,stationid)
    hour, min = tc.time_counter(hour, min)


'''
save

EUS_saveに車庫の在線状況を保存する。
24時までシミュレーションを行った場合に、
24時時点での在線状況をセーブして終了する。
'''
