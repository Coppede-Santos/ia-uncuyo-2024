# Trabajo Práctico 6: Satisfacción de restricciones 
### Describir en detalle una formulación CSP para el Sudoku
Para la formulación de CSP para sudoku se debería implementar como variables las distintas casillas, el dominio de posibles valores que podría tener cada variable son números entre el cero al nueve, y cada una debería tener como restricción no tener el mismo valor que alguna variable perteneciente a su columna, fila o a su cuadricula.
### Utilizar el algoritmo AC-3 para demostrar que la arco consistencia puede detectar la inconsistencia de la asignación parcial WA=red, V=blue para el problema de colorear el mapa de Australia.


### ¿Cuál es la complejidad en el peor caso cuando se ejecuta AC-3 en un árbol estructurado CSP? (i.e. cuando el grafo de restricciones forma un árbol: cualquiera dos variables están relacionadas por a lo sumo un camino).


###  AC-3 coloca de nuevo en la cola todo arco (Xk, Xi) cuando cualquier valor es removido del dominio de Xi incluso si cada valor de Xk es consistente con los valores restantes de Xi. Supongamos que por cada arco (Xk, Xi) se puede llevar la cuenta del número de valores restantes de  Xi que sean consistentes con cada valor de Xk. Explicar cómo actualizar ese número de manera  eficiente y demostrar que la arco consistencia puede lograrse en un tiempo total O(n^2d^2).


### Demostrar la correctitud del algoritmo CSP para árboles estructurados (sección 6.5, AIMA 3ra edición). Para ello, demostrar:
#### a) Para un CSP cuyo grafo de restricciones es un árbol, la 2-consistencia (consistencia de arco) implica n−consistencia, siendo n el número total de variables.
#### b) Argumentar por qué lo demostrado en 5a es suficiente.


### 