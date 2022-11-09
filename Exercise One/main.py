import jinja2
import requests
import os

cat_facts = requests.get('https://catfact.ninja/facts').json()
tpl_dir = jinja2.FileSystemLoader('.')
tpl_env = jinja2.Environment(loader=tpl_dir)
template = tpl_env.get_template('index.html')

datos = {
    'title': 'Cat Facts',
    'facts': cat_facts['data']
}

os.system('cls')
print(template.render(data=datos))