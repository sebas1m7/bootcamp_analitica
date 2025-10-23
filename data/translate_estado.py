import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).parent
INPUT_CSV = DATA_DIR / "../uju.csv"
BACKUP_CSV = DATA_DIR / "../uju_original_backup.csv"
OUTPUT_CSV = DATA_DIR / "../uju_traducido.csv"


def main():
    # Leer CSV
    df = pd.read_csv(INPUT_CSV)

    if 'Estado' not in df.columns:
        # soporte para columna con mayúscula diferente
        possible = [c for c in df.columns if c.lower() == 'estado']
        if possible:
            df.rename(columns={possible[0]: 'Estado'}, inplace=True)
        else:
            raise SystemExit("No se encontró la columna 'Estado' en el archivo.")

    print('Valores únicos (antes):')
    print(df['Estado'].value_counts(dropna=False))

    # Mapeo manual de inglés -> español
    mapping = {
        'Delivered': 'Entregado',
        'Processing': 'En proceso',
        'Shipped': 'Enviado',
        'Order': 'Pedido',
        'Cancelled': 'Cancelado',
        'Returned': 'Devuelto',
        # añadir más mapeos si los datos lo requieren
    }

    # Normalizar valores: eliminar espacios y capitalizar formato
    def normalize(s):
        if pd.isna(s):
            return s
        return str(s).strip()

    df['Estado_norm'] = df['Estado'].apply(normalize)

    # Aplicar traducción con fallback a mantener el valor original
    df['Estado_traducido'] = df['Estado_norm'].map(mapping).fillna(df['Estado_norm'])

    # Hacer backup del original
    BACKUP_CSV = Path(BACKUP_CSV).resolve()
    df.to_csv(BACKUP_CSV, index=False)

    # Reemplazar la columna Estado por la traducida y guardar
    df['Estado'] = df['Estado_traducido']
    df.drop(columns=['Estado_norm', 'Estado_traducido'], inplace=True)

    OUTPUT_CSV = Path(OUTPUT_CSV).resolve()
    df.to_csv(OUTPUT_CSV, index=False)

    print('\nTraducción completada. Archivo guardado en:', OUTPUT_CSV)
    print('\nValores únicos (después):')
    print(df['Estado'].value_counts(dropna=False))


if __name__ == '__main__':
    main()
