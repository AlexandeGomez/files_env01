import numpy as np
from fxpmath import Fxp
import math

numberofcases = 1000
dim = 32
cnt = 1

SQNR_list = []
sourceFile = "/home/jhonatang/Documentos/PYTHON3/ALL_CASES/"

for i in range(numberofcases):
    reales = []
    with open(sourceFile+"outputR_"+str(cnt)+".txt", "r") as fname:
        for lineas in fname:
            numero = Fxp('0b'+lineas[:-1], signed=True, n_word=32, n_frac=16)
            reales.append(numero)  
        rnp = np.array(reales)
        rmtx = rnp.reshape(dim,dim)


    imag = []
    with open(sourceFile+"outputI_"+str(cnt)+".txt", "r") as fname:
        for lineas in fname:
            numero = Fxp('0b'+lineas[:-1], signed=True, n_word=32, n_frac=16)
            imag.append(numero)
        inp = np.array(imag)
        imtx = inp.reshape(dim,dim)
    
    m = []
    for i in range(rmtx[0].size):
        n = []
        for j in range(rmtx[0].size):
            ncomplex = complex(rmtx[i][j], imtx[i][j])
            n.append(ncomplex)
        m.append(n)
    M = np.array(m)

    ##Fin de la conversión de las salidas de quartus a matrices numpy de python

    F = []
    with open(sourceFile+"Matrix_AB_PythonOut_"+str(cnt)+".txt","r") as archivo:
        for line in archivo:
            l = line[1:-2]
            lc = complex(l)
            F.append(lc)
        F = np.array(F)
        F.resize(dim, dim)
    
    Acum=0
    for i in range(F[0].size):
        for j in range(F[0].size):
            Acum = Acum + math.pow(abs(F[i][j]),2)
    Px = Acum/F[0].size


    Acum=0
    for i in range(F[0].size):
        for j in range(F[0].size):
            Acum = Acum + math.pow((abs(F[i][j])-(abs(M[i][j]))),2)
    Pe = Acum/F[0].size

    SQNR = 10*math.log(Px/Pe, 10)
    
    SQNR_list.append(SQNR)

    print("Prueba número: "+str(cnt))
    cnt = cnt + 1

print(SQNR_list)

promSQNR = sum(SQNR_list)/len(SQNR_list)

print("promedio: ", promSQNR)

with open("SQNR_results.txt", "w") as file:
    file.write("Resultado de las 1000 pruebas:\n")
    file.write("Número de pruebas: "+str(len(SQNR_list))+"\n")
    file.write("Promedio de las pruebas: "+str(promSQNR))







