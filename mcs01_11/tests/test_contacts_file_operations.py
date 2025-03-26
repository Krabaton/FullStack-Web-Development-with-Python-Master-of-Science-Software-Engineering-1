import unittest
from unittest.mock import patch, mock_open
from src.method.main import write_contacts_to_file, read_contacts_from_file

class TestContactsFileOperations(unittest.TestCase):
    def setUp(self):
        self.mock_open = mock_open()
        self.contacts = [
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
    @patch('builtins.open', new_callable=mock_open)
    def test_write_contacts(self, mock_file, mock_dump):
        write_contacts_to_file('contacts.json', self.contacts)

        # Verify file was opened in write mode
        mock_file.assert_called_with('contacts.json', 'w')
        
        # Verify json.dump was called with correct data
        mock_dump.assert_called_with({"contacts": self.contacts}, mock_file())
        
        # Ensure write function is called only once
        self.assertEqual(mock_dump.call_count, 1)

    @patch('json.load')
    @patch('builtins.open', new_callable=mock_open)
    def test_read_contacts(self, mock_file, mock_load):
        mock_load.return_value = {"contacts": self.contacts}

        read_contacts = read_contacts_from_file('contacts.json')
        self.assertEqual(read_contacts, self.contacts)

        # Verify file was opened in read mode
        mock_file.assert_called_with('contacts.json', 'r')
        
        # Ensure read function is called only once
        self.assertEqual(mock_load.call_count, 1)

    @patch('builtins.open', new_callable=mock_open)
    def test_write_contacts_file_error(self, mock_file):
        mock_file.side_effect = IOError("File not accessible")
        with self.assertRaises(IOError):
            write_contacts_to_file('contacts.json', self.contacts)

    @patch('builtins.open', new_callable=mock_open)
    def test_read_contacts_file_error_raises_io_error(self, mock_file):
        mock_file.side_effect = IOError("File not accessible")
        with self.assertRaises(IOError):
            read_contacts_from_file('contacts.json')

    def tearDown(self):
        self.mock_open.reset_mock()  # Скидаємо стан mock_open

if __name__ == '__main__':
    unittest.main()
