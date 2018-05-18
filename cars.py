#!/usr/bin/python3
# -*- coding: UTF-8 -*-

def entry_cars(houe,sec,unyo_number,fuji,kama):
    car=[]
    if car is None:
        car[0]= fuji
        car[1]= kama
    return car

def add_cars(ud, car, train):
    #単行に出庫車を連結する場合
    if ud = 'd':
        train[1] = car
    else:
        train[0] = train[1]
        train[0] = car
        pass


def parge_cars(ud, train, car):
    #重連を開放して入庫する場合
    if ud = 'd':
        train[0] = train[1]
        del train[1]
    else:
        del train[1]
        pass


def change_cars(ud, car, train):
    #重連の前に2両を連結し、後ろ2両を開放する場合
    if ud = 'd':
        train
        train[0] = train[1]
        train[1] = car
    else:
        train[1] = train[0]
        train[0] = car
        pass