import tkinter as tk
from tkinter import messagebox
import json

# Declaración de las listas a nivel global
ingresos = []
gastos = []

# Funciones existentes del programa
def guardar_datos():
    global ingresos, gastos
    try:
        with open("datos.json", "w") as f:
            json.dump({"ingresos": ingresos, "gastos": gastos}, f)
        messagebox.showinfo("Éxito", "Datos guardados correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudieron guardar los datos: {e}")

def cargar_datos():
    global ingresos, gastos
    try:
        with open("datos.json", "r") as f:
            datos = json.load(f)
            ingresos = datos.get("ingresos", [])
            gastos = datos.get("gastos", [])
            messagebox.showinfo("Éxito", "Datos cargados correctamente.")
    except FileNotFoundError:
        messagebox.showwarning("Aviso", "No se encontraron datos previos. Se comenzará desde cero.")
    except Exception as e:
        messagebox.showerror("Error", f"Error al cargar los datos: {e}")

def mostrar_resumen():
    total_ingresos = sum(ingresos)
    total_gastos = sum(gastos)
    resultado = total_ingresos - total_gastos
    resumen = (
        f"Ingresos totales: ${total_ingresos:.2f}\n"
        f"Gastos totales: ${total_gastos:.2f}\n"
        f"Resultado: {'Beneficio' if resultado >= 0 else 'Pérdida'} de ${abs(resultado):.2f}"
    )
    messagebox.showinfo("Resumen", resumen)

# Funciones para la interfaz gráfica
def registrar_ingreso():
    try:
        monto = float(entry_ingreso.get())
        ingresos.append(monto)
        entry_ingreso.delete(0, tk.END)
        messagebox.showinfo("Éxito", f"Ingreso de ${monto:.2f} registrado.")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un número válido.")

def registrar_gasto():
    try:
        monto = float(entry_gasto.get())
        gastos.append(monto)
        entry_gasto.delete(0, tk.END)
        messagebox.showinfo("Éxito", f"Gasto de ${monto:.2f} registrado.")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un número válido.")

# Ventana principal
root = tk.Tk()
root.title("Calculadora de Cuenta de Resultados")
root.geometry("400x300")

# Mantener la ventana principal activa
def on_closing():
    if messagebox.askokcancel("Salir", "¿Deseas salir del programa?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

# Widgets
tk.Label(root, text="Registrar Ingreso:").grid(row=0, column=0, padx=10, pady=5)
entry_ingreso = tk.Entry(root)
entry_ingreso.grid(row=0, column=1, padx=10, pady=5)
tk.Button(root, text="Añadir Ingreso", command=registrar_ingreso).grid(row=0, column=2, padx=10, pady=5)

tk.Label(root, text="Registrar Gasto:").grid(row=1, column=0, padx=10, pady=5)
entry_gasto = tk.Entry(root)
entry_gasto.grid(row=1, column=1, padx=10, pady=5)
tk.Button(root, text="Añadir Gasto", command=registrar_gasto).grid(row=1, column=2, padx=10, pady=5)

tk.Button(root, text="Mostrar Resumen", command=mostrar_resumen).grid(row=2, column=0, columnspan=3, pady=10)
tk.Button(root, text="Guardar Datos", command=guardar_datos).grid(row=3, column=0, columnspan=3, pady=10)
tk.Button(root, text="Cargar Datos", command=cargar_datos).grid(row=4, column=0, columnspan=3, pady=10)

# Ejecutar la ventana
root.mainloop()