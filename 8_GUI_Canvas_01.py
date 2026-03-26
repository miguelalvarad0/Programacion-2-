import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

# Dibujar un rectángulo (x1, y1, x2, y2)
canvas.create_rectangle(50, 50, 150, 100, fill="blue", outline="black")

# Dibujar un óvalo (circunscrito en el rectángulo)
canvas.create_oval(200, 50, 300, 100, fill="red")

# Dibujar una línea
canvas.create_line(0, 0, 400, 300, fill="green", width=2)

# Agregar texto
canvas.create_text(200, 150, text="¡Hola Canvas!", font=("Arial", 16), fill="purple")

root.mainloop()
