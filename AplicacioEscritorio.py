import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3

conn = sqlite3.connect("pileta.db")

cursor = conn.cursor()

try:
	cursor.execute('CREATE TABLE alumnos (nombre TEXT, cursos NUMERIC);')
except sqlite3.OperationalError:
	pass


def agregar():
    nombre_alumno = caja_nombre.get()
    cursos = lista_despegable.get()
    alumno = (nombre_alumno, cursos)
    alumno = list(alumno)
    if nombre_alumno == "":
        messagebox.showerror(message="Error: no ha ingresado un nombre válido.", title="Sistema")
    else:
        lista1.insert(0, str(alumno[0]) +'  ' + str(alumno[1]))
        conn = sqlite3.connect("pileta.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO alumnos VALUES(?, ?);", (nombre_alumno, cursos))
        conn.commit()
        messagebox.showinfo(message="Has ingresado el alumno correctamente.", title="Sistema")
        
def ver_cursos():
	nombre = caja_nombre.get()
	for alumno in alumnos:
			if  nombre == alumno[0]:
				messagebox.showinfo(message="Cursos: " + str(alumno[1]), title="Sistema")
				break
			else:
				messagebox.showwarning(message="El alumno no esta' presente en la lista.", title="Sistema")

def nuevo():
	print('Nuevo archivo.')
	
def acerca_de():
	print('Acerca de:')

ventana = tk.Tk()

ventana.title("La pileta de Liliana")

menu_barra = tk.Menu()

menu_archivo = tk.Menu(menu_barra, tearoff = 0)
menu_archivo.add_command(label = 'Nuevo', command = nuevo)

menu_ayuda = tk.Menu(menu_barra, tearoff = 0)
menu_ayuda.add_command(label = 'Acerca de....', command = acerca_de)

menu_barra.add_cascade(label = 'Archivo', menu = menu_archivo)
menu_barra.add_cascade(label = 'Ayuda', menu = menu_ayuda)

etiqueta_nombre = ttk.Label(text="Nombre alumno:")
etiqueta_nombre.place(x=10, y=20)

caja_nombre = ttk.Entry()
caja_nombre.place(x=110, y=20, width=150, height=20)

etiqueta_cursos = ttk.Label(text="Cursos:")
etiqueta_cursos.place(x=10, y=50)

lista_despegable = ttk.Combobox(values = [1, 2, 3, 4])
lista_despegable.place(x=110, y=50, width=50, height=20)

boton_agregar = ttk.Button(text="Agregar a la lista", command=agregar)
boton_agregar.place(x=10, y=100)

boton_cursos = ttk.Button(text="Ver cantidad de cursos", command=ver_cursos)
boton_cursos.place(x=115, y=100)

lista1 = tk.Listbox()
lista1.place(x=10, y=130, width=300, height=250)
cursor.execute("SELECT * FROM alumnos;")
alumnos = cursor.fetchall()
for alumno in alumnos:
	lista1.insert(tk.END, alumno[0] + '  ' + str(alumno[1]))
ventana.config(width=600, height=400, menu = menu_barra)

conn.close()

ventana.mainloop()
