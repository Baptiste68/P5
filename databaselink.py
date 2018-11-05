import mysql.connector
from mysql.connector import errorcode

class Databaselink:
    def __init__(self):
        self.config = {
          'user': 'root',
          'password': 'root',
          'host': '127.0.0.1',
          'database': 'foodexo',
          'raise_on_warnings': True
        }


    def connect_to_foodexo(self):
        try:
          self.cnx = mysql.connector.connect(**self.config)
        except mysql.connector.Error as err:
          if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
          elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
          else:
            print(err)


    def send_query(self,my_query):
        mycursor = self.cnx.cursor()
        mycursor.execute(my_query)
        myresult = mycursor.fetchall()
        return(myresult)
