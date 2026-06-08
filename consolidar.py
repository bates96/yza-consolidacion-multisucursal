import pandas as pd
import glob
import os
from sqlalchemy import create_engine # <-- NUEVA IMPORTACIÓN

# [Todo tu código anterior se queda exactamente IGUAL hasta el paso 4]
ruta_busqueda = os.path.join("datos_sucursales", "*.csv")
archivos_csv = glob.glob(ruta_busqueda)
lista_dataframes = []

for archivo in archivos_csv:
    df_sucursal = pd.read_csv(archivo)
    nombre_sucursal = os.path.basename(archivo).replace("ventas_", "").replace(".csv", "").upper()
    df_sucursal['sucursal'] = nombre_sucursal
    lista_dataframes.append(df_sucursal)

df_maestro = pd.concat(lista_dataframes, ignore_index=True)
df_maestro['ingresos'] = df_maestro['cantidad'] * df_maestro['precio_unitario']
print("--> ¡Consolidación masiva terminada exitosamente!")

# =======================================================
# ACTUALIZADO: PASO 5. Guardar en CSV y en Base de Datos SQL
# =======================================================
df_maestro.to_csv("consolidado_merida.csv", index=False)

print("--> Conectando a la Base de Datos Central de YZA...")
engine = create_engine("sqlite:///yza_merida_master.db")

# Guardamos el dataframe maestro en la tabla 'reporte_global'
df_maestro.to_sql("reporte_global", con=engine, if_exists="replace", index=False)
print("--> ¡Éxito! Todos los datos masivos fueron cargados en 'yza_merida_master.db'.")
