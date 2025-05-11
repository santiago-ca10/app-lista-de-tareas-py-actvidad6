# views/main_view.py

# Importación de módulos de Tkinter para la interfaz gráfica.
import tkinter as tk
from tkinter import messagebox, simpledialog, colorchooser
# Importación de funciones para guardar y cargar configuraciones.
from utils.file_manager import save_settings, load_settings

# Clase principal para la vista (interfaz) de la aplicación de lista de tareas.
class MainView:
    def __init__(self, root, controller):
        self.root = root  # Ventana principal de Tkinter.
        self.controller = controller  # Controlador que gestiona la lógica de las tareas.
        self.settings = load_settings()  # Carga las configuraciones guardadas.
        self.bg_color = self.settings.get('background_color', "#f0f0f0")  # Color de fondo por defecto.

        # Configuración básica de la ventana principal.
        self.root.title("Lista de Tareas")
        self.root.geometry("500x600")
        self.root.configure(bg=self.bg_color)

        self.create_widgets()  # Crea los componentes gráficos.
        self.refresh_task_list()  # Muestra la lista de tareas.

    # Método que crea los widgets principales de la interfaz.
    def create_widgets(self):
        self.title_entry = tk.Entry(self.root)  # Campo para el título.
        self.title_entry.pack(pady=5)

        self.desc_entry = tk.Entry(self.root)  # Campo para la descripción.
        self.desc_entry.pack(pady=5)

        add_button = tk.Button(self.root, text="Agregar Tarea", command=self.add_task)  # Botón para agregar tareas.
        add_button.pack(pady=5)

        color_button = tk.Button(self.root, text="Cambiar Fondo", command=self.change_background_color)  # Cambiar color de fondo.
        color_button.pack(pady=5)

        # Frame donde se mostrarán las tareas.
        self.task_frame = tk.Frame(self.root, bg=self.bg_color)
        self.task_frame.pack(fill=tk.BOTH, expand=True)

    # Método que agrega una tarea utilizando los campos de entrada.
    def add_task(self):
        title = self.title_entry.get()
        description = self.desc_entry.get()

        if title and description:
            self.controller.add_task(title, description)  # Se agrega la tarea a través del controlador.
            self.title_entry.delete(0, tk.END)
            self.desc_entry.delete(0, tk.END)
            self.refresh_task_list()  # Se actualiza la lista de tareas.
        else:
            # Muestra advertencia si los campos están vacíos.
            messagebox.showwarning("Campos vacíos", "Debes ingresar título y descripción.")

    # Método que actualiza la lista de tareas en la interfaz.
    def refresh_task_list(self):
        # Limpia el frame de tareas antes de volver a llenar.
        for widget in self.task_frame.winfo_children():
            widget.destroy()

        # Recorre y muestra cada tarea en un frame.
        for index, task in enumerate(self.controller.tasks):
            frame = tk.Frame(self.task_frame, bd=1, relief=tk.RAISED, padx=5, pady=5, bg=self.bg_color)
            frame.pack(fill=tk.X, padx=5, pady=5)

            # Muestra el título con un icono de completado o no.
            title = f"{'[✓]' if task.completed else '[ ]'} {task.title}"
            tk.Label(frame, text=title, font=('Arial', 12, 'bold'), bg=self.bg_color).pack(anchor='w')
            tk.Label(frame, text=task.description, font=('Arial', 10), bg=self.bg_color).pack(anchor='w')

            # Frame con los botones de acción para cada tarea.
            btn_frame = tk.Frame(frame, bg=self.bg_color)
            btn_frame.pack(anchor='e')

            # Botones para completar, editar y eliminar tareas.
            tk.Button(btn_frame, text="Completar", command=lambda i=index: self.complete_task(i)).pack(side=tk.LEFT)
            tk.Button(btn_frame, text="Editar", command=lambda i=index: self.edit_task(i)).pack(side=tk.LEFT)
            tk.Button(btn_frame, text="Eliminar", command=lambda i=index: self.delete_task(i)).pack(side=tk.LEFT)

    # Marca una tarea como completada.
    def complete_task(self, index):
        self.controller.complete_task(index)
        self.refresh_task_list()

    # Elimina una tarea por índice.
    def delete_task(self, index):
        self.controller.delete_task(index)
        self.refresh_task_list()

    # Edita el título y la descripción de una tarea.
    def edit_task(self, index):
        task = self.controller.tasks[index]
        new_title = simpledialog.askstring("Editar título", "Nuevo título:", initialvalue=task.title)
        new_desc = simpledialog.askstring("Editar descripción", "Nueva descripción:", initialvalue=task.description)

        if new_title and new_desc:
            self.controller.edit_task(index, new_title, new_desc)
            self.refresh_task_list()

    # Permite cambiar el color de fondo de la interfaz y guarda la configuración.
    def change_background_color(self):
        color = colorchooser.askcolor(title="Selecciona un color")[1]
        if color:
            self.bg_color = color
            self.root.configure(bg=color)
            self.task_frame.configure(bg=color)
            self.settings['background_color'] = color
            save_settings(self.settings)
            self.refresh_task_list()
