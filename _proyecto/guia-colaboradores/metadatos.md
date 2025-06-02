---
layout: post
title: "Guía de Metadatos"
date: 2024-06-02
tags:
- proyecto
- guia
- metadatos
---

# Metadatos YAML - Proyecto Subordinación y Valor

Todos los archivos `.md` del proyecto deben incluir metadatos YAML al inicio del archivo.

## Estructura Básica

```yaml
titulo: "Título Único del Documento"
ruta: "ruta/completa/del/archivo.md"
tags:
  - "palabra_clave_1"
  - "palabra_clave_2"
```

## Campos Obligatorios

- **`titulo`**: Identificador único del documento (usado para referencias)
- **`ruta`**: Ruta completa del archivo desde la raíz del proyecto
- **`tags`**: Lista de palabras clave en minúsculas, con guiones bajos para palabras compuestas

## Campos Específicos por Tipo

- **`fecha`**: Fecha del evento (para eventos cronológicos)
- **`region`**: Ubicación principal (para eventos cronológicos)
- **`faccion_principal`**: Facción principal (para personajes)
- **`estado_actual`**: Estado actual del personaje (para personajes)
- **`edad_aparente`**: Edad aparente (para personajes)

## Ejemplos por Tipo

**Evento Cronológico:**
```yaml
titulo: "Año 2030: El Umbral de la Gran Fractura"
ruta: "01_Lore/01_Cronologia/2035_2039-Guerra/2030.md"
tags:
  - "cronologia"
  - "2030"
  - "guerra"
fecha: "2030"
region: "Global"
```

**Personaje:**
```yaml
titulo: "Comandante María Vásquez"
ruta: "02_Personajes/Canonicos/maria_vasquez.md"
tags:
  - "personaje"
  - "militar"
  - "sia"
faccion_principal: "Santa Inquisición Argentina"
estado_actual: "Vivo"
edad_aparente: "45 años"
```



## Reglas Importantes

1. El `titulo` debe ser único en todo el proyecto
2. La `ruta` debe coincidir exactamente con la ubicación del archivo
3. Los `tags` deben usar minúsculas y guiones bajos para palabras compuestas
4. Usar campos específicos según el tipo de documento (fecha/region para eventos, faccion_principal/estado_actual/edad_aparente para personajes)