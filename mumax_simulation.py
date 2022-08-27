# call Mumax to simulate
# Writen by Alexander Qiu, 07/24, 2022
import os
import mumax3_read

def Mumax_simulation(pathBasic, filename, pathOut):
    print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
    print('%% Partner with Mumax 3.0')
    print('%% Ruizhi_qiu@foxmail.com')
    print('%% version1.0 20/03/2022')
    print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')

    print('Begin to calculate...')
    print('-------------------------------------------------------------------')
    print('-------------------------Simulation1---------------------------------')
    # begin to simulate
    # fileDir = 'mumax3 ' + pathBasic + filename + '.mx3'
    fileSimulationName = pathBasic + filename
    fileDir = 'mumax3 ' +  fileSimulationName

    print("仿真指令：")
    print(fileDir)
    os.system(fileDir)
    
    cpShell = 'cp '+ pathBasic + filename + '.out  ' + pathOut
    os.system(cpShell)
    print("cp shell bash exc")
    print(cpShell)
    
    
    
    # mvShell = 'mv '+ pathBasic + filename+ '.out  ' + pathOut
    # os.system(mvShell)
    # print("mv shell bash exc")
    # print(mvShell)
    
    fileSimulationNameout =fileSimulationName.replace(".mx3",".out/")
    [t, mx, my, mz] = mumax3_read.Mumax3_read(fileSimulationNameout)
    print('-------------------------------------------------------------------')
    print(filename)
    print('End of Simulation!!!')
    print('-------------------------------------------------------------------')
    
    End_mz = mz[len(mz) - 10]
    
    return End_mz