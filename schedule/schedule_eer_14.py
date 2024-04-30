from eus_timer import time_count as tc
from train import train

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
    move_some_train(event, 14, 1, stationid)
    return

def start_from_kamakura_track5(event, stationid):
    move_some_train(event, 15, 2, stationid)
    return

def turn_on_fujisawa(event, stationid):
    move_some_train(event, 30, -30, stationid)
    return

#パターンダイヤ時の時刻に合わせて動かす
def startingsignal_sta_pattern(event, hour, min, stationid):
    #[14分間隔の時の時間[その時間の時に出発する駅ID]]
    #1分や13分に出発するのは駅番号０の藤沢、5のえのしま、10の稲村ケ崎
    time_down = [[0],[1,6],[11],[2,7],[],[3,8,12],[13,9],[],[4,14],[],[],[],[],[10,5]]
    time_up = [[16,26],[17,22,27],[],[18,23],[],[19,24,28],[29],[25,20],[30],[],[],[],[],[21]]
    #14分間隔のうち、例えば1分の時だったら配列の１にある０と10の駅で座標入れかえ
    i = tc.calc_reminder_14_pattern(hour, min)
    for j in range(len(time_down[i])):
        sta = time_down[i][j]
        if sta == 14:
            turn_on_kamakura_track3(event, stationid)            
        else:
            move_to_next_station(event, sta, stationid)
       
    for j in range(len(time_up[i])):
        sta = time_up[i][j]
        if sta == 30:
            turn_on_fujisawa(event, stationid)
        elif sta == 16:
            #鎌倉5番に電車が居るときは鎌倉5番から出す。
            if stationid[15] != 0 and stationid[16] == 0:
                start_from_kamakura_track5(event, stationid)
            #3番に居ても、和田塚に電車が居る場合は入れ替えない(分割併合の可能性があるため)
            elif stationid[17] == 0:
                move_to_next_station(event, 16, stationid)
        else:
            move_to_next_station(event, sta, stationid)
    return stationid
'''

#早朝用運用管理(廃止) 
def startingsignal_sta_morning(event, hour, min, stationid):

    time_down = [[0],[1,6],[11],[2,7],[],[3,8,12],[13,9],[],[4,14],[],[],[],[],[10,5]]
    time_up = [[16,26],[17,22,27],[],[18,23],[],[19,24,28],[29],[25,20],[30],[],[],[],[],[21]]
    #14分間隔のうち、例えば1分の時だったら配列の１にある０と10の駅で座標入れかえ
    i = tc.calc_reminder_14_pattern(hour, min)
    for j in range(len(time_down[i])):
        sta = time_down[i][j]
        if sta == 14:
            turn_on_kamakura_track3(event, stationid)
        else:
            move_to_next_station(event, sta, stationid)

    for j in range(len(time_up[i])):
        sta = time_up[i][j]
        if sta == 30:
            turn_on_fujisawa(event, stationid)
        elif sta == 16:
            # 5:20発を5番から。ちょっとズレてるのでいずれ直す
            if tc.timesig(5,22, hour, min):
                start_from_kamakura_track5(event, stationid)
            #鎌倉駅3番ホーム発車時刻
            #鎌倉0550発はしばらく止まるので発車を抑止
            if not tc.timesig(5,36, hour, min):
                move_to_next_station(event, sta, stationid)
        else:
            move_to_next_station(event, sta, stationid)

    return stationid
'''
'''
#深夜運用用の関数(廃止) 
def startingsignal_sta_night(event, hour, min, stationid):
    #[14分間隔の時の時間[その時間の時に出発する駅ID]]
    #1分や13分に出発するのは駅番号０の藤沢、5のえのしま、10の稲村ケ崎
    #time_down = [[0,5,10],[1,6],[11],[7],[2,12],[3,8],[13],[9],[4,14],[],[],[]]
    #time_up = [[16,26],[27],[17,21],[18],[22],[19,28,23],[24,29],[20],[25,30],[],[],[]]
    time_down_14 = [[0,5],[1,6],[11],[2,7],[],[3,8,12],[13],[],[4,9,14],[],[],[],[],[10]]
    # time_down_26 = [[0,5,7],[1,12],[8,13],[2,9],[14],[3,8],[],[],[4],[],[10],[5],[],[6,11]]
    time_down_26 = [[0,6],[1],[7,12],[2,13],[8,14],[3,9],[],[],[4],[],[10],[5],[11]]
    time_up_14 = [[16,26],[17,22,27],[],[18,23],[],[19,24,28],[29],[25,20],[30],[],[],[],[],[21]]
    #14分間隔のうち、例えば1分の時だったら配列の１にある0と10の駅で座標入れかえ
    h = (tc.calc_reminder_26_pattern(hour, min) + 13) % 13
    for j in range(len(time_down_26[h])):
        sta = time_down_26[h][j]
        if sta == 14:
            turn_on_kamakura_track3(event, stationid)
        elif sta == 0 & tc.calc_reminder_26_pattern(hour, min) != 0:
            pass
        else:
            move_to_next_station(event, sta, stationid)

        if tc.timesig(23,39, hour, min):
            move_to_next_station(event, 10, stationid)
        if tc.timesig(23,0, hour, min):
            turn_on_kamakura_track3(event, stationid)
    
    i = tc.calc_reminder_14_pattern(hour, min)
    for j in range(len(time_up_14[i])):
        sta = time_up_14[i][j]
        if sta == 30:
            turn_on_fujisawa(event, stationid)
        elif sta == 16:
            if stationid[15] != 0 and stationid[16] == 0:
                start_from_kamakura_track5(event, stationid)
            elif stationid[17] == 0:
                move_to_next_station(event, 16, stationid)
        else:
            move_to_next_station(event, sta, stationid)

        if tc.timesig(23,5, hour, min):
           move_to_next_station(event, 16, stationid)

    return stationid
'''