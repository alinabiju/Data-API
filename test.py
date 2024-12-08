import unittest
from unittest.mock import MagicMock
from simulator import catalogueSimulator
import random

class TestSimulator(unittest.TestCase):
    
    def test_db_update_call(self):
        mock_db_conn = MagicMock()
        mock_db_conn.getAllObjects.return_value = [{'id': 1, 'title': 'test-item-1', 'status': 'Available'},{'id': 2, 'title': 'test-item-2', 'status': 'On loan'},{'id': 3, 'title': 'test-item-3', 'status': 'Reserved'}]
        random.seed(0)
        
        catalogueSimulator(mock_db_conn)
        mock_db_conn.updateObjectState.assert_called_with(2,"Available")
    
if __name__=='__main__':
    unittest.main()