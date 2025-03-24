import unittest
from unittest.mock import patch, mock_open
from src.method.main import write_contacts_to_file, read_contacts_from_file

class TestContactsFileOperations(unittest.TestCase):
    mock_open = mock_open()
    contacts = [
        {
            "name": "John Doe",
            "email": "john@example.com",
            "phone": "123-456-7890"
        },
        {
            "name": "Jane Smith",
            "email": "jane@example.com",
            "phone": "987-654-3210"
        }
    ]

    @patch('json.dump')
    @patch('builtins.open', mock_open)
    def test_write_contacts(self, mock_dump):
        # Write contacts to file
        write_contacts_to_file('contacts.json', self.contacts)

        # Verify file was opened in write mode
        self.mock_open.assert_called_with('contacts.json', 'w')
        
        # Verify json.dump was called with correct data
        mock_dump.assert_called_with({"contacts": self.contacts}, self.mock_open())

    @patch('json.load')
    @patch('builtins.open', mock_open)
    def test_read_contacts(self, mock_load):
        # Set up mock to return test data
        mock_load.return_value = {"contacts": self.contacts}

        # Read contacts from file
        read_contacts = read_contacts_from_file('contacts.json')
        self.assertEqual(read_contacts, self.contacts)

        # Verify file was opened in read mode
        self.mock_open.assert_called_with('contacts.json', 'r')
        



if __name__ == '__main__':
    unittest.main()
