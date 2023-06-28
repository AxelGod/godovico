import mysql.connector as mariadb 
def consultar(sql):
    mariadb_conexion = mariadb.connect(host='localhost', port='3306',
                                    user='angel', password='23032003', database='nessgym')
    cursor = mariadb_conexion.cursor()
    try:
        cursor.execute(sql)
        return cursor.fetchall()
    except mariadb.Error as error:
        print("Error: {}".format(error))
    mariadb_conexion.close()
