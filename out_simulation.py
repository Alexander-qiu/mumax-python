# encoding:utf-8
import mumax_simulation
import mumax3_plot_5
import mumax3_read
import os

pathBasic =  os.getcwd() + '/'
file = 'z_added_test-0822'
filename =  file + '.mx3'
pathOut = '/hy-tmp/'
print(pathBasic)

End_mz = mumax_simulation.Mumax_simulation(pathBasic=pathBasic, filename=filename, pathOut=pathOut)
print(End_mz)
pathOrigin = pathBasic + file + '.out/'
pathSimulation = pathOut + file + '.out/'  

# mumax3_plot.Mumax3_plot(pathOrigin)
mumax3_plot_5.Mumax3_plot_5(pathOrigin, file)
# mumax3_read.Mumax3_read()

# ssh -p 38224 root@region-3.autodl.com
# Bb0T3+eTwm

