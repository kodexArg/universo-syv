---
layout: home
title: Subordinación y Valor
description: Un universo distópico ambientado en la Argentina post-apocalíptica del
  año 2178
---


# Subordinación y Valor

Un universo distópico donde la supervivencia, la fe y la resistencia se entrelazan en las sombras de Ciudad Dársena.

## Sobre el Proyecto

"Subordinación y Valor" es un universo distópico ambientado en la Argentina post-apocalíptica del año 2178. Tras la devastación de la Gran Guerra Global y el colapso tecnológico, Ciudad Dársena emerge como el último bastión de la civilización en un mundo sumido en la oscuridad.

## Últimas Entradas

### Proyecto
{% assign proyecto_posts = site.proyecto | sort: 'date' | reverse %}
{% for post in proyecto_posts limit:3 %}
- [{{ post.title }}]({{ post.url | relative_url }}) - {{ post.date | date: "%d/%m/%Y" }}
{% endfor %}

### Lore
{% assign lore_posts = site.lore | sort: 'date' | reverse %}
{% for post in lore_posts limit:3 %}
- [{{ post.title }}]({{ post.url | relative_url }}) - {{ post.date | date: "%d/%m/%Y" }}
{% endfor %}

### Personajes
{% assign personajes_posts = site.personajes | sort: 'date' | reverse %}
{% for post in personajes_posts limit:3 %}
- [{{ post.title }}]({{ post.url | relative_url }}) - {{ post.date | date: "%d/%m/%Y" }}
{% endfor %}

### Historias
{% assign historias_posts = site.historias | sort: 'date' | reverse %}
{% for post in historias_posts limit:3 %}
- [{{ post.title }}]({{ post.url | relative_url }}) - {{ post.date | date: "%d/%m/%Y" }}
{% endfor %}

### Manual del Jugador
{% assign rpg_posts = site.rpg | sort: 'date' | reverse %}
{% for post in rpg_posts limit:3 %}
- [{{ post.title }}]({{ post.url | relative_url }}) - {{ post.date | date: "%d/%m/%Y" }}
{% endfor %}

## Contacto

[GitHub](https://github.com/kodexArg/universo-syv)

---

*"En las sombras de Dársena, la verdad es el arma más peligrosa"* 