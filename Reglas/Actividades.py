#%%
# Importar módulos
import pandas as pd
from one_r import OneR
from prism_rules import PrismRules

#%%
# Lectura de los datos
datos = pd.read_csv('adult_data.csv', sep=';')

# Imprimir info de los datos
datos.info()
display(datos.head())

#%%
# OneR y Prism no pueden trabajar con datos faltantes.
# En este ejemplo simplemente se eliminan las filas con datos faltantes

datos_limpio = datos.dropna()
datos_limpio.info()

#%%
# Seleccionar el atributo "target" a predecir

target = "Class"

#%%
# Obtener un modelo con el algoritmo OneR

oner = OneR()
results = oner.fit(datos_limpio.drop(columns=[target]), datos_limpio[target])

print(oner)
print(results[oner.ideal_variable])

#%%
# Obtener un modelo con el algoritmo Prism

prism = PrismRules()
results = prism.get_prism_rules(datos_limpio, target)
