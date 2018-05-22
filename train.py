#!/usr/bin/python3
# -*- coding: UTF-8 -*-

#列車と運用についてのデータを定義する
#列車の運行を開始する
import cars as car
import time_count as tc

class UnyouClass:
    def __init__(self, car1, car2, stationnum, icon):
        self.train =[]
        self.train.append(car1)
        if car2 != "":
            #４両編成の場合、車両を追加
            self.train.append(car2)
        self.location = stationnum
        self.icon = "[" + str(icon) + "]"


    def move_train(self, new_location):
        self.location = new_location
        return self.location

    def set_train(self, stationid):
        print(str(len(self.train)))
        if len(self.train) == 2:
            stationid[self.location] = str(self.icon) + self.train[0] + '+' + self.train[1]
        else:
            stationid[self.location] = str(self.icon) + self.train[0] + '     '
        return stationid

    def out_train(self, stationid,idnum):
        #入庫措置

        #江ノ島留置
        if idnum == 26 and len(self.train) == 1:
            if stationid[33] == 0:
                stationid[idnum], stationid[33] = stationid[33], stationid[idnum]
                self.location = idnum
            elif stationid[32] == 0:
                stationid[idnum], stationid[34] = stationid[34], stationid[idnum]
                self.location = idnum
 
        #極楽寺留置
        if idnum == 11 or idnum == 20:
            for i in range(37, 42):
                if stationid[i] == 0:
                    stationid[idnum], stationid[i] = stationid[i], stationid[idnum]
                    self.location = i
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
def startingsignal_sta_pattern(hour, min, stationid):
    #[12分間隔の時の時間[その時間の時に出発する駅ID]]
    #1分や13分に出発するのは駅番号０の藤沢、5のえのしま、10の稲村ケ崎
    time_down = [[0,5,10],[1,6],[11],[7],[2,12],[3,8],[13],[9],[4,14],[],[],[11]]
    time_up = [[16,26],[27],[17,21],[18],[22],[19,28,23],[24,29],[20],[25,30],[],[],[]]
    for i in range(11):
        #12分間隔のうち、例えば1分の時だったら配列の１にある０と10の駅で座標入れかえ
        if min % 12 == i:
            for j in range(len(time_down[i])):
                sta = time_down[i][j]
                if sta == 14:
                    stationid[14],stationid[16]=stationid[16],stationid[14]
                    
                else:
                    stationid[sta],stationid[sta+1] = stationid[sta+1],stationid[sta]
                
            for j in range(len(time_up[i])):
                sta = time_up[i][j]
                if sta == 30:
                    stationid[sta],stationid[0]=stationid[sta+1],stationid[sta]
                elif sta == 16:
                    if stationid[15] != 0 and stationid[16] == 0:
                        stationid[15],stationid[17] = stationid[17],stationid[15]
                    elif stationid[17] == 0:
                        stationid[16],stationid[17] = stationid[17],stationid[16]
                else:
                    stationid[sta],stationid[sta+1] = stationid[sta+1],stationid[sta]
    return stationid

#早朝用運用管理
def startingsignal_sta_morning(hour, min, stationid):

    time_down = [[0,5,10],[1,6],[11],[7],[2,12],[3,8],[13],[9],[4,14],[],[],[11]]
    time_up = [[16,26],[27],[17,21],[18],[22],[19,28,23],[24,29],[20],[25,30],[],[],[15]]
    for i in range(11):
        #12分間隔のうち、例えば1分の時だったら配列の１にある０と10の駅で座標入れかえ
        if min % 12 == i:
            for j in range(len(time_down[i])):
                sta = time_down[i][j]
                if sta == 14:
                    #和田塚0532発を鎌倉5番線に入選させる
                    if tc.timesig(5,32, hour, min) == True:
                        stationid[14],stationid[15]=stationid[15],stationid[14] 
                    else:
                        stationid[14],stationid[16]=stationid[16],stationid[14]
                #早朝藤沢24発48分発を除外する
                elif sta == 0:
                    if min % 24 == 0:
                        pass
                    else:
                        stationid[sta],stationid[sta+1] = stationid[sta+1],stationid[sta]
                else:
                    stationid[sta],stationid[sta+1] = stationid[sta+1],stationid[sta]
        
            for j in range(len(time_up[i])):
                sta = time_up[i][j]
                if sta == 30:
                    #石上駅に列車がいるときだけ入れ替える
                    if stationid[30] != 0:
                        stationid[sta],stationid[0]=stationid[0],stationid[sta]
                elif sta == 15:
                    if tc.timesig(5,59, hour, min) == True:
                        stationid[15],stationid[17]=stationid[17],stationid[15]
                elif sta == 16:
                    #鎌倉駅3番ホーム発車時刻
                    #鎌倉0559発は3番発車をキャンセルせず駅15から発車させる
                    stationid[16],stationid[17]=stationid[17],stationid[16]
                else:
                    stationid[sta],stationid[sta+1] = stationid[sta+1],stationid[sta]

    return stationid