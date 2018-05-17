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
    
    return

def print_train():
