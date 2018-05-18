#!/usr/bin/python3
# -*- coding: UTF-8 -*-

def locate_train(stationid, unyo_num, idno):
    stationid[int(idno)] = unyo_num
    return stationid



def draw_train(hour,sec):
    
    stationid = []
    """
    fujisawa
    kugenuma
    enoshima
    minegahara
    inamuragasaki
    gokurakuji
    hase
    kamakura
    """
    un1 = "1002+ 22 "
    un2 = "2001+1201"
    un3 = " 10 +1501"
    un4 = "2003+1502"
    un5 = " 501+ 305"
    un6 = "1101+1001"
    stationid =[0 for i in range(32)]

    locate_train(stationid, un1, 0)
    locate_train(stationid, un2, 5)
    locate_train(stationid, un3, 10)
    locate_train(stationid, un4, 16)
    locate_train(stationid, un5, 21)
    locate_train(stationid, un6, 26)

    down=""
    downicon=""
    up=""
    upicon=""

    #location = "藤沢　石上　柳小路　鵠沼　湘南海岸公園　江ノ島　腰越　鎌倉高校前　峰が原　七里ヶ浜　稲村ケ崎　極楽寺　長谷　由比ガ浜　和田塚　鎌倉"
    location = "藤沢　石上　柳小　鵠沼　湘南　江ノ　腰越　鎌高　峰原　七里　稲村　極楽　長谷　由比　和田　鎌倉"
    track_s =  "                  ----        ----              ----        ----        ----              ----"
    track_m =  "----------------------------------------------------------------------------------------------"
    for i in range(0,16):
        print(i)
        if stationid[i] != 0:
            down += str(stationid[i]) 
            down += " "
        else:
            if i != 0 and stationid[i-1] != 0:
                down += "  "
            else:            
                down += "      " 

        if stationid[i] != 0:
            downicon += "  |>  "
        else:
            downicon += "      "
    
    for i in reversed(range(16,32)):
        print(i)
        if stationid[i] != 0:
            up += str(stationid[i])
            up += " "
            
        else:
            if i < 31 and stationid[i+1] != 0:
                up += "  "
            else:
                up += "      " 

        if stationid[i] != 0:
            upicon += " <|   "
        else:
            upicon += "      "

    print("Enoden Unyo Simurator test")
    print( "\n\n" + hour + "時" + sec + "分現在の" + "江ノ電車両位置" + "\n\n")
    print(down)
    print(downicon)
    print(track_s)
    print(location)
    print(track_m)
    print(upicon)
    print(up)
    print("\n遅延など反映できない場合があります。\n")
    print("\n")
    print("\nこれはテスト画面です。実際の運用ではありません。\n")


    return

draw_train('9','48')