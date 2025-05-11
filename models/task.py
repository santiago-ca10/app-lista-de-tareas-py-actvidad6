# Definición de la clase Task que representa una tarea individual.
class Task:
    # Método constructor que inicializa los atributos de una tarea: título, descripción y estado de completado.
    def __init__(self, title, description, completed=False):
        self.title = title  # Título de la tarea.
        self.description = description  # Descripción de la tarea.
        self.completed = completed  # Estado de completado (por defecto es False).

    # Método que convierte el objeto Task en un diccionario, útil para guardar en archivos JSON.
    def to_dict(self):
        return {
            'title': self.title,
            'description': self.description,
            'completed': self.completed
        }

    # Método de clase que crea un objeto Task a partir de un diccionario.
    @classmethod
    def from_dict(cls, data):
        return cls(
            data['title'],  # Extrae el título del diccionario.
            data['description'],  # Extrae la descripción del diccionario.
            data.get('completed', False)  # Obtiene el estado de completado (por defecto False si no existe).
        )
