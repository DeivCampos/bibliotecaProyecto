import tkinter as tk
from tkinter import messagebox

def ventana_admin():
    admin_window = tk.Toplevel()
    admin_window.title("Panel de Administración")

    tk.Label(admin_window, text="Bienvenido, Admin").pack(pady=10)

    # Botón para gestionar usuarios
    tk.Button(admin_window, text="Gestionar Usuarios", command=gestionar_usuarios).pack(pady=5)
    # Botón para ver informes
    tk.Button(admin_window, text="Ver Informes", command=ver_informes).pack(pady=5)
    # Botón para gestionar libros
    tk.Button(admin_window, text="Gestionar Libros", command=gestionar_libros).pack(pady=5)

def gestionar_usuarios():
    messagebox.showinfo("Gestionar Usuarios", "Funcionalidad no implementada.")

def ver_informes():
    messagebox.showinfo("Ver Informes", "Funcionalidad no implementada.")

def gestionar_libros():
    messagebox.showinfo("Gestionar Libros", "Funcionalidad no implementada.")
