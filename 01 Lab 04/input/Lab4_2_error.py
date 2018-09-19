from numpy import pi, sin, sinh, cos, arange, subtract, around, exp, insert
import matplotlib.pyplot as plt
from config_2 import *
import pickle

r_1 = list(arange(0,a+a/4,a/4)) #axis 0<r<a
r_2 = list(arange(a,11*a,a)) #axis a<r<10a
phi = [x/360*2*pi for x in list(arange(0,90+90/4,90/4))] #axis 0<phi<pi/2

with open('../output/temp_lab4_2_r_err[et='+str(eltype)+'_dof69].dump', 'rb') as f:
    r_err4 = pickle.load(f)
with open('../output/temp_lab4_2_r_err[et='+str(eltype)+'_dof241].dump', 'rb') as f:
    r_err8 = pickle.load(f)
with open('../output/temp_lab4_2_r_err[et='+str(eltype)+'_dof897].dump', 'rb') as f:
    r_err16 = pickle.load(f)
with open('../output/temp_lab4_2_r_err[et='+str(eltype)+'_dof3457].dump', 'rb') as f:
    r_err32 = pickle.load(f)

with open('../output/temp_lab4_2_phi_err[et='+str(eltype)+'_dof69].dump', 'rb') as f:
    phi_err4 = pickle.load(f)
with open('../output/temp_lab4_2_phi_err[et='+str(eltype)+'_dof241].dump', 'rb') as f:
    phi_err8 = pickle.load(f)
with open('../output/temp_lab4_2_phi_err[et='+str(eltype)+'_dof897].dump', 'rb') as f:
    phi_err16 = pickle.load(f)
with open('../output/temp_lab4_2_phi_err[et='+str(eltype)+'_dof3457].dump', 'rb') as f:
    phi_err32 = pickle.load(f)

fig = plt.figure()
fig.set_size_inches(20, 10)
c_err = fig.add_subplot(221)
c_err.plot(r_1,r_err4[0],marker='o',label="$Error$ $dof = 69$",linestyle='--',linewidth=1, color='r',markersize=8)
c_err.plot(r_1,r_err8[0],marker='o',label="$Error$ $dof = 241$",linestyle='--',linewidth=1, color='g',markersize=8)
c_err.plot(r_1,r_err16[0],marker='o',label="$Error$ $dof = 897$",linestyle='--',linewidth=1, color='b',markersize=8)
c_err.plot(r_1,r_err32[0],marker='o',label="$Error$ $dof = 3457$",linestyle='--',linewidth=1, color='y',markersize=8)
c_err.set_xlabel("$r, m$",fontsize=15)
c_err.set_ylabel("$U, H$",fontsize=15)
c_err.legend(loc='best',fontsize=15,numpoints=1)
c_err.grid()
c_err.set_title('$Error$ $vs$ $r,$ $0<r<a$',fontsize=20)

c_err = fig.add_subplot(222)
c_err.plot(r_2,r_err4[1],marker='o',label="$Error$ $dof = 69$",linestyle='--',linewidth=1, color='r',markersize=8)
c_err.plot(r_2,r_err8[1],marker='o',label="$Error$ $dof = 241$",linestyle='--',linewidth=1, color='g',markersize=8)
c_err.plot(r_2,r_err16[1],marker='o',label="$Error$ $dof = 897$",linestyle='--',linewidth=1, color='b',markersize=8)
c_err.plot(r_2,r_err32[1],marker='o',label="$Error$ $dof = 3457$",linestyle='--',linewidth=1, color='y',markersize=8)
c_err.set_xlabel("$r, m$",fontsize=15)
c_err.set_ylabel("$U, H$",fontsize=15)
c_err.legend(loc='best',fontsize=15,numpoints=1)
c_err.grid()
c_err.set_title('$Error$ $vs$ $r,$ $a<r<10a$',fontsize=20)

c_err = fig.add_subplot(223)
c_err.plot(phi,phi_err4[0],marker='x',label="$Error$ $r = a/2$ $dof = 69$",linestyle='--',linewidth=1, color='r',markersize=8,mew=2)
c_err.plot(phi,phi_err8[0],marker='x',label="$Error$ $r = a/2$ $dof = 241$",linestyle='--',linewidth=1, color='g',markersize=8,mew=2)
c_err.plot(phi,phi_err16[0],marker='x',label="$Error$ $r = a/2$ $dof = 897$",linestyle='--',linewidth=1, color='b',markersize=8,mew=2)
c_err.plot(phi,phi_err32[0],marker='x',label="$Error$ $r = a/2$ $dof = 3457$",linestyle='--',linewidth=1, color='y',markersize=8,mew=2)
c_err.plot(phi,phi_err4[1],marker='o',label="$Error$ $r = a$ $dof = 69$",linestyle='--',linewidth=1, color='r',markersize=8)
c_err.plot(phi,phi_err8[1],marker='o',label="$Error$ $r = a$ $dof = 241$",linestyle='--',linewidth=1, color='g',markersize=8)
c_err.plot(phi,phi_err16[1],marker='o',label="$Error$ $r = a$ $dof = 897$",linestyle='--',linewidth=1, color='b',markersize=8)
c_err.plot(phi,phi_err32[1],marker='o',label="$Error$ $r = a$ $dof = 3457$",linestyle='--',linewidth=1, color='y',markersize=8)
c_err.set_xlabel("$\phi, rad$",fontsize=15)
c_err.set_ylabel("$U, H$",fontsize=15)
c_err.legend(loc='best',fontsize=10,numpoints=1)
c_err.grid()
c_err.set_title('$Error$ $vs$ $\phi,$ $r=a/2, r=a$',fontsize=20)
c_err.set_xticks([0., 0.125*pi, 0.25*pi,0.375*pi, .5*pi])
c_err.set_xticklabels(["$0$", r"$\frac{\pi}{8}$", r"$\frac{\pi}{4}$", r"$\frac{3\pi}{8}$", r"$\frac{\pi}{2}$"],fontsize=20)


