# Se importan las clases y funciones necesarias desde otros módulos del proyecto.
from models.task import Task  # Importa la clase Task desde el modelo.
from utils.file_manager import load_tasks, save_tasks  # Importa funciones para cargar y guardar tareas.

# Se define la clase TaskController, encargada de manejar la lógica de las tareas.
class TaskController:
    def __init__(self):
        # Al inicializar el controlador, se cargan las tareas guardadas desde el archivo
        # y se convierten en objetos de tipo Task.
        self.tasks = [Task.from_dict(data) for data in load_tasks()]

    # Método para agregar una nueva tarea con título y descripción.
    def add_task(self, title, description):
        self.tasks.append(Task(title, description))  # Se añade una nueva tarea a la lista.
        self.save()  # Se guarda el estado actualizado de las tareas.

    # Método para marcar una tarea como completada a partir de su índice.
    def complete_task(self, index):
        self.tasks[index].completed = True  # Se cambia el estado a completado.
        self.save()  # Se guarda el cambio.

    # Método para eliminar una tarea por su índice en la lista.
    def delete_task(self, index):
        del self.tasks[index]  # Se elimina la tarea.
        self.save()  # Se guarda el cambio.

    # Método para editar una tarea existente (título y descripción) usando su índice.
    def edit_task(self, index, new_title, new_description):
        self.tasks[index].title = new_title  # Se actualiza el título.
        self.tasks[index].description = new_description  # Se actualiza la descripción.
        self.save()  # Se guarda el cambio.

    # Método auxiliar que guarda todas las tareas en formato diccionario usando la función save_tasks.
    def save(self):
        save_tasks([task.to_dict() for task in self.tasks])  # Convierte las tareas a diccionarios y las guarda.
