class TransformerSale:
    """
    Realiza transformaciones mínimas (validación) sobre los datos de ventas.
    """
    def __init__(self, df):
        self.df = df

    def clean(self):

        """
        Aplica validaciones básicas:
        - Eliminar duplicados
        - Rellenar valores nulos
        """
        import pandas as pd
        df = self.df.copy()

        # Validar duplicados
        df = df.drop_duplicates()

        # Validar columnas con valores nulos
        df = df.fillna("Unknown")

        print("✅ Datos transformados y validados")
        return df
