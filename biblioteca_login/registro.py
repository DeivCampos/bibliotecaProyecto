from tkinter import Tk, Label, Entry, Button, messagebox, Frame, StringVar
from tkinter import ttk  # Importar ttk para el combobox
import mysql.connector
from conexion_bd import conectar_bd

def registrar_usuario():
    username = username_var.get()
    password = password_var.get()
    user_type = user_type_var.get()

    if not username or not password:
        messagebox.showerror("Registro", "Por favor, complete todos los campos.")
        return

    try:
        db = conectar_bd()
        cursor = db.cursor()
        cursor.execute("INSERT INTO usuarios (username, password, tipo) VALUES (%s, %s, %s)", (username, password, user_type))
        db.commit()
        messagebox.showinfo("Registro", "¡Usuario registrado exitosamente!")
        db.close()
        root.destroy()  # Cerrar la ventana de registro después de registrar
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Error al registrar: {e}")

# Crear la ventana principal
root = Tk()
root.title("Registro de Usuario")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

# Agregar un marco para la estética
frame = Frame(root, bg="#ffffff")
frame.pack(pady=20)

# Títulos y campos
title_label = Label(frame, text="Registrar Usuario", font=("Helvetica", 20), bg="#ffffff", fg="#333333")
title_label.pack(pady=10)

username_var = StringVar()
password_var = StringVar()
user_type_var = StringVar(value="Estudiante")  # Por defecto

username_label = Label(frame, text="Usuario:", font=("Helvetica", 12), bg="#ffffff", fg="#333333")
username_label.pack(pady=5)
username_entry = Entry(frame, textvariable=username_var, font=("Helvetica", 12), bg="#e0e0e0", width=25)
username_entry.pack(pady=5)

password_label = Label(frame, text="Contraseña:", font=("Helvetica", 12), bg="#ffffff", fg="#333333")
password_label.pack(pady=5)
password_entry = Entry(frame, textvariable=password_var, show="*", font=("Helvetica", 12), bg="#e0e0e0", width=25)
password_entry.pack(pady=5)

user_type_label = Label(frame, text="Tipo de Usuario:", font=("Helvetica", 12), bg="#ffffff", fg="#333333")
user_type_label.pack(pady=5)

# Crear un combobox para seleccionar el tipo de usuario
user_type_combobox = ttk.Combobox(frame, textvariable=user_type_var, font=("Helvetica", 12), state="readonly")
user_type_combobox['values'] = ("Estudiante", "Docente")  # Opciones del combobox
user_type_combobox.current(0)  # Establecer por defecto "Estudiante"
user_type_combobox.pack(pady=5)

register_button = Button(frame, text="Registrar", command=registrar_usuario, font=("Helvetica", 12), bg="#4CAF50", fg="#ffffff")
register_button.pack(pady=20)

# Ejecutar el loop principal
root.mainloop()
