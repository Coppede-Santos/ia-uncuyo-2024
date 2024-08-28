## 2.10 Consider a modified version of the vacuum environment in Exercise 2.8, in which the agent is penalized one point for each movement.
### a. Can a simple reflex agent be perfectly rational for this environment? Explain.
No, en un entorno de estas condiciones no sería realmente racional, ya que podría existir el caso de que limpie todas las casillas y de igual forma se continue moviendo y siendo penalizado, lo que no parece ser un comportamiento razonable.
### b.What about a reflex agent with state? Design such an agent
Si solo pudiera almacenar información sin tener información previa sobre el entorno, seguiría sin ser racional porque no tendría forma de saber si quedan casillas por limpiar o no.
### c.How do your answers to a and b change if the agent’s percepts give it the clean/dirty status of every square in the environment?
Entonces un agente podría ser racional, porque podría moverse deliberadamente hacia los espacios que están sucios y en caso de que exista ninguno sucio podría frenarse, por lo que seria racional independiente de si tiene estados o no.
## 2.11 Consider a modified version of the vacuum environment in Exercise 2.8, in which the geography of the environment—its extent, boundaries, and obstacles—is unknown, as is the initial dirt configuration. (The agent can go Up and Down as well as Left and Right.)
### a. Can a simple reflex agent be perfectly rational for this environment? Explain.
Podría ser racional dependiendo las medidas de desempeño que se utilicen, en caso de que no se penalice por sus movimientos y solo se evalué la cantidad de casillas que limpio, un agente reflexivo simple podría tener un buen desempeño.
### b. Can a simple reflex agent with a randomized agent function outperform a simple reflex agent? Design such an agent and measure its performance on several environments
Como se puede observar en el informe tp2-results.md un agente aleatorio tendría un desempeño similar a un agente reflexivo, aunque ligeramente inferior, para entornos chicos, mientras que para entornos de gran tamaño el agente reflexivo simple tendría un desempeño notablemente superior. 
### c. Can you design an environment in which your randomized agent will perform poorly? Show your results.
Si, seria en entornos grandes, y específicamente con una baja probabilidad de suciedad, como lo es un entorno de 128x128 con una probabilidad de suciedad de 0.1 como podemos ver en el informe.
### d. Can a reflex agent with state outperform a simple reflex agent?
Si, un agente reflexivo con estados podría guardar la información de las casillas por las que paso y probablemente tenga un mejor desempeño que un agente reflexivo simple. 
