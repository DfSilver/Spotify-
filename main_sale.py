from Config.config_sale import ConfigSale
from Extract.extractor_sale import ExtractorSale
from Transform.transformer_sale import TransformerSale
from Load.loader_sale import LoaderSale

def main():
    try:
        print("🚀 Iniciando ETL de ventas...")

        # EXTRAER
        print("📥 Extrayendo datos...")
        extractor = ExtractorSale(ConfigSale.INPUT_PATH)
        raw_data = extractor.extract()
        if raw_data is None or raw_data.empty:
            print("❌ No se extrajeron datos, fin del proceso.")
            return

        # TRANSFORMAR
        print("🔄 Transformando datos...")
        transformer = TransformerSale(raw_data)
        transformed_data = transformer.clean()

        # CARGAR
        print("📤 Cargando datos...")
        loader = LoaderSale(transformed_data)
        loader.to_csv()
        loader.to_sqlite()

        print("✅ ETL de ventas finalizado correctamente.")

    except Exception as e:
        print(f"❌ Error en el proceso ETL: {e}")

if __name__ == "__main__":
    main()
