#  El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u
#  otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
#  objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con
#  ayuda de la fuerza” realizar las siguientes actividades:
#  a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
#  queden más objetos en la mochila;
#  b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar
#  para encontrarlo;
#  c. Utilizar un vector para representar la mochila.


#  C
mochila=['obj1','obr2','bosdbsod','ereas','sable de luz','obj3','obj4','obj5','obj6','obj7']

objeto_a_buscar=input('Ingrese el objeto que necesita: ').lower()

#  A
def usar_la_fuerza(mochila,buscado):
    if (len(mochila)==0):
        return -1
    elif(buscado==mochila[-1]):
        return len(mochila)-1
    else:
        return usar_la_fuerza(mochila[:-1],buscado)

contador=usar_la_fuerza(mochila,objeto_a_buscar)      

print()
#  B
if (contador==0):
    print(f'Se encontro el {objeto_a_buscar}.')
    print(f'{objeto_a_buscar} fue el primer objeto dentro de la mochila.')
elif (contador>0):
    print(f'Se encontro el {objeto_a_buscar}.')
    print(f'Se necesitaron sacar {contador} objetos para encontrarlo.')
else:
    print(f'No hay ningun {objeto_a_buscar} dentro de la mochila.')
print()













