# Pipenv

Основні команди:

```bash
pip install pipenv --user      # Встановлення Pipenv
pipenv --python 3.12           # Створення середовища для Python 3.12
pipenv install flask           # Встановлення пакета Flask
pipenv shell                   # Вхід у середовище
pipenv run python main.py       # Запуск скрипта в середовищі
pipenv uninstall flask         # Видалення пакета Flask
pipenv --rm                    # Видалення віртуального середовища
```

# Poetry

Основні команди:

```bash
pip install poetry --user       # Встановлення Poetry
poetry new my_project           # Створення нового проєкту
poetry init                     # Ініціалізація існуючого проєкту
poetry add requests             # Додавання пакета requests
poetry remove requests          # Видалення пакета
poetry install                  # Встановлення залежностей
poetry update                   # Оновлення залежностей
poetry shell                    # Вхід у віртуальне середовище
poetry run python main.py        # Запуск скрипта
```

# UV

Основні команди:

```bash
uv venv create         # Створення віртуального середовища
uv venv path           # Показати шлях до активного середовища
uv run python main.py  # Запуск скрипта у середовищі
uv pip install flask   # Встановлення пакета Flask
uv pip uninstall flask # Видалення пакета Flask
```
