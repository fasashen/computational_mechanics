from numpy import pi, sin, sinh, cos, arange, subtract, around, exp, insert
import matplotlib.pyplot as plt
from config import *
import os
import pickle

def get_stress(k_list,es_list,es_model):
    m = 'model' if es_model == 0 else 'submodel'
    stress = []
    doflist = []
    disp_conv = []
    for k in k_list:
        stress.append([])
        doflist.append([])
        disp_conv.append([])
        for es in es_list:
            with open('params.txt','w') as f:
                f.truncate()
                f.write('k = '  + str(k)+'\n')
                if m == 'model':
                    f.write('es0 = ' + str(es)+'\n')
                    f.write('submodel = 0')
                elif m == 'submodel':
                    f.write('es0 = ' + str(es_model)+'\n')
                    f.write('es1 = ' + str(es)+'\n')
                    f.write('submodel = 1')
            print('APDL working... k = '+str(k)+' es = ' + str(es))
            os.system('apdl.bat')
            with open('./output/stress_'+m+'.txt','r') as f:
                stroke = f.readlines()[14][21:32]
                nstress = float(stroke)
                print(stroke,'-->',nstress)
                nstress = nstress/sigma_nom
                stress[-1].append(nstress)
            # print('Done, K =',nstress)
            with open('./output/dof_'+m+'.txt','r') as f:
                dof = float(f.readlines()[1][52:60])
                doflist[-1].append(dof)
                # print('DOF:',dof,'\n')
            if m == 'model':
                with open('./output/disp_conv.txt','r') as f:
                    disp = float(f.readlines()[1][59:])
                    disp_conv[-1].append(disp)
            else:
                disp_conv[-1].append(0)

    with open('./results/stress_results_'+m+'.pickle','wb') as f:
        pickle.dump(stress, f)
    with open('./results/dof_results_'+m+'.pickle','wb') as f:
        pickle.dump(doflist, f)
    if m == 'model':
        with open('./results/disp_conv_results.pickle','wb') as f:
            pickle.dump(disp_conv, f)

    return read_result(m)

def read_result(m):
    with open('./results/stress_results_'+m+'.pickle', 'rb') as f:
        stress = pickle.load(f)
    with open('./results/dof_results_'+m+'.pickle', 'rb') as f:
        doflist = pickle.load(f)
    with open('./results/disp_conv_results.pickle', 'rb') as f:
        disp_conv = pickle.load(f)
    if m == 'model':
        return stress, doflist, disp_conv
    else:
        return stress, doflist

k_list = [x * 0.01 for x in range(5, 25)]
k_list = [0.1, 0.15, 0.2]
es_list = [D/8,D/16,D/32,D/64,D/128]

stress_fe, doflist, disp_conv = get_stress(k_list,es_list,0)
stress_fe, doflist, disp_conv = read_result('model')

print(stress_fe, doflist, disp_conv)

fig1 = plt.figure()
fig1.set_size_inches(12, 6)
p1 = fig1.add_subplot(111)
for k,d,s in zip(k_list,doflist,stress_fe):
    if k == 0.10:
        p1.plot(d,s,marker='o', label="$r/d = 0.10$",linewidth=1, color='r',markersize=6, mew=0)
    elif k == 0.15:    
        p1.plot(d,s,marker='o', label="$r/d = 0.15$",linewidth=1, color='b',markersize=6, mew=0)
    elif k == 0.20:
        p1.plot(d,s,marker='o', label="$r/d = 0.20$",linewidth=1, color='g',markersize=6, mew=0)
p1.set_xlabel("$DOF$", fontsize=20)
p1.set_ylabel("$K_{tn}$", fontsize=20)
p1.legend(loc='lower right',fontsize=15,numpoints=1)
p1.grid()
p1.set_title('$K_{tn}$ $vs$ $DOF$ $w/o$ $submodeling$',fontsize=20)
fig1.savefig('plot_conv_model', dpi=300)

