from fxpmath import Fxp
import math

DIM = 3

q = Fxp(0, signed=False, n_word=math.ceil(math.log((DIM*DIM)-1,2))+1)
cntAux = Fxp(0, signed=False, n_word=math.ceil(math.log(DIM,2))+1)
cntJump = Fxp(0, signed=False, n_word=math.ceil(math.log(DIM,2))+1)
cntAddr = Fxp(0, signed=False, n_word=math.ceil(math.log(DIM,2))+1)

ex = 0
flag = 1
while(flag):

    if(cntAddr.get_val()==DIM):
        cntAddr.set_val(0)
        cntAux.set_val(cntAux+1)

    if(cntAux.get_val()==DIM):
        cntJump.set_val(cntJump + 1)
        cntAux.set_val(0)

    q.set_val(cntAddr+DIM*cntJump)
    cntAddr.set_val(cntAddr + 1)
    ex += 1
    print(q.get_val())

    if(ex==DIM*DIM*DIM):
        flag=0

print(q.info(verbose=2))

#####################################################3

q = Fxp(0, signed=False, n_word=math.ceil(math.log((DIM*DIM)-1, 2))+1)
cntAddr = Fxp(0, signed=False, n_word=math.ceil(math.log(DIM, 2))+1)
cntJump = Fxp(0, signed=False, n_word=math.ceil(math.log(DIM, 2))+1)

ex = 0
flag = 1
while(flag):
    if(cntAddr.get_val()==DIM):
        cntAddr.set_val(0)
        cntJump.set_val(cntJump+1)
    if(cntJump.get_val()==DIM):
        cntJump.set_val(0)
    q.set_val(DIM*cntAddr+cntJump)
    print(q.get_val())
    cntAddr.set_val(cntAddr+1)
    ex += 1
    if(ex==DIM*DIM*DIM):
        flag=0
print(q.info(verbose=3))