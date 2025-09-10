# 🚀 Proyecto ETL - Ventas

Este proyecto implementa un **pipeline ETL (Extract, Transform, Load)** en Python usando un archivo de datos de ventas (`Sale_G_limpio.csv`).  
El objetivo es extraer datos de un archivo CSV, transformarlos (validación y limpieza mínima) y cargarlos en dos destinos:

- Un archivo CSV limpio
- Una base de datos SQLite

---

## 📂 Estructura del proyecto

│
├── Config/
│ └── config_sale.py # Configuración de rutas y parámetros
│
├── Extract/
│ ├── extractor_sale.py # Clase para extracción de datos
│ └── Files/
│ └── Sale_G_limpio.csv # Archivo CSV de ventas limpio
│
├── Transform/
│ └── transformer_sale.py # Clase para validación y transformación
│
├── Load/
│ └── loader_sale.py # Clase para carga en CSV y SQLite
│
├── main_sale.py # Script principal que ejecuta el ETL
└── requirements.txt # Dependencias del proyecto

---

## ⚙️ Dependencias

Este proyecto requiere **Python 3.10+** y las siguientes librerías:

- `pandas`
- `sqlite3` (incluido en Python por defecto)

Instalación:

```bash
pip install -r requirements.txt

Ejecucion del ETL 

* python main_sale.py

El flujo será:

Extracción: se leen los datos desde Extract/Files/Sale_G_limpio.csv.

Transformación: se eliminan duplicados y se rellenan valores nulos.

Carga:

Se guarda un nuevo CSV en:
Extract/Files/sales_clean_output.csv

Se guarda en SQLite en:
Extract/Files/sales_data.db (tabla sales_clean)

Para consultar los datos de la BD dentro de la consola 

* sqlite3 Extract/Files/sales_data.db

Y continuamente 

.tables
SELECT * FROM sales_clean LIMIT 10;

Esto hara que mostrata por tabla los primeros diez registros de la base de datos