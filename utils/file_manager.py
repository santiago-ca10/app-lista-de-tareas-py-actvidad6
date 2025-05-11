# Se importan los módulos necesarios para manejo de archivos y datos en formato JSON.
import os
import json

# Ruta absoluta del directorio base del proyecto.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Ruta a la carpeta 'data' donde se almacenarán los archivos JSON.
DATA_DIR = os.path.join(BASE_DIR, 'data')

# Crea la carpeta 'data' si no existe, para evitar errores al guardar archivos.
os.makedirs(DATA_DIR, exist_ok=True)

# Definición de las rutas completas para los archivos de tareas y configuraciones.
TASKS_FILE = os.path.join(DATA_DIR, 'tasks.json')
SETTINGS_FILE = os.path.join(DATA_DIR, 'settings.json')

# Función para cargar las tareas desde el archivo tasks.json.
def load_tasks():
    if os.path.exists(TASKS_FILE):  # Verifica si el archivo existe.
        with open(TASKS_FILE, 'r', encoding='utf-8') as file:  # Abre el archivo en modo lectura.
            return json.load(file)  # Retorna la lista de tareas cargada desde el JSON.
    return []  # Si no existe el archivo, retorna una lista vacía.

# Función para guardar las tareas en el archivo tasks.json.
def save_tasks(tasks):
    with open(TASKS_FILE, 'w', encoding='utf-8') as file:  # Abre el archivo en modo escritura.
        json.dump(tasks, file, indent=4)  # Guarda la lista de tareas como JSON con indentación.

# Función para cargar configuraciones desde el archivo settings.json.
def load_settings():
    if os.path.exists(SETTINGS_FILE):  # Verifica si el archivo existe.
        with open(SETTINGS_FILE, 'r', encoding='utf-8') as file:  # Abre el archivo.
            return json.load(file)  # Retorna las configuraciones como diccionario.
    return {"bg_color": "#ffffff"}  # Valor por defecto si el archivo no existe.

# Función para guardar las configuraciones en el archivo settings.json.
def save_settings(settings):
    with open(SETTINGS_FILE, 'w', encoding='utf-8') as file:  # Abre el archivo en modo escritura.
        json.dump(settings, file, indent=4)  # Guarda las configuraciones con formato JSON legible.

