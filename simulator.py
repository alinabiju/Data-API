import time
import random
from databaseConnector import DatabaseConnector

def catalogueSimulator(conn: DatabaseConnector):
     
     all_items = conn.getAllObjects()

     index = random.randrange(0,len(all_items))
     record_to_update = all_items[index]

     if record_to_update['status']=='Available':
        record_to_update['status'] = 'Reserved'
     elif record_to_update['status'] == 'Reserved':
        record_to_update['status'] = 'On loan'
     elif record_to_update['status']=='On loan':
        record_to_update['status'] = 'Available'
     else:
        print('Invalid State')
    
     conn.updateObjectState(record_to_update['id'],record_to_update['status'])
     print('Updated')

if __name__ =="__main__":
    conn = DatabaseConnector()
    try:
        while True:
                catalogueSimulator(conn)
                time.sleep(60)
    except KeyboardInterrupt:
        print('Program Interrupted')
        print('Exiting Code...')
        conn.closeConnection()

