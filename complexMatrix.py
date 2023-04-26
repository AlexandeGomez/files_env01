import random as rm

def createComplexMat(num):
    N = []
    for k in range(num):
        M = []
        for j in range(num):
            ls = []
            for i in range(2):
                n = rm.randrange(-14, 14)
                d = rm.random()
                if(n<0):
                    n -= d
                else:
                    n += d
                ls.append(n)
            nc = complex(ls[0], ls[1])
            M.append(nc)
        N.append(M)
    return N