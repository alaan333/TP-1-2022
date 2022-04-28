#Desarrollar una función que permita convertir un número romano en un número decimal.

valores= {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

def  conversion_numeros(romano):
    if (len(romano)==1):                            
        #print(valores[romano])
        return valores[romano]
    elif (valores[romano[0]] >= valores[romano[1]]):                 
        return  conversion_numeros(romano[1:]) + valores[romano[0]]      #Ej: 'XVI'  [:1]=VI + X        
    elif (valores[romano[0]] < valores[romano[1]]):
        return  conversion_numeros(romano[1:]) - valores[romano[0]]         
    
n_r=input('Ingrese un numero romano: ').upper()          #upper para poder ingresar minusculas o mayusculas
if conversion_numeros(n_r):
    print(conversion_numeros(n_r))

