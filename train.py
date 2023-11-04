#!/usr/bin/python3
# -*- coding: UTF-8 -*-

#列車と運用についてのデータを定義する
#列車の運行を開始する

#車両の文字と番号を配列で管理できるようにしたが、結局文字列変換して保存してしまっているので、IDで管理して描画のとこだけ文字列に変換する処理がしたい
import cars as car
from eus_timer import time_count as tc


class UnyouClass:
    '''
    #  各運用が持つデータを定義する。
    train 車両の配列。最長2つ。
    中に入れるのは、carクラスのcaridである。
    つまり、呼ばれた車番305から車番IDの305を探して打ち込む。
    藤、鎌、初期スタート地点、運用番号を設定すれば完了。
    車両はintで管理され、0の場合は車両がいないことを指す。
    '''
    def __init__(self, car1, car2, stationnum, icon):
        self.train =[]
        for i in range(len(car.carid[0])):
            if car.carid[0][i] == car1:
                self.train.append(car.carid[1][i])
        if car2 != 0:
            #４両編成の場合、車両を追加
            for i in range(len(car.carid[0])):
                if car.carid[0][i] == car2:
                    self.train.append(car.carid[1][i])
        self.location = stationnum
        self.icon = "[" + str(icon) + "]"

        if len(self.train) == 2:
            self.carname = str(self.icon) + self.train[0] + '+' + self.train[1]
        else:
            self.carname = str(self.icon) + self.train[0] + '     '
    
    def input_cars(self, car1, car2):
        for i in range(len(car.carid[0])):
            if car.carid[0][i] == car1:
                self.train.append(car.carid[1][i])
        if car2 != 0:
            #４両編成の場合、車両を追加
            for i in range(len(car.carid[0])):
                if car.carid[0][i] == car2:
                    self.train.append(car.carid[1][i])

        if len(self.train) == 2:
            self.carname = str(self.icon) + self.train[0] + '+' + self.train[1]
        else:
            self.carname = str(self.icon) + self.train[0] + '     '

        
    def __del__(self):
        #運用の配列を削除してから運用を削除
        pass

    def desc_train(self):
        trainname = self.carname
        return trainname
  
    dict_enoshima = {"no1": "32", "no3": "33", "no4": "34"}

    def set_train(self, stationid):
        # print(str(len(self.train)))
        if len(self.train) == 2:
            stationid[self.location] = self
            self.carname = str(self.icon) + self.train[0] + '+' + self.train[1]
        else:
            stationid[self.location] = self
            self.carname = str(self.icon) + self.train[0] + '     '
        return stationid

    def out_train(self, stationid, idnum, depot1, depot2='default'):
        #idnum は終着駅のID
        out_services = []
        out_services.append(self.train[0])
        depot1.push_car(self.train[0])
        if len(self.train) == 2:
            out_services.append(self.train[1])
            depot2.push_car(self.train[1])

        stationid[idnum]=0
        del self

        '''
        #入庫措置
        #idnumは留置線のIDだが、Depotクラスで管理するので、これは渡されたdepotクラスを参照する方式に今後改める
        #江ノ島留置
        if idnum == 26 and len(self.train) == 1:
            if stationid[33] == 0:
                stationid[idnum], stationid[33] = 0, stationid[idnum]
                self.location = idnum
            elif stationid[34] == 0:
                stationid[idnum], stationid[34] = 0, stationid[idnum]
                self.location = idnum
            elif stationid[32] == 0:
                stationid[idnum], stationid[34] = 0, stationid[idnum]
                self.location = idnum
 
        #極楽寺留置
        #37は入庫線。一時的に値を格納して置き、基本的には単行にばらして保管する
        #極楽寺2とか3は重連でもおいておけるけどここをどう定義するか悩みどころ
        #38、39は重連対応にする？
        if idnum == 11 or idnum == 20:
            stationid[idnum], stationid[37] = 0, stationid[idnum]            
            for i in range(38, 42):
                for j in range(len(self.train)):
                
                    if stationid[i] == 0:
                        stationid[i]= stationid[37]
                        break
            self.location = 37
            #stationid[37] = 0
        
        stationid[idnum]=0
        del self
        return stationid
        '''

    def add_cars(self, location, car_new, stationid):
        #単行に出庫車を連結する場合
        for i in range(len(car.carid[0])):
            if car.carid[0][i] == car_new:
                carword = car.carid[1][i]
        if location < 16:
            self.train.append(carword)
        else:
            #train[0] = train[1]
            #train[0] = car_new
            self.train.append(carword)
            self.train[0], self.train[1] = self.train[1], self.train[0]

        self.carname = str(self.icon) + self.train[0] + '+' + self.train[1]
        return stationid


    def parge_cars(self, location, stationid):
        #重連を開放して入庫する場合
        if location < 16:
            out_service = self.train[0]
            self.train[0] = self.train[1]
            del self.train[1]
        else:
            out_service = self.train[1]
            del self.train[1]


        self.carname = str(self.icon) + self.train[0] + '     '
        return out_service


    def change_back_cars(self, location, car_new, stationid):
        #重連の前に2両を連結し、後ろ2両を開放する場合
        if self.location < 16:
            #train[0] = train[1]
            #train[1] = car_new
            out_service = self.train[0]
            self.train[0], self.train[1] = self.train[1], car_new
        else:
            #train[1] = train[0]
            #train[0] = car_new
            out_service = self.train[1]
            self.train[0], self.train[1] = car_new, self.train[0]

        self.carname = str(self.icon) + self.train[0] + '+' + self.train[1]
        return out_service

    def change_all_cars(self, location, car_new, stationid):
        #重連の前に2両を待機させ、後ろ4両をそのまま入庫させる場合
        for i in range(len(car.carid[0])):
            if car.carid[0][i] == int(car_new):
                carword = car.carid[1][i]
        out_services = []
        out_services.append(self.train[0])
        out_services.append(self.train[1])
        if self.location < 16:
            self.train[0] = carword
            del self.train[1]
        else:
            self.train[0] = carword
            del self.train[1]

        self.carname = str(self.icon) + self.train[0] + '     '
        return out_services

