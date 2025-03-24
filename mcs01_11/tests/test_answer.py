import unittest
from unittest.mock import patch, MagicMock
from src.reduce_sum.answer import sum_numbers

class TestSumNumbers(unittest.TestCase):
    @patch('src.reduce_sum.answer.reduce')
    def test_sum_positive_numbers(self, mock_reduce):
        """Test sum of positive numbers with mocked reduce"""
        numbers = [1, 14, 6, 19, 34, 22]
        expected_result = 96
        
        # Configure the mock to return the expected result
        mock_reduce.return_value = expected_result
        
        result = sum_numbers(numbers)
        
        # Verify the result
        self.assertEqual(result, expected_result)
        
        # Verify that reduce was called with the correct arguments
        mock_reduce.assert_called_once()
        args, kwargs = mock_reduce.call_args
        self.assertEqual(args[1], numbers)  # Check the numbers list
        # Check that the lambda function is a function that adds two numbers
        self.assertTrue(callable(args[0]))
        self.assertEqual(args[0](1, 2), 3)  # Verify the lambda function behavior

    @patch('src.reduce_sum.answer.reduce')
    def test_sum_empty_list(self, mock_reduce):
        """Test sum of empty list with mocked reduce"""
        numbers = []
        
        # Configure the mock to return 0 for empty list
        mock_reduce.return_value = 0
        
        result = sum_numbers(numbers)
        
        # Verify the result
        self.assertEqual(result, 0)
        
        # Verify that reduce was called with the correct arguments
        mock_reduce.assert_called_once()
        args, kwargs = mock_reduce.call_args
        self.assertEqual(args[1], numbers)
        self.assertTrue(callable(args[0]))
        self.assertEqual(args[0](1, 2), 3)

    @patch('src.reduce_sum.answer.reduce')
    def test_sum_negative_numbers(self, mock_reduce):
        """Test sum of negative numbers with mocked reduce"""
        numbers = [-1, -2, -3, -4]
        expected_result = -10
        
        mock_reduce.return_value = expected_result
        result = sum_numbers(numbers)
        
        self.assertEqual(result, expected_result)
        mock_reduce.assert_called_once()
        args, kwargs = mock_reduce.call_args
        self.assertEqual(args[1], numbers)
        self.assertTrue(callable(args[0]))
        self.assertEqual(args[0](1, 2), 3)

    @patch('src.reduce_sum.answer.reduce')
    def test_sum_mixed_numbers(self, mock_reduce):
        """Test sum of mixed positive and negative numbers with mocked reduce"""
        numbers = [1, -2, 3, -4, 5]
        expected_result = 3
        
        mock_reduce.return_value = expected_result
        result = sum_numbers(numbers)
        
        self.assertEqual(result, expected_result)
        mock_reduce.assert_called_once()
        args, kwargs = mock_reduce.call_args
        self.assertEqual(args[1], numbers)
        self.assertTrue(callable(args[0]))
        self.assertEqual(args[0](1, 2), 3)

    @patch('src.reduce_sum.answer.reduce')
    def test_sum_float_numbers(self, mock_reduce):
        """Test sum of floating-point numbers with mocked reduce"""
        numbers = [1.5, 2.5, 3.5]
        expected_result = 7.5
        
        mock_reduce.return_value = expected_result
        result = sum_numbers(numbers)
        
        self.assertEqual(result, expected_result)
        mock_reduce.assert_called_once()
        args, kwargs = mock_reduce.call_args
        self.assertEqual(args[1], numbers)
        self.assertTrue(callable(args[0]))
        self.assertEqual(args[0](1, 2), 3)

if __name__ == '__main__':
    unittest.main()