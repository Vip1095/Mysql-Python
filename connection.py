import mysql.connector as connection

try:
    mydb = connection.connect(host='localhost',
                              user = 'root',
                              password='root',
                              port='3306')
    query = "SHOW DATABASES;"
    cursor = mydb.cursor() # Create a cursor to execute queries
    cursor.execute(query)
    print(cursor.fetchall())
    mydb.close()
except Exception as e:
    mydb.close()
    print(e)