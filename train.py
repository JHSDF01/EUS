#!/usr/bin/python3
# -*- coding: UTF-8 -*-

#列車と運用についてのデータを定義する
#列車の運行を開始する
import cars as car
import time_count as tc

unyouid = []
if __name__ == '__main__':
    un1 = UnyouClass(" 501","2003", 20, 1)
    un2 = UnyouClass(" 10 ","1001", 5, 2)
    un3 = UnyouClass("2002","1502", 5, 3)
    un4 = UnyouClass("1101"," 22 ", 26, 4)
    un5 = UnyouClass(" 21 ","1501", 10, 5)
    un6 = UnyouClass("1002"," 305", 21, 6)
    un7 = UnyouClass("1501"," 502", 21, 6)   
    testrun = UnyouClass("1201","", 21, 6)      
    stationid = []

class UnyouClass:
    def __init__(self, car1, car2, stationnum, icon):
        self.train =[]
        self.train.append(car1)
        if car2 != "":
            #４両編成の場合、車両を追加
            self.train.append(car2)
        self.location = stationnum
        self.icon = "[" + str(icon) + "]"

        if len(self.train) == 2:
            self.carname = str(self.icon) + self.train[0] + '+' + self.train[1]
        else:
            self.carname = str(self.icon) + self.train[0] + '     '
        unyouid.append(self)

    def __del__(self):
        #運用の配列を削除してから運用を削除
        pass

    def move_train(self, location, distance, stationid):
        #1駅移動するときは1駅移動する先と内容を交換して、位置情報を更新する
        self.location = location + distance
        stationid[location],stationid[location+distance] = stationid[location+distance],stationid[location]
        return
        

    def set_train(self, stationid):
        # print(str(len(self.train)))
        if len(self.train) == 2:
            stationid[self.location] = self
            self.carname = str(self.icon) + self.train[0] + '+' + self.train[1]
        else:
            stationid[self.location] = self
            self.carname = str(self.icon) + self.train[0] + '     '
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
        #37は入庫線。一時的に値を格納して置き、基本的には単行にばらして保管する
        #極楽寺2とか3は重連でもおいておけるけどここをどう定義するか悩みどころ
        #38、39は重連対応にする？
        if idnum == 11 or idnum == 20:
            stationid[idnum], stationid[37] = stationid[37], stationid[idnum]            
            for i in range(38, 42):
                for j in range(len(self.train)):
                
                    if stationid[i] == 0:
                        stationid[i]= str(self.train[j])
                        break
            self.location = 37
            #stationid[37] = 0
    
        del self
        return stationid

    def add_cars(self, location, car, stationid):
        #単行に出庫車を連結する場合
        if location < 16:
            self.train.append(car)
        else:
            #train[0] = train[1]
            #train[0] = car
            self.train.append(car)
            self.train[0], self.train[1] = car, self.train[0]

        self.carname = str(self.icon) + self.train[0] + '+' + self.train[1]
        return stationid


    def parge_cars(self, location, stationid):
        #重連を開放して入庫する場合
        if location < 16:
            self.train[0] = self.train[1]
            del self.train[1]
        else:
            del self.train[1]

        self.carname = str(self.icon) + self.train[0] + '     '
        return stationid


    def change_back_cars(self, location, car, stationid):
        #重連の前に2両を連結し、後ろ2両を開放する場合
        if self.location < 16:
            #train[0] = train[1]
            #train[1] = car
            self.train[0], self.train[1] = self.train[1], car
        else:
            #train[1] = train[0]
            #train[0] = car
            self.train[0], self.train[1] = car, self.train[0]

        self.carname = str(self.icon) + self.train[0] + '+' + self.train[1]
        return stationid

    def change_all_cars(self, location, car, stationid):
        #重連の前に2両を待機させ、後ろ4両をそのまま入庫させる場合
        if self.location < 16:
            self.train[0] = car
            del self.train[1]
        else:
            self.train[0] = car
            del self.train[1]

        self.carname = str(self.icon) + self.train[0] + '     '
        return stationid


