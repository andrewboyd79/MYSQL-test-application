import pymysql
import os

#  Get username from workspace
username = os.getenv('C9_USER')

#  Connect to database
connection = pymysql.connect(host='localhost',
                                user =username,
                                password ='',
                                db ='Chinook')

try:
    #R  un a query
    with connection.cursor() as cursor:
        sql = "Select * from Artist;"
        cursor.execute(sql)
        result=cursor.fetchall()
        print(result)
finally:
    #  Close the connection, regardless of success
    connection.close
