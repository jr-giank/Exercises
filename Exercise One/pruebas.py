from jinja2 import Template;
import requests;

# cat_facts = requests.get('https://catfact.ninja/facts').json()

# print(cat_facts['data'])

template = Template('Hola {{ nombre }}!')

print(template.render(nombre='IMD'))
