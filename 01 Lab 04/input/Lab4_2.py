from numpy import pi, sin, cos, arange, subtract
import matplotlib.pyplot as plt
from config_2 import *
import pickle

def T(r,phi):
    if r <= a:
        A = 2/(m+1)
    else:    
        A = (1-(m-1)/(m+1)*(a/r)**2)
    return -H*r*cos(phi)*A

def get_path_data(comp):
    files = {'phi1':'phi1_temp.txt','phi2':'phi2_temp.txt','phi3':'phi3_temp.txt','r1':'r1_temp.txt','r2':'r2_temp.txt'}
    s = []
    with open('../output/'+files[comp]) as path_txt:
        for line in path_txt.readlines()[5:16]:
            s.append(line[13:])
    return [float(i) for i in s]

#Getting analyt sol and reading data from ansys:
r_1 = list(arange(0,a+a/4,a/4)) #axis 0<r<a
r_1_sm = list(arange(0,a+a/16,a/16))  #smooth axis 0<r<a
r_2 = list(arange(a,11*a,a)) #axis a<r<10a
r_2_sm = list(arange(a,10*a+a/10,a/10)) #smooth axis a<r<10a
phi = [x/360*2*pi for x in list(arange(0,90+90/4,90/4))] #axis 0<phi<pi/2
phi_sm = [x/360*2*pi for x in list(arange(0,90+90/16,90/16))] #smooth axis 0<phi<pi/2

phi1_cae = get_path_data('phi1')
phi2_cae = get_path_data('phi2')
phi3_cae = get_path_data('phi3')
r1_cae = get_path_data('r1')
r2_cae = get_path_data('r2')

phi1_an, phi2_an, phi3_an = [], [], []
phi1_an_sm, phi2_an_sm, phi3_an_sm = [], [], []
r1_an, r1_an_sm = [], []
r2_an, r2_an_sm = [], []

for p in phi:
    phi1_an.append(T(r1,p))
    phi2_an.append(T(r2,p))
    phi3_an.append(T(r3,p))
for p in phi_sm:
    phi1_an_sm.append(T(r1,p))
    phi2_an_sm.append(T(r2,p))
    phi3_an_sm.append(T(r3,p))
for x in r_1:
    r1_an.append(T(x,0))
for x in r_1_sm:
    r1_an_sm.append(T(x,0))
for x in r_2:
    r2_an.append(T(x,0))
for x in r_2_sm:
    r2_an_sm.append(T(x,0))

#Plots:
dof = {4:69, 8:241, 16:897, 32:3457, 64:13569, 128:53761}
dof = dof[elnum]

fig = plt.figure()
fig.suptitle(lab_name+': dof'+ str(dof)+', plane' + str(eltype) )
fig.set_size_inches(20.0, 12.0)

radial_plot1 = fig.add_subplot(221)
radial_plot1.set_title('$f=U(r,0), 0<r<a$')
radial_plot1.set_xlabel("$r, m$",fontsize=15)
radial_plot1.set_ylabel("$U, H$",fontsize=15)
radial_plot1.set_xlim(0, a)
radial_plot1.grid()
radial_plot1.plot(r_1_sm,r1_an_sm,'-k')
radial_plot1.plot(r_1,r1_an,marker='s', label="$Analytical$ $Solution$",linewidth=0, color='k', markersize=8, mew=1,fillstyle='none')
radial_plot1.plot(r_1,r1_cae,linestyle='-',marker='o', label="$CAE$ $Solution$ $\phi = \pi/2$",linewidth=0, color='r',markersize=6, mew=0)
radial_plot1.legend(loc='best',fontsize=12,numpoints=1)


radial_plot2 = fig.add_subplot(222)
radial_plot2.set_title('$f=U(r,0), a<r<10a$')
radial_plot2.set_xlabel("$r, m$",fontsize=15)
radial_plot2.set_ylabel("$U, H$",fontsize=15)
radial_plot2.set_xlim(a, 10*a)
radial_plot2.grid()
radial_plot2.plot(r_2_sm,r2_an_sm,'-k')
radial_plot2.plot(r_2,r2_an,marker='s', label="$Analytical$ $Solution$",linewidth=0, color='k', markersize=8, mew=1,fillstyle='none')
radial_plot2.plot(r_2,r2_cae,marker='o', label="$CAE$ $Solution$ $\phi = \pi/2$",linewidth=0, color='r',markersize=6, mew=0)
radial_plot2.legend(loc='best',fontsize=12,numpoints=1)

