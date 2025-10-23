import pandas as pd
import argparse
from pathlib import Path


def parse_args():
    p = argparse.ArgumentParser(description='Traducir columna de estado ES->EN')
    p.add_argument('--input', '-i', default='..\\uju.csv', help='Ruta al CSV de entrada (por defecto data\\uju.csv)')
    p.add_argument('--column', '-c', default='Estado', help='Nombre de la columna a traducir (por defecto Estado)')
    p.add_argument('--output', '-o', default='..\\uju_traducido_es_en.csv', help='Ruta al CSV de salida')
    return p.parse_args()


def main():
    args = parse_args()
    input_path = Path(__file__).parent / args.input
    output_path = Path(__file__).parent / args.output
    backup_path = output_path.with_name(output_path.stem + '_backup' + output_path.suffix)

    df = pd.read_csv(input_path)

    # localizar columna (case-insensitive)
    col = None
    for c in df.columns:
        if c.lower() == args.column.lower():
            col = c
            break
    if col is None:
        raise SystemExit(f"No se encontró la columna '{args.column}' en {input_path}")

    print('Valores únicos (antes):')
    print(df[col].value_counts(dropna=False))

    # Mapeo manual ES -> EN
    mapping = {
        'Entregado': 'Delivered',
        'En proceso': 'Processing',
        'Enviado': 'Shipped',
        'Pedido': 'Order',
        'Cancelado': 'Cancelled',
        'Devuelto': 'Returned',
        # agrega más si es necesario
    }

    def norm(s):
        if pd.isna(s):
            return s
        return str(s).strip()

    df[col + '_norm'] = df[col].apply(norm)
    df[col + '_translated'] = df[col + '_norm'].map(mapping).fillna(df[col + '_norm'])

    # guardar backup del output anterior si existe
    if output_path.exists():
        output_path.replace(backup_path)

    # escribir archivo con columna traducida
    df[col] = df[col + '_translated']
    df.drop(columns=[col + '_norm', col + '_translated'], inplace=True)
    df.to_csv(output_path, index=False)

    print('\nTraducción completada. Archivo guardado en:', output_path)
    print('\nValores únicos (después):')
    print(df[col].value_counts(dropna=False))


if __name__ == '__main__':
    main()
