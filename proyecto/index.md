---
layout: page
title: Proyecto
permalink: /proyecto/
---

{% for proyecto_item in site.proyecto %}
## [{{ proyecto_item.title }}]({{ proyecto_item.url | relative_url }})
{% if proyecto_item.description %}
{{ proyecto_item.description }}
{% endif %}

{% endfor %} 