---
layout: home
title: Subordinación y Valor
description: Un universo distópico ambientado en la Argentina post-apocalíptica del año 2178
---

# Subordinación y Valor

Un universo distópico donde la supervivencia, la fe y la resistencia se entrelazan en las sombras de Ciudad Dársena.

## Sobre el Proyecto

"Subordinación y Valor" es un universo distópico ambientado en la Argentina post-apocalíptica del año 2178. Tras la devastación de la Gran Guerra Global y el colapso tecnológico, Ciudad Dársena emerge como el último bastión de la civilización en un mundo sumido en la oscuridad.

## Últimas Entradas

{% for post in site.posts limit:5 %}
- [{{ post.title }}]({{ post.url | relative_url }}) - {{ post.date | date: "%d/%m/%Y" }}
{% endfor %}

## Contacto

[GitHub](https://github.com/kodexArg/universo-syv)

---

*"En las sombras de Dársena, la verdad es el arma más peligrosa"* 