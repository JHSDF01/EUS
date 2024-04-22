from eus_timer import time_count as tc
import train

def move_some_train(event, location, distance, stationid):
    if type(stationid[location]) == train.UnyouClass:
        stationid[location],stationid[location+distance] = stationid[location+distance],stationid[location]
    return

def move_to_next_station(event, location, stationid):
    move_some_train(event, location, 1, stationid)
    return

def turn_on_kamakura_track3(event, stationid):
    move_some_train(event, 14, 2, stationid)
    return

def stay_on_kamakura_track5(event, stationid):
    move_some_train(event, 14, 2, stationid)
    return

def turn_on_fujisawa(event, stationid):
    move_some_train(event, 30, -30, stationid)
    return


#パターンダイヤ時の時刻に合わせて動かす
def startingsignal_sta_pattern(event, hour, min, stationid):
    #[12分間隔の時の時間[その時間の時に出発する駅ID]]
    #1分や13分に出発するのは駅番号０の藤沢、5のえのしま、10の稲村ケ崎
    time_down = [[0,5,10],[1,6],[11],[7],[2,12],[3,8],[13],[9],[4,14],[],[],[]]
    time_up = [[16,26],[27],[17,21],[18],[22],[19,28,23],[24,29],[20],[25,30],[],[],[]]
    #12分間隔のうち、例えば1分の時だったら配列の１にある０と10の駅で座標入れかえ
    i = min % 12
    for j in range(len(time_down[i])):
        sta = time_down[i][j]
        if sta == 14:
            turn_on_kamakura_track3(event, stationid)
            #stationid[14],stationid[16]=stationid[16],stationid[14]
            
        else:
            move_to_next_station(event, sta, stationid)
            #stationid[sta],stationid[sta+1] = stationid[sta+1],stationid[sta]
        
    for j in range(len(time_up[i])):
        sta = time_up[i][j]
        if sta == 30:
            turn_on_fujisawa(event, stationid)
            #stationid[sta],stationid[0]=stationid[sta+1],stationid[sta]
        elif sta == 16:
            if stationid[15] != 0 and stationid[16] == 0:
                move_some_train(event, 15, 2, stationid)
                #stationid[15],stationid[17] = stationid[17],stationid[15]
            elif stationid[17] == 0:
                move_to_next_station(event, sta, stationid)
                #stationid[16],stationid[17] = stationid[17],stationid[16]
        else:
            move_some_train(event, sta, 1, stationid)
            #stationid[sta],stationid[sta+1] = stationid[sta+1],stationid[sta]
    return stationid

#早朝用運用管理
def startingsignal_sta_morning(event, hour, min, stationid):

    time_down = [[0,5,10],[1,6],[11],[7],[2,12],[3,8],[13],[9],[4,14],[],[],[]]
    time_up = [[16,26],[27],[17,21],[18],[22],[19,28,23],[24,29],[20],[25,30],[],[],[15]]
    #12分間隔のうち、例えば1分の時だったら配列の１にある０と10の駅で座標入れかえ
    i = min % 12
    for j in range(len(time_down[i])):
        sta = time_down[i][j]
        if sta == 14:
            #和田塚0532発を鎌倉5番線に入選させる
            if tc.timesig(5,32, hour, min) == True:
                move_some_train(event, 14, 1, stationid)
                #stationid[14],stationid[15]=stationid[15],stationid[14] 
            else:
                move_some_train(event, 14, 2, stationid)
                #stationid[14],stationid[16]=stationid[16],stationid[14]
        #早朝藤沢24発48分発を除外する
        elif sta == 0:
            if min % 24 == 0:
                pass
            else:
                move_some_train(event, sta, 1, stationid)
                #stationid[sta],stationid[sta+1] = stationid[sta+1],stationid[sta]
        else:
            move_some_train(event, sta, 1, stationid)
            #stationid[sta],stationid[sta+1] = stationid[sta+1],stationid[sta]

    for j in range(len(time_up[i])):
        sta = time_up[i][j]
        if sta == 30:
            #石上駅に列車がいるときだけ入れ替える
            if stationid[30] != 0:
                move_some_train(event, sta, -30, stationid)
                #stationid[sta],stationid[0]=stationid[0],stationid[sta]
        elif sta == 15:
            if tc.timesig(5,59, hour, min) == True:
                move_some_train(event, 15, 2, stationid)
                #stationid[15],stationid[17]=stationid[17],stationid[15]
        elif sta == 16:
            #鎌倉駅3番ホーム発車時刻
            #鎌倉0559発は3番発車をキャンセルせず駅15から発車させる
            move_some_train(event, sta, 1, stationid)
            #stationid[16],stationid[17]=stationid[17],stationid[16]
        else:
            move_some_train(event, sta, 1, stationid)
            #stationid[sta],stationid[sta+1] = stationid[sta+1],stationid[sta]

    return stationid

#深夜運用用の関数
def startingsignal_sta_night(event, hour, min, stationid):
    #[12分間隔の時の時間[その時間の時に出発する駅ID]]
    #1分や13分に出発するのは駅番号０の藤沢、5のえのしま、10の稲村ケ崎
    #time_down = [[0,5,10],[1,6],[11],[7],[2,12],[3,8],[13],[9],[4,14],[],[],[]]
    #time_up = [[16,26],[27],[17,21],[18],[22],[19,28,23],[24,29],[20],[25,30],[],[],[]]

    time_down_2 = [[],[],[0,5,10],[1,6],[11],[7],[2,12],[3,8],[13],[9],[4,14],[]]
    time_up_2 = [[],[],[16,26],[27],[17,21],[18],[22],[19,28,23],[24,29],[20],[25,30],[]]
    #12分間隔のうち、例えば1分の時だったら配列の１にある0と10の駅で座標入れかえ
    i = min % 12
    for j in range(len(time_down_2[i])):
        sta = time_down_2[i][j]
        if sta == 14:
            move_some_train(event, 14, 2, stationid)
            #stationid[14],stationid[16]=stationid[16],stationid[14]
            
        else:
            move_some_train(event, sta, 1, stationid)
            #stationid[sta],stationid[sta+1] = stationid[sta+1],stationid[sta]
        
    for j in range(len(time_up_2[i])):
        sta = time_up_2[i][j]
        if sta == 30:
            move_some_train(event, 30, -30, stationid)
            #stationid[sta],stationid[0]=stationid[sta+1],stationid[sta]
        elif sta == 16:
            if stationid[15] != 0 and stationid[16] == 0:
                move_some_train(event, 15, 2, stationid)
                #stationid[15],stationid[17] = stationid[17],stationid[15]
            elif stationid[17] == 0:
                move_some_train(event, 16, 1, stationid)
                #stationid[16],stationid[17] = stationid[17],stationid[16]
        else:
            move_some_train(event, sta, 1, stationid)
            #stationid[sta],stationid[sta+1] = stationid[sta+1],stationid[sta]
    return stationid
