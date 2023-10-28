import time
import random

def resta():
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    r = x - y
    print(f"{x} - {y} = {r}")  

def suma():
    x = random.randint(1, 90)
    y = random.randint(1, 90)
    r = x + y
    print(f"{x} + {y} = {r}")  

def division():
    x = random.randint(1, 70)
    y = random.randint(1, 70)
    r = x / y
    print(f"{x} / {y} = {r}")  

def multiplicacion():
    x = random.randint(1, 50)
    y = random.randint(1, 50)
    r = x * y
    print(f"{x} * {y} = {r}")  

def main():
    A = [resta, suma, division, multiplicacion, division, suma, resta]
    tiempo_ejecucion = random.randint(1,10)
    total_tiempo_inicial = time.time()

    for c in A:
        start_time = time.time()
        while time.time() - start_time < tiempo_ejecucion:
            c()

    total_tiempo_transcurrido = time.time() - total_tiempo_inicial
    print(f"Proceso de las operaciones finalizado. Tiempo total: {total_tiempo_transcurrido:.2f} segundos")  # Mostrar tiempo total con dos decimales

if __name__ == "__main__":
    main()


