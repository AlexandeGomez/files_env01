#%%
import matplotlib.pyplot as plt
import numpy as np

#%%
PATH = "/home/jhonatang/Documentos/PYTHON3/files_env01/"
ls = []
with open(PATH+"SQNR_list.txt", "r") as file:
    for line in file:
        ls.append(line[1:-2].split(","))

ls = ls[0]

lista = []
for i in range(len(ls)):
    lista.append(float(ls[i]))

lista = np.array(lista)
media = []
for i in range(len(lista)):
    media.append(lista.mean())

# %%

plt.plot(lista)
plt.plot(media)
plt.show()
# %%
