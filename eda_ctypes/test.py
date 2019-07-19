import numpy as np
import eda_ctypes
import time
import tensorflow as tf

#dm = np.array([[1, 0.2, 0.3],[0.2,1,0.5],[0.1,0.3,1]])
#dm = np.array([1.0,2,3])
nao = 10
natom = 1
dm = np.random.rand(nao,nao)
#nao = 3
#eri = np.random.rand(nao**4)
eri = np.random.rand(nao,nao,nao,nao)
bas2atm = []
for i in range(nao):
    bas2atm.append(i//10 - 1)

tf_dm = tf.convert_to_tensor(dm)
tf_eri = tf.convert_to_tensor(eri)

a = time.time()
#eda_ctypes.c_get_coul(dm,eri,bas2atm,natom)

tf_dmdm = tf.einsum('ij,kl->ijkl', tf_dm ,tf_dm)
b1 = time.time()
print("time: %f s"%(b1-a))

E = tf.einsum('ijkl,ijkl->ijkl', tf_dmdm, tf_eri)
b2 = time.time()
print("time: %f s"%(b2-b1))

np_dmdm = np.einsum('ij,kl->ijkl', dm ,dm)
b3 = time.time()
print("time: %f s"%(b3-b2))

E = np.einsum('ijkl,ijkl->ijkl', np_dmdm, eri)
b4 = time.time()
print("time: %f s"%(b4-b3))
#b = time.time()
#print("time: %f s"%(b-a))
