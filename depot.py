#!/usr/bin/python3
# -*- coding: UTF-8 -*-

'''
#車庫と留置線のデータを持ち、運用を外れている車両を管理する。

江ノ島駅ホーム　1番線AB　2番線AB　計4個所
稲村ヶ崎駅　1番線AB　計2か所(終夜運転でどうするかは別途考える)

江ノ島留置線　1,(2), 3, 4AB 計5か所
極楽寺留置線　1AB, 2AB, 3, 4,(5), 6　計8箇所
検査車両　1~2本


#管理方法
江ノ島留置線は規則性がはっきりしているので、これに関しては線路ごとに管理するものとする。

'''
import cars as car
from eus_timer import time_count as tc
# import json

'''
depot_now = {
    "E01": "0","E02": "0","E03": "0","E04A": "0","E04B": "0",
    "G01A": "0","G01B": "0","G02A": "0","G02B": "0","G03": "0","G04": "0","G05": "0","G06A": "0","G06B": "0",
    "5A": "0","5B": "0","26A": "0","26B": "0","21A": "0","21B": "0"}
'''
class DepotClass:
    def __init__(self, car):
        #各留置線の状態を確認する
        self.capacity = 1
        self.car = 0
        if int(car) != 0:
            self.capacity = 0
            self.car = car
    
    def __del__(self):
        #留置線の設定を削除
        pass

    def push_car(self, car):
        self.car = int(car)

    def desc_car(self):
        return self.car
    
    def pull_car(self):
        resp = self.car
        self.car = 0
        return resp

class templeClass:
    def __init__(self, carslist):
        self.carslist = carslist

    def push_car(self,car):
        self.carslist.append(int(car))
        #車両を入庫車リストの一番後ろに格納する

    def push_cars(self,carslist):
        for cars in carslist:
            self.carslist.append(int(cars))
        #重連の入庫車両を入庫車リストの一番後ろに格納する

    def desc_cars(self):
        return self.carslist

        
    def pull_car(self):
        #入庫車リストの一番手前を出庫させる
        resp = 0
        if len(self.carslist)!=0:
            resp = self.carslist[0]
            del self.carslist[0]
        return int(resp)

'''
if __name__ == "__main__":
    E01 = DepotClass(0)
    E02 = DepotClass(0)
    E03 = DepotClass(1001)
    E04A = DepotClass(0)
    E04B = DepotClass(0)
    T05A = DepotClass(2002)
    T05B = DepotClass(1502)
    T26A = DepotClass(22)
    T26B = DepotClass(0)
    T21A = DepotClass(0)
    T21B = DepotClass(0)
    Gtemp = DepotClass(0)
    goku = templeClass([])
    #土日夜の一時的な入庫で使うためのバケツ
'''