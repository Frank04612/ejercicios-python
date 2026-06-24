import string
import random

longitud = int(input("Ingrese la longitud deseada de la contraseña (min 1, max 50): "))
if longitud < 1 or longitud > 50:
    print("Longitudd de la contraseña no válida. Por favor, ingrese un número entre 1 y 50.") 
else:
    mayusculas = input("¿Desea incluir mayúsculas en su contraseña? (S/N): ").upper()
    minusculas = input("¿Desea incluir minúsculas en su contraseña? (S/N): ").upper()
    numeros = input("¿Desea incluir números en su contraseña? (S/N): ").upper()
    simbolos = input("¿Desea incluir símbolos en su contraseña? (S/N): ").upper()
    
pool = ""
if mayusculas == "S":
    pool += string.ascii_uppercase
if minusculas == "S":
    pool += string.ascii_lowercase
if numeros == "S":
    pool += string.digits
if simbolos == "S":
    pool += string.punctuation
random.choice(pool)
password = ""
for i in range(longitud):
    password += random.choice(pool)
print(f"Contraseña generada: {password}")