import pandas as pd

print("====================================================")
# 1. Cargar el archivo consolidado
df = pd.read_csv("consolidado_merida.csv")

# 2. Análisis 1: Ingresos totales por Sucursal
# Agrupamos por sucursal, sumamos la columna ingresos y ordenamos de mayor a menor
reporte_sucursales = df.groupby('sucursal')['ingresos'].sum().reset_index()
reporte_sucursales = reporte_sucursales.sort_values(by='ingresos', ascending=False)

print(" RENDIMIENTO ECONÓMICO POR SUCURSAL ")
print(reporte_sucursales.to_string(index=False))
print("----------------------------------------------------")

# 3. Análisis 2: El Producto Más Vendido (en cantidad de unidades)
reporte_productos = df.groupby('producto')['cantidad'].sum().reset_index()
reporte_productos = reporte_productos.sort_values(by='cantidad', ascending=False)

print("PRODUCTOS MÁS DEMANDADOS EN MÉRIDA")
print(reporte_productos.to_string(index=False))
print("====================================================")
