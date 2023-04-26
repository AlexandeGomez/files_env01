#%%

print(chr(9633))
print(chr(9674))
print(chr(126))
print(chr(8744))
print(chr(8743))

#%%

s1 = "□(A)x◊(B)"

s2 = "◊(A)"

s3 = "◊(□(p and p) implies ◊(q or q))" # no reconce

s4 = "□(□A)x◊(□B)"

#%%
eval = s3

aux = ""
for char in eval:
    aux = char + aux

#%%

fse = (eval.find("("), eval.find(")"))
lse = (len(eval)-(aux.find(")")+1), len(eval)-(aux.find("(")+1))

print(fse[0]==lse[1] and fse[1]==lse[0])
# %%

r1 = [s3.find("("), s3.find(")")]

if(s3[r1[0]+1:r1[1]].find("(")==-1):
    print("clase 1")
else:
    print("encontrado")


    
# %%

if(eval[0]=="□"):
    str1 = "forall(S(x,y)imples_)"
    
elif (eval[0]=="◊"):
    str1 = "every(S(x,y)and_)"

