import pandas as pd
traduciones = {
        'Delivered': 'Entregado',
        'Processing': 'En proceso',
        'Shipped': 'Enviado',
        'Order': 'Pedido'
}
df["Estado"] = df["Estado"].map(traduciones).fillna(df["Estado"])