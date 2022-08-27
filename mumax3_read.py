# encoding:utf-8
import numpy as np
import os

def Mumax3_read(path):
    data_txt = path + 'table.txt'
    f = open(data_txt)
    data = f.readlines()  # 逐行读取txt并存成list。每行是list的一个元素，数据类型为str
    print(len(data))
    l = []
    mx = []
    my = []
    mz = []
    t = []
    for i in range(len(data)):  # len(data)为数据行数
        spilt_data = data[i].split()
        # print(spilt_data)
        if i > 0:
            t.append(float(spilt_data[0])*1e9)
            mx.append(float(spilt_data[1]))
            my.append(float(spilt_data[2]))
            mz.append(float(spilt_data[3]))
        # else:
        #     t.append('t')
        #     mx.append('mx')
        #     my.append('my')
        #     mz.append('mz')

    # show the correct
    print("\033[31m mx: \033[0m")
    for j in range(len(mx)):
        if j % 1 == 0:
            print(mx[j])

    print("\033[31m my: \033[0m")
    for j in range(len(my)):
        if j % 1 == 0:
            print(my[j])

    print("\033[31m mz: \033[0m")
    for j in range(len(mz)):
        if j % 1 == 0:
            print(mz[j])

    print("\033[31m t: \033[0m")
    for j in range(len(t)):
        if j % 1 ==  0:
            print(t[j])

    return[t, mx, my, mz]


