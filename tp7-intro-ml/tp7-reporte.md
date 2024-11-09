# TP7- Introducción

## For each of parts (a) through (d), indicate whether we would generally expect the performance of a fexible statistical learning method to be better or worse than an infexible method. Justify your answer.
### (a) The sample size n is extremely large, and the number of predictors p is small.

Mejor, ya que con una gran cantidad de datos, un método flexible no se verá limitado por una muestra pequeña que pueda generar sesgo y logrará capturar mejor la variabilidad y los patrones en los datos.

### (b) The number of predictors p is extremely large, and the number of observations n is small.

Peor, ya que en este caso un método flexible corre el riesgo de ajustarse demasiado a los datos, generando sobreajuste debido al alto número de predictores en comparación con la cantidad limitada de observaciones.

### (c) The relationship between the predictors and response is highly non-linear.

Mejor, ya que un método flexible se puede ajustar mejor a las relaciones complejas y no lineales, mientras que uno inflexible podría no capturar adecuadamente dichas características.

### (d) The variance of the error terms, i.e. σ2 = Var(ϵ), is extremely high.

Peor, ya que un método flexible tenderá a sobreajustar los datos debido a la alta variabilidad en los errores, capturando ruido en lugar de patrones consistentes.

## Explain whether each scenario is a classifcation or regression problem, and indicate whether we are most interested in inference or prediction. Finally, provide n and p.
### (a) We collect a set of data on the top 500 frms in the US. For each frm we record proft, number of employees, industry and the CEO salary. We are interested in understanding which factors  afect CEO salary.

Este es un problema de regresión, enfocado en la inferencia, con un 
𝑛
=
500
n=500 y un 
𝑝
=
4
.

### (b) We are considering launching a new product and wish to know whether it will be a success or a failure. We collect data on 20  similar products that were previously launched. For each product we have recorded whether it was a success or failure, price charged for the product, marketing budget, competition price,  and ten other variables. 

Es un problema de clasificación, orientado a la predicción, con n=20 y un p=15.

### (c) We are interested in predicting the % change in the USD/Euro exchange rate in relation to the weekly changes in the world stock markets. Hence we collect weekly data for all of 2012. For each week we record the % change in the USD/Euro, the % change in the US market, the % change in the British market, and the % change in the German market.

Es un problema de regresión, centrado en la predicción, con n=52 y un p=4.

## What are the advantages and disadvantages of a very fexible (versus a less fexible) approach for regression or classifcation? Under what circumstances might a more fexible approach be preferred to a less fexible approach? When might a less fexible approach be preferred?

Las ventajas de un método flexible incluyen la capacidad para ajustarse bien a relaciones complejas y no lineales, especialmente cuando se dispone de una gran cantidad de datos. Esto permite que el modelo sea más preciso al capturar patrones sutiles en los datos. Los métodos flexibles son ideales cuando se enfrentan a conjuntos de datos extensos y con relaciones intrincadas entre los predictores.

Por otro lado, los métodos menos flexibles son preferibles cuando las relaciones en los datos son lineales o simples, cuando se tiene una cantidad limitada de datos o cuando los recursos computacionales son limitados. Al ser menos propensos a sobreajustarse, los métodos inflexibles ofrecen mayor estabilidad y generalización en estos contextos.
## Describe the diﬀerences between a parametric and a non-parametric statistical learning approach. What are the advantages of a parametric approach to regression or classification (as opposed to a non-parametric approach)? What are its disadvantages?

**Modelos Paramétricos**: En los modelos paramétricos, se supone una forma funcional específica, generalmente una relación matemática definida que se asume que describe bien el comportamiento de los datos. El objetivo es ajustar esta forma predefinida a los datos estimando un conjunto fijo de parámetros. Los modelos paramétricos son comunes en estadística y en aprendizaje automático, y suelen ser adecuados cuando se tiene una idea clara de la estructura que siguen los datos. 

**Modelos No Paramétricos**: En los modelos no paramétricos, no se hace suposición alguna sobre la forma funcional de los datos. En su lugar, el modelo se ajusta de manera flexible para adaptarse a la estructura de los datos sin imponer una fórmula predefinida. Este enfoque permite una mayor adaptabilidad, especialmente útil cuando la estructura de los datos es compleja o desconocida, y resulta en modelos que pueden seguir patrones complejos.

**Ventajas de los Modelos Paramétricos**:  
- **Simples y Rápidos**: Al tener una forma fija y menos parámetros, son más rápidos de entrenar y menos costosos computacionalmente.
- **Interpretables**: La estructura predefinida facilita la interpretación y la comprensión de los parámetros, lo que permite entender mejor las relaciones que modela.
  
**Desventajas de los Modelos Paramétricos**:  
- **Potencialmente Inexactos**: Si la forma funcional asumida no es adecuada para los datos, el modelo puede resultar inexacto, generando sesgo y limitando su precisión.

**Ventajas de los Modelos No Paramétricos**:  
- **Capacidad de Ajuste a Datos Complejos**: Al no estar limitados por una estructura fija, estos modelos pueden ajustarse mejor a los datos, capturando relaciones complejas y patrones intrincados que los modelos paramétricos pueden pasar por alto.
  
**Desventajas de los Modelos No Paramétricos**:  
- **Propensos al Sobreajuste**: Debido a su flexibilidad, los modelos no paramétricos pueden ajustarse demasiado a los datos de entrenamiento, capturando ruido o variaciones específicas de estos datos y disminuyendo su capacidad de generalización.

## The table below provides a training data set containing six observations, three predictors, and one qualitative response variable.

| Obs. | X1  | X2  | X3  |  Y   |
|------|----|----|----|-------|
|  1   |  0 |  3 |  0 |  Red  |
|  2   |  2 |  0 |  0 |  Red  |
|  3   |  0 |  1 |  3 |  Red  |
|  4   |  0 |  1 |  2 | Green |
|  5   | -1 |  0 |  1 | Green |
|  6   |  1 |  1 |  1 |  Red  |

### Suppose we wish to use this data set to make a prediction for Y when X1 = X2 = X3 = 0 using K-nearest neighbors.

#### (a) Compute the Euclidean distance between each observation and the test point, X1 = X2 = X3 = 0.

| **Observación** | **Distancia Euclidiana** |
|------------------|---------------------------|
| 1                | 3                         |
| 2                | 2                         |
| 3                | \(\sqrt{10}\)             |
| 4                | \(\sqrt{5}\)              |
| 5                | \(\sqrt{2}\)              |
| 6                | \(\sqrt{3}\)              |

#### (b) What is our prediction with K = 1? Why?

Verde, ya que el punto más cercano es verde.

#### (c) What is our prediction with K = 3? Why?

Roj, ya que dos de los tres vecinos más cercanos son rojos.

#### (d) If the Bayes decision boundary in this problem is highly non-linear, then would we expect the best value for K to be large or small? Why?

Se espera que el valor de k sea pequeño. Ya que un valor de k grande suavisaria demasiado la frontera de decision y se perderia mucha información.








