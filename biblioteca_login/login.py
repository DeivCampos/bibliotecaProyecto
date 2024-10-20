from tkinter import Tk, Label, Entry, Button, messagebox, Frame, StringVar
import mysql.connector
from conexion_bd import conectar_bd

def login():
    username = username_var.get()
    password = password_var.get()

    if not username or not password:
        messagebox.showerror("Login", "Por favor, complete todos los campos.")
        return

    try:
        db = conectar_bd()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE username=%s AND password=%s", (username, password))
        user = cursor.fetchone()
        db.close()

        if user:
            is_admin = user[4]  # Suponiendo que is_admin es el quinto campo (index 4)

            if is_admin:  # Verifica si es un admin
                messagebox.showinfo("Login", "¡Bienvenido, Admin!")
                ventana_admin()  # Llama a la ventana del administrador
            else:
                messagebox.showinfo("Login", "¡Bienvenido, Usuario!")
                ventana_usuario()  # Llama a la ventana del usuario normal
        else:
            messagebox.showerror("Login", "Usuario o contraseña incorrectos.")
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Error al conectar a la base de datos: {e}")

def ventana_usuario():
    # Aquí puedes crear la ventana para usuarios normales
    user_window = Tk()
    user_window.title("Panel de Usuario")
    user_window.geometry("400x300")
    user_window.configure(bg="#f0f0f0")

    label = Label(user_window, text="Bienvenido al Panel de Usuario", font=("Helvetica", 16), bg="#f0f0f0", fg="#333333")
    label.pack(pady=20)

    # Aquí puedes agregar más funcionalidades para el usuario normal

    user_window.mainloop()

def ventana_admin():
    # Aquí puedes crear la ventana o el panel para el admin
    admin_window = Tk()
    admin_window.title("Panel de Administración")
    admin_window.geometry("400x300")
    admin_window.configure(bg="#f0f0f0")

    label = Label(admin_window, text="Bienvenido al Panel de Administración", font=("Helvetica", 16), bg="#f0f0f0", fg="#333333")
    label.pack(pady=20)

    # Aquí puedes agregar más funcionalidades para el admin

    admin_window.mainloop()

# Crear la ventana principal
root = Tk()
root.title("Sistema de Biblioteca")
root.geometry("400x300")
root.configure(bg="#f0f0f0")  # Color de fondo

# Agregar un marco para la estética
frame = Frame(root, bg="#ffffff")
frame.pack(pady=20)

# Títulos y campos
title_label = Label(frame, text="Iniciar Sesión", font=("Helvetica", 20), bg="#ffffff", fg="#333333")
title_label.pack(pady=10)

username_var = StringVar()
password_var = StringVar()

username_label = Label(frame, text="Usuario:", font=("Helvetica", 12), bg="#ffffff", fg="#333333")
username_label.pack(pady=5)
username_entry = Entry(frame, textvariable=username_var, font=("Helvetica", 12), bg="#e0e0e0", width=25)
username_entry.pack(pady=5)

password_label = Label(frame, text="Contraseña:", font=("Helvetica", 12), bg="#ffffff", fg="#333333")
password_label.pack(pady=5)
password_entry = Entry(frame, textvariable=password_var, show="*", font=("Helvetica", 12), bg="#e0e0e0", width=25)
password_entry.pack(pady=5)

login_button = Button(frame, text="Iniciar Sesión", command=login, font=("Helvetica", 12), bg="#4CAF50", fg="#ffffff")
login_button.pack(pady=20)

def abrir_registro():
    root.destroy()  # Cierra la ventana de login
    import registro  # Importa y ejecuta el archivo de registro

# Agregar un botón para registrar un nuevo usuario
register_button = Button(frame, text="Registrar Nuevo Usuario", command=abrir_registro, font=("Helvetica", 12), bg="#2196F3", fg="#ffffff")
register_button.pack(pady=10)

# Ejecutar el loop principal
root.mainloop()
