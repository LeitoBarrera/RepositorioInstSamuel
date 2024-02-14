def crear_diccionario_colores():
    diccionario_colores = {
        "red": "rojo",
        "blue": "azul",
        "green": "verde",
        "yellow": "amarillo",
        "purple": "morado",
        "orange": "naranja",
        "pink": "rosa",
        "brown": "marrón",
        "gray": "gris",
        "black": "negro"
    }
    return diccionario_colores

def traducir_espa_ingles(dicci, color_espa):
    color_espa = color_espa.lower()
    diccionario_espa_ingles = {v.lower(): k for k, v in dicci.items()}
    traduccion = diccionario_espa_ingles.get(color_espa, "No encontrado")
    return traduccion

def traducir_ingles_espa(diccio, color_ingles):
    color_ingles = color_ingles.lower()
    traduccion = diccio.get(color_ingles, "No encontrado")
    return traduccion

diccionario_colores = crear_diccionario_colores()

color_entra = input("Ingresa un color en español o inglés: ")

traduccion_espa_ingles = traducir_espa_ingles(diccionario_colores, color_entra)
if traduccion_espa_ingles != "No encontrado":
    print(f"Traducción de español a inglés: {traduccion_espa_ingles}")

traduccion_ingles_espa = traducir_ingles_espa(diccionario_colores, color_entra)
if traduccion_ingles_espa != "No encontrado":
    print(f"Traducción de inglés a español: {traduccion_ingles_espa}")
