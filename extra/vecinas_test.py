from time import time
#import matplotlib
#import matplotlib.pyplot as plt
# Vecinas a distancia 20 - Calcular tiempo de un algoritmo similar al de los k-mers

def vecinas1(patron):
 
    vecinasd1=[]
    patron = patron.upper()

    for indice in range(0,len(patron)):     # Iteramos por los índices de la cadena:

        nucleotidos=['A','C','G','T']
        nucleotidos.remove(patron[indice])  # Eliminamos la base correspondiente al índice, de nucleótidos:
        vecina_candidata = patron           
        for nucleotido in nucleotidos:      # Iteramos por cada base !=  patrón[índice]

        	vecina_candidata=vecina_candidata[:indice]+nucleotido+patron[indice+1:] # Cambiamos patron[indice] por nucleótido
        	vecinasd1.append(vecina_candidata) # Añadimos la vecina a la lista vecinasd1

    return vecinasd1


def vecinas_d(patron,d):
   
    if d == 1:
        return set(vecinas1(patron))
    elif d == 0: 
        return patron
    else:
        vecinas=[]
    # Calculamos las vecinas a distancia 1, añadimos a vecinas_d1
        vecinas_d1=vecinas1(patron)
    # Calculamos vecinas a distancia d:

    # A cada elemento de vecinas_d1 calculamos sus vecinas a distancia 1 y añadimos
    # a vecinas_d1; esto se repite tantas veces como distancia haya. Ejemplo: Si AAT es vecina a 
    # distancia 1 de AAA, una vecina a distancia 2 de AAA será ATT, que es vecina a 1 de AAA. Al convertir
    # a set, se eliminan posibles repeticiones. 

        for i in range(1,d):   
            for cadena in vecinas_d1:  
                vecinas+=vecinas1(cadena)
   
        vecinas_set=set(vecinas)
        return vecinas_set



# Ahora lo mismo pero con recursión

def vecinas_rec(patron,d):
    if d == 0:
        return [patron]
    else:
        vecinas=[patron]
        for i in range(0,len(patron)):
    
            vecina=patron
            nucleotidos=['A','C','G','T']
            nucleotidos.remove(patron[i]) 
            for t in nucleotidos:
                if patron[i] not in nucleotidos:
                    vecina=vecina[:i]+t+patron[i+1:]
                    vecinas.append(vecina)
                for u in range(1,d):
                    vecinas= vecinas + vecinas_rec(vecina,d-1)
                
    return vecinas

iteraciones_tiempo=[]
for i in range(1,100):
    patron='A'*i
    inicio=time()
    vecinas_d(patron,2)
    final=time()
    iteraciones=i
    iteraciones_tiempo.append(final-inicio)

print(max(iteraciones_tiempo))

recursion_tiempo=[]
for i in range(1,100):
    patron='A'*i
    inicio=time()
    vecinas_rec(patron,2)
    final=time()
    recursion_tiempo.append(final-inicio)

print(max(recursion_tiempo))

#plt.plot(recursion_tiempo)
#plt.plot(iteraciones_tiempo)
#plt.savefig('iter_vs_rec.png')
