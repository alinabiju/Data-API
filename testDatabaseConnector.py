import unittest
from unittest.mock import patch, MagicMock
from databaseConnector import DatabaseConnector

class TestDatabaseConnector(unittest.TestCase):

    @patch("databaseConnector.psycopg")
    def test_getAllObjects(self, mock_psycopg):
        mock_cur = mock_psycopg.connect().cursor()
        mock_cur.execute.return_value = [(1,'test-item-1','Available'),(2,'test-item-2', 'On loan')]

        exp_res = [{'id': 1, 'title': 'test-item-1', 'status': 'Available'},{'id': 2, 'title': 'test-item-2', 'status': 'On loan'}]

        conn = DatabaseConnector()
        res = conn.getAllObjects()
        conn.closeConnection()

        self.assertDictEqual(res[0],exp_res[0])
        self.assertDictEqual(res[1],exp_res[1])

        mock_cur.execute.assert_called_with("SELECT id, title, status FROM Items ORDER BY id")

    @patch("databaseConnector.psycopg")
    def test_updateObjectState(self, mock_psycopg):
        mock_cur = mock_psycopg.connect().cursor()

        conn = DatabaseConnector()
        conn.updateObjectState(0,'Reserved')

        conn.closeConnection()
        mock_cur.execute.assert_called_with("""UPDATE Items SET status=%s WHERE id=%s""",('Reserved',0))
    

if __name__=='__main__':
    unittest.main()