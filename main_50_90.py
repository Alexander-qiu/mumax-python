# This code is use to call mumax3
# Writen by Alexander Qiu, 07/24, 2022
import matplotlib.pyplot as plt
import mumax3_plot
import os
import file_gen
from mumax_simulation_gpu1 import Mumax_simulation_gpu1
import mumax3_read

# Press the green button in the gutter to run the script.
def mkdir(path):
    folder = os.path.exists(path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print
        "---  new folder...  ---"
        print
        "---  OK  ---"

    else:
        print
        "---  There is this folder!  ---"


if __name__ == '__main__':

    plt.close('all') 
    file1 = os.getcwd() + "/test.txt"
    filename = "z_added_0826.mx3"
    pathBasic = os.getcwd()
    pathOut = os.getcwd() + "/mumax3Gen_40_90/"
    pathStorage = '/hy-tmp/ruizhi/'
    
    
    path = pathBasic + filename + '.out/'
    mkdir(pathOut)
    print(pathOut)

    # 批量生成文件
    current_start = 0.1
    current_scale = 2.5
    num_current = 10

    # num_current = 70;
    angle_start = 40.1
    angle_scale = 5
    num_angle = int((91 - angle_start) / angle_scale)

    
    if not os.path.exists(pathOut):
        os.makedirs(pathOut)
    print(file1)
    if not os.path.exists(pathStorage):
        os.makedirs(pathStorage)
    print(pathStorage)
    
    
    # alter(file1, "python", "测试", pahtOut, "/testOut.txt")
    # 生成仿真文件
    file_gen.Mumax3_simulation_gen(pathBasic, filename, pathOut, 
                          current_start, current_scale, num_current,
                          angle_start, angle_scale, num_angle)
    
    fileName = os.listdir(pathOut)
    path_simulation = pathOut
    print("文件名")
    print(fileName)
    End_mz_list = []
    for i in range(len(fileName)):
        End_mz = Mumax_simulation_gpu1(pathBasic=path_simulation,
                                  filename=fileName[i],
                                  pathOut=pathStorage)
        End_mz_list.append(End_mz)
    
    with open('45.1_90.1_simualtion.csv', 'w', newline='') as student_file:
        writer = csv.writer(student_file)
        # writer.writerow(["RollNo", "Name", "Subject"])
        for i in range(len(End_mz_list)):
            writer.writerow(End_mz_list[i])