circle_plot1 = fig.add_subplot(223)
circle_plot1.axhline(y=0, color='k',linewidth=0.5)
circle_plot1.axvline(x=0, color='k',linewidth=0.5)
circle_plot1.set_title('$f_1=U(a/2,\phi), f_2=U(a,\phi), 0<\phi<\pi/2$')
circle_plot1.set_xlabel("$\phi, rad$",fontsize=15)
circle_plot1.set_ylabel("$U, H$",fontsize=15)
circle_plot1.grid()
circle_plot1.set_xlim(0, pi/2)
circle_plot1.plot(phi_sm,phi1_an_sm,'-k')
circle_plot1.plot(phi_sm,phi2_an_sm,'-k')
circle_plot1.plot(phi,phi1_an,marker='s',linewidth=0, color='k', markersize=8, mew=1,fillstyle='none')
circle_plot1.plot(phi,phi2_an,marker='s', label="$Analytical$ $Solution$",linewidth=0, color='k', markersize=8, mew=1,fillstyle='none')
circle_plot1.plot(phi,phi1_cae,marker='o', label="$CAE$ $Solution$ $r = a/2$",linewidth=0, color='r',markersize=6, mew=0)
circle_plot1.plot(phi,phi2_cae,marker='o', label="$CAE$ $Solution$ $r = a$",linewidth=0, color='b',markersize=6, mew=0)
circle_plot1.legend(loc='best',fontsize=10,numpoints=1)
circle_plot1.set_xticks([0., 0.125*pi, 0.25*pi,0.375*pi, .5*pi])
circle_plot1.set_xticklabels(["$0$", r"$\frac{\pi}{8}$", r"$\frac{\pi}{4}$", r"$\frac{3\pi}{8}$", r"$\frac{\pi}{2}$"],fontsize=20)

circle_plot2 = fig.add_subplot(224)
circle_plot2.axhline(y=0, color='k',linewidth=0.5)
circle_plot2.axvline(x=0, color='k',linewidth=0.5)
circle_plot2.set_title('$f=U(2a,\phi), 0<\phi<\pi/2$')
circle_plot2.set_xlabel("$\phi, rad$",fontsize=15)
circle_plot2.set_ylabel("$U, H$",fontsize=15)
circle_plot2.grid()
circle_plot2.set_xlim(0, pi/2)
circle_plot2.plot(phi_sm,phi3_an_sm,'-k')
circle_plot2.plot(phi,phi3_an,marker='s', label="$Analytical$ $Solution$",linewidth=0, color='k', markersize=8, mew=1,fillstyle='none')
circle_plot2.plot(phi,phi3_cae,linestyle='-',marker='o', label="$CAE$ $Solution$",linewidth=0, color='g',markersize=6, mew=0)
circle_plot2.legend(loc='best',fontsize=10,numpoints=1)
circle_plot2.set_xticks([0., 0.125*pi, 0.25*pi, 0.375*pi, .5*pi])
circle_plot2.set_xticklabels(["$0$", r"$\frac{\pi}{8}$", r"$\frac{\pi}{4}$",r"$\frac{3\pi}{8}$", r"$\frac{\pi}{2}$"],fontsize=20)

# with open('../output/versioncounter', 'rb') as f:
#     version = pickle.load(f)
# with open('../output/versioncounter', 'wb') as f:
#     version += 1
#     pickle.dump(version, f)

filename = '../output/plots/'+lab_name+'_plots[dof' +str(dof)+ ', et'+ str(eltype) + ']_.png'
fig.savefig(filename, dpi=300)

#Errors:
r1_err = abs(subtract(r1_an,r1_cae))
r2_err = abs(subtract(r2_an,r2_cae))
phi1_err = abs(subtract(phi1_an,phi1_cae))
phi2_err = abs(subtract(phi2_an,phi2_cae))
phi3_err = abs(subtract(phi3_an,phi3_cae))

r_err = [r1_err, r2_err]
phi_err = [phi1_err, phi2_err, phi3_err]

with open('../output/temp_'+lab_name+'_r_err[et='+str(eltype)+'_dof'+str(dof)+'].dump', 'wb') as f:
    pickle.dump(r_err, f)
with open('../output/temp_'+lab_name+'_phi_err[et='+str(eltype)+'_dof'+str(dof)+'].dump', 'wb') as f:
    pickle.dump(phi_err, f)

with open('../output/temp_'+lab_name+'_phi_conv[et='+str(eltype)+'_dof'+str(dof)+'].dump', 'wb') as f:
    pickle.dump(phi3_cae, f)


test = []
for i, x in enumerate(phi1_err):
    test.append(x/phi1_an[i]*100)
print(test)
test = []
for i, x in enumerate(phi2_err):
    test.append(x/phi2_an[i]*100)
print(test)
test = []
for i, x in enumerate(phi3_err):
    test.append(x/phi3_an[i]*100)
print(test)