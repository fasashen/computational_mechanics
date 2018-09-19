from numpy import pi, sin, sinh, cos, arange, subtract, around, exp, insert
import matplotlib.pyplot as plt
from config import *
import pickle

fig2 = plt.figure()
fig2.set_size_inches(12, 7)
time20_plot = fig2.add_subplot(111)

with open( '../output/time200_dof5.dump', 'rb') as f:
    time20_1 = pickle.load(f)
with open( '../output/time200_dof9.dump', 'rb') as f:
    time20_2 = pickle.load(f)
with open( '../output/time200_dof33.dump', 'rb') as f:
    time20_3 = pickle.load(f)
with open( '../output/time200_dof129.dump', 'rb') as f:
    time20_4 = pickle.load(f)
with open( '../output/time200_dof185.dump', 'rb') as f:
    time20_5 = pickle.load(f)

time20_plot.plot(5,time20_1,marker='o',label="$DOF = 5$",linewidth=0, color='r',markersize=10)
time20_plot.plot(9,time20_2,marker='o',label="$DOF = 9$",linewidth=0, color='g',markersize=10)
time20_plot.plot(33,time20_3,marker='o',label="$DOF = 33$",linewidth=0, color='b',markersize=10)
time20_plot.plot(129,time20_3,marker='o',label="$DOF = 129$",linewidth=0, color='gray',markersize=10)
time20_plot.plot(185,time20_3,marker='o',label="$DOF = 185$",linewidth=0, color='k',markersize=10)

time20_plot.set_xscale('symlog')

time20_plot.set_xlabel("$DOF$", fontsize=20)
time20_plot.set_ylabel("$T, C^o$", fontsize=20)
time20_plot.legend(loc='lower right',fontsize=15,numpoints=1)
time20_plot.grid()
time20_plot.set_ylim(185, 186.5)
time20_plot.set_title('$Temp | 140 sec$ $vs$ $DOF$ \n $(dt = 1)$',fontsize=20)
filename = '../output/plots/Temp140secConvergence.png'
fig2.savefig(filename)