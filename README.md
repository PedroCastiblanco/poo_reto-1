# Reto 1
### Punto 1:
Se utilizó un `for` para separar la entrada en una lista de manera que los dos números  y el símbolo del operador quedaran separados para ser usados en las operaciones posteriores, con  el símbolo del operador usado para comprobar que tipo de operación se realizara con un `if` y mostrar el resultado.
### Punto 2:
Se determina si la longitud de la palabra es par o impar y luego se compara la última letra con la primera con un `for` para tener un `if` con condición `a[i]!=a[-(i+1)]`  al momento de que se entra a este `if` se imprime que no es palíndromo y luego se da un `break` , si el `for`  acaba sin entrar al `if` se imprimirá que si es palíndromo.
### Punto 3:
Se separan los números en una lista de enteros con una función que los separa cuando el carácter es  `“,”` luego entra en la función en la cual se crea una lista donde se saca módulo de todos los números del 1 hasta ese numero para después contar cuales elementos de la lista son iguales a 0 si existen solo 2 el número se agrega a otra lista, este proceso se repite con toda la lista de entrada y al final se imprime la lista que solo tenía los números con solo 2 módulos iguales a 0.
### Punto 4:
Se separa la entrada en una lista de enteros para luego entrar en la función que tiene un `for` por el cual se suman el elemento  `i` con el elemento `i+1`  y se agregan en una lista a la cual se le busca el máximo con la función `max()` para luego imprimir ese numero.
### Punto 5: 
Se separan la entrada en una lista de strings y lue3go se crea una lista que le corresponden los  mismos elemento pero ordenado cada elemento alfabéticamente para luego en un `for` compara los elementos de esta segunda lista y cuando sean iguales agregarlos a una lista y cambiar el elemento correspondiente de la segunda lista para evitar repeticiones,  esta función se puede usar para cuando hay más de un grupo de palabras con los mismos caracteres en estos casos la salida mostrara una lista con listas como elementos que representa cada grupo.
