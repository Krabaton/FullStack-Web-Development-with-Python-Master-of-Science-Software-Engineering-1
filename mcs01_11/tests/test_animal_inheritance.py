from src.my_class.main import Animal, Cat, Dog, CatDog, DogCat

def test_animal():
    animal = Animal("Test", 10)
    assert animal.nickname == "Test"
    assert animal.weight == 10
    assert animal.say() is None

def test_cat():
    cat = Cat("Murzik", 5)
    assert cat.nickname == "Murzik"
    assert cat.weight == 5
    assert cat.say() == "Meow"

def test_dog():
    dog = Dog("Rex", 15)
    assert dog.nickname == "Rex"
    assert dog.weight == 15
    assert dog.say() == "Woof"

def test_catdog():
    catdog = CatDog("Mix", 8)
    assert catdog.nickname == "Mix"
    assert catdog.weight == 8
    assert catdog.say() == "Meow"  # Cat's say() comes first in MRO
    assert catdog.info() == "Mix-8"

def test_dogcat():
    dogcat = DogCat("Mix", 8)
    assert dogcat.nickname == "Mix"
    assert dogcat.weight == 8
    assert dogcat.say() == "Woof"  # Dog's say() comes first in MRO
    assert dogcat.info() == "Mix-8" 