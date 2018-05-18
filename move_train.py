#!/usr/bin/python3
# -*- coding: UTF-8 -*-

#Unyoは配列名で、Un1からun6まである。
# Un6 は　藤沢・鎌倉の1次元2要素の配列

def set_train(hour, sec, un_number, station):
    if hour == 5 and sec == 43:
        station = un_number
        un1 = entry_cars(hour,sec,fuji,kama)

        #stationにunyoをセットする。5時43分に運用1が出庫するので、この場合は極楽寺駅に[1]が格納される
    elif hour == 5 and sec == 24:
        station = un_number
        un2 = entry_cars(hour,sec,fuji,kama)
    
        #un1 に　train をセット


def move_train(hour,sec,un1, un2, un3, un4, un5, un6):
    #駅とホームにナンバーを割り当てて配列化する
    #藤沢基準
    station = []
    fujisawa = "---------"
    kugenuma = "---------"
    enoshima = "---------"
    minegahara = "---------"
    inamuragasaki = "---------"
    gokurakuji = "---------"
    hase = "---------"
    kamakura = "---------"
    #駅番号　藤沢から０～１６

    if sec % 12 == 0:
        #藤沢待機
        


    elif sec % 12 == 6:
        #峰が原待機

    elif sec % 12 == 7:
        #上り極楽寺

    elif sec % 12 == 2:
        #下り極楽寺

    down = 
    up = 
