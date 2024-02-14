import random


lista=[]
print (type(lista))
lista=100
print (type(lista))

#identacion
def filllist(lista,tam):
    for i in range(tam):
        num=random.randrange(100)
        lista.append(num)
    return lista

mylist=[]
filllist(mylist,10)
print(mylist)

def funcioncita():
    print('Hola  Mundo')
    
funcioncita()