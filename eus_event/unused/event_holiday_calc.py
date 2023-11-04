#!/usr/bin/python3
# coding: utf-8

from time import sleep
from eus_timer import time_count as tc
import train as tr
import depot as dp
import save_depot as save
import json

#車庫に留置されている車両を登録する。
# save機能で取得するようにする
# 昼の運用から予想するモード

class EventHolidayCalc(EventClass): 

    def __init__(self):
        super().__init__()
    
    def set_unyou(self):
        super().set_unyou()

    def input_unyou(self):
        super().input_unyou()
        
    def delete_depot(self):
        super().delete_depot()

    def get_unyou_list(self):
        super().get_unyou_list()

    def output_unyo(self):
        super().output_unyo()

    def run_train(hour,min, stationid):
        if tc.timesig(5,43, hour, min) == True:
            del self.un1
            self.un1 = tr.UnyouClass(dp.goku.pull_car(), 0, 20, 1)
            self.un1.set_train(stationid) 
        if tc.timesig(5,22, hour, min) == True:
            del self.un2
            self.un2 = tr.UnyouClass(dp.E03.pull_car(),0, 5, 2)
            self.un2.set_train(stationid)
        if tc.timesig(5,9, hour, min) == True:
            del self.un3
            self.un3 = tr.UnyouClass(dp.T05A.pull_car(),dp.T05B.pull_car(), 5, 3)
            self.un3.set_train(stationid)
        if tc.timesig(5,10, hour, min) == True:
            del self.un4
            self.un4 = tr.UnyouClass(dp.T26A.pull_car(),dp.T26B.pull_car(), 26, 4)
            self.un4.set_train(stationid)
        if tc.timesig(6,11, hour, min) == True:
            del self.un5
            self.un5 = tr.UnyouClass(dp.goku.pull_car(),0, 10, 5)
            self.un5.set_train(stationid)
        if tc.timesig(5,22, hour, min) == True:
            del self.un6
            self.un6 = tr.UnyouClass(dp.T21A.pull_car(),dp.T21B.pull_car(), 21, 6)
            self.un6.set_train(stationid)

        if tc.timesig(6, 00, hour, min) == True:
            self.un1.add_cars(26, dp.E01.pull_car(), stationid)

        if tc.timesig(8, 19, hour, min) == True:
            self.un2.add_cars(20,dp.goku.pull_car(), stationid)

        if tc.timesig(8, 43, hour, min) == True:
            self.un4.add_cars(20,dp.goku.pull_car(), stationid)

        if tc.timesig(6, 48, hour, min) == True:
            self.un5.add_cars(26, dp.E04B.pull_car() , stationid)

        if tc.timesig(19, 2, hour, min) == True:
            dp.goku.push_car(self.un3.parge_cars(11, stationid))

        
        if tc.timesig(19, 12, hour, min) == True:
            dp.E04B.push_car(self.un1.parge_cars(26, stationid))


        #if tc.timesig(19, 2, hour, min) == True:
        #    self.un3.parge_cars(11, stationid)

        if tc.timesig(18,  14, hour, min) == True:
            dp.Gtemp.push_car(self.un5.parge_cars(11, stationid))
    #ここで切り離した車は後続6番に交換される

        if tc.timesig(18, 26, hour, min) == True:
            dp.goku.push_cars(self.un6.change_all_cars(11, dp.Gtemp.pull_car(), stationid))

        if tc.timesig(22,16, hour, min) == True:
            self.un1.out_train(stationid,11,dp.goku,dp.goku)
        if tc.timesig(24,0, hour, min) == True:
            self.un2.out_train(stationid,21,dp.T21A,dp.T21B)
        if tc.timesig(22,0, hour, min) == True:
            self.un3.out_train(stationid,26,dp.E03,'')
        if tc.timesig(23,50, hour, min) == True:
            self.un4.out_train(stationid,5,dp.T05A,dp.T05B)
        if tc.timesig(22,25, hour, min) == True:
            self.un5.out_train(stationid,26,dp.E01,'')
        if tc.timesig(23,49, hour, min) == True:
            self.un6.out_train(stationid,26,dp.T26A,dp.T26B)

        if tc.timesig(24,0, hour, min) == True:
            delete_depot()
    
        if tc.timesig(11, 00, hour, min) == True:
            # 1から6までの運用を出力する。
            input_unyou(stationid)
            pass
        """
        if tc.timesig(9, 25, hour, min) == True:
            self.un4.parge_cars(11, stationid)


        if tc.timesig(7,23, hour, min) == True:
            self.un1.out_train(stationid,26)
        if tc.timesig(7,25, hour, min) == True:
            self.un2.out_train(stationid,11)
        """