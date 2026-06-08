# Pipeline de Consolidación Masiva - Farmacias YZA

Este proyecto implementa un pipeline de Ingeniería de Datos diseñado para centralizar, procesar y automatizar el flujo de información de ventas proveniente de múltiples sucursales distribuidas.

## Arquitectura del Sistema

1. **Ingesta y Consolidación (`consolidar.py`):** Escanea de forma dinámica directorios locales buscando archivos fuente en formato CSV. Extrae metadatos a partir del nombre del archivo para identificar la sucursal de origen, unifica las estructuras en un DataFrame maestro y calcula los indicadores de ingresos financieros.
2. **Persistencia de Datos (SQL):** El set de datos consolidado se inyecta de forma automática en una base de datos relacional centralizada (`SQLite3`), sobreescribiendo de manera segura los registros del día.
3. **Módulo de Analítica (`analisis_yza.py`):** Realiza agregaciones de datos para identificar el rendimiento económico por zona comercial y la rotación física de inventario en masa.
4. **Automatización (Bash & Crontab):** Un script contenedor en Shell (`ejecutar_pipeline.sh`) gestiona el ciclo de vida del entorno virtual y la ejecución del pipeline. Este proceso está programado a nivel de sistema operativo para ejecutarse de forma autónoma en segundo plano todas las noches a las 23:00 horas.

## Requisitos e Instalación

El proyecto se ejecuta sobre un entorno aislado de Python 3.12+ en sistemas basados en Linux.

```bash
# Clonar el repositorio e ingresar al directorio
git clone git@github.com:bates96/yza-consolidacion-multisucursal.git
cd yza-consolidacion-multisucursal

# Configurar el entorno virtual e instalar dependencias
python3 -m venv env
source env/bin/activate
pip install pandas sqlalchemy
