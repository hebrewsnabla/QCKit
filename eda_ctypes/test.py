import numpy as np
import eda_ctypes
import time

#dm = np.array([[1, 0.2, 0.3],[0.2,1,0.5],[0.1,0.3,1]])
#dm = np.array([1.0,2,3])
nao = 10
natom = 1
dm = np.random.rand(nao,nao)
#nao = 3
eri = np.random.rand(nao**4)
bas2atm = []
for i in range(nao):
    bas2atm.append(i//10 + 1)
a = time.time()
eda_ctypes.c_get_coul(dm,eri,bas2atm,natom)
b = time.time()
print("time: %f s"%(b-a))
