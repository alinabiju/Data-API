import psycopg

class DatabaseConnector:

    def __init__(self):
        self.connection = psycopg.connect(
        dbname="postgres",
        user="postgres",
        password="doyourthing",
        host="localhost",
        port="5432")

    def getAllObjects(self)->any:
        cursor = self.connection.cursor()

        cursor.execute("SELECT id, title, status FROM Items")
        dataset = cursor.fetchall()

        return dataset