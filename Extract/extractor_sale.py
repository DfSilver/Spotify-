import pandas as pd

class ExtractorSale:
    """
    Extrae datos del archivo de ventas limpio.
    """
    def __init__(self, file_path):
        self.file_path = file_path

    """
    Lee el archivo CSV usando pandas y devuelve un DataFrame.
    """
    def extract(self):
        try:
            df = pd.read_csv(self.file_path)
            print(f"✅ Datos extraídos desde {self.file_path}")
            return df
        except Exception as e:
            print(f"❌ Error al extraer datos: {e}")
            return None
