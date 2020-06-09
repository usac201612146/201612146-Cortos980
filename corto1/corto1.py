#Secuencias Collatz
#201612146
# de 2 hasta 146


def secu_N(n):
#ve si el numero es par o no 
    if n%2==0: 
        a=n/2
        return a #retorna el valor si es par
    else:
        b=3*n+1
        return b #retorna el valor si es impar

m=146
c=[]
def fileAppend(fileName = 'corto.txt'):
    
    #Si el archivo 'fileName' no existe, se crea uno nuevo con ese nombre.
    archivo = open(fileName,'a') #Abrir para agregar a archivo existente
    archivo.write('\n\nNuevo evento de append...\n')
    print('Espere, agregando datos al archivo...')
   
    for n in range(2,m):
        c.append(secu_N(n)) #guarda los numeros en esta lista 
        archivo.write(str(n),str(c)+'\n')
        


    archivo.close() #Siempre cerrar el archivo al finalizar la escritura
    print('\n\nAppend finalizado')