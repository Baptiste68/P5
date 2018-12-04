import mysql.connector
from mysql.connector import errorcode


"""
    This module is use to connect to the database
    and to send queries
"""


class Databaselink:
    """
        This classe create the link
    """

    def __init__(self):
        """
            This function initiate the object using
            the configuration
        """
        self.config = {
            'user': 'root',
            'password': 'root',
            'host': '127.0.0.1',
            'port': '3307',
            'database': 'foodexo',
            'raise_on_warnings': True
        }

    def connect_to_foodexo(self):
        """
            This function is used to connect to
            foodexo database
        """
        try:
            self.cnx = mysql.connector.connect(**self.config)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    def send_query(self, my_query):
        """
            This function send simple Select requests
            with no commit
        """
        mycursor = self.cnx.cursor()
        mycursor.execute(my_query)
        myresult = mycursor.fetchall()
        mycursor.close()
        return(myresult)

    def send_insert(self, my_insert):
        """
            This function send Insert requests
            using commit
        """
        mycursor = self.cnx.cursor()
        mycursor.execute(my_insert)
        try:
            self.cnx.commit()
        except mysql.connector.Error as error:
            connection.rollback()  # rollback if any exception occured
            print("Failed inserting record into python_users table {}".format(error))
        mycursor.close()

    def close_all(self):
        """
            This function is used to close the connection
        """
        if(self.cnx.is_connected()):
            self.cnx.close()
            print("MySQL connection is closed")

