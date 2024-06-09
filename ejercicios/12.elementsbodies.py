
"""  
la abundancia natural de los elemenotos en el cuerpo humano, expresada como porcentaje en masa, es: oxigeno (0) 65%;
carbono (C), 18%; hidrogeno (H), 10%; nitrogeno(N), 3%; calcio (Ca), 1.6%; fosforo (P), 1.2%; los otros
elementos constituyen el 1.2%. Calcule la masa en gramos de cada elemento en el cuerop de una persona de 62 Kg. 
"""
# De codigo determina el porcentaje en gramos para el peso de cualquier persona

#variables

elements = {
    "0": 65,
    "C": 18,
    "H": 10,
    "N": 3,
    "Ca": 1.6,
    "P": 1.2,
    "Other": 1.2
}

person = float(input("Ingrese el peso de la persona en kilogramos: "))
person_g = person * 1000
factor = person_g / 100

grams = lambda x: x * factor

multiplied_values = map(grams, elements.values())
percentage_elements = dict(zip(elements.keys(), multiplied_values))

print(percentage_elements)
