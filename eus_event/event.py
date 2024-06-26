#!/usr/bin/python3
# coding: utf-8

from time import sleep
from eus_timer import time_count as tc
from train import train as tr
from train import depots
from train import save_depot as save
import json
from eus_event import event 

class EventClass:

    def __init__(self):
        depot_morning = save.EUS_load()
        self.dp = depots.DepotsClass(depot_morning)
        self.un1 = tr.UnyouClass(self.dp.goku.desc_cars()[0], 0, 20, 1)
        self.un2 = tr.UnyouClass(self.dp.E04B.desc_car(),0, 5, 2)
        self.un3 = tr.UnyouClass(self.dp.T05A.desc_car(),self.dp.T05B.desc_car(), 5, 3)
        self.un4 = tr.UnyouClass(self.dp.T26A.desc_car(),self.dp.T26B.desc_car(), 26, 4)
        self.un5 = tr.UnyouClass(self.dp.goku.desc_cars()[2],self.dp.goku.desc_cars()[3], 10, 5)
        self.un6 = tr.UnyouClass(self.dp.T21A.desc_car(),self.dp.T21B.desc_car(), 21, 6)
        self.unyolist = [self.un1,self.un2,self.un3,self.un4,self.un5,self.un6]
        """
        with open('save/unyo.json') as uload:
            noon = json.load(uload)
            self.un1 = tr.UnyouClass(noon["[1]"][0], noon["[1]"][1], 0, 1)
            self.un2 = tr.UnyouClass(noon["[2]"][0], noon["[2]"][1], 5, 2)
            self.un3 = tr.UnyouClass(noon["[3]"][0], noon["[3]"][1], 10, 3)
            self.un4 = tr.UnyouClass(noon["[4]"][0], noon["[4]"][1], 16, 4)
            self.un5 = tr.UnyouClass(noon["[5]"][0], noon["[5]"][1], 21, 5)
            self.un6 = tr.UnyouClass(noon["[6]"][0], noon["[6]"][1], 26, 6)
            self.un7 = tr.UnyouClass(0, 0, 21, 6)   
            self.testrun = tr.UnyouClass(0, 0, 20, 6) 
        self.unyolist = [self.un1,self.un2,self.un3,self.un4,self.un5,self.un6,self.un7,self.testrun]
        """
        
        
    """    
    def set_depot(self):
        depot_morning = save.EUS_load()
        self.dp = depots.DepotsClass(depot_morning)
    """
    
    def set_unyou(self):
        self.un1 = tr.UnyouClass(self.dp.goku.desc_cars()[0], 0, 20, 1)
        self.un2 = tr.UnyouClass(self.dp.E04B.desc_car(),0, 5, 2)
        self.un3 = tr.UnyouClass(self.dp.T05A.desc_car(),self.dp.T05B.desc_car(), 5, 3)
        self.un4 = tr.UnyouClass(self.dp.T26A.desc_car(),self.dp.T26B.desc_car(), 26, 4)
        self.un5 = tr.UnyouClass(self.dp.E01.desc_car()[2],0, 10, 5)
        self.un6 = tr.UnyouClass(self.dp.T15A.desc_car(),self.dp.T15B.desc_car(), 21, 6)
        self.un7 = tr.UnyouClass(0, 0, 21, 6)   
        self.testrun = tr.UnyouClass(0, 0, 20, 6) 

        """    
        12分の時はこれ
        self.un1 = tr.UnyouClass(self.dp.goku.desc_cars()[0], 0, 20, 1)
        self.un2 = tr.UnyouClass(self.dp.E03.desc_car(),0, 5, 2)
        self.un3 = tr.UnyouClass(self.dp.T05A.desc_car(),self.dp.T05B.desc_car(), 5, 3)
        self.un4 = tr.UnyouClass(self.dp.T26A.desc_car(),self.dp.T26B.desc_car(), 26, 4)
        self.un5 = tr.UnyouClass(self.dp.goku.desc_cars()[2],self.dp.goku.desc_cars()[3], 10, 5)
        self.un6 = tr.UnyouClass(self.dp.T21A.desc_car(),self.dp.T21B.desc_car(), 21, 6)
        """    

    def input_unyou(self):
        with open('save/unyo.json') as uload:
            noon = json.load(uload)
            self.un1 = tr.UnyouClass(noon["[1]"][0], noon["[1]"][1], 0, 1)
            self.un2 = tr.UnyouClass(noon["[2]"][0], noon["[2]"][1], 5, 2)
            self.un3 = tr.UnyouClass(noon["[3]"][0], noon["[3]"][1], 10, 3)
            self.un4 = tr.UnyouClass(noon["[4]"][0], noon["[4]"][1], 16, 4)
            self.un5 = tr.UnyouClass(noon["[5]"][0], noon["[5]"][1], 21, 5)
            self.un6 = tr.UnyouClass(noon["[6]"][0], noon["[6]"][1], 26, 6)
            self.un7 = tr.UnyouClass(noon["[7]"][0], noon["[7]"][1], 21, 6)   
            self.testrun = tr.UnyouClass(noon["[8]"][0], noon["[8]"][1], 20, 6) 

    def delete_depot(self):
        depot_midnight = {"E01": self.dp.E01.desc_car(),"E02": self.dp.E02.desc_car(),"E03": self.dp.E03.desc_car(),"E04A": self.dp.E04A.desc_car(),"E04B": self.dp.E04B.desc_car(),
            "Gtemp": 0, "goku": self.dp.goku.desc_cars(),
            "5A": self.dp.T05A.desc_car(),"5B": self.dp.T05B.desc_car(),"26A": self.dp.T26A.desc_car(),"26B": self.dp.T26B.desc_car(),"21A": self.dp.T21A.desc_car(),"21B": self.dp.T21B.desc_car()}
        save.EUS_save(depot_midnight)

    def get_unyou_list(self):
        return self.unyolist

    def output_unyo(self):
        output =str(str(self.un1.desc_train())
            +"\n"+ str(self.un2.desc_train())
            +"\n"+ str(self.un3.desc_train())
            +"\n"+ str(self.un4.desc_train())
            +"\n"+ str(self.un5.desc_train())
            +"\n"+ str(self.un6.desc_train())
            +"\ngoku"+ str(self.dp.goku.desc_cars())
        )
        with open('save/unyo.txt', 'w') as fsave:
            fsave.write(output)

    def run_train(self, hour, min, stationid):
        
        if tc.timesig(5,46, hour, min) == True:
            del self.un1
            self.un1 = tr.UnyouClass(self.dp.goku.pull_car(), 0, 20, 1)
            self.un1.set_train(stationid) 
        if tc.timesig(5,22, hour, min) == True:
            del self.un2
            self.un2 = tr.UnyouClass(self.dp.E04B.pull_car(),0, 5, 2)
            self.un2.set_train(stationid)
        if tc.timesig(5,8, hour, min) == True:
            del self.un3
            self.un3 = tr.UnyouClass(self.dp.T05A.pull_car(),self.dp.T05B.pull_car(), 5, 3)
            self.un3.set_train(stationid)
        if tc.timesig(5,14, hour, min) == True:
            del self.un4
            self.un4 = tr.UnyouClass(self.dp.T26A.pull_car(),self.dp.T26B.pull_car(), 26, 4)
            self.un4.set_train(stationid)
        if tc.timesig(5,34, hour, min) == True:
            del self.un5
            self.un5 = tr.UnyouClass(self.dp.E01.pull_car(),0, 26, 5)
            self.un5.set_train(stationid)
        if tc.timesig(5,18, hour, min) == True:
            del self.un6
            self.un6 = tr.UnyouClass(self.dp.T15A.pull_car(),self.dp.T15B.pull_car(), 15, 6)
            self.un6.set_train(stationid)

        if tc.timesig(22,50, hour, min) == True:
            self.un1.out_train(stationid,26,self.dp.E01,'')
        if tc.timesig(23,41, hour, min) == True:
            self.un2.out_train(stationid,11,self.dp.Gtemp,'')
        if tc.timesig(21,23, hour, min) == True:
            self.un3.out_train(stationid,15,self.dp.T15A,self.dp.T15B)
        if tc.timesig(23,53, hour, min) == True:
            self.un4.out_train(stationid,5,self.dp.T05A,self.dp.T05B)
        if tc.timesig(21,44, hour, min) == True:
            self.un5.out_train(stationid,11,self.dp.goku,'')
        if tc.timesig(23,59, hour, min) == True:
            self.un6.out_train(stationid,26,self.dp.T26A,self.dp.T26B)
            self.delete_depot()

        if tc.timesig(24,0, hour, min) == True:
            self.delete_depot()


        if tc.timesig(11, 00, hour, min) == True:
            # 1から6までの運用を出力する。
            self.output_unyo()
            pass

