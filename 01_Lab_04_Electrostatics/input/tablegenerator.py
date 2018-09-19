from numpy import pi, sin, sinh, cos, arange, subtract, around, exp, insert
from config_2 import *

def H(x):
    return -10*x

n = 0
with open('Hfunc.txt', 'w') as f:
    f.write('*dim,Hfunc,table,'+str(101)+',,,X\n')    
    for x in arange(0,10*a,a/10):
        n += 1
        f.write('*taxis,Hfunc('+str(n)+'),1,'+str(x)+'\n')
        f.write('Hfunc('+str(n)+') = '+str('%8.3f'%H(x))+'\n')

# '%8.3f'%