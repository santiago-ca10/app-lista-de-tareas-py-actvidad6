# Importación del módulo Tkinter para crear la interfaz gráfica
import tkinter as tk

# Importación del controlador de tareas que maneja la lógica de negocio
from controllers.task_controller import TaskController

# Importación de la vista principal que contiene la interfaz gráfica
from views.main_view import MainView

# Punto de entrada principal de la aplicación
if __name__ == '__main__':
    root = tk.Tk()  # Crea la ventana principal de la aplicación con Tkinter
    controller = TaskController()  # Instancia el controlador que maneja las tareas
    app = MainView(root, controller)  # Crea la vista principal y la conecta con la ventana y el controlador
    root.mainloop()  # Inicia el bucle principal de la interfaz gráfica (la aplicación permanece abierta)


