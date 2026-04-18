
import unittest
from api_phonebook import Phonebook, User

class TestPhonebook(unittest.TestCase):
    
    def setUp(self) -> None:
        self.p = Phonebook()
        self.original_data = self.p.load_data()
    
    def tearDown(self) -> None:
        self.p.save_data(self.original_data)
    
    def test_create_entry(self) -> None:        
        u = User('User3', 'Surname3', '101102103', 'Odesa')
        self.p.create_entry(u)
        user_data = u.transform_as_dict()
        self.assertIn(user_data, self.p.load_data())
        
    def test_update_entry(self) -> None:
        u = User('User4', 'Surname4', '104105106', 'Kyiv')
        self.p.create_entry(u)
        updated = User('User4', 'Surname4', '104105106', 'Lviv')
        self.p.update_entry(updated, '104105106')
        data = self.p.load_data()
        expected = updated.transform_as_dict()
        self.assertIn(expected, data)
        
    def test_delete_entry(self) -> None:
        u = User('User5', 'Surname5', '107108109', 'Kharkiv')
        self.p.create_entry(u)
        self.p.delete_entry('107108109')
        data = self.p.load_data()
        user_data = u.transform_as_dict()
        self.assertNotIn(user_data, data)
        
    def test_read_entry(self) -> None:
        u = User('User6', 'Surname6', '110111112', 'Dnipro')
        self.p.create_entry(u)
        self.assertTrue(self.p.read_entry('User6'))
        self.assertTrue(self.p.read_entry('Surname6'))
        self.assertTrue(self.p.read_entry('110111112'))
        self.assertTrue(self.p.read_entry('Dnipro'))
    
if __name__ == '__main__':
    unittest.main()
    



