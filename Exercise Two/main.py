from flask import Flask, jsonify
import sqlite3

def select(id = None, columns=None, table=None, joins=False):

    if columns:

        column = ''

        for col in columns:

            if column == '':
                column = col 
            else:
                column = column + ', ' + col

        return f'select {column} from {table} where id={id}'

    if joins:

        return 'select user.id, user.username, user.password, user.profile_picture, user.user_full_name,  user_role_association_table.user_id,  user_role_association_table.role_id, role.id, role.name, role.description from user inner join user_role_association_table on user_role_association_table.user_id=user.id inner join role on role.id=user_role_association_table.user_id'

    return 'select * from project'

app = Flask(__name__)

@app.route('/proyecto/<id_proyecto>')
def home(id_proyecto):

    try:
        sql_connection = sqlite3.connect('../sitio.db')
        cursor = sql_connection.cursor()

        print('Successfully connected to the DataBase')

        proyectos_query = select(id=id_proyecto, columns=['project_name'], table='project')
        cursor.execute(proyectos_query)

        proyectos = cursor.fetchall()

        usuarios_query = select(joins=True)
        cursor.execute(usuarios_query)

        usuarios = cursor.fetchall()

        data = {"projects": proyectos, "users": usuarios}

    except sqlite3.Error as error:
        print('Error while connecting', error)

    finally:
        if sql_connection:
            sql_connection.close()
            print('The connection with de DB in closed')

    return jsonify(data=str(data))

if __name__ == '__main__':
    app.run(debug=True)
