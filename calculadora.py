import json
def cuenta_de_resultados():
    ingresos = []
    gastos = []

    while True:
        print("\n1. Registrar ingreso")
        print("2. Registrar gasto")
        print("3. Mostrar resumen")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            monto = float(input("Monto del ingreso: "))
            ingresos.append(monto)
        elif opcion == "2":
            monto = float(input("Monto del gasto: "))
            gastos.append(monto)
        elif opcion == "3":
            total_ingresos = sum(ingresos)
            total_gastos = sum(gastos)
            resultado = total_ingresos - total_gastos

            print(f"\n--- Resumen ---")
            print(f"Ingresos totales: ${total_ingresos:.2f}")
            print(f"Gastos totales: ${total_gastos:.2f}")
            print(f"Resultado: {'Beneficio' if resultado >= 0 else 'Pérdida'} de ${abs(resultado):.2f}")
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")

cuenta_de_resultados()

def guardar_datos(ingresos, gastos):
    with open("datos.json", "w") as f:
        json.dump({"ingresos": ingresos, "gastos": gastos}, f)

def cargar_datos():
    try:
        with open("datos.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"ingresos": [], "gastos": []}
