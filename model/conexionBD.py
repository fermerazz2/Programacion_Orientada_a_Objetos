import mysql.connector

try:
    conexion=mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='bd_coches'
    )
    cursor=conexion.cursor(buffered=True)
except:
    print("Ocurrio un error con la BD verifique ...")    

