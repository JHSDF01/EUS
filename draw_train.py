#!/usr/bin/python3
# coding: utf-8

from time import sleep
import time_count as tc
import train as tr
import depot as dp
def locate_train(stationid, unyo_num, idno):
    stationid[int(idno)] = unyo_num
    return stationid

"""
un1= tr.UnyouClass(" 501","", 0, 1)
#un1= tr.UnyouClass(" 501","2003", 0, 1)
un2= tr.UnyouClass(" 10 ","1001", 5, 2)
un3= tr.UnyouClass("2002","1502", 10, 3)
un4= tr.UnyouClass("1101"," 22 ", 16, 4)
un5= tr.UnyouClass(" 21 ","1501", 21, 5)
un6= tr.UnyouClass("1002"," 305", 26, 6)

"""
if __name__ == '__main__':
    un1= tr.UnyouClass(1002, 22 , 0, 1)
    un2= tr.UnyouClass(2001,1201, 5, 2)
    un3= tr.UnyouClass( 10 ,1501, 10, 3)
    un4= tr.UnyouClass(2003,1502, 16, 4)
    un5= tr.UnyouClass( 501, 305, 21, 5)
    un6= tr.UnyouClass(1101,1001, 26, 6)
    stationid =[0 for i in range(42)]

"""
tr.UnyouClass.set_train(un1,stationid)
tr.UnyouClass.set_train(un2,stationid)
tr.UnyouClass.set_train(un3,stationid)
tr.UnyouClass.set_train(un4,stationid)
tr.UnyouClass.set_train(un5,stationid)
tr.UnyouClass.set_train(un6,stationid)
"""

"""
locate_train(stationid, un1, 0)
locate_train(stationid, un2, 5)
locate_train(stationid, un3, 10)
locate_train(stationid, un4, 16)
locate_train(stationid, un5, 21)
locate_train(stationid, un6, 26)
"""


def draw_train(hour,min,stationid,day_mode_name,event):
    
    down=""
    downicon=""
    up=""
    upicon=""
    """
    for i in len(tr.unyouid):
        stationid[tr.unyouid[i].location] 
         = tr.unyouid[i].carname
    """

    #location = "藤沢　石上　柳小路　鵠沼　湘南海岸公園　江ノ島　腰越　鎌倉高校前　峰が原　七里ヶ浜　稲村ケ崎　極楽寺　長谷　由比ガ浜　和田塚　鎌倉"
    location = "藤沢　石上　柳小　鵠沼　湘南　江ノ　腰越　鎌高　峰原　七里　稲村　極楽　長谷　由比　和田　鎌倉"
    track_s =  "----              ----        ----              ----        ----        ----              ----"
    track_m =  "    ------------------------------------------------------------------------------------------"
    track_e4 =  "                                --"
    track_e3 =  "                                 --"
    track_e1 =  "                                  --"
    track_goku = "                                                         ____検車区 "
    track_gtmp = "                                                                "
    #下り列車の描画位置設定
    for i in range(0,16):
        #print(i)
        #駅に車両がいるかどうか
        if stationid[i] != 0:
            #列車番号記入
            down += str(stationid[i].carname) 
            down += ""
        else:
            if i != 0 and stationid[i-1] != 0:
                down += ""
            else:            
                down += "      " 

        if stationid[i] != 0:
            downicon += "  |>  "
        else:
            downicon += "      "
    
    #上り列車の描画位置設定
    for i in reversed(range(16,32)):
        #print(i)
        if stationid[i] != 0:
            up += str(stationid[i].carname)
            up += ""
            
        else:
            if i < 31 and stationid[i+1] != 0:
                up += ""
            else:
                up += "      " 

        if stationid[i] != 0:
            upicon += " <|   "
        else:
            upicon += "      "
    '''
    #江の島極楽寺留置は未実装
    '''

    if event.dp.E01.desc_car() != 0:
        track_e1 += str(event.dp.E01.desc_car()).rjust(4)
    else:
        track_e1 += "----"
    
    if event.dp.E03.desc_car() != 0:
        track_e3 += str(event.dp.E03.desc_car()).rjust(4)
    else:
        track_e3 += "----"
    
    if event.dp.E04A.desc_car() != 0:
        track_e4 += str(event.dp.E04A.desc_car()).rjust(4)
    else:
        track_e4 += "----"
    track_e4 += "-"          
    if event.dp.E04B.desc_car() != 0:
        track_e4 += str(event.dp.E04B.desc_car()).rjust(4)
    else:
        track_e4 += "----"
    if event.dp.Gtemp.desc_car() != 0:
        track_gtmp += str(event.dp.Gtemp.desc_car()).rjust(4)
    else:
        track_gtmp += "----"

    for car in event.dp.goku.carslist:
        track_goku += " - " + str(car)


    
    print("Enoden Unyo Simurator v2.3.1")
    print( "\n\n" + "(" + day_mode_name + ")" + str(hour) + "時" + str(min) + "分現在の" + "江ノ電車両位置" + "\n\n")
    print(track_goku)
    print(track_gtmp)
    print( "\n")
    print(down)
    print(downicon)
    print(track_s)
    print(location)
    print(track_m)
    print(upicon)
    print(up)
    print( "\n")
    print(track_e4)
    print(track_e3)
    print(track_e1)
    
    print("\nこれはテスト画面です。実際の運用ではありません。\n")


    return stationid



if __name__ == '__main__':
    hour = 9
    min = 24
    import event_weekday as event
    draw_train(hour,min,stationid,"平日",event)
    sleep(1)
    #tr.startingsignal_sta_pattern(hour,min,stationid)
    hour, min = tc.time_counter(hour, min)