class EventWeekDay(EventClass):

    def run_train(self, hour, min, stationid):
        
        #5:47発だがずらす。
        if tc.timesig(5,46, hour, min) == True:
            del self.un1
            self.un1 = tr.UnyouClass(self.dp.goku.pull_car(), 0, 20, 1)
            self.un1.set_train(stationid) 
        if tc.timesig(5,22, hour, min) == True:
            del self.un2
            self.un2 = tr.UnyouClass(self.dp.E04B.pull_car(),0, 5, 2)
            self.un2.set_train(stationid)
        if tc.timesig(5,8, hour, min) == True:
            del self.un3
            self.un3 = tr.UnyouClass(self.dp.T05A.pull_car(),self.dp.T05B.pull_car(), 5, 3)
            self.un3.set_train(stationid)
        if tc.timesig(5,14, hour, min) == True:
            del self.un4
            self.un4 = tr.UnyouClass(self.dp.T26A.pull_car(),self.dp.T26B.pull_car(), 26, 4)
            self.un4.set_train(stationid)
        if tc.timesig(5,34, hour, min) == True:
            del self.un5
            self.un5 = tr.UnyouClass(self.dp.E01.pull_car(),0, 26, 5)
            self.un5.set_train(stationid)
        if tc.timesig(5,18, hour, min) == True:
            del self.un6
            self.un6 = tr.UnyouClass(self.dp.T15A.pull_car(),self.dp.T15B.pull_car(), 15, 6)
            self.un6.set_train(stationid)


        if tc.timesig(6, 48, hour, min) == True:
            self.un1.add_cars(11, self.dp.goku.pull_car(), stationid)

        if tc.timesig(5, 57, hour, min) == True:
            self.un2.add_cars(20,self.dp.goku.pull_car(), stationid)

        if tc.timesig(6, 20, hour, min) == True:
            self.un5.add_cars(11,self.dp.goku.pull_car(), stationid)

        if tc.timesig(23, 45, hour, min) == True:
            self.un6.add_cars(20,self.dp.Gtemp.pull_car(), stationid)

        if tc.timesig(19, 10, hour, min) == True:
            self.dp.goku.push_cars(self.un6.change_all_cars(11, self.dp.goku.pull_car(), stationid))

        if tc.timesig(18,  14, hour, min) == True:
            self.dp.goku.push_car(self.un2.parge_cars(11, stationid))

        if tc.timesig(20,  1, hour, min) == True:
            self.dp.E04B.push_car(self.un1.parge_cars(26, stationid))

        if tc.timesig(18, 56, hour, min) == True:
            self.dp.goku.push_car(self.un5.parge_cars(11, stationid))

        if tc.timesig(22,50, hour, min) == True:
            self.un1.out_train(stationid,26,self.dp.E01,'')
        if tc.timesig(23,41, hour, min) == True:
            self.un2.out_train(stationid,11,self.dp.Gtemp,'')
        if tc.timesig(21,23, hour, min) == True:
            self.un3.out_train(stationid,15,self.dp.T15A,self.dp.T15B)
        if tc.timesig(23,53, hour, min) == True:
            self.un4.out_train(stationid,5,self.dp.T05A,self.dp.T05B)
        if tc.timesig(21,44, hour, min) == True:
            self.un5.out_train(stationid,11,self.dp.goku,'')
        if tc.timesig(23,59, hour, min) == True:
            self.un6.out_train(stationid,26,self.dp.T26A,self.dp.T26B)
            self.delete_depot()

        if tc.timesig(24,0, hour, min) == True:
            self.delete_depot()


        if tc.timesig(11, 00, hour, min) == True:
            # 1から6までの運用を出力する。
            self.output_unyo()
            pass

