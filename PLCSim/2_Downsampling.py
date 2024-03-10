import pandas as pd
import matplotlib.pyplot as plt

Datos = pd.read_csv('Ventas.csv')
Datos.head()  
Datos.plot.scatter(x='Mes',y='Ventas')
plt.show()

