#!/usr/bin/python3
# -*- coding: UTF-8 -*-

def locate_train(unyo_num, idno):
    stationid[idno] = unyo_num
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
    stationid =[0 for i in range(31)]

    locate_train(un1, '0')
    locate_train(un2, '6')
    locate_train(un3, '11')
    locate_train(un4, '15')
    locate_train(un5, '19')
    locate_train(un6, 's')

    doun=""
    downicon=""
    up=""
    upicon=""

    location = "藤沢　石上　柳小路　鵠沼　湘南海岸公園　江ノ島　腰越　鎌倉高校前　峰が原　七里ヶ浜　稲村ケ崎　極楽寺　長谷　由比ガ浜　和田塚"
    for i in range(0,15):
        down += stationid[i] + " "
        if stationid[i] != 0:
            downicon += "    |     "
        else:
            downicon += "          "
    
    for i in range(16,31):
        up += stationid[i]
        up += " "
        if stationid[i] != 0:
            upicon += "    |     "
        else:
            upicon += "          "

    print(down)
    print(downicon)
    print(location)
    print(upicon)
    print(up)
    return

draw_train('9','45')