class EventHoliday(EventClass): 
    
    def run_train(self, hour,min, stationid):
        if tc.timesig(5,46, hour, min) == True:
            del self.un1
            self.un1 = tr.UnyouClass(self.dp.goku.pull_car(), 0, 20, 1)
            self.un1.set_train(stationid) 
        if tc.timesig(5,22, hour, min) == True:
            del self.un2
            self.un2 = tr.UnyouClass(self.dp.E04B.pull_car(),0, 5, 2)
            self.un2.set_train(stationid)
        if tc.timesig(5,8, hour, min) == True:
            del self.un3
            self.un3 = tr.UnyouClass(self.dp.T05A.pull_car(),self.dp.T05B.pull_car(), 5, 3)
            self.un3.set_train(stationid)
        if tc.timesig(5,14, hour, min) == True:
            del self.un4
            self.un4 = tr.UnyouClass(self.dp.T26A.pull_car(),self.dp.T26B.pull_car(), 26, 4)
            self.un4.set_train(stationid)
        if tc.timesig(5,34, hour, min) == True:
            del self.un5
            self.un5 = tr.UnyouClass(self.dp.E01.pull_car(),0, 26, 5)
            self.un5.set_train(stationid)
        if tc.timesig(5,18, hour, min) == True:
            del self.un6
            self.un6 = tr.UnyouClass(self.dp.T15A.pull_car(),self.dp.T15B.pull_car(), 15, 6)
            self.un6.set_train(stationid)

        if tc.timesig(6, 48, hour, min) == True:
            self.un1.add_cars(11, self.dp.goku.pull_car(), stationid)

        if tc.timesig(7, 21, hour, min) == True:
            self.un2.add_cars(20,self.dp.goku.pull_car(), stationid)

        if tc.timesig(7, 44, hour, min) == True:
            self.un5.add_cars(11,self.dp.goku.pull_car(), stationid)

        if tc.timesig(23, 45, hour, min) == True:
            self.un6.add_cars(20,self.dp.Gtemp.pull_car(), stationid)

        if tc.timesig(19, 10, hour, min) == True:
            self.dp.goku.push_cars(self.un6.change_all_cars(11, self.dp.goku.pull_car(), stationid))

        if tc.timesig(18,  14, hour, min) == True:
            self.dp.goku.push_car(self.un2.parge_cars(11, stationid))

        if tc.timesig(20,  1, hour, min) == True:
            self.dp.E04B.push_car(self.un1.parge_cars(26, stationid))

        if tc.timesig(18, 56, hour, min) == True:
            self.dp.goku.push_car(self.un5.parge_cars(11, stationid))

        if tc.timesig(22,50, hour, min) == True:
            self.un1.out_train(stationid,26,self.dp.E01,'')
        if tc.timesig(23,41, hour, min) == True:
            self.un2.out_train(stationid,11,self.dp.goku,'')
        if tc.timesig(23,53, hour, min) == True:
            self.un3.out_train(stationid,15,self.dp.T15A,self.dp.T15B)
        if tc.timesig(23,50, hour, min) == True:
            self.un4.out_train(stationid,5,self.dp.T05A,self.dp.T05B)
        if tc.timesig(21,44, hour, min) == True:
            self.un5.out_train(stationid,20,self.dp.goku,'')
        if tc.timesig(23,59, hour, min) == True:
            self.un6.out_train(stationid,26,self.dp.T26A,self.dp.T26B)
            self.delete_depot()
    
        if tc.timesig(24,0, hour, min) == True:
            self.delete_depot()

        if tc.timesig(11, 00, hour, min) == True:
            # 1から6までの運用を出力する。
            self.output_unyo()
            pass