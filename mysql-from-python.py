import pymysql
import datetime
import os

#  Get username from workspace
username = os.getenv('C9_USER')

#  Connect to database
connection = pymysql.connect(host='localhost',
                                user =username,
                                password ='',
                                db ='Chinook')

try:
    #  Run a query
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute("DELETE FROM Friends WHERE name = 'Lyle'") #  Cursor is obj to ex queries
        connection.commit()
        
finally:
    #  Close the connection, regardless of success
    connection.close
    
