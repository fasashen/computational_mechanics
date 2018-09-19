from numpy import pi, sin, sinh, cos, arange, subtract, around, exp, insert
import matplotlib.pyplot as plt
from config import *
import os


def read_result():

    dof1, temp1, grad1 = [], [], []
    dof2, temp2, grad2 = [], [], []

    with open('./output/result_data.txt','r') as f:
        data = f.readlines()
        print()
        for line in data[0:elsize_num]:
            dof, t1, g1 = line.split()
            dof1.append(dof)
            temp1.append(t1)
            grad1.append(g1)
        for line in data[elsize_num+1:2*elsize_num]:
            dof, t2, g2 = line.split()
            dof2.append(dof)
            temp2.append(t2)
            grad2.append(g2)
        # for line in data[2*elsize_num+2:3*elsize_num+3]:
        #     dof, f1, f2, f3 = line.split()
        #     dof_beam.append(dof)
        #     freq1_beam.append(f1)
        #     freq2_beam.append(f2)
        #     freq3_beam.append(f3)
    # return [dof_2d,freq1_2d,freq2_2d,freq3_2d],[dof_3d,freq1_3d,freq2_3d,freq3_3d],[dof_beam,freq1_beam,freq2_beam,freq3_beam]
    return [dof1, temp1, grad1],[dof2, temp2, grad2]

# os.system('start.bat')
data1,data2 = read_result()

fig1 = plt.figure()
fig1.set_size_inches(12, 6)

p1 = fig1.add_subplot(111)
p1.plot(data1[0],data1[1],marker='o',linewidth=1, color='k',markersize=6, mew=0)
p1.set_xlabel("$Nodes$", fontsize=20)
p1.set_ylabel("$Temperature, K$", fontsize=20)
p1.grid()
p1.set_title('$Convergence$ $plot$',fontsize=20)
fig1.savefig('plot_conv_model1', dpi=300)


fig2 = plt.figure()
fig2.set_size_inches(12, 6)

p2 = fig2.add_subplot(111)
p2.plot(data2[0],data2[1],marker='o',linewidth=1, color='k',markersize=6, mew=0)
p2.set_xlabel("$Nodes$", fontsize=20)
p2.set_ylabel("$Temperature, K$", fontsize=20)
p2.grid()
p2.set_title('$Convergence$ $plot$',fontsize=20)
fig2.savefig('plot_conv_model2', dpi=300)



R = b1
a = a1
Jt = pi/2*R**4*(1-2*a**2/R**2*(1-8/3/pi*a/R+1/4*a**2/R**2))
Wt = Jt/(2*R-a)
tmax = G*v*(2*R-a)
ro = R/2
Phi  = 2*G*v*(2*R*cos(0)-ro)*(ro/a-a/ro)*a/2
C = G*(pi/2*R**4-pi*a**2*(R**2+a**2/4-8/3/pi*a*R))

print('Задача 1')
print(Jt)
print(Wt)
print('Максимум касательных напряжений:',tmax)
print('Жесткость:',C)
print('Максимум функции напряжений Ф:',Phi,'\n')

b = b2
a = a2
d = d2
Jt = 2/3*(2-1.081*d/a)*a*d**3
Wt = Jt/1.02/d
tmax = G*v*d*1.015
ro = R/2


print('Задача 2')
print('Крутильная жесткость С',Jt*G)
print(Wt)
print(tmax)

nodal_temp = []
i = 0
nodal_sum = 0
with open('./output/nodal_data.txt','r') as f:
        for line in f:
            i += 1
            nodal_sum += float(line)
            nodal_temp.append(float(line))
print(2*2/v*nodal_sum*(elsize_start2/(elsize_num-1))**2)            
print(4*111.646/v)