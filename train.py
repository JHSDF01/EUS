#!/usr/bin/python3
# -*- coding: UTF-8 -*-

#列車と運用についてのデータを定義する
#列車の運行を開始する

class UnyouClass:
    def __init__(self, cars, stationid):
        self.cars = cars
        self.location = stationid

    def move_train(self, new_location):
        self.location = new_location
        return self.location
    

un1= UnyouClass("1002+ 22 ", 0)
un2= UnyouClass("2001+1201", 5)
un3= UnyouClass(" 10 +1501", 10)
un4= UnyouClass("2003+1502", 15)
un5= UnyouClass(" 501+ 305", 21)
un6= UnyouClass("1101+1001", 26)


un1.location += 5
print(un1.location)
un2.location += 5
print(un2.location)
unlist = [un1,un2,un3,un4,un5,un6]

#パターンダイヤ時の時刻に合わせて動かす
def startingsignal_sta(sec, stationid):
    time_down = [[0,10],[1,6],[11],,[2,6,12],[3,8],[13],[9],[4,14],,,[11]]
    time_up = [[16,26],[27],[17,21],[18],[22],[19,28],[24,29],[20],[25,30],,,]
    for in len(time_down)
        if sec == time_down:
            for j in len(time_down[i])
                stationid[i],stationid[i+1] = stationid[i+1],stationid[i]
