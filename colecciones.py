persona={
    "nombre":"Mauricio",
    "edad":42,
    "ciudad":"Chinquira",
    "edad":43
}
print (persona["edad"])
persona["nombre"]="Lucio"
print(persona)
persona["profesion"]="Ingeniero"
print(persona)
print(persona.keys())
data2={
    "estrato":3,
    "eps":"Sura",
    "comidas":["pastas","Mexicana"],
    "Profecion":"Autronauta",
    "direccion":{
        "calle": "carrera",
        "numero":"64-71",
        "complemento":"Apto 711"
    }
}
persona.update(data2)
print(persona)
print(f"Nombre: {persona["nombre"]} apartamento: {persona["direccion"]}")
print(f"Nombre: {persona["nombre"]} apartamento: {persona["direccion"]["complemento"]}")
print(f"segunda comida {persona ["comidas"]}")
print(f"segunda comida {persona ["comidas"][1]}")