# # Submodel convergence
stress_fe,doflist = get_stress(k_list,es_list,es_list[-1])
stress_fe, doflist = read_result('submodel')
print(disp_conv)

fig2 = plt.figure()
fig2.set_size_inches(12, 6)
p2 = fig2.add_subplot(111)
for k,d,s in zip(k_list,doflist,stress_fe):
    if k == 0.10:
        p2.plot(d,s,marker='o', label="$r/d = 0.10$",linewidth=1, color='r',markersize=6, mew=0)
    elif k == 0.15:    
        p2.plot(d,s,marker='o', label="$r/d = 0.15$",linewidth=1, color='b',markersize=6, mew=0)
    elif k == 0.20:
        p2.plot(d,s,marker='o', label="$r/d = 0.20$",linewidth=1, color='g',markersize=6, mew=0)
p2.set_xlabel("$DOF$", fontsize=20)
p2.set_ylabel("$K_{tn}$", fontsize=20)
p2.legend(loc='upper right',fontsize=15,numpoints=1)
p2.grid()
p2.set_title('$K_{tn}$ $vs$ $DOF$ $w/$ $submodeling$',fontsize=20)
fig2.savefig('plot_conv_submodel', dpi=300)
#Submodel K vs r/d
fig3 = plt.figure()
fig3.set_size_inches(12, 6)
p3 = fig3.add_subplot(111)
for rd,Ktn in zip(k_list,stress_fe):
    if rd == 0.1 or rd == 0.15 or rd == 0.20:
        p3.plot(rd,Ktn[-1],marker='o',linewidth=0, color='r',markersize=6, mew=0)
    else:
        p3.plot(rd,Ktn[-1],marker='o',linewidth=0, color='k',markersize=4, mew=0)   
p3.set_xlabel("$r/d$", fontsize=20)
p3.set_ylabel("$K_{tn}$", fontsize=20)
p3.set_xlim(0.05, 0.25)
# p3.set_ylim(1.5, 3)
p3.grid()
p3.set_title('$K_{tn}$ $vs$ $r/d$. $D/d=1.3$',fontsize=20)
fig3.savefig('plot_K_submodel', dpi=300)
#Submodel n vs r/d
fig4 = plt.figure()
fig4.set_size_inches(12, 6)
p4 = fig4.add_subplot(111)
for rd,Ktn in zip(k_list,stress_fe):
    n = yi/Ktn[-1]/sigma_nom
    p4.plot(rd,n,marker='o',linewidth=0, color='k',markersize=6, mew=0)
p4.plot([0.05, 0.25],[2,2],marker='o',linewidth=2, color='r',markersize=0, mew=0)
p4.set_xlabel("$r/d$", fontsize=20)
p4.set_ylabel("$n=\sigma_{T}/\sigma_{max}$", fontsize=20)
p4.set_xlim(0.05, 0.25)
p4.grid()
p4.set_title('$n=\sigma_{T}/\sigma_{max}$ $vs$ $r/d$. $D/d=1.3$',fontsize=20)
fig4.savefig('plot_nt_submodel', dpi=300)

fig5 = plt.figure()
fig5.set_size_inches(12, 6)
p5 = fig5.add_subplot(111)
for k,d,s in zip(k_list,doflist,disp_conv):
    if k == 0.10:
        p5.plot(d,s,marker='o', label="$r/d = 0.10$",linewidth=1, color='r',markersize=6, mew=0)
    elif k == 0.15:    
        p5.plot(d,s,marker='o', label="$r/d = 0.15$",linewidth=1, color='b',markersize=6, mew=0)
    elif k == 0.20:
        p5.plot(d,s,marker='o', label="$r/d = 0.20$",linewidth=1, color='g',markersize=6, mew=0)
p5.set_xlabel("$DOF$", fontsize=20)
p5.set_ylabel("$Displacement, m$", fontsize=20)
p5.legend(loc='lower right',fontsize=15,numpoints=1)
p5.grid()
p5.set_title('$Macromodel$ $displacement$ $convergence$',fontsize=20)
fig5.savefig('disp_conv', dpi=300)


