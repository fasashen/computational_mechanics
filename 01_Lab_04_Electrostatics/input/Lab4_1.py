from numpy import pi, sin, sinh, cos, arange, subtract, around
import matplotlib.pyplot as plt
from config_1 import *
import pickle

def T(r,phi):
    summ = 0
    for n in range(1,10):
        m = 2*n-1
        add = ((r/a)**m-(a/r)**m)*sin(m*phi)/((b/a)**m-(a/b)**m)/m
        summ += add
    return 4*U0/pi*summ   

def get_path_data(comp):
    s = []
    file = ''
    if comp == 'r':
        file += '../output/rpath_temp.txt'
    elif comp == 'c':
        file += '../output/cpath_temp.txt'
    with open(file) as path_txt:
        for line in path_txt.readlines()[5:16]:
            s.append(line[14:])
    return [float(i) for i in s]

def asym(data):
    data_asym = [-x for x in data]
    for i, x in enumerate(data_asym):
        data.append(data_asym[-1*i-1])
    return data

#Getting analyt sol and reading data from ansys:
r = list(arange(a,b,0.0006))
r_sm = list(arange(a,b+0.0001,0.0001)) #for smooth line plot
phi = asym(list(arange(90/360*2*pi,(1-11.125)/360*2*pi,(-11.125)/360*2*pi)))
phi_sm = asym(list(arange(90/360*2*pi,(1-0.5)/360*2*pi,-0.5/360*2*pi))) #for smooth line plot

ctemp_cae = asym(get_path_data('c'))
rtemp_cae1 = get_path_data('r')
rtemp_cae2 = [-x for x in rtemp_cae1]

ctemp_an = []
ctemp_an_sm = []

rtemp_an1 = []
rtemp_an2 = []
rtemp_an1_sm = []
rtemp_an2_sm = []
for p in phi:
    ctemp_an.append(T(r_c,p))
for p in phi_sm:
    ctemp_an_sm.append(T(r_c,p))    
for p in r:
    rtemp_an1.append(T(p,(90-4*deg_step)/360*2*pi))
    rtemp_an2.append(T(-p,(90-4*deg_step)/360*2*pi))
for p in r_sm:
    rtemp_an1_sm.append(T(p,(90-4*deg_step)/360*2*pi))
    rtemp_an2_sm.append(T(-p,(90-4*deg_step)/360*2*pi))

test=[]
for i, x in enumerate(ctemp_an):
    test.append((ctemp_an[i]-ctemp_cae[i])/ctemp_an[i])
print(test)

#Plots:
dof = (2*elnum+2)*(elnum+1)
fig = plt.figure()
fig.suptitle(lab_name+': dof'+ str(dof)+', plane' + str(eltype) )
fig.set_size_inches(10.0, 10.0)

radial_plot = fig.add_subplot(211)
radial_plot.axhline(y=0, color='k',linewidth=0.5)
radial_plot.set_title('$\phi = \pi/2,a<r<b$')
radial_plot.set_xlabel("$r, m$",fontsize=15)
radial_plot.set_ylabel("$U, V$",fontsize=15)
radial_plot.set_xlim(a, b)
radial_plot.grid()
radial_plot.plot(r_sm,rtemp_an1_sm,'-k')
radial_plot.plot(r,rtemp_an1,marker='s', label="$Analytical$ $Solution$",linewidth=0, color='k', markersize=8, mew=1,fillstyle='none')
radial_plot.plot(r,rtemp_cae1,linestyle='-',marker='o', label="$CAE$ $Solution$ $\phi = \pi/2$",linewidth=0, color='r',markersize=6, mew=0)
radial_plot.plot(r_sm,rtemp_an2_sm,'-k')
radial_plot.plot(r,rtemp_an2,marker='s',linewidth=0, color='k', markersize=8, mew=1,fillstyle='none')
radial_plot.plot(r,rtemp_cae2,linestyle='-',marker='o', label="$CAE$ $Solution$ $\phi = -\pi/2$",linewidth=0, color='b',markersize=6, mew=0)
radial_plot.legend(loc='best',fontsize=12,numpoints=1)

circle_plot = fig.add_subplot(212)
circle_plot.axhline(y=0, color='k',linewidth=0.5)
circle_plot.axvline(x=0, color='k',linewidth=0.5)
circle_plot.set_title('$r = (a+b)/2, 0<\phi<\pi/2$')
circle_plot.set_xlabel("$\phi, rad$",fontsize=15)
circle_plot.set_ylabel("$U, V$",fontsize=15)
circle_plot.grid()
circle_plot.set_xlim(-pi/2, pi/2)
circle_plot.plot(phi_sm,ctemp_an_sm,'-k')
circle_plot.plot(phi,ctemp_an,marker='s', label="$Analytical$ $Solution$",linewidth=0, color='k', markersize=8, mew=1,fillstyle='none')
circle_plot.plot(phi,ctemp_cae,linestyle='-',marker='o', label="$CAE$ $Solution$",linewidth=0, color='g',markersize=6, mew=0)
circle_plot.legend(loc='best',fontsize=10,numpoints=1)
circle_plot.set_xticks([-0.5*pi,-0.25*pi, 0., 0.25*pi, .5*pi])
circle_plot.set_xticklabels([r"$-\frac{\pi}{2}$",r"$-\frac{\pi}{4}$","$0$", r"$\frac{\pi}{4}$", r"$\frac{\pi}{2}$"],fontsize=15)


# with open('../output/versioncounter', 'rb') as f:
#     version = pickle.load(f)
# with open('../output/versioncounter', 'wb') as f:
#     version += 1
#     pickle.dump(version, f)

filename = '../output/plots/'+lab_name+'_plots[dof' +str(dof)+ ', et'+ str(eltype) + '].png'
fig.savefig(filename, dpi=300)

#Errors:
c_err = abs(subtract(ctemp_an,ctemp_cae))
r_err = abs(subtract(rtemp_an1,rtemp_cae1))
max_c_err = max(c_err)
max_r_err = max(r_err)

with open('../output/temp_'+lab_name+'_c_err[et='+str(eltype)+'_dof'+str(dof)+'].dump', 'wb') as f:
    pickle.dump(c_err, f)
with open('../output/temp_'+lab_name+'_r_err[et='+str(eltype)+'_dof'+str(dof)+'].dump', 'wb') as f:
    pickle.dump(r_err, f)


with open('../output/temp_'+lab_name+'_c_temp[et='+str(eltype)+'_dof'+str(dof)+'].dump', 'wb') as f:
    pickle.dump(ctemp_cae[-2], f)
with open('../output/temp_'+lab_name+'_r_temp[et='+str(eltype)+'_dof'+str(dof)+'].dump', 'wb') as f:
    pickle.dump(rtemp_cae1[-2], f)