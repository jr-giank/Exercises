## Soluciones - Basilio De Paula

### Dependencias

Para correr los diferentes programas debera crear un ambiente virtual de python desde la carpeta raiz del proyecto, lo puede hacer con py -m venv venv. Luego debe activar el ambiente virtual e instalar los paquetes necesarios lo cual puede hacer mediante pip install -r requirements.txt.

### Ejercicio #1

- Desarrolle un programa en python 3.8 o superior que haga las siguientes operaciones:

•	Importe el módulo jinja2.
•	importar el módulo requests o uno equivalente.
•	hacer un llamado al api https://catfact.ninja/ para traer una lista de hechos sobre los gatos.
•	hacer una plantilla html con una lista simple (<ul>y <li>) en donde se itere sobre la lista de hechos sobre los gatos.
•	cargar la plantilla con el módulo jinja2 y renderizarla con los hechos sobre los gatos.
•	imprimir en la consola el resultado de del renderizado del template de jinja2.
•	debe imprimir el html de una lista desordenada (ul) donde cada item (li) es un hecho sobre los gatos.

### Ejercicio #2

- Escriba un controlador en flask cuya url sea /proyecto/<id proyecto>. que realice la siguientes operaciones:

•	Importe el módulo sqlite3 de python.
•	conectarse al archivo de base de datos sitio.db
•	hacer una consulta en la tabla project y traer todos los resultados que tengan el valor del parámetro id proyecto en cualquier posición de la columna project  name.
•	traer todos los resultados de esta consulta y convertirlos en un arreglo que se guardara temporalmente con el nombre “proyectos”.
•	hacer una consulta que haga un join entre las tablas user, user_role_associ y role y traiga todas las columnas.
•	traer todos los resultados de esta consulta y convertirlos en un arreglo que se guardara temporalmente con el nombre “usuarios”.
•	crear in objeto {“projects’: proyectos, “users”:usuarios} en donde cada key corresponde con su variable.
•	convertir el objeto del paso anterior a formato json y enviarlo al navegador del cliente.