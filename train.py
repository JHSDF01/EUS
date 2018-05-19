#!/usr/bin/python3
# -*- coding: UTF-8 -*-

#列車と運用についてのデータを定義する
#列車の運行を開始する

class UnyouClass:
    def __init__(self, cars, stationnum,icon):
        self.cars = cars
        self.location = stationnum
        self.icon = "[" + str(icon) + "]"

    def move_train(self, new_location):
        self.location = new_location
        return self.location

    def set_train(self, stationid):
        stationid[self.location] = str(self.icon) + self.cars
        return stationid

    
"""
un1= UnyouClass("1002+ 22 ", 0, 1)
un2= UnyouClass("2001+1201", 5, 2)
un3= UnyouClass(" 10 +1501", 10, 3)
un4= UnyouClass("2003+1502", 15, 4)
un5= UnyouClass(" 501+ 305", 21, 5)
un6= UnyouClass("1101+1001", 26, 6)

un1.location += 5
print(un1.location)
un2.location += 5
print(un2.location)



unlist = [un1,un2,un3,un4,un5,un6]
"""


#パターンダイヤ時の時刻に合わせて動かす
def startingsignal_sta_pattern(sec, stationid):
    time_down = [[0,5,10],[1,6],[11],[7],[2,12],[3,8],[13],[9],[4,14],[],[],[11]]
    time_up = [[16,26],[27],[17,21],[18],[22],[19,28,23],[24,29],[20],[25,30],[],[],[]]
    for i in range(11):
        #12分間隔のうち、例えば1分の時だったら配列の１にある０と10の駅で座標入れかえ
        if sec % 12 == i:
            for j in range(len(time_down[i])):
                sta = time_down[i][j]
                if sta == 14:
                    stationid[sta],stationid[16]=stationid[sta+1],stationid[sta]
                    
                else:
                    stationid[sta],stationid[sta+1] = stationid[sta+1],stationid[sta]
                
            for j in range(len(time_up[i])):
                sta = time_up[i][j]
                if sta == 30:
                    stationid[sta],stationid[0]=stationid[sta+1],stationid[sta]
                    
                else:
                    stationid[sta],stationid[sta+1] = stationid[sta+1],stationid[sta]
    return stationid