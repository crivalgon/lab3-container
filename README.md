Repositorio creado para realizar el lab3 de la asignatura Computacion en la Nube.

Extra: 

De forma similar al ejercicio propuesto, se ha comparado el tiempo de procesado de dos algoritmos diferentes que resuelven el problema de la distancia de Hamming.  Dado un patrón (una cadena), el problema consiste en encontrar las cadenas del mismo tamaño con una distancia de Hamming menor o igual que un cierto valor d.

En el primer caso, tenemos un algoritmo que resuelve el problema de forma iterativa, y en el segundo caso tenemos una solución recursiva que es mucho más costosa a nivel de procesamiento. El coste aumenta cuanto más largo es el patrón y cuanto mayor sea la distancia que se quiere calcular. 

Para comparar el tiempo tardado por cada algoritmo, se han lanzado las dos funciones 100 veces, aumentando cada iteración la longitud del patrón y manteniendo la distancia a 2. 

Despues se han ejecutado las dos funciones desde el container de Singularity. En extra/RESULTADOS.txt aparece el tiempo máximo de cada uno de los dos algoritmos. Se puede apreciar que cuando se ejecuta desde el container se incrementa ligeramente este tiempo, pero el resultado es muy similar a la ejecución nativa.  Los algoritmos se han lanzado en el nodo ochoa. 

