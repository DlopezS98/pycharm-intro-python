import pandas as pd
import matplotlib.pyplot as plt

data = {
    'product':  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    'category': ['Electrónica', 'Hogar', 'Electrónica', 'Deportes', 'Hogar', 'Juguetes', 'Deportes', 'Electrónica', 'Juguetes', 'Hogar'],
    'ventas': [500, 300, 700, 200, 400, 100, 350, 900, 150, 600]
}
df_ventas = pd.DataFrame(data)

# print(df_ventas.head())

ventas_ordernadas = df_ventas.sort_values(by='ventas', ascending=False)

# print(ventas_ordernadas.head())

ventas_por_categoria = ventas_ordernadas.groupby('category')['ventas'].sum()

print(ventas_por_categoria.head())

# Crear el histograma
plt.figure(figsize=(8, 5))
ventas_por_categoria.plot(kind='bar', color='skyblue', edgecolor='black', linewidth=0.5)
plt.xlabel('Categoría')
plt.ylabel('Total de Ventas')
plt.title('Ventas Totales por Categoría')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Mostrar gráfico
plt.show()

# Line Chart
plt.figure(figsize=(8, 5))
ventas_por_categoria.plot(kind='line', marker='o', linestyle='-', color='blue', linewidth=2)
plt.xlabel('Categoría')
plt.ylabel('Total de Ventas')
plt.title('Ventas Totales por Categoría (Línea)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=0)
plt.show()

# Pie Chart
plt.figure(figsize=(8, 5))
ventas_por_categoria.plot(
    kind='pie',
    autopct='%1.1f%%',
    colors=['lightblue', 'lightgreen', 'lightcoral', 'orange', 'purple']
)
plt.ylabel('')  # Remove the default y-label
plt.title('Distribución de Ventas por Categoría')
plt.show()


df_ventas.to_csv("Ventas.csv", index_label="INDICE")
ventas_por_categoria.to_csv("Ventas_por_categoria.csv")