import json

# Declaración de las listas a nivel global
ingresos = []
gastos = []

def cuenta_de_resultados():
    global ingresos, gastos  # Indicamos que usaremos las variables globales

    while True:
        print("\n1. Registrar ingreso")
        print("2. Registrar gasto")
        print("3. Mostrar resumen")
        print("4. Guardar y salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                monto = float(input("Monto del ingreso: "))
                ingresos.append(monto)
            except ValueError:
                print("Por favor, ingrese un número válido.")
        elif opcion == "2":
            try:
                monto = float(input("Monto del gasto: "))
                gastos.append(monto)
            except ValueError:
                print("Por favor, ingrese un número válido.")
        elif opcion == "3":
            total_ingresos = sum(ingresos)
            total_gastos = sum(gastos)
            resultado = total_ingresos - total_gastos

            print(f"\n--- Resumen ---")
            print(f"Ingresos totales: ${total_ingresos:.2f}")
            print(f"Gastos totales: ${total_gastos:.2f}")
            print(f"Resultado: {'Beneficio' if resultado >= 0 else 'Pérdida'} de ${abs(resultado):.2f}")
        elif opcion == "4":
            guardar_datos()
            print("Datos guardados. Saliendo del programa.")
            break
        else:
            print("Opción inválida.")

def guardar_datos():
    global ingresos, gastos  # Indicamos que usaremos las variables globales
    try:
        with open("datos.json", "w") as f:
            json.dump({"ingresos": ingresos, "gastos": gastos}, f)
    except Exception as e:
        print(f"No se pudieron guardar los datos: {e}")

def cargar_datos():
    global ingresos, gastos  # Indicamos que usaremos las variables globales
    try:
        with open("datos.json", "r") as f:
            datos = json.load(f)
            ingresos = datos.get("ingresos", [])
            gastos = datos.get("gastos", [])
    except FileNotFoundError:
        print("No se encontraron datos previos. Se comenzará desde cero.")
    except Exception as e:
        print(f"Error al cargar los datos: {e}")

# Cargar los datos al iniciar
cargar_datos()

# Ejecutar el programa
cuenta_de_resultados()
