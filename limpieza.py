import pandas as pd

def limpiar_csv(input_file="Sale_G.csv", output_file="Sale_G_limpio.csv"):
    # Detectar separador automáticamente
    df = pd.read_csv(input_file, sep=None, engine="python")

    print("📊 Dataset cargado con éxito")
    print("Filas y columnas originales:", df.shape)

    # Limpieza
    df = df.drop_duplicates()
    df = df.dropna()
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    df = df.reset_index(drop=True)

    # Guardar limpio
    df.to_csv(output_file, index=False)
    print(f"💾 Archivo limpio guardado como {output_file}")

if __name__ == "__main__":
    limpiar_csv()

