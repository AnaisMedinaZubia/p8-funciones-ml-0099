# Medina Anais NC 0099

print("===== EJEMPLO 1: FUNCIÓN SIN PARÁMETROS =====")

def saludo():
    print("Hola, bienvenido a Python")

saludo()


print("===== EJEMPLO 2: FUNCIÓN CON PARÁMETROS =====")

def sumar(a, b):
    print("La suma es:", a + b)

sumar(10, 5)


print("===== EJEMPLO 3: FUNCIÓN CON RETURN =====")

def multiplicar(a, b):
    return a * b

resultado = multiplicar(4, 6)
print("El resultado es:", resultado)


print("===== EJEMPLO 4: FUNCIÓN CON VALOR PREDETERMINADO =====")

def presentar(nombre="Estudiante"):
    print("Mi nombre es:", nombre)

presentar()
presentar("Anais")


print("===== EJEMPLO 5: FUNCIÓN QUE CALCULA EL PROMEDIO =====")

def calcular_promedio(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

promedio = calcular_promedio(9, 8, 10)
print("El promedio es:", promedio)
print("Medina Anais NC 0099")

