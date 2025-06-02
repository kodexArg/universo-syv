import os
import unicodedata
import re

# Carpetas raíz de colecciones Jekyll
JEKYLL_COLLECTIONS = {
    '_lore', '_historias', '_personajes', '_proyecto', '_rpg', '_rpg-manual-del-jugador', '_posts'
}

README_CANONICAL = 'README.md'

def normalize_name(name, is_root_collection=False):
    """Convierte un nombre a minúsculas, elimina acentos y usa guiones, preservando el guion bajo inicial solo en colecciones root."""
    if name.lower() == 'readme.md':
        return README_CANONICAL
    # Si es una colección root de Jekyll, preservar el guion bajo inicial
    if is_root_collection and name.startswith('_'):
        prefix = '_'
        name_body = name[1:]
    else:
        prefix = ''
        name_body = name
    # Convertir a minúsculas
    name_body = name_body.lower()
    # Normalizar caracteres Unicode (eliminar acentos)
    name_body = unicodedata.normalize('NFKD', name_body).encode('ASCII', 'ignore').decode('ASCII')
    # Reemplazar espacios y guiones bajos por guiones
    name_body = re.sub(r'[ _]+', '-', name_body)
    # Eliminar guiones al principio o final
    name_body = name_body.strip('-')
    return prefix + name_body

def should_rename(name, is_root_collection=False):
    """Determina si un archivo o carpeta debe ser renombrado."""
    if name == README_CANONICAL:
        return False
    normalized = normalize_name(name, is_root_collection)
    return name != normalized

def rename_path(path, is_root_collection=False):
    """Renombra un archivo o carpeta si es necesario."""
    old_name = os.path.basename(path)
    if not should_rename(old_name, is_root_collection):
        return path
    
    dir_name = os.path.dirname(path)
    new_name = normalize_name(old_name, is_root_collection)
    
    # Si es README.md y ya existe, no sobrescribir
    if new_name == README_CANONICAL and os.path.exists(os.path.join(dir_name, new_name)):
        print(f"No se renombra {path} porque ya existe {os.path.join(dir_name, new_name)}")
        return path
    
    new_path = os.path.join(dir_name, new_name)
    try:
        os.rename(path, new_path)
        print(f"Renombrado: {path} -> {new_path}")
        return new_path
    except Exception as e:
        print(f"Error al renombrar {path}: {e}")
        return path

def process_directory(root_dir, is_root=False):
    """Procesa recursivamente un directorio y sus subdirectorios."""
    try:
        # Primero procesar archivos y carpetas en el directorio actual
        for item in os.listdir(root_dir):
            full_path = os.path.join(root_dir, item)
            
            # ¿Es una colección root de Jekyll?
            is_collection = is_root and item in JEKYLL_COLLECTIONS
            # Si es un archivo markdown, intentar renombrarlo
            if os.path.isfile(full_path) and item.lower().endswith('.md'):
                rename_path(full_path, is_root_collection=False)
            # Si es un directorio, intentar renombrarlo y luego procesar su contenido
            elif os.path.isdir(full_path):
                # Renombrar según si es colección root o no
                new_dir_path = rename_path(full_path, is_root_collection=is_collection)
                # Procesar el contenido del directorio
                process_directory(new_dir_path, is_root=False)
    except Exception as e:
        print(f"Error al procesar directorio {root_dir}: {e}")

def main():
    # Obtener el directorio raíz del proyecto
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(f"Procesando directorio: {root_dir}")
    
    # Procesar el directorio raíz
    process_directory(root_dir, is_root=True)
    print("¡Proceso completado!")

if __name__ == "__main__":
    main() 