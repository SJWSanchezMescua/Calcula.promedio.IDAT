import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Promedios")
ventana.geometry("400x400")

# Función de validación
def validar_entrada(char, entry):
    return char.isdigit() and len(entry.get()) < 2

#título
lbl_titulo = tk.Label(ventana, text="Escriba sus notas (1-20)")
lbl_titulo.pack(pady=10)

# Crear diccionarios para almacenar notas y pesos
notas = {}
pesos = {'ec1': 0.04, 'ec2': 0.12, 'ec3': 0.24, 'evfinal': 0.60}

# Crear etiquetas y entradas para las notas
etiquetas = ['EC1', 'EC2', 'EC3', 'EV.FINAL']
for etiqueta in etiquetas:
    lbl_nota = tk.Label(ventana, text=f"{etiqueta}:")
    lbl_nota.pack()
    
    # Crear la entrada
    txt_nota = tk.Entry(ventana, validate='key')
    txt_nota.pack()
    
    # Configurar la validación para esta entrada
    vcmd = (ventana.register(lambda char, entry=txt_nota: validar_entrada(char, entry)), '%S')
    txt_nota.config(validatecommand=vcmd)
    
    # Almacenar referencia a la entrada
    notas[etiqueta.lower().replace(".", "").replace(" ", "")] = txt_nota

# Función para calcular el promedio
def calcular_promedio():
    try:
        notas_valores = {}
        for key in notas.keys():
            valor = float(notas[key].get())
            if valor < 1 or valor > 20:
                raise ValueError("Las notas deben estar entre 1 y 20.")
            notas_valores[key] = valor
        
        # Calcular promedio
        pf = sum(notas_valores[key] * pesos[key] for key in pesos.keys())
        resultado_label.config(text=f"Promedio Final: {pf:.2f}")
    except ValueError as ve:
        messagebox.showerror("Error", str(ve))
        resultado_label.config(text="")
    except KeyError as e:
        resultado_label.config(text=f"Error: clave no encontrada {e}")

# Función para limpiar las entradas
def limpiar_campos():
    for entry in notas.values():
        entry.delete(0, tk.END)  # Limpiar el campo
    resultado_label.config(text="")  # Limpiar el resultado

# Botón para calcular promedio
calcular_button = tk.Button(ventana, text="Calcular Promedio", command=calcular_promedio)
calcular_button.pack(pady=10)

# Botón para limpiar campos
limpiar_button = tk.Button(ventana, text="Limpiar", command=limpiar_campos)
limpiar_button.pack(pady=5)

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(ventana, text="", font=("Arial", 12))
resultado_label.pack(pady=10)

# Inicia el bucle principal
ventana.mainloop()
