from numpy import pi, sin, sinh, cos, arange, subtract, around, exp, insert
import matplotlib.pyplot as plt
from config import *
import pickle

fig = plt.figure()
fig.set_size_inches(12, 7)
errorplot = fig.add_subplot(111)

time = arange(0,fulltime+timestep,timestep)

with open('../output/error_et='+str(eltype)+'_dof='+str(2*elnum+1)+'_dt=0.1.dump', 'rb') as f:
    error1 = pickle.load(f)
with open('../output/error_et='+str(eltype)+'_dof='+str(2*elnum+1)+'_dt=1.dump', 'rb') as f:
    error2 = pickle.load(f)
with open('../output/error_et='+str(eltype)+'_dof='+str(2*elnum+1)+'_dt=5.dump', 'rb') as f:
    error3 = pickle.load(f)

errorplot.plot(time,error1,marker='o',label="$Error$ $DELTIM = 0.1$",linestyle='--',linewidth=0, color='r',markersize=10)
errorplot.plot(time,error2,marker='o',label="$Error$ $DELTIM = 1.0$",linestyle='--',linewidth=0, color='g',markersize=10)
errorplot.plot(time,error3,marker='o',label="$Error$ $DELTIM = 5.0$",linestyle='--',linewidth=0, color='b',markersize=10)

errorplot.set_xlabel("$time, s$", fontsize=20)
errorplot.set_ylabel("$ΔT, C^o$", fontsize=20)
errorplot.legend(loc='best',fontsize=15)
errorplot.grid()
errorplot.set_title('$Error$ $vs$ $Time$ DOF='+str(2*elnum+1),fontsize=20)
filename = '../output/plots/error_v_time_et='+str(eltype)+'_dof='+str(2*elnum+1)+'.png'
fig.savefig(filename)