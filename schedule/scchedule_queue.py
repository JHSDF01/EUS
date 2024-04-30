from eus_timer import time_count as tc
from train import train
from schedule import schedule_eer_14 as sc

def starting_signal_by_queue(event, hour, min, stationid):
    pass

def starting_signal_by_queue(event, hour, min, stationid):
        for i in range (len(schedule[hour])):
            for j in range (len(schedule[hour][i])):
                if schedule[hour][i][j] % 60 == min:
                    if i==14:
                        if schedule[hour][14][j] > 60:
                            sc.stay_on_kamakura_track5(event, stationid)
                        else:
                            sc.turn_on_kamakura_track3(event, stationid)
                    elif i==15:
                        sc.start_from_kamakura_track5(event, stationid)
                    elif i==30:
                        sc.turn_on_fujisawa(event, stationid)
                    else:
                        sc.move_to_next_station(event, i, stationid)

schedule_5 = {
    0: [36,50],
    1: [37,51],
    2: [39,53],
    3: [41,55],
    4: [44,58],
    5: [10,23,49],
    6: [12,25,51],
    7: [14,27,53],
    8: [16,29,55],
    9: [17,30,56],
    10: [22,36],
    11: [24,39],
    12: [26,41],
    13: [28,43],
    14: [60+29,44],
    15: [20],
    16: [50],
    17: [21,51],
    18: [23,53],
    19: [27,55],
    20: [29,46,57],
    21: [36,49],
    22: [39,52],
    23: [41,54],
    24: [42,56],
    25: [44,58],
    26: [15,36,50],
    27: [16,37,51],
    28: [19,41,55],
    29: [21,42,56],
    30: [22,44,58],
}

schedule_21 = {
    0: [0,14,28,42,56],
    1: [1,15,29,43,57],
    2: [3,17,31,45,59],
    3: [5,19,33,47],
    4: [8,22,36,50],
    5: [13,27,41,55],
    6: [1,15,29,43,57],
    7: [3,17,31,45,59],
    8: [5,19,33,47],
    9: [6,20,34,48],
    10: [13,27,39,55],
    11: [2,16,30,58],
    12: [5,19,32],
    13: [6,20,34],
    14: [8,60+22,36],
    15: [],
    16: [0,14,42],
    17: [1,15,43],
    18: [3,17,45],
    19: [5,19,47],
    20: [7,21,49],
    21: [13,27,55],
    22: [2,16,30,56],
    23: [4,18,32,58],
    24: [6,20,34],
    25: [8,22,36],
    26: [0,14,28,42],
    27: [1,15,29,43],
    28: [5,19,33,47],
    29: [6,20,34,48],
    30: [8,22,36,50],
}

schedule_22 = {
    0: [24,50],
    1: [25,51],
    2: [27,53],
    3: [1,29,55],
    4: [4,32,58],
    5: [9,35],
    6: [11,37],
    7: [13,39],
    8: [1,15,41],
    9: [2,16,42],
    10: [9,23,49],
    11: [12,26,52],
    12: [0,15,29,55],
    13: [2,16,30,56],
    14: [3,18,32,56],
    15: [],
    16: [10,24,38],
    17: [11,25,39],
    18: [13,27,41],
    19: [15,29,43],
    20: [17,31,45],
    21: [22,35,50],
    22: [25,38,53],
    23: [1,27,40,55],
    24: [2,28,42,56],
    25: [4,30,44,56],
    26: [10,36],
    27: [11,37],
    28: [15,41],
    29: [16,42],
    30: [18,44],
}

schedule_23 = {
    0: [16,42],
    1: [17,43],
    2: [19,45],
    3: [21,47],
    4: [24,50],
    5: [3,27],
    6: [5,30],
    7: [7,32],
    8: [9,34],
    9: [10,35],
    10: [17,39],
    11: [19],
    12: [22],
    13: [23],
    14: [25],
    15: [],
    16: [5,37],
    17: [6,39],
    18: [8,40],
    19: [10,43],
    20: [12,45],
    21: [16,49],
    22: [19,52],
    23: [20,53],
    24: [22,55],
    25: [24,57],
    26: [2,26],
    27: [3,30],
    28: [7,33],
    29: [8,35],
    30: [10,36],
}

schedule = {
    5:schedule_5,
    21:schedule_21,
    22:schedule_22,
    23:schedule_23
}