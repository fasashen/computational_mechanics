from numpy import pi, sin, sinh, cos, arange, subtract, around, exp, insert
import matplotlib.pyplot as plt
from config import *
import os



def read_result():
    dof_2d,freq1_2d,freq2_2d,freq3_2d = [], [], [], []
    dof_3d,freq1_3d,freq2_3d,freq3_3d = [], [], [], []
    dof_beam,freq1_beam,freq2_beam,freq3_beam = [], [], [], []
    with open('./output/result_data.txt','r') as f:
        data = f.readlines()
        print()
        for line in data[0:elsize_num]:
            dof, f1, f2, f3 = line.split()
            dof_2d.append(dof)
            freq1_2d.append(f1)
            freq2_2d.append(f2)
            freq3_2d.append(f3)
        for line in data[elsize_num+1:2*elsize_num+1]:
            dof, f1, f2, f3 = line.split()
            dof_3d.append(dof)
            freq1_3d.append(f1)
            freq2_3d.append(f2)
            freq3_3d.append(f3)
        for line in data[2*elsize_num+2:3*elsize_num+3]:
            dof, f1, f2, f3 = line.split()
            dof_beam.append(dof)
            freq1_beam.append(f1)
            freq2_beam.append(f2)
            freq3_beam.append(f3)
    return [dof_2d,freq1_2d,freq2_2d,freq3_2d],[dof_3d,freq1_3d,freq2_3d,freq3_3d],[dof_beam,freq1_beam,freq2_beam,freq3_beam]

os.system('start.bat')
data_2d, data_3d, data_beam = read_result()

fig1 = plt.figure()
fig1.set_size_inches(12, 8)

p2d1 = fig1.add_subplot(311)
p2d1.plot(data_2d[0],data_2d[1],marker='o', label="$2D$ $Mode$ $1$",linewidth=1, color='r',markersize=6, mew=0)
p2d2 = fig1.add_subplot(312)
p2d2.plot(data_3d[0],data_3d[1],marker='o', label="$3D$ $Mode$ $1$",linewidth=1, color='r',markersize=6, mew=0)
p2d3 = fig1.add_subplot(313)
p2d3.plot(data_beam[0],data_beam[1],marker='o', label="$Beam$ $Mode$ $1$",linewidth=1, color='r',markersize=6, mew=0)

p2d3.set_xlabel("$Nodes$", fontsize=20)
p2d2.set_ylabel("$Frequency, Hz$", fontsize=20)
p2d1.legend(loc='upper right',fontsize=15,numpoints=1)
p2d2.legend(loc='upper right',fontsize=15,numpoints=1)
p2d3.legend(loc='upper right',fontsize=15,numpoints=1)
p2d1.grid()
p2d2.grid()
p2d3.grid()
p2d1.set_title('$Convergence$ $plot$',fontsize=20)
fig1.savefig('plot_conv_model1', dpi=300)




fig1 = plt.figure()
fig1.set_size_inches(12, 8)

p2d1 = fig1.add_subplot(311)
p2d1.plot(data_2d[0],data_2d[2],marker='o', label="$2D$ $Mode$ $2$",linewidth=1, color='r',markersize=6, mew=0)
p2d2 = fig1.add_subplot(312)
p2d2.plot(data_3d[0],data_3d[2],marker='o', label="$3D$ $Mode$ $2$",linewidth=1, color='r',markersize=6, mew=0)
p2d3 = fig1.add_subplot(313)
p2d3.plot(data_beam[0],data_beam[2],marker='o', label="$Beam$ $Mode$ $2$",linewidth=1, color='r',markersize=6, mew=0)

p2d3.set_xlabel("$Nodes$", fontsize=20)
p2d2.set_ylabel("$Frequency, Hz$", fontsize=20)
p2d1.legend(loc='upper right',fontsize=15,numpoints=1)
p2d2.legend(loc='upper right',fontsize=15,numpoints=1)
p2d3.legend(loc='upper right',fontsize=15,numpoints=1)
p2d1.grid()
p2d2.grid()
p2d3.grid()
p2d1.set_title('$Convergence$ $plot$',fontsize=20)
fig1.savefig('plot_conv_model2', dpi=300)



fig1 = plt.figure()
fig1.set_size_inches(12, 8)

p2d1 = fig1.add_subplot(311)
p2d1.plot(data_2d[0],data_2d[3],marker='o', label="$2D$ $Mode$ $3$",linewidth=1, color='r',markersize=6, mew=0)
p2d2 = fig1.add_subplot(312)
p2d2.plot(data_3d[0],data_3d[3],marker='o', label="$3D$ $Mode$ $3$",linewidth=1, color='r',markersize=6, mew=0)
p2d3 = fig1.add_subplot(313)
p2d3.plot(data_beam[0],data_beam[3],marker='o', label="$Beam$ $Mode$ $3$",linewidth=1, color='r',markersize=6, mew=0)

p2d3.set_xlabel("$Nodes$", fontsize=20)
p2d2.set_ylabel("$Frequency, Hz$", fontsize=20)
p2d1.legend(loc='upper right',fontsize=15,numpoints=1)
p2d2.legend(loc='upper right',fontsize=15,numpoints=1)
p2d3.legend(loc='upper right',fontsize=15,numpoints=1)
p2d1.grid()
p2d2.grid()
p2d3.grid()
p2d1.set_title('$Convergence$ $plot$',fontsize=20)
fig1.savefig('plot_conv_model3', dpi=300)


freq_an = []
for k in [55.826, 117.143, 192.70]:
    freq_formula = k/(2*3.1415*R**2*(3.1415/2)**2)*(E*J/(rho*b*h))**0.5
    freq_an.append(freq_formula)
print(freq_an)