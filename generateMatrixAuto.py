from fxpmath import Fxp
from complexMatrix import createComplexMat
import numpy as np

A = np.array(createComplexMat(32))

B = np.array(createComplexMat(32))


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

#
AB = np.dot(A,B)
with open("Matrix_AB_PythonOut.txt", "w") as archivo:
    for i in range(AB[0].size):
        for j in range(AB[0].size):
            ABstr = str(AB[i,j])
            archivo.write(ABstr+"\n")
