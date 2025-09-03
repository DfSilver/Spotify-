# 🎵 Spotify ETL Pipeline

Un pipeline ETL (Extract, Transform, Load) completo y robusto para procesar datasets de canciones de Spotify. Este proyecto está diseñado para limpiar, transformar y preparar datos de música para análisis posteriores.

## 📋 Tabla de Contenidos

- [Características](#características)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Instalación](#instalación)
- [Uso Rápido](#uso-rápido)
- [Configuración](#configuración)
- [Módulos Principales](#módulos-principales)
- [Transformaciones Incluidas](#transformaciones-incluidas)
- [Archivos de Salida](#archivos-de-salida)
- [Ejemplos](#ejemplos)

## ✨ Características

- **📥 Extracción automática**: Detecta y carga automáticamente archivos CSV de Spotify
- **🔄 Transformaciones inteligentes**: Limpieza, normalización y enriquecimiento de datos
- **💾 Carga estructurada**: Múltiples formatos de salida para diferentes usos
- **📊 Validación de calidad**: Verificaciones automáticas de integridad de datos
- **⚙️ Altamente configurable**: Configuración flexible mediante archivos de configuración
- **📋 Logging detallado**: Registro completo de todas las operaciones
- **🎯 Análisis específico**: Creación de métricas musicales especializadas

## 🗂️ Estructura del Proyecto

```
SpotifyETL/
├── Extract/
│   └── SpotifyExtract.py      # Módulo de extracción
├── Transform/
│   └── SpotifyTransform.py    # Módulo de transformación  
├── Load/
│   └── SpotifyLoad.py         # Módulo de carga
├── Config/
│   └── configuraciones.py     # Configuración del sistema
├── Files/                     # Directorio de datos
│   ├── [archivos_entrada].csv
│   └── [archivos_salida].csv
├── main.py                    # Pipeline principal
├── limpieza.py               # Script de limpieza existente
└── README.md                 # Esta documentación
```

## 🚀 Instalación

### Requisitos

- Python 3.7+
- pandas
- numpy
- logging

### Instalación de dependencias

```bash
pip install pandas numpy
```

## ⚡ Uso Rápido

### 1. Ejecución básica

```python
# Ejecutar el pipeline completo
python main.py
```

### 2. Uso programático

```python
from main import SpotifyETLPipeline

# Crear pipeline
pipeline = SpotifyETLPipeline(
    data_path="Files/",
    output_path="Files/"
)

# Ejecutar ETL completo
result_df = pipeline.run_full_pipeline()

# El resultado contiene el dataset procesado
print(f"Dataset procesado: {result_df.shape}")
```

## ⚙️ Configuración

### Archivo de configuración

El sistema utiliza `configuraciones.py` para personalizar el comportamiento:

```python
# Paths principales
DATA_PATH = "Files/"
OUTPUT_PATH = "Files/"

# Archivos de entrada soportados
INPUT_FILES = [
    "spotify_data.csv",
    "songs.csv", 
    "tracks.csv"
]

# Configurar transformaciones
TRANSFORMATION_CONFIG = {
    'outlier_method': 'iqr',
    'iqr_multiplier': 3.0,
    'enable_mood_score': True
}
```

### Crear configuración personalizada

```python
from configuraciones import save_config_template

# Crear template de configuración
save_config_template("mi_config.json")
```

## 🔧 Módulos Principales

### 1. SpotifyExtract.py - Extracción

```python
from SpotifyExtract import SpotifyExtractor

extractor = SpotifyExtractor("Files/")
df = extractor.extract_spotify_data("mi_archivo.csv")
```

**Funciones principales:**
- `extract_spotify_data()`: Carga archivo CSV individual
- `extract_multiple_files()`: Carga múltiples archivos
- `validate_spotify_columns()`: Valida estructura de datos
- `get_data_info()`: Información detallada del dataset

### 2. SpotifyTransform.py - Transformación

```python
from SpotifyTransform import SpotifyTransformer

transformer = SpotifyTransformer()
df_clean = transformer.transform_full_pipeline(df)
```

**Funciones principales:**
- `clean_data()`: Limpieza básica (duplicados, columnas)
- `standardize_text_columns()`: Estandarización de texto
- `normalize_numeric_features()`: Normalización 0-1
- `create_popularity_categories()`: Categorías de popularidad
- `create_music_mood_score()`: Score de estado de ánimo
- `handle_outliers()`: Manejo de valores atípicos

### 3. SpotifyLoad.py - Carga

```python
from SpotifyLoad import SpotifyLoader

loader = SpotifyLoader("Files/")
loader.save_processed_data(df, "resultado_final")
```

**Funciones principales:**
- `save_processed_data()`: Guarda dataset principal
- `save_data_splits()`: División train/validation/test
- `save_data_for_analysis()`: Archivos para análisis
- `save_summary_report()`: Reporte de ETL
- `create_data_catalog()`: Catálogo de archivos

## 🔄 Transformaciones Incluidas

### 1. Limpieza Básica
- ✅ Eliminación de duplicados
- ✅ Estandarización de nombres de columnas
- ✅ Manejo de valores nulos

### 2. Estandarización de Texto
- ✅ Limpieza de nombres de artistas y canciones
- ✅ Capitalización consistente
- ✅ Eliminación de espacios extra

### 3. Características Musicales
- ✅ Normalización de características (0-1)
- ✅ Conversión de duración (ms → segundos → minutos)
- ✅ Creación de formato MM:SS

### 4. Enriquecimiento de Datos
- ✅ **Categorías de Popularidad**: Very Low, Low, Medium, High, Very High
- ✅ **Mood Score**: Basado en valence + energy + danceability
- ✅ **Mood Categories**: Sad, Neutral, Happy

### 5. Control de Calidad
- ✅ Detección y eliminación de outliers
- ✅ Validación de rangos de características
- ✅ Verificación de integridad

## 📁 Archivos de Salida

El ETL genera múltiples archivos organizados:

### Archivos Principales
- `spotify_final_dataset.csv` - Dataset procesado completo
- `spotify_etl_report.json` - Reporte detallado del ETL

### Splits de Datos
- `spotify_train_set_[timestamp].csv` - Conjunto de entrenamiento (70%)
- `spotify_validation_set_[timestamp].csv` - Conjunto de validación (15%)
- `spotify_test_set_[timestamp].csv` - Conjunto de prueba (15%)

### Archivos de Análisis
- `spotify_numeric_features_[timestamp].csv` - Solo características numéricas
- `spotify_statistics_[timestamp].csv` - Estadísticas descriptivas
- `data_catalog_[timestamp].json` - Catálogo de todos los archivos

### Logs y Reportes
- `etl_log_[timestamp].log` - Log detallado de ejecución
- `spotify_quality_report.json` - Reporte de calidad de datos

## 📊 Ejemplos de Uso

### Ejemplo 1: ETL Básico

```python
from main import SpotifyETLPipeline

# Pipeline básico
pipeline = SpotifyETLPipeline()
df_result = pipeline.run_full_pipeline(
    input_filename="mi_dataset.csv",
    save_intermediates=True
)

print(f"Procesadas {len(df_result)} canciones")
```

### Ejemplo 2: Configuración Personalizada

```python
from configuraciones import UserConfig

# Personalizar filtros
UserConfig.DATA_FILTERS = {
    'min_duration_ms': 60000,    # Mínimo 1 minuto
    'min_popularity': 20,        # Popularidad mínima 20
    'include_explicit': False    # Sin contenido explícito
}

# Ejecutar con configuración personalizada
pipeline = SpotifyETLPipeline()
df_result = pipeline.run_full_pipeline()
```

### Ejemplo 3: Solo Transformación

```python
from SpotifyTransform import SpotifyTransformer
import pandas as pd

# Cargar datos existentes
df = pd.read_csv("mi_dataset.csv")

# Solo aplicar transformaciones
transformer = SpotifyTransformer()
df_clean = transformer.transform_full_pipeline(df)

# Guardar resultado
df_clean.to_csv("dataset_transformado.csv", index=False)
```

### Ejemplo 4: Verificación de Calidad

```python
from main import SpotifyETLPipeline

pipeline = SpotifyETLPipeline()

# Cargar datos procesados
df = pipeline.loader.load_processed_data("spotify_final_dataset.csv")

# Verificar calidad
quality_report = pipeline.run_data_quality_check(df)

print(f"Valores nulos: {quality_report['checks']['null_values']['null_percentage']}%")
print(f"Duplicados: {quality_report['checks']['duplicates']['duplicate_percentage']}%")
```

## 🎯 Características Específicas de Spotify

El ETL está optimizado para trabajar con las características típicas de Spotify:

### Características de Audio (0-1)
- **danceability**: Qué tan bailable es la canción
- **energy**: Intensidad y actividad percibida
- **valence**: Positividad musical
- **acousticness**: Qué tan acústica es la canción
- **instrumentalness**: Probabilidad de ser instrumental
- **liveness**: Probabilidad de ser grabación en vivo
- **speechiness**: Detección de palabras habladas

### Métricas Adicionales
- **loudness**: Volumen general en dB
- **tempo**: Tempo en BPM
- **key**: Clave musical (0-11)
- **mode**: Modalidad (mayor/menor)
- **time_signature**: Compás de tiempo

### Campos Calculados
- **mood_score**: Combinación de valence + energy + danceability
- **popularity_category**: Categorización de popularidad
- **duration_formatted**: Duración en formato MM:SS

## 🔍 Verificación y Debugging

### Ver logs en tiempo real

```python
import logging

# Configurar logging detallado
logging.basicConfig(level=logging.INFO)

# Ejecutar pipeline
pipeline = SpotifyETLPipeline()
result = pipeline.run_full_pipeline()
```

### Verificar configuración

```python
from configuraciones import SpotifyETLConfig

# Validar configuración actual
validation = SpotifyETLConfig.validate_config()

if not validation['valid']:
    print("Errores en configuración:")
    for error in validation['errors']:
        print(f"- {error}")
```

### Análisis de datos de entrada

```python
from SpotifyExtract import SpotifyExtractor

extractor = SpotifyExtractor()
df = extractor.extract_spotify_data("mi_archivo.csv")

# Información detallada
info = extractor.get_data_info(df)
print(f"Forma: {info['shape']}")
print(f"Valores nulos: {info['missing_values']}")
print(f"Duplicados: {info['duplicates']}")
```

## 🤝 Contribuciones

Para contribuir al proyecto:

1. Fork del repositorio
2. Crear rama para nueva característica
3. Hacer cambios y tests
4. Crear Pull Request

## 📧 Soporte

Si tienes problemas o preguntas:

1. Revisa los logs generados en `Files/etl_log_*.log`
2. Verifica la configuración con `configuraciones.py`
3. Consulta los reportes de calidad generados

---

**¡Tu ETL de Spotify está listo para procesar miles de canciones! 🎵✨**