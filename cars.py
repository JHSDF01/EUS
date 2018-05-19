#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# Un6 = entry_cars(9, 24, 305, 1001)
#　みたいな書き方をしていく
# Un6 は　藤沢・鎌倉の1次元2要素の配列




def entry_cars(hour,sec,fuji,kama):
    #始発運用に車両を登録する場合
    train=[]
    if car is None:
        train[0]= fuji
        train[1]= kama
    else:
        print("error")
    return train

def add_cars(ud, car, train):
    #単行に出庫車を連結する場合
    if ud == 'd':
        train.append(car)
    else:
        #train[0] = train[1]
        #train[0] = car
        train[0],train[1] = car, train[0]
    return train


def parge_cars(ud, train, car):
    #重連を開放して入庫する場合
    if ud == 'd':
        train[0] = train[1]
        del train[1]
    else:
        del train[1]
    return train


def change_cars(ud, car, train):
    #重連の前に2両を連結し、後ろ2両を開放する場合
    if ud == 'd':
        #train[0] = train[1]
        #train[1] = car
        train[0],train[1] = train[1], car
    else:
        #train[1] = train[0]
        #train[0] = car
        train[0],train[1] = car, train[0]
    return train