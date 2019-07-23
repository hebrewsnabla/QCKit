
import numpy as np
import ctypes as ct
ceda = ct.CDLL("./ceda.so")

'''
def init(mf, atomlist, spinlist):


    #return dmlist, slicelist, enuclist, e1list, basrange1, basrange2, basrange3, basrange4

def get_maxrange(somelist):

    #return num

def addzero(somelist, num):
    # maybe unnecessary here
    #return newlist

def bas2atm(a,b,c,d,oneatom):
    # find atom which some basis belongs to
    #return A,B,C,D

def get_atomE(mf, basrange1):
    eri = mf.mol.intor("int2e_sph",aosym='s8')
    dm = mf.make_rdm1()
    nao = len(dm)
    #return c_get_coul(dm, eri_s8)
'''
def c_get_coul(dm, eri, bas2atm, natom):
    ## input
    c_dm = dm.ctypes.data_as(ct.c_void_p)
    nao = dm.shape[0]
    #c_dm = dm.ctypes.data_as((ct.c_int*nao)*nao)
    c_nao = ct.c_int(nao)
    c_eri = eri.ctypes.data_as(ct.c_void_p)
    #c_eri = eri.ctypes.data_as((((ct.c_int*nao)*nao)*nao)*nao)
    #c_neri = ct.c_int(len(eri))
    #natom = len(basrange1)
    c_natom = ct.c_int(natom)
    #c_basrg = np.asarray(basrange1).data_as(ctypes.c_void_p)
    c_bas2atm = np.asarray(bas2atm).ctypes.data_as(ct.c_void_p)
    #c_bas2atm = (ct.c_int*nao)(bas2atom)
    #c_nbas = ct.c_int(len(bas2atm))
    ## output
    #c_ecoul = ctypes.c_void_p()
    #c_necoul = c_int()'''

    #ceda.ecoul(c_dm, c_nao, c_eri, c_neri, c_basrg, c_natom, c_ecoul, c_necoul)
    ceda.ecoul(c_dm, c_nao, c_eri, c_bas2atm, c_natom)
    return 0
'''
def get_E():

    #return E_dict
'''

