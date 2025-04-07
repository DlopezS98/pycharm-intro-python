import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos desde un CSV (simulación)
data = pd.DataFrame({
    'producto': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    'categoria': ['Electrónica', 'Hogar', 'Electrónica', 'Deportes', 'Hogar', 'Juguetes', 'Deportes', 'Electrónica', 'Juguetes', 'Hogar'],
    'ventas': [500, 300, 700, 200, 400, 100, 350, 900, 150, 600]
})

print(data.head())

# Ordenar por ventas
top_ventas = data.sort_values(by='ventas', ascending=False)



# Mostrar los 5 productos más vendidos
print(top_ventas.head())

# Agrupar las ventas por categoría
ventas_por_categoria = data.groupby('categoria')['ventas'].sum()

# Crear el histograma
plt.figure(figsize=(8, 5))
ventas_por_categoria.plot(kind='bar', color='skyblue', edgecolor='black')
plt.xlabel('Categoría')
plt.ylabel('Total de Ventas')
plt.title('Ventas Totales por Categoría')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Mostrar gráfico
plt.show()



# Guardar los datos ordenados en un archivo CSV
top_ventas.to_csv('ventas_ordenadas.csv', index=False)

# Guardar el resumen por categoría
ventas_por_categoria.to_csv('ventas_por_categoria.csv')

print("Archivos guardados correctamente.")
