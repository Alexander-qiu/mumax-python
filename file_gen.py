from hashlib import new
from operator import ne
import os
from shutil import copyfile


def Mumax3_simulation_gen(path_basic, filename, path_out, 
                          current_start, current_scale, num_current,
                          angle_start, angle_scale, num_angle):
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print("%%filewrite")
    

    file_read = path_basic + "/"+ filename
    old_current = "jc:=10e10"
    # old_B = "B_affix:=0.01"
    old_angle = "angle:=1"


    for i in range(num_current+1):
        for j in range(num_angle+1):
            file_out = path_out + 'GEN' + str(i) + '-' + str(j) + ".mx3"
            copyfile(file_read, file_out)
            aimCurrent = i * current_scale + current_start
            aimAngle = angle_start + j * angle_scale 
            new_current = "jc:=" + str(aimCurrent) + "e10" 
            new_angle = "angle:=" + str(aimAngle)
            # print(new_current + " " + new_angle)
            
            with open(file_read, "r") as f1, open(file_out, "w") as f2:
                for line in f1:
                    if old_current in line:
                        line = line.replace(old_current, new_current)
                    if old_angle in line:
                        line = line.replace(old_angle, new_angle)
                    f2.write(line)

    return 





