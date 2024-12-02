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

        cursor.execute("SELECT id, title, status FROM Items ORDER BY id")
        dataset = cursor.fetchall()

        data = []
        for (id,title,status) in dataset:
            data.append({'id': id, 'title': title, 'status': status})

        return data
    
    def updateObjectState(self,id,new_state)->None:
        print('Do nothing for now')
        