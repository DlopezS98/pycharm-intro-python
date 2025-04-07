import pandas as pd
import matplotlib.pyplot as plt
from bs4.diagnose import rword

file_path = "./Data/Pen Sales Data.xlsx"
df_pen_sales = pd.read_excel(file_path, sheet_name="Pen Sales")

# print(df_pen_sales)

# Análisis de costos de envío
df_avg_pen_costs = df_pen_sales.groupby("Item")["Shipping Cost"].mean().sort_values()
# print(df_avg_pen_costs)

plt.figure(figsize=(10, 5))
df_avg_pen_costs.plot(kind="barh", color="purple")
plt.title("Costo de envio promedio por producto")
plt.xlabel("Coste medio de envio")
plt.ylabel("Tipo de producto")
# plt.show()

# 3.	Ranking de popularidad de bolígrafos
# Tarea: Identificar el tipo de bolígrafo que se compra con más frecuencia.
# Pasos:
# •	Cuente el número de compras por artículo.
# •	Ordenar en orden descendente.
# •	Traza un gráfico de barras horizontales para mayor claridad.
# •	Visualización: 📊 Gráfico de barras horizontales (bolígrafos más vendidos)

conteo_de_productos = df_pen_sales["Item"].value_counts()
# print(conteo_de_productos)
plt.figure(figsize=(10, 5))
conteo_de_productos.plot(kind="barh", color="green")
plt.title("Ranking de popularidad de productos")
plt.xlabel("Cantidad de ventas")
plt.ylabel("Tipo de producto")
plt.gca().invert_yaxis()
# plt.show()

# 4.	Análisis de Tiempo de Entrega
# Tarea: Calcular el tiempo medio de entrega para cada tipo de bolígrafo.
# Pasos:
# •	Calcular tiempo de entrega = Fecha de entrega - Fecha de compra.
# •	Agrupe por artículo y encuentre el tiempo medio de entrega.
# •	Traza un gráfico de barras para comparar los tiempos de entrega.
# •	Visualización: ⏳ Gráfico de barras (tiempo medio de entrega por tipo de bolígrafo)

# Purchase Date y Delivery Date
# print(df_pen_sales["Delivery Date"])
# print(df_pen_sales["Purchase Date"])

tiempo_de_entrega = (df_pen_sales["Delivery Date"] - df_pen_sales["Purchase Date"]).dt.days
df_pen_sales["Tiempo de entrega"] = tiempo_de_entrega
tiempo_medio_de_entrega = df_pen_sales.groupby("Item")["Tiempo de entrega"].mean().sort_values()
plt.figure(figsize=(10, 5))
tiempo_medio_de_entrega.plot(kind="bar", color="orange")
plt.title("Tiempo medio de entrega de productos")
plt.xlabel("Tipo de producto")
plt.ylabel("Tiempo medio de entrega")
plt.xticks(rotation=45, ha="right")
# plt.show()

# 5.	Análisis de sentimiento de las reseñas
# Tarea: Extraer el sentimiento de las opiniones de los clientes.
# Pasos:
# •	Dividir la columna Review para separar el nombre del revisor y el comentario.
# •	Realizar un análisis básico de sentimientos (contar las apariciones de palabras positivas como amor, genial, bueno frente a palabras negativas como malo, disgusto).
# •	Genere una nube de palabras o un gráfico circular de sentimientos.
# •	Visualización: 🥧 Gráfico de pastel o circular (críticas positivas vs. negativas)
# Nombre de la persona | Este producto no me gusto porque ....

# review = df_pen_sales["Review"]
# reviews = ["User|This product is amazing", "user|I love this product", "user|This product sucks!"]
# positive_words = ["I like it", "i love it", "love", "good", "excellent", "best", "amazing"]

plt.figure(figsize=(6, 6))
