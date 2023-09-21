# Запуск проекта
1. Установить pipenv `sudo apt update`, `apt install pipenv`
2. Создать виртуальное окружение и установить зависимости: `pipenv sync`
3. Запустить виртуальное окружение: `pipenv shell`
4. Создать и заполнить БД: `pipenv run python add_users.py`

    Полезное:
1. Создать новое виртуальное окружение: `pipenv --python 3.X` где "X"- версия python или `pipenv --three`
2. Установка httpie `apt install httpie`

### ДЗ: День-1
- [x] Данные из текстового файла перенесены в БД main.db
- [x] Все функции в app.py (за первый день) переделаны для работы с БД