'''
[[2.81460166220116, 3.172245782358145, 3.3657089768167525, 3.4460475090563554, 3.4733275714056284], [2.697722862961613, 2.982286449118711, 3.1259447591047915, 3.182507090214294, 3.2007772237142658], [2.590104268372737, 2.8241121426532, 2.93448377105714, 2.9757792782831043, 2.988793619954317], [2.497427139125619, 2.6904648647218985, 2.777060291995738, 2.808344767166923, 2.817855247618963], [2.414060269689446, 2.5745871686878297, 2.644414117269914, 2.6686908700027536, 2.676199144043838], [2.3396532739422997, 2.4749023170023663, 2.5317900066536487, 2.5510612433590985, 2.5568175867905967], [2.2687751669944634, 2.3865299315388033, 2.4338570855777717, 2.4496244610640487, 2.454229535809247], [2.2073074301781195, 2.3084939366717996, 2.34801248570804, 2.361001799799116, 2.3647309092395217], [2.1514708988925886, 2.238666988089715, 2.272454221274595, 2.283266135893756, 2.2863695558307375], [2.100389607833078, 2.1763983687089885, 2.205155058286342, 2.2142901250363276, 2.2168929933705703], [2.051285495604386, 2.1196608445385277, 2.144713452255613, 2.1525220572583406, 2.1547244843103917], [2.008137947448288, 2.0684794431584694, 2.090128299976929, 2.096860719033768, 2.098737787544039], [1.9681188468093083, 2.0212774270201854, 2.040398498244814, 2.0462299244167226, 2.047856717125624], [1.9312532212675841, 1.9785052925661417, 1.9952487436777597, 2.0003543700256974, 2.001755914513366], [1.8952135058703792, 1.9388365780490793, 1.953828098551111, 1.9583080353956248, 1.9595594144024722], [1.8632532860354967, 1.9024214489498201, 1.9156860664224025, 1.9196654516641771, 1.9207416376100659], [1.833370355351981, 1.8684089675437079, 1.880372150849169, 1.8839260672286156, 1.8848771152738195], [1.80541454833901, 1.8370494096321122, 1.847711158770452, 1.8508896614478443, 1.8517405991725007], [1.778034375669189, 1.8076920581314724, 1.817452814384882, 1.8203059585204941, 1.8210818135047395], [1.75350734713498, 1.780512106102747, 1.7892717591506786, 1.7918495999047843, 1.792550372148619]]
[[121.0, 433.0, 1583.0, 6043.0, 23603.0], [121.0, 433.0, 1633.0, 6239.0, 24379.0], [135.0, 459.0, 1683.0, 6435.0, 25155.0], [135.0, 459.0, 1733.0, 6631.0, 25931.0], [135.0, 485.0, 1783.0, 6827.0, 26707.0], [135.0, 485.0, 1833.0, 7023.0, 27483.0], [149.0, 511.0, 1883.0, 7219.0, 28259.0], [149.0, 511.0, 1933.0, 7415.0, 29035.0], [149.0, 537.0, 1983.0, 7611.0, 29811.0], [149.0, 537.0, 2033.0, 7807.0, 30587.0], [163.0, 563.0, 2083.0, 8003.0, 31363.0], [163.0, 563.0, 2133.0, 8199.0, 32139.0], [163.0, 589.0, 2183.0, 8395.0, 32915.0], [163.0, 589.0, 2233.0, 8591.0, 33691.0], [177.0, 615.0, 2283.0, 8787.0, 34467.0], [177.0, 615.0, 2333.0, 8983.0, 35243.0], [177.0, 641.0, 2383.0, 9179.0, 36019.0], [177.0, 641.0, 2433.0, 9375.0, 36795.0], [191.0, 667.0, 2483.0, 9571.0, 37765.0], [191.0, 667.0, 2533.0, 9767.0, 38541.0]]
'''