from collections import Counter
import sys
import string
import json

STOP_WORDS = ["el", "la", "los", "las", "de", "y", "a", "en", "es", "un"]

def analizar_texto(texto):
    palabras = [palabra.lower().strip(string.punctuation) for palabra in texto.split()]
    palabras = [palabra for palabra in palabras if palabra not in STOP_WORDS]
    conteo = Counter(palabras)
    return {
        "caracteres": len(texto),
        "palabras": len(palabras),
        "lineas": texto.count('\n') + 1,
        "palabra_mas_larga": max(palabras, key = len) if palabras else "",
        "palabra_mas_frecuente": conteo.most_common(1)[0] if conteo else "",
        "5_palabras_mas_comunes": conteo.most_common(5)
    }

def imprimir_reporte(resultado, archivo = None):
    palabra = resultado['palabra_mas_frecuente'][0]
    cantidad = resultado['palabra_mas_frecuente'][1]
    print("===== REPORTE =====", file = archivo)
    print(f"Caracteres: {resultado['caracteres']}", file = archivo)
    print(f"Palabras: {resultado['palabras']}", file = archivo)
    print(f"Líneas: {resultado['lineas']}", file = archivo)
    print(f"\nPalabra más larga:\n{resultado['palabra_mas_larga']}", file = archivo)
    print(f"\nPalabra más frecuente:\n{palabra} ({cantidad} veces)", file = archivo)
    print("Top 5 palabras:", file = archivo)
    for i, (palabra, cantidad) in enumerate(resultado['5_palabras_mas_comunes'], start = 1):
        print(f"{i}. {palabra} ({cantidad})", file = archivo)
        print("#" * cantidad, file = archivo)

def exportar_json(resultado, nombre_archivo):
    datos = {
        "caracteres": resultado['caracteres'],
        "palabras": resultado['palabras'],
        "lineas": resultado['lineas'],
        "palabras_mas_larga": resultado['palabra_mas_larga'],
        "mas_frecuente": resultado['palabra_mas_frecuente'][0],
        "frecuencia": resultado['palabra_mas_frecuente'][1],
        "top_5": [{"palabra": p, "cantidad": c} for p, c in resultado['5_palabras_mas_comunes']]
    }
    with open(nombre_archivo, 'w', encoding = 'utf-8') as f:
        json.dump(datos, f, indent = 2, ensure_ascii = False)

if __name__ == "__main__":
    if len(sys.argv) > 2:
        with open(sys.argv[1]) as archivo:
            texto = archivo.read()
        resultado = analizar_texto(texto)
        if sys.argv[2].endswith('.json'):
            exportar_json(resultado, sys.argv[2])
        else:
            with open(sys.argv[2], 'w', encoding = 'utf-8') as salida:
                imprimir_reporte(resultado, salida)
    elif len(sys.argv) > 1:
        with open(sys.argv[1]) as archivo:
            texto = archivo.read()
        resultado = analizar_texto(texto)
        imprimir_reporte(resultado)
    else:
        texto = input("Introduce el texto para analizar: ")
        resultado = analizar_texto(texto)
        imprimir_reporte(resultado)