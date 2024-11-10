import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

# Leer los datos desde el archivo CSV
df = pd.read_csv('tennis.csv')

# Mostrar las primeras filas del archivo CSV para asegurarse de que los datos se leyeron correctamente
print(df.head())

# Convertir las columnas categóricas a variables numéricas
df['outlook'] = df['outlook'].map({'sunny': 0, 'overcast': 1, 'rainy': 2})
df['temp'] = df['temp'].map({'hot': 0, 'mild': 1, 'cool': 2})
df['humidity'] = df['humidity'].map({'high': 0, 'normal': 1})
df['windy'] = df['windy'].map({'false': 0, 'true': 1})
df['play'] = df['play'].map({'no': 0, 'yes': 1})

# Establecer los predictores (X) y la variable de respuesta (y)
X = df[['outlook', 'temp', 'humidity', 'windy']]  # Predictores
y = df['play']  # Variable a predecir

# Crear el modelo de árbol de decisión
model = DecisionTreeClassifier()

# Entrenar el modelo
model.fit(X, y)

# Visualizar el árbol de decisión
tree.plot_tree(model, feature_names=X.columns, class_names=['no', 'yes'], filled=True)

# Realizar predicciones con el modelo
predicciones = model.predict(X)

# Mostrar las predicciones
print("Predicciones:", predicciones)

# Mostrar el árbol de decisión en formato texto
print("\nÁrbol de decisión:")
tree_rules = tree.export_text(model, feature_names=X.columns.tolist())
print(tree_rules)
