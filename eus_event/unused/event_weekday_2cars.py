#!/usr/bin/python3
# coding: utf-8

from time import sleep
from eus_timer import time_count as tc
import train as tr
import depot as dp

class EventWeekDay2cars(EventClass): 

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
            self.un1.set_train(stationid) 
        if tc.timesig(5,22, hour, min) == True:
            self.un2.set_train(stationid)
        if tc.timesig(5,9, hour, min) == True:
            self.un3.set_train(stationid)
        if tc.timesig(5,10, hour, min) == True:
            self.un4.set_train(stationid)
        if tc.timesig(6,11, hour, min) == True:
            self.un5.set_train(stationid)
        if tc.timesig(5,22, hour, min) == True:
            self.un6.set_train(stationid)

        if tc.timesig(6, 00, hour, min) == True:
            self.un1.add_cars(26, 501, stationid)

        if tc.timesig(5, 55, hour, min) == True:
            self.un2.add_cars(20,  10, stationid)

        if tc.timesig(6, 18, hour, min) == True:
            self.un4.add_cars(20,1101, stationid)


        if tc.timesig(9, 7, hour, min) == True:
            self.un6.change_all_cars(20, 1201, stationid)

        if tc.timesig(9, 24, hour, min) == True:
            self.un6.add_cars(26, 502, stationid)

        if tc.timesig(17, 50, hour, min) == True:
            self.un3.parge_cars(11, stationid)

        if tc.timesig(18,  2, hour, min) == True:
            self.un5.parge_cars(11, stationid)

        if tc.timesig(19,  0, hour, min) == True:
            self.un6.parge_cars(26, stationid)

        if tc.timesig(18, 38, hour, min) == True:
            self.un1.parge_cars(11, stationid)

        if tc.timesig(22,16, hour, min) == True:
            self.un1.out_train(stationid,11)
        if tc.timesig(24,0, hour, min) == True:
            self.un2.out_train(stationid,21)
        if tc.timesig(22,0, hour, min) == True:
            self.un3.out_train(stationid,26)
        if tc.timesig(23,50, hour, min) == True:
            self.un4.out_train(stationid,5)
        if tc.timesig(22,25, hour, min) == True:
            self.un5.out_train(stationid,26)
        if tc.timesig(23,49, hour, min) == True:
            self.un6.out_train(stationid,26)


        """
        if tc.timesig(9, 25, hour, min) == True:
            self.un4.parge_cars(11, stationid)


        if tc.timesig(7,23, hour, min) == True:
            self.un1.out_train(stationid,26)
        if tc.timesig(7,25, hour, min) == True:
            self.un2.out_train(stationid,11)
        """
        