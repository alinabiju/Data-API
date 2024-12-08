import psycopg
import yaml

class DatabaseConnector:

    def __init__(self):
        with open('cred.yml','r') as cred_file:
            cred_details = yaml.load(cred_file, Loader=yaml.SafeLoader)
        self.connection = psycopg.connect(
        dbname=cred_details.get('DBNAME'),
        user=cred_details.get('DB_USER'),
        password=cred_details.get('PASSWORD'),
        host=cred_details.get('HOSTNAME'),
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
        cursor = self.connection.cursor()
        cursor.execute("""UPDATE Items SET status=%s WHERE id=%s""",(new_state,id))
        self.connection.commit()
        