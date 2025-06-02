import os
import re
import yaml

def fix_yaml_paths(file_path):
    """Corrige las rutas en los archivos YAML."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Encontrar el bloque YAML
    yaml_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not yaml_match:
        return
    
    yaml_content = yaml_match.group(1)
    try:
        data = yaml.safe_load(yaml_content)
        
        # Corregir rutas en los metadatos
        if 'ruta' in data:
            data['ruta'] = data['ruta'].replace('_', '-')
        
        # Reconstruir el contenido YAML
        new_yaml = yaml.dump(data, allow_unicode=True, sort_keys=False)
        new_content = f"---\n{new_yaml}---\n{content[yaml_match.end():]}"
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
    except yaml.YAMLError as e:
        print(f"Error procesando YAML en {file_path}: {e}")

def fix_config_yml():
    """Corrige las rutas en _config.yml."""
    with open('_config.yml', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Corregir nombres de colecciones y rutas
    content = content.replace('rpg_manual_del_jugador', 'rpg-manual-del-jugador')
    content = content.replace('_rpg_manual_del_jugador', '_rpg-manual-del-jugador')
    
    with open('_config.yml', 'w', encoding='utf-8') as f:
        f.write(content)

def process_markdown_files():
    """Procesa todos los archivos Markdown para corregir rutas."""
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                fix_yaml_paths(file_path)

def main():
    print("Corrigiendo rutas en _config.yml...")
    fix_config_yml()
    
    print("Procesando archivos Markdown...")
    process_markdown_files()
    
    print("¡Proceso completado!")

if __name__ == "__main__":
    main() 