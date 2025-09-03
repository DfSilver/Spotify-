import sqlite3
from Config.config_sale import ConfigSale

class LoaderSale:
    """
    Carga los datos de ventas a CSV y SQLite.
    """
    def __init__(self, df):
        self.df = df

    def to_csv(self, output_path=None):
        output_path = output_path or ConfigSale.OUTPUT_PATH
        try:
            self.df.to_csv(output_path, index=False)
            print(f"✅ Datos guardados en {output_path}")
        except Exception as e:
            print(f"❌ Error al guardar CSV: {e}")

    def to_sqlite(self, db_path=None, table_name=None):
        db_path = db_path or ConfigSale.SQLITE_DB_PATH
        table_name = table_name or ConfigSale.SQLITE_TABLE
        try:
            conn = sqlite3.connect(db_path)
            self.df.to_sql(table_name, conn, if_exists='replace', index=False)
            conn.close()
            print(f"✅ Datos guardados en SQLite → {db_path}, tabla: {table_name}")
        except Exception as e:
            print(f"❌ Error al guardar en SQLite: {e}")
