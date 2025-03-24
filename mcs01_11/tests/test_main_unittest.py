import unittest
from src.my_class.main import Animal, Cat, Dog, CatDog, DogCat

class TestAnimal(unittest.TestCase):
    def test_animal_creation(self):
        """Тест створення базового класу Animal"""
        animal = Animal("Test", 10)
        self.assertEqual(animal.nickname, "Test")
        self.assertEqual(animal.weight, 10)
        self.assertIsNone(animal.say())

    def test_cat_creation(self):
        """Тест створення класу Cat"""
        cat = Cat("Murzik", 5)
        self.assertEqual(cat.nickname, "Murzik")
        self.assertEqual(cat.weight, 5)
        self.assertEqual(cat.say(), "Meow")

    def test_dog_creation(self):
        """Тест створення класу Dog"""
        dog = Dog("Rex", 15)
        self.assertEqual(dog.nickname, "Rex")
        self.assertEqual(dog.weight, 15)
        self.assertEqual(dog.say(), "Woof")

    def test_catdog_creation(self):
        """Тест створення класу CatDog"""
        catdog = CatDog("Mix", 8)
        self.assertEqual(catdog.nickname, "Mix")
        self.assertEqual(catdog.weight, 8)
        self.assertEqual(catdog.say(), "Meow")  # Cat's say() comes first in MRO
        self.assertEqual(catdog.info(), "Mix-8")

    def test_dogcat_creation(self):
        """Тест створення класу DogCat"""
        dogcat = DogCat("Mix", 8)
        self.assertEqual(dogcat.nickname, "Mix")
        self.assertEqual(dogcat.weight, 8)
        self.assertEqual(dogcat.say(), "Woof")  # Dog's say() comes first in MRO
        self.assertEqual(dogcat.info(), "Mix-8")

    def test_mro_order(self):
        """Тест порядку розрішення методів (MRO)"""
        catdog = CatDog("Mix", 8)
        dogcat = DogCat("Mix", 8)
        
        # Перевіряємо, що CatDog використовує метод say() з Cat
        self.assertEqual(catdog.say(), "Meow")
        # Перевіряємо, що DogCat використовує метод say() з Dog
        self.assertEqual(dogcat.say(), "Woof")

if __name__ == '__main__':
    unittest.main()
