from tkinter import * #import tkinter as tk

           
           
def mostrar_combo():
    seleccion = combo_var.get()
    print ('Seleccionó el combo: ', seleccion)
    precio_total = 0

    if seleccion == 'Hamburguesa':
        precio_total += 3000
        if agrandar_var.get(): 
            print('Agregó refresco')
            precio_total += 700
            print(precio_total)
        if papitas_var.get():
            print('Agregó papas')
            precio_total += 800
            print(precio_total)
        if postre_var.get():
            print('Agregó postre')
            precio_total += 600
            print(precio_total)

    if seleccion == 'Pizza Personal':
        precio_total += 2800
        if agrandar_var.get(): 
            print('Agregó refresco')
            precio_total += 700
            print(precio_total)
        if papitas_var.get():
            print('Agregó papas')
            precio_total += 800
            print(precio_total)
        if postre_var.get():
            print('Agregó postre')
            precio_total += 600
            print(precio_total)

    if seleccion == 'Hot Dog':
        precio_total += 2500
        if agrandar_var.get(): 
            print('Agregó refresco')
            precio_total += 700
            print(precio_total)
        if papitas_var.get():
            print('Agregó papas')
            precio_total += 800
            print(precio_total)
        if postre_var.get():
            print('Agregó postre')
            precio_total += 600
            print(precio_total)

    valor = str(precio_total)
       
    success_var.set("El precio total es " + valor )   
    print('se muestra precio en pantalla')

#Crear ventana
ventana = Tk()
ventana.title('Mi primera ventana en Tk')
ventana.geometry("700x500")


#Variables gáficas


success_var = StringVar()
combo_var = StringVar(value='Pizza Personal') #es la varibale para el grupo de radiobuttons
#variables para checkbuttons
agrandar_var = BooleanVar()
papitas_var = BooleanVar()
postre_var = BooleanVar()

precio_total = IntVar()




button_pares = Button (ventana, command=mostrar_combo, text = "Calcular precio", font=("Arial",20), bg = "#04acb5", fg = "black", width = 15, height = 2)
button_pares.place(x = 240, y=430)

#Labels resultado
lbl_success = Label(ventana, textvariable = success_var, fg="green", font= ("Arial",16))
lbl_success.place(x = 40, y = 430)



#RadioButton de combos

Label(ventana, text = 'Elige tu combo:', fg= 'blue', font= ("Arial",20)).place(x=40, y=220)

radio_hamburguesa = Radiobutton(ventana,text = "Hamburguesa", variable=combo_var, value='Hamburguesa')
radio_pizza = Radiobutton(ventana,text = "Pizza Personal", variable=combo_var, value= 'Pizza Personal')
radio_sandwich = Radiobutton(ventana,text = "Hot Dog", variable=combo_var, value='Hot Dog')

radio_hamburguesa.place(x=240, y = 220)
radio_pizza.place(x=360, y = 220)
radio_sandwich.place(x=480, y = 220)

Label(ventana, text = 'Elige opciones extra:', fg= 'blue', font= ("Arial",20)).place(x=40, y=260)

check_agrandar = Checkbutton(ventana, text='Agregar refresco', variable=agrandar_var)
check_papitas = Checkbutton(ventana, text='Agregar papitas', variable=papitas_var)
check_postre = Checkbutton(ventana, text='Agregar postre', variable= postre_var)

check_agrandar.place(x=240, y = 300)
check_papitas.place(x=240, y = 330)
check_postre.place(x=240, y = 360)

precio_total = 0
ventana.mainloop()


