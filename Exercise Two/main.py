from flask import Flask, jsonify
import sqlite3

data = []

def select(columns=None, table=None, joins=None):

    if columns:

        column = ''

        for col in columns:

            if column == '':
                column = col 
            else:
                column = column + ', ' + col

        return f'select {column} from {table}'

    if joins:

        tables = ''

        for table in joins:

            if tables == '':
                tables = table 
            else:
                if table == joins[len(joins)-1]:
                    tables = f'{tables} {table}'
                else:
                    tables = f'{tables} {table} inner join '

        return f'select * from {tables}'

    return f'select * from {table}'

try:
    sql_connection = sqlite3.connect('../sitio.db')
    cursor = sql_connection.cursor()

    print('Successfully connected to the DataBase')

    proyectos_query = select(columns=['id', 'project_name'], table='project')
    cursor.execute(proyectos_query)

    proyectos = cursor.fetchall()

    usuarios_query = select(joins=['user', 'user_role_association_table', 'role'])
    cursor.execute(usuarios_query)

    usuarios = cursor.fetchall()

    data = {"projects": proyectos, "users": usuarios}

except sqlite3.Error as error:
    print('Error while connecting', error)

finally:
    if sql_connection:
        sql_connection.close()
        print('The connection with de DB in closed')

app = Flask(__name__)

@app.route('/')
def home():

    return jsonify(data=str(data))

if __name__ == '__main__':
    app.run()
