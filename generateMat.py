#%%
from fxpmath import Fxp
from complexMatrix import createComplexMat
import random as rm
import numpy as np
import math


# %%
## analisis de los pasos intermedios
a1b1 = npx[0]*npx[2]
a2b2 = npx[1]*npx[3]
a1b2 = npx[0]*npx[3]
a2b1 = npx[1]*npx[2]

a1b1.resize(True, 32, 32-10)
a2b2.resize(True, 32, 32-10)
a1b2.resize(True, 32, 32-10)
a2b1.resize(True, 32, 32-10)


r = a1b1 - a2b2
i = a1b2 + a2b1

r.resize(True, 32, 32-11)
i.resize(True, 32, 32-11)

#--------------------------------------------

# %%
A = np.array(createComplexMat(3))

B = np.array(createComplexMat(3))

# %%

with open("Reales_M1.txt", "w") as archivo:
    k = A[0].size
    for i in range(k):
        for j in range(k):
            re = np.real(A[i][j])
            rfp = Fxp(re, signed = True, n_word =32, n_frac=32-5)
            archivo.write(rfp.bin()+"\n")

with open("Imagin_M1.txt", "w") as archivo:
    k = A[0].size
    for i in range(k):
        for j in range(k):
            im = np.imag(A[i][j])
            ifp = Fxp(im, signed = True, n_word =32, n_frac=32-5)
            archivo.write(ifp.bin()+"\n")

with open("Reales_M2.txt", "w") as archivo:
    k = B[0].size
    for i in range(k):
        for j in range(k):
            re = np.real(B[i][j])
            rfp = Fxp(re, signed = True, n_word =32, n_frac=32-5)
            archivo.write(rfp.bin()+"\n")

with open("Imagin_M2.txt", "w") as archivo:
    k = B[0].size
    for i in range(k):
        for j in range(k):
            im = np.imag(B[i][j])
            ifp = Fxp(im, signed = True, n_word =32, n_frac=32-5)
            archivo.write(ifp.bin()+"\n")


# %%

ABfxp = Fxp(AB, signed=True, n_word=32)

# %%
dim = 32

with open("outputR.txt","r") as archivo:
    for k in archivo:
        b = Fxp('0b'+k[:-1], signed=True, n_word = 32, n_frac=11)
        #print(k[:-1])
        print(b)

print("***************")
# %%
for i in range(dim):
    for j in range(dim):
        r = np.real(ABfxp[i][j])
        r.resize(True, n_word=32, n_frac=11)
        #print(r.bin())
        print(r)
# %%

#guardar cada linea como elemento de una lista

reales = []
with open("outputR.txt") as fname:
    for lineas in fname:
       numero = Fxp('0b'+lineas[:-1], signed=True, n_word=32, n_frac=11)
       reales.append(numero)  
rnp = np.array(reales)
rmtx = rnp.reshape(32,32)


imag = []
with open("outputI.txt") as fname:
    for lineas in fname:
        numero = Fxp('0b'+lineas[:-1], signed=True, n_word=32, n_frac=11)
        imag.append(numero)
inp = np.array(imag)
imtx = inp.reshape(32,32)

m = []
for i in range(rmtx[0].size):
    n = []
    for j in range(rmtx[0].size):
        ncomplex = complex(rmtx[i][j], imtx[i][j])
        n.append(ncomplex)
    m.append(n)
M = np.array(m)

# %%

#SQNR

Acum=0
for i in range(AB[0].size):
    for j in range(AB[0].size):
        Acum = Acum + math.pow(abs(AB[i][j]),2)
Px = Acum/AB[0].size


Acum=0
for i in range(AB[0].size):
    for j in range(AB[0].size):
        Acum = Acum + math.pow((abs(AB[i][j])-(abs(M[i][j]))),2)
Pe = Acum/AB[0].size

SQNR = 10*math.log(Px/Pe, 10)
print(SQNR) #SQNR=100
# %%
