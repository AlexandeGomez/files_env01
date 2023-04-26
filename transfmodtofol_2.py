#%%
print(chr(9633))
print(chr(9674))
print(chr(126))
print(chr(8744))
print(chr(8743))

#%%
s2 = "◊(A)"
s3 = "◊(□(p∧p)x◊(q∨q))"
s4 = "□(p∧p)x◊(q∨q)"
s5 = "□p x ◊q"

#%%
eval = s3

regleft = []
regright = []
for i in range(len(eval)):
    if(eval[i]=="("):
        regleft.append(i)
    
    if(eval[len(eval)-i-1]==")"):
        regright.append(len(eval)-i-1)
print(regleft)
print(regright)


# %%

if(len(regleft)==len(regright) and len(regleft)==1):
    if(eval[0] == '□'):
        rs = "forall y:(S(x,y) -> _)"
    elif(eval[0] == '◊'):
        rs = "exist y:(S(x,y) ∧ _)"

elif(len(regleft)==len(regright) and len(regleft)==2):
    if(eval[regleft[0]-1]=='□'):
        rs1 = "forall y:(S(x,y) -> _)"
    elif(eval[regleft[0]-1]=='◊'):
        rs1 = "exist y:(S(x,y) ∧ _)"

    if(eval[regleft[1]-1]=='□'):
        rs2 = "forall y:(S(x,y) -> _)"
    elif(eval[regleft[1]-1]=='◊'):
        rs2 = "exist y:(S(x,y) ∧ _)"
    rs = rs1 + rs2

elif(len(regleft)==len(regright) and len(regleft)==3):
    if(eval[regleft[0]-1]=='□'):
        rsc = "forall y:(S(x,y) -> _)"
    elif(eval[regleft[0]-1]=='◊'):
        rsc = "exist y:(S(x,y) ∧ _)"

    if(eval[regleft[1]-1]=='□'):
        rs1 = "forall y:(S(x,y) -> _)"
    elif(eval[regleft[1]-1]=='◊'):
        rs1 = "exist y:(S(x,y) ∧ _)"
    
    if(eval[regleft[2]-1]=='□'):
        rs2 = "forall y:(S(x,y) -> _)"
    elif(eval[regleft[2]-1]=='◊'):
        rs2 = "exist y:(S(x,y) ∧ _)"
    
    rsc = rsc[:-1] + "(" + rs1 + "operador" + rs2 +")"
    


# %%
