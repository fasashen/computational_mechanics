from numpy import pi, sin, sinh, cos, arange, subtract, around, exp, insert
import matplotlib.pyplot as plt
from config_1 import *
import pickle

# dof = (2*elnum+2)*(elnum+1)
# r = arange(a,b,0.0006)
# phi = [x/360*2*pi for x in list(arange(90,-90-11.125,-11.125))]

# with open('../output/temp_lab4_1_c_err[et='+str(eltype)+'_dof50].dump', 'rb') as f:
#     c_err4 = pickle.load(f)
# with open('../output/temp_lab4_1_c_err[et='+str(eltype)+'_dof162].dump', 'rb') as f:
#     c_err8 = pickle.load(f)
# with open('../output/temp_lab4_1_c_err[et='+str(eltype)+'_dof578].dump', 'rb') as f:
#     c_err16 = pickle.load(f)
# with open('../output/temp_lab4_1_c_err[et='+str(eltype)+'_dof2178].dump', 'rb') as f:
#     c_err32 = pickle.load(f)

# with open('../output/temp_lab4_1_r_err[et='+str(eltype)+'_dof50].dump', 'rb') as f:
#     r_err4 = pickle.load(f)
# with open('../output/temp_lab4_1_r_err[et='+str(eltype)+'_dof162].dump', 'rb') as f:
#     r_err8 = pickle.load(f)
# with open('../output/temp_lab4_1_r_err[et='+str(eltype)+'_dof578].dump', 'rb') as f:
#     r_err16 = pickle.load(f)
# with open('../output/temp_lab4_1_r_err[et='+str(eltype)+'_dof2178].dump', 'rb') as f:
#     r_err32 = pickle.load(f)

# fig = plt.figure()
# fig.set_size_inches(10, 12)
# c_err = fig.add_subplot(211)
# c_err.plot(phi,c_err4,marker='o',label="$Error$ $dof = 50$",linestyle='--',linewidth=1, color='r',markersize=10)
# c_err.plot(phi,c_err8,marker='o',label="$Error$ $dof = 162$",linestyle='--',linewidth=1, color='g',markersize=10)
# c_err.plot(phi,c_err16,marker='o',label="$Error$ $dof = 278$",linestyle='--',linewidth=1, color='b',markersize=10)
# c_err.plot(phi,c_err32,marker='o',label="$Error$ $dof = 2178$",linestyle='--',linewidth=1, color='y',markersize=10)
# c_err.set_xlabel("$\phi, rad$",fontsize=15)
# c_err.set_ylabel("$U, V$",fontsize=15)
# c_err.legend(loc='best',fontsize=15,numpoints=1)
# c_err.grid()
# c_err.set_xlim(0,.5*pi)
# c_err.set_title('$Error$ $vs$ $\phi$',fontsize=20)
# c_err.set_xticks([0., 0.25*pi, .5*pi])
# c_err.set_xticklabels(["$0$", r"$\frac{\pi}{4}$", r"$\frac{\pi}{2}$"],fontsize=15)



# r_err = fig.add_subplot(212)
# r_err.plot(r,r_err4,marker='o',label="$Error$ $dof = 50$",linestyle='--',linewidth=1, color='r',markersize=10)
# r_err.plot(r,r_err8,marker='o',label="$Error$ $dof = 162$",linestyle='--',linewidth=1, color='g',markersize=10)
# r_err.plot(r,r_err16,marker='o',label="$Error$ $dof = 278$",linestyle='--',linewidth=1, color='b',markersize=10)
# r_err.plot(r,r_err32,marker='o',label="$Error$ $dof = 2178$",linestyle='--',linewidth=1, color='y',markersize=10)
# r_err.set_xlabel("$r, m$",fontsize=15)
# r_err.set_ylabel("$U, V$",fontsize=15)
# r_err.legend(loc='best',fontsize=15,numpoints=1)
# r_err.grid()
# r_err.set_title('$Error$ $vs$ $r$',fontsize=20)


# filename = '../output/plots/lab4_1_error_plots_et='+str(eltype)+'.png'
# fig.savefig(filename)

with open('../output/temp_lab4_1_c_temp[et='+str(eltype)+'_dof50].dump', 'rb') as f:
    c_temp_conv4 = pickle.load(f)
with open('../output/temp_lab4_1_c_temp[et='+str(eltype)+'_dof162].dump', 'rb') as f:
    c_temp_conv8 = pickle.load(f)
