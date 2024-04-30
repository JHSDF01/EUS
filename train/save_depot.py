#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import json

'''
終電後の留置線に配置されている車両データを保存する関数
翌日のシミュレーション開始時に初期位置を決定する
基本的には、EUS_mainから受け取ったdepotクラスの在線状況をファイル出力し、
ファイル入力からdepotクラスに留置車両を定義する。
ファイルはJSONで記載する。留置車がいない場合は、default値として0を入力するようにする。
'''
def EUS_load():
    morning = {"E01": 0,"E02": 0,"E03": 0,"E04A": 0,"E04B": 0, "Gtemp": 0, "goku": 0,
        "G01A": 0,"G01B": 0,"G02A": 0,"G02B": 0,"G03": 0,"G04": 0,"G05": 0,"G06A": 0,"G06B": 0,
        "5A": 0,"5B": 0,"26A": 0,"26B": 0,"10A": 0,"10B": 0,"21A": 0,"21B": 0,"15A": 0,"15B": 0,}

    with open('save/depot_load.json') as fload:
        morning = json.load(fload)

    return morning


def EUS_save(depot_now):

    with open('save/depot_save.json', 'w') as fsave:
       json.dump(depot_now, fsave)

    return depot_now

    