def move_some_train(location, distance, stationid):
    #stationid[location].move_train(location, distance, stationid)
    if un1 == stationid[location]:
        un1.move_train(location, distance, stationid)
    if un2 == stationid[location]:
        un2.move_train(location, distance, stationid)
    if un3 == stationid[location]:
        un3.move_train(location, distance, stationid)
    if un4 == stationid[location]:
        un4.move_train(location, distance, stationid)
    if un5 == stationid[location]:
        un5.move_train(location, distance, stationid)
    if un6 == stationid[location]:
        un6.move_train(location, distance, stationid)
    if un7 == stationid[location]:
        un7.move_train(location, distance, stationid)
    if testrun == stationid[location]:
        testrun.move_train(location, distance, stationid)


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
    time_down = [[0,5,10],[1,6],[11],[7],[2,12],[3,8],[13],[9],[4,14],[],[],[]]
    time_up = [[16,26],[27],[17,21],[18],[22],[19,28,23],[24,29],[20],[25,30],[],[],[]]
    for i in range(11):
        #12分間隔のうち、例えば1分の時だったら配列の１にある０と10の駅で座標入れかえ
        if min % 12 == i:
            for j in range(len(time_down[i])):
                sta = time_down[i][j]
                if sta == 14:
                    move_some_train(14, 2, stationid)
                    #stationid[14],stationid[16]=stationid[16],stationid[14]
                    
                else:
                    move_some_train(sta, 1, stationid)
                    #stationid[sta],stationid[sta+1] = stationid[sta+1],stationid[sta]
                
            for j in range(len(time_up[i])):
                sta = time_up[i][j]
                if sta == 30:
                    move_some_train(30, -30, stationid)
                    #stationid[sta],stationid[0]=stationid[sta+1],stationid[sta]
                elif sta == 16:
                    if stationid[15] != 0 and stationid[16] == 0:
                        move_some_train(15, 2, stationid)
                        #stationid[15],stationid[17] = stationid[17],stationid[15]
                    elif stationid[17] == 0:
                        move_some_train(16, 1, stationid)
                        #stationid[16],stationid[17] = stationid[17],stationid[16]
                else:
                    move_some_train(sta, 1, stationid)
                    #stationid[sta],stationid[sta+1] = stationid[sta+1],stationid[sta]
    return stationid

#早朝用運用管理
def startingsignal_sta_morning(hour, min, stationid):

    time_down = [[0,5,10],[1,6],[11],[7],[2,12],[3,8],[13],[9],[4,14],[],[],[]]
    time_up = [[16,26],[27],[17,21],[18],[22],[19,28,23],[24,29],[20],[25,30],[],[],[15]]
    for i in range(11):
        #12分間隔のうち、例えば1分の時だったら配列の１にある０と10の駅で座標入れかえ
        if min % 12 == i:
            for j in range(len(time_down[i])):
                sta = time_down[i][j]
                if sta == 14:
                    #和田塚0532発を鎌倉5番線に入選させる
                    if tc.timesig(5,32, hour, min) == True:
                        move_some_train(14, 1, stationid)
                        #stationid[14],stationid[15]=stationid[15],stationid[14] 
                    else:
                        move_some_train(14, 2, stationid)
                        #stationid[14],stationid[16]=stationid[16],stationid[14]
                #早朝藤沢24発48分発を除外する
                elif sta == 0:
                    if min % 24 == 0:
                        pass
                    else:
                        move_some_train(sta, 1, stationid)
                        #stationid[sta],stationid[sta+1] = stationid[sta+1],stationid[sta]
                else:
                    move_some_train(sta, 1, stationid)
                    #stationid[sta],stationid[sta+1] = stationid[sta+1],stationid[sta]
        
            for j in range(len(time_up[i])):
                sta = time_up[i][j]
                if sta == 30:
                    #石上駅に列車がいるときだけ入れ替える
                    if stationid[30] != 0:
                        move_some_train(sta, -30, stationid)
                        #stationid[sta],stationid[0]=stationid[0],stationid[sta]
                elif sta == 15:
                    if tc.timesig(5,59, hour, min) == True:
                        move_some_train(15, 2, stationid)
                        #stationid[15],stationid[17]=stationid[17],stationid[15]
                elif sta == 16:
                    #鎌倉駅3番ホーム発車時刻
                    #鎌倉0559発は3番発車をキャンセルせず駅15から発車させる
                    move_some_train(sta, 1, stationid)
                    #stationid[16],stationid[17]=stationid[17],stationid[16]
                else:
                    move_some_train(sta, 1, stationid)
                    #stationid[sta],stationid[sta+1] = stationid[sta+1],stationid[sta]

    return stationid