c_err = fig.add_subplot(224)
c_err.plot(phi,phi_err4[2],marker='o',label="$Error$ $r = a$ $dof = 69$",linestyle='--',linewidth=1, color='r',markersize=8)
c_err.plot(phi,phi_err8[2],marker='o',label="$Error$ $r = a$ $dof = 241$",linestyle='--',linewidth=1, color='g',markersize=8)
c_err.plot(phi,phi_err16[2],marker='o',label="$Error$ $r = a$ $dof = 897$",linestyle='--',linewidth=1, color='b',markersize=8)
c_err.plot(phi,phi_err32[2],marker='o',label="$Error$ $r = a$ $dof = 3457$",linestyle='--',linewidth=1, color='y',markersize=8)
c_err.set_xlabel("$\phi, rad$",fontsize=15)
c_err.set_ylabel("$U, H$",fontsize=15)
c_err.legend(loc='best',fontsize=15,numpoints=1)
c_err.grid()
c_err.set_title('$Error$ $vs$ $\phi,$ $r=2a$',fontsize=20)
c_err.set_xticks([0., 0.125*pi, 0.25*pi,0.375*pi, .5*pi])
c_err.set_xticklabels(["$0$", r"$\frac{\pi}{8}$", r"$\frac{\pi}{4}$", r"$\frac{3\pi}{8}$", r"$\frac{\pi}{2}$"],fontsize=20)

filename = '../output/plots/lab4_2_error_plots_et='+str(eltype)+'.png'
fig.savefig(filename, dpi=300)

with open('../output/temp_lab4_2_phi_conv[et='+str(eltype)+'_dof69].dump', 'rb') as f:
    phi_conv4 = pickle.load(f)
with open('../output/temp_lab4_2_phi_conv[et='+str(eltype)+'_dof241].dump', 'rb') as f:
    phi_conv8 = pickle.load(f)
with open('../output/temp_lab4_2_phi_conv[et='+str(eltype)+'_dof897].dump', 'rb') as f:
    phi_conv16 = pickle.load(f)
with open('../output/temp_lab4_2_phi_conv[et='+str(eltype)+'_dof3457].dump', 'rb') as f:
    phi_conv32 = pickle.load(f)
with open('../output/temp_lab4_2_phi_conv[et='+str(eltype)+'_dof13569].dump', 'rb') as f:
    phi_conv64 = pickle.load(f)
with open('../output/temp_lab4_2_phi_conv[et='+str(eltype)+'_dof53761].dump', 'rb') as f:
    phi_conv128 = pickle.load(f)

fig2 = plt.figure()
fig2.set_size_inches(10, 5)
c_temp = fig2.add_subplot(111)
c_temp.plot(69,phi_conv4[0],marker='o',label="$Error$ $dof = 69$",linestyle='--',linewidth=1, color='r',markersize=10)
c_temp.plot(241,phi_conv8[0],marker='o',label="$Error$ $dof = 241$",linestyle='--',linewidth=1, color='g',markersize=10)
c_temp.plot(897,phi_conv16[0],marker='o',label="$Error$ $dof = 897$",linestyle='--',linewidth=1, color='b',markersize=10)
c_temp.plot(3457,phi_conv32[0],marker='o',label="$Error$ $dof = 3457$",linestyle='--',linewidth=1, color='y',markersize=10)
c_temp.plot(13569,phi_conv64[0],marker='o',label="$Error$ $dof = 13569$",linestyle='--',linewidth=1, color='m',markersize=10)
c_temp.plot(53761,phi_conv128[0],marker='o',label="$Error$ $dof = 53761$",linestyle='--',linewidth=1, color='c',markersize=10)

c_temp.set_xlabel("$dof$",fontsize=15)
c_temp.set_ylabel("$U, H$",fontsize=15)
c_temp.set_xscale('symlog')
c_temp.legend(loc='lower right',fontsize=15,numpoints=1)
c_temp.grid()
c_temp.set_title('$r = 2a, \phi = 0$',fontsize=20)

filename = '../output/plots/lab4_2_conv_plots_et='+str(eltype)+'.png'
fig2.savefig(filename, dpi=300)