listamaria=[]
listajuanita=[]

for i in range(2):
    producto=input("ingrese el producto de maria ")
    listamaria.append(producto)

for i in range(2):
    producto=input("ingrese el producto de juanita ")
    listajuanita.append(producto)

productosComun=[]
for i in range(2):
    for j in range(2):
        if   listajuanita[i]==listamaria[j]:
            productosComun.append(listajuanita[i])



listaUNida=listamaria+listajuanita

print(listaUNida)
print(productosComun)