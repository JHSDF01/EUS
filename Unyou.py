#!/usr/bin/python3
# -*- coding: UTF-8 -*-
unyo_file = 'unyo_20171107.txt'
unyo = []
def inputunyo(unyo_file):
    with open(unyo_file, 'r', coding = 'utf-8') as uf:
        reader = uf.readline()
        for row in reader:
            unyo.append(row)
    return unyo

def move():
    #列車の位置を移動させるための関数。12分ごとに上り下りの列車を移動させていく
    #各運番が格納する座標と車両のうち座標に手を付けるつもりなのでvoid型でいいよね・・・？
    return

def print_train():
    #TODOに書いたような列車位置を描画する。アニメーションは500ms程度で動くのがよいだろう
    #
    return