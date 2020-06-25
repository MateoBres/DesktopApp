import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

alumnos = {}


def ver_lista():
    print("Lista de alumnos:")
    # El bucle "for" aplicado sobre un diccionario recorre sus
    # claves.
    for nombre in alumnos:
        cursos = alumnos[nombre]
        print(nombre + " - " + str(cursos) + " cursos")


def agregar():
    # Obtener el nombre de la caja de texto.
    nombre_alumno = caja_nombre.get()
    # Obtener la cantidad de cursos de la caja de texto y convertirla
    # a un entero.
    cursos = int(caja_cursos.get())
    if nombre_alumno == "":
        print("Error: no ha ingresado un nombre válido.")
    else:
        # Agregar un nuevo par clave-valor al diccionario "alumnos".
        # La clave es el nombre del alumno y el valor, la cantidad
        # de cursos.
        alumnos[nombre_alumno] = cursos
        print("Has ingresado el alumno correctamente.")


def ver_cursos():
    # Obtener el nombre de la caja de texto.
    nombre = caja_nombre.get()
    print("Cursos: " + str(alumnos[nombre]))


ventana = tk.Tk()
ventana.config(width=600, height=400)
#ventana.state('zoomed')
ventana.title("Proyecto integrador")

boton_lista = tk.Button(text="Ver lista de alumnos", command=ver_lista)
boton_lista.place(x=10, y=10)

etiqueta_nombre = tk.Label(text="Nombre alumno:")
etiqueta_nombre.place(x=10, y=60)

caja_nombre = tk.Entry()
caja_nombre.place(x=110, y=60, width=150, height=20)

etiqueta_cursos = tk.Label(text="Cursos:")
etiqueta_cursos.place(x=10, y=100)

caja_cursos = tk.Entry()
caja_cursos.place(x=110, y=100, width=50, height=20)

boton_agregar = tk.Button(text="Agregar a la lista", command=agregar)
boton_agregar.place(x=10, y=150)

boton_cursos = tk.Button(text="Ver cantidad de cursos", command=ver_cursos)
boton_cursos.place(x=115, y=150)

lista1 = tk.Listbox()
lista1.place(x=10, y=200, width=300, height=250)




ventana.mainloop()
