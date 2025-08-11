import tkinter as tk
from tkinter import messagebox

def calcularIMC():
    peso = float(txtPeso.get())
    altura = float(txtAltura.get())
    imc = peso / (altura * altura)
    messagebox.showinfo(
        title="Información",
        message=f"Su IMC es de: {imc}."
    )
    if imc < 18.5:
        lblEstado.config(text="Estado: Peso Bajo.")
    elif imc >= 18.5 and imc <= 24.9:
        lblEstado.config(text="Estado: Peso Normal.")
    elif imc >= 25 and imc <= 29.9:
        lblEstado.config(text="Estado: Sobrepeso.")
    elif imc >= 30 and imc <= 34.9:
        lblEstado.config(text="Estado: Obesidad Tipo 1.")
    elif imc >= 35 and imc <= 39.9:
        lblEstado.config(text="Estado: Obesidad Tipo 2.")
    else:
        lblEstado.config(text="Estado: Obesidad Tipo 3.")


frmCalcular = tk.Tk()
frmCalcular.title = "Sistema para calcular el IMC"
# Definir la cuadricula
# Columnas: 3, Filas: 5
frmCalcular.rowconfigure(0, weight=1)
frmCalcular.rowconfigure(1, weight=1)
frmCalcular.rowconfigure(2, weight=1)
frmCalcular.rowconfigure(3, weight=1)
frmCalcular.rowconfigure(4, weight=1)
frmCalcular.columnconfigure(0, weight=3)
frmCalcular.columnconfigure(1, weight=3)
frmCalcular.columnconfigure(2, weight=3)
lblTitulo = tk.Label(
    frmCalcular, 
    text="Cálculo del Índice de Masa Corporal",
    font={"Arial", 26, "bold"}
)
lblTitulo.grid(row=0, column=0, columnspan=3)
lblPeso = tk.Label(frmCalcular, text="Peso:")
lblPeso.grid(row=1, column=0)
txtPeso = tk.Entry(frmCalcular)
txtPeso.grid(row=1, column=1, columnspan=2)
lblAltura = tk.Label(frmCalcular, text="Altura:")
lblAltura.grid(row=2, column=0)
txtAltura = tk.Entry(frmCalcular)
txtAltura.grid(row=2, column=1, columnspan=2)
btnEjecutar = tk.Button(
    frmCalcular, 
    text="Calcular IMC",
    command=calcularIMC
)
btnEjecutar.grid(row=3, column=2)
lblEstado = tk.Label(frmCalcular, text="Estado:")
lblEstado.grid(
    row=4,
    column=0,
    columnspan=3,
    padx=5,
    pady=5,
    sticky="W"
)
frmCalcular.mainloop()