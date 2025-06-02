---
layout: page
title: Personajes
permalink: /personajes/
---

{% for personaje in site.personajes %}
- [{{ personaje.title }}]({{ personaje.url | relative_url }})
{% endfor %} 