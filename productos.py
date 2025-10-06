productos=[
    {"nombre": "Manzana","categoria":"frutas","valor":500},
    {"nombre": "pera","categoria":"frutas","valor":400},
    {"nombre": "pam rollo","categoria":"pam","valor":300},
    {"nombre": "Espinacas","categoria":"verdura","valor":700},
    {"nombre": "Guineo","categoria":"frutas","valor":800},
    {"nombre": "zanahoria","categoria":"frutas","valor":400}
]

#agrupar productos por categoria

agrupados={}
for producto in productos:
    cat=producto["categoria"]
    if cat not in agrupados:
        agrupados[cat]=[]
    agrupados[cat].append([producto["nombre"],producto["valor"]])
    
    
print(agrupados)
#Que mas 