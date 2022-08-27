# encoding:utf-8
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def Mumax3_plot(path):
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
    plt.figure()
    m_x = plt.plot(t, mx, color='red', linewidth=1.0,)
    m_y = plt.plot(t, my, color='green', linewidth=1.0, linestyle='--')
    m_z = plt.plot(t, mz, color='blue', linewidth=1.0, linestyle='-')
    plt.xlabel('t(ns)')
    plt.ylabel('m')
    plt.ylim((-1.2, 1.2))
    plt.legend(handles=[m_x, m_y, m_z], labels=['m_x', 'm_y', 'm_z'])
    plt.savefig("./m-t_fig_"+path+".jpg", dpi=300, bbox_inches='tight')

    plt.figure()
    ax1 = plt.axes(projection='3d')
    ax1.plot3D(mx, my, mz, 'red')  # 绘制空间曲线
    plt.savefig("./3D_sphere.jpg", dpi=300, bbox_inches='tight')
    plt.show()

    print("\033[31m t: \033[0m")
    for j in range(len(t)):
        if j % 1 ==  0:
            print(t[j])
            
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

    

def create_sphere(cx,cy,cz, r, resolution=360):
    '''
    create sphere with center (cx, cy, cz) and radius r
    '''
    phi = np.linspace(0, 2*np.pi, 2*resolution)
    theta = np.linspace(0, np.pi, resolution)

    theta, phi = np.meshgrid(theta, phi)

    r_xy = r*np.sin(theta)
    x = cx + np.cos(phi) * r_xy
    y = cy + np.sin(phi) * r_xy
    z = cz + r * np.cos(theta)

    return np.stack([x,y,z])



def mumax3_plot_test():

    x = np.linspace(-1, 1, 50)
    y1 = 2 * x + 1
    y2 = x ** 2

    plt.figure()
    plt.plot(x, y1)
    plt.savefig("./1.jpg")

    plt.figure()
    plt.scatter(x, y2)
    plt.savefig("./2.jpg")

    plt.figure()
    plt.plot([0, 1], [3, 5])
    plt.savefig("./3.jpg")
    plt.show()

    print("绘图模块调用成功")