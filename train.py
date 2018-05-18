#!/usr/bin/python3
# -*- coding: UTF-8 -*-

#列車と運用についてのデータを定義する

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
