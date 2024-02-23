import tkinter as tk

def sumar():
    try:
        resultado.set(float(num1.get()) + float(num2.get()))
    except ValueError:
        resultado.set("Error")

def restar():
    try:
        resultado.set(float(num1.get()) - float(num2.get()))
    except ValueError:
        resultado.set("Error")

def multiplicar():
    try:
        resultado.set(float(num1.get()) * float(num2.get()))
    except ValueError:
        resultado.set("Error")

def dividir():
    try:
        if float(num2.get()) == 0:
            resultado.set("Error")
        else:
            resultado.set(float(num1.get()) / float(num2.get()))
    except ValueError:
        resultado.set("Error")

root = tk.Tk()
root.title("Calculadora Básica")

num1 = tk.StringVar()
num2 = tk.StringVar()
resultado = tk.StringVar()

tk.Label(root, text="Número 1:").grid(row=0, column=0)
tk.Entry(root, textvariable=num1).grid(row=0, column=1)
tk.Label(root, text="Número 2:").grid(row=1, column=0)
tk.Entry(root, textvariable=num2).grid(row=1, column=1)

tk.Button(root, text="Sumar", command=sumar).grid(row=2, column=0)
tk.Button(root, text="Restar", command=restar).grid(row=2, column=1)
tk.Button(root, text="Multiplicar", command=multiplicar).grid(row=3, column=0)
tk.Button(root, text="Dividir", command=dividir).grid(row=3, column=1)

tk.Label(root, text="Resultado:").grid(row=4, column=0)
tk.Label(root, textvariable=resultado).grid(row=4, column=1)

root.mainloop()