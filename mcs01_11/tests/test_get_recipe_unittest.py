import unittest
from src.get_recipe.get_recipe import get_recipe
import os

class TestGetRecipe(unittest.TestCase):
    def setUp(self):
        # Створюємо тимчасовий CSV файл для тестів
        self.test_file = 'test_ingredients.csv'
        with open(self.test_file, 'w') as f:
            f.write("60b90c1c13067a15887e1ae1,Піца,томати,сир,базилік\n")
            f.write("60b90c1c13067a15887e1ae2,Салат,огірки,томати,майонез\n")
            f.write("60b90c1c13067a15887e1ae3,Суп,картопля,морква,цибуля\n")

    def tearDown(self):
        # Видаляємо тимчасовий файл після тестів
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_get_existing_recipe(self):
        """Тест отримання існуючого рецепту"""
        result = get_recipe(self.test_file, "60b90c1c13067a15887e1ae1")
        self.assertIsNotNone(result)
        self.assertEqual(result['id'], "60b90c1c13067a15887e1ae1")
        self.assertEqual(result['name'], "Піца")
        self.assertEqual(result['ingredients'], ["томати", "сир", "базилік"])

    def test_get_non_existing_recipe(self):
        """Тест отримання неіснуючого рецепту"""
        result = get_recipe(self.test_file, "non_existing_id")
        self.assertIsNone(result)

    def test_empty_file(self):
        """Тест роботи з порожнім файлом"""
        with open(self.test_file, 'w') as f:
            f.write("")
        result = get_recipe(self.test_file, "any_id")
        self.assertIsNone(result)

    def test_invalid_file_format(self):
        """Тест роботи з некоректним форматом файлу"""
        with open(self.test_file, 'w') as f:
            f.write("invalid,format\n")
        result = get_recipe(self.test_file, "any_id")
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
