import mysql.connector as sql


def v():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        database="project1"
    )
    cursor = mydb.cursor()
    cursor.execute('SHOW TABLES')
    for x in cursor:
        print(x)
    print(mydb)
