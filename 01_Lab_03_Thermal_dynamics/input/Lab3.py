from numpy import pi, sin, sinh, cos, arange, subtract, around, exp, insert
import matplotlib.pyplot as plt
from config import *
import pickle

def qc(t):
    tau = k/c/ro*t        
    qc = q0*(1-exp(-pi**2*tau/a**2))
    # qc = q0
    return qc

def caeTemp(comp):
    s = [0]
    file = ''
    if comp == 'r1':
        file += '../output/temp_r1.txt'
    elif comp == 'r2':
        file += '../output/temp_r2.txt'
    elif comp == 'r3':
        file += '../output/temp_r3.txt'
    with open(file) as path_txt:
        for line in path_txt.readlines()[14:14+steps]:
            s.append(line[14:])
    return [float(i) for i in s]

def anTemp(x,step):
    g = [0, 4.49341, 7.72525, 10.9041, 14.0662, 17.2208, 20.3713, 23.5195, 26.6661, 29.8116, 32.9564]
    time = arange(0,fulltime+step,step)
    temp = []
    for t in time:
        tau = k/c/ro*t
        summ = 0
        for n in range(1,11):
            if x != 0:
                # add = (1-exp(-g[n]**2/a**2*tau))/(g[n]**2*sin(g[n]))*sin(g[n]*x/a)/x
                add = (g[n]**2*(1-exp(-pi**2/a**2*tau))-pi**2*(1-exp(-g[n]**2/a**2*tau)))/(g[n]**2*(g[n]**2-pi**2)*sin(g[n]))*sin(g[n]*x/a)/x
            else:
                # add = (1-exp(-g[n]**2/a**2*tau))/(g[n]**2*sin(g[n]))*g[n]/a
                add = (g[n]**2*(1-exp(-pi**2/a**2*tau))-pi**2*(1-exp(-g[n]**2/a**2*tau)))/(g[n]**2*(g[n]**2-pi**2)*sin(g[n]))*g[n]/a
            summ += add
        result = 3*q0/k/a*(tau-a**2/pi**2*(1-exp(-pi**2*tau/a**2)))+2*q0*a**2/k*summ    
        # result = 3*q0/k/a*tau+2*q0*a**2/k*summ
        temp.append(result)
    return temp

time = arange(0,fulltime+timestep,timestep)
temp1_cae = caeTemp('r1')
temp2_cae = caeTemp('r2')
temp3_cae = caeTemp('r3')

temp1_an = anTemp(Xp1,timestep)
temp2_an = anTemp(Xp2,timestep)
temp3_an = anTemp(Xp3,timestep)

tstep = 1
time_smooth = arange(0,fulltime+tstep,tstep)
temp1_an_smooth = anTemp(Xp1,tstep)
temp2_an_smooth = anTemp(Xp2,tstep)
temp3_an_smooth = anTemp(Xp3,tstep)
dtemp = subtract(temp1_an_smooth[1:],temp1_an_smooth[0:-1])


ddtemp = subtract(dtemp[1:],dtemp[0:-1])/tstep
# print(ddtemp)
# dtemp = temp3_an_smooth - temp3_an_smooth

error = abs(subtract(temp3_an,temp3_cae))
with open('../output/error_et='+str(eltype)+'_dof='+str(2*elnum+1)+'_dt='+str(its)+'.dump', 'wb') as f:
        pickle.dump(error, f)


time200 = temp3_cae[-1]
with open('../output/time200_dof'+str(2*elnum+1)+'.dump', 'wb') as f:
        pickle.dump(time200, f)
 


fig = plt.figure()
fig.set_size_inches(12, 7)
timeplot = fig.add_subplot(111)

timeplot.plot(time,temp1_cae,marker='o', label="$CAE$ $r=0$",linewidth=0, color='r',markersize=7, mew=0)
timeplot.plot(time,temp2_cae,marker='o', label="$CAE$ $r=a/2$", linewidth=0, color='g',markersize=7, mew=0)
timeplot.plot(time,temp3_cae,marker='o', label="$CAE$ $r=a$", linewidth=0, color='b',markersize=7, mew=0)

timeplot.plot(time,temp1_an,marker='s',fillstyle='none',label="$Analytical$",linewidth=0, color='k',markersize=15, mew=1.5)
timeplot.plot(time,temp2_an,marker='s',fillstyle='none',linewidth=0, color='k',markersize=15, mew=1.5)
timeplot.plot(time,temp3_an,marker='s',fillstyle='none',linewidth=0, color='k',markersize=15, mew=1.5)
timeplot.plot(time_smooth,temp1_an_smooth,linestyle='-',linewidth=1, color='k')
timeplot.plot(time_smooth,temp2_an_smooth,linestyle='-',linewidth=1, color='k')
timeplot.plot(time_smooth,temp3_an_smooth,linestyle='-',linewidth=1, color='k')

timeplot.set_xlabel("$time, s$", fontsize=20)
timeplot.set_ylabel("$T, C^o$", fontsize=20)
timeplot.legend(loc='upper left',fontsize=15,numpoints=1)
timeplot.grid()
timeplot.set_xlim(0, fulltime)
timeplot.set_ylim(0, 200)
timeplot.set_title('$Temperature$ $vs$ $Time$',fontsize=20)

filename = '../output/plots/TempVsTime_et='+str(eltype)+'_dof='+str(2*elnum+1)+'_dt='+str(its)+'.png'
fig.savefig(filename)