with open('../output/temp_lab4_1_c_temp[et='+str(eltype)+'_dof578].dump', 'rb') as f:
    c_temp_conv16 = pickle.load(f)
with open('../output/temp_lab4_1_c_temp[et='+str(eltype)+'_dof2178].dump', 'rb') as f:
    c_temp_conv32 = pickle.load(f)

with open('../output/temp_lab4_1_r_temp[et='+str(eltype)+'_dof50].dump', 'rb') as f:
    r_temp_conv4 = pickle.load(f)
with open('../output/temp_lab4_1_r_temp[et='+str(eltype)+'_dof162].dump', 'rb') as f:
    r_temp_conv8 = pickle.load(f)
with open('../output/temp_lab4_1_r_temp[et='+str(eltype)+'_dof578].dump', 'rb') as f:
    r_temp_conv16 = pickle.load(f)
with open('../output/temp_lab4_1_r_temp[et='+str(eltype)+'_dof2178].dump', 'rb') as f:
    r_temp_conv32 = pickle.load(f)




fig2 = plt.figure()
fig2.set_size_inches(10, 12)
# c_temp = fig2.add_subplot(211)
# c_temp.plot(50,c_temp_conv4,marker='o',label="$Error$ $dof = 50$",linestyle='--',linewidth=1, color='r',markersize=10)
# c_temp.plot(162,c_temp_conv8,marker='o',label="$Error$ $dof = 162$",linestyle='--',linewidth=1, color='g',markersize=10)
# c_temp.plot(278,c_temp_conv16,marker='o',label="$Error$ $dof = 278$",linestyle='--',linewidth=1, color='b',markersize=10)
# c_temp.plot(2178,c_temp_conv32,marker='o',label="$Error$ $dof = 2178$",linestyle='--',linewidth=1, color='y',markersize=10)
# c_temp.set_xlabel("$dof$",fontsize=15)
# c_temp.set_ylabel("$T, C$",fontsize=15)
# c_temp.set_xscale('symlog')
# c_temp.legend(loc='best',fontsize=15,numpoints=1)
# c_temp.grid()
# c_temp.set_title('$r = (a+b)/2, \phi = \pi/16$',fontsize=20)

# r_temp = fig2.add_subplot(212)
# r_temp.plot(50,r_temp_conv4,marker='o',label="$Error$ $dof = 50$",linestyle='--',linewidth=1, color='r',markersize=10)
# r_temp.plot(162,r_temp_conv8,marker='o',label="$Error$ $dof = 162$",linestyle='--',linewidth=1, color='g',markersize=10)
# r_temp.plot(278,r_temp_conv16,marker='o',label="$Error$ $dof = 278$",linestyle='--',linewidth=1, color='b',markersize=10)
# r_temp.plot(2178,r_temp_conv32,marker='o',label="$Error$ $dof = 2178$",linestyle='--',linewidth=1, color='y',markersize=10)
# r_temp.set_xlabel("$dof$",fontsize=15)
# r_temp.set_ylabel("$T, C$",fontsize=15)
# r_temp.set_xscale('symlog')
# r_temp.legend(loc='lower right',fontsize=15,numpoints=1)
# r_temp.grid()
# r_temp.set_ylim(9.205, 9.235)
# r_temp.set_title('$r = 0.0045, \phi = \pi/2$',fontsize=20)


convline = [c_temp_conv4,c_temp_conv8,c_temp_conv16,c_temp_conv32]
convline2 = [r_temp_conv4,r_temp_conv8,r_temp_conv16,r_temp_conv32]

dof = [50,162,278,2178]
c_temp = fig2.add_subplot(211)
c_temp.plot(dof,convline,marker='o',linestyle='-',linewidth=2, color='r',markersize=5)
c_temp.set_xlabel("dof",fontsize=10)
c_temp.set_ylabel("T, C",fontsize=10)
c_temp.set_xscale('symlog')
c_temp.grid()
c_temp.set_title('r = (a+b)/2, phi = pi/16',fontsize=15)

r_temp = fig2.add_subplot(212)
r_temp.plot(dof,convline2,marker='o',linestyle='-',linewidth=2, color='r',markersize=5)
r_temp.set_xlabel("dof",fontsize=10)
r_temp.set_ylabel("T, C",fontsize=10)
r_temp.set_xscale('symlog')
r_temp.grid()
r_temp.set_ylim(9.205, 9.235)
r_temp.set_title('r = 0.0045, phi = pi/2',fontsize=15)

filename = '../output/plots/Mlab4_1_conv_plots_et='+str(eltype)+'.png'
fig2.savefig(filename)