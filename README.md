# Сервис YaCut

## Технологии:
 ![GitHub](https://img.shields.io/badge/-GitHub-464646??style=flat-square&logo=GitHub)  ![Python](https://img.shields.io/badge/-Python-464646??style=flat-square&logo=Python)
 ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)

## Описание проекта
Сервис укорачивания ссылок с web интерфейсом и REST API. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.
___
## Как запустить проект

Клонируйте репозиторий, перейдите в папку, создайте виртуальное окружение и активируйте:
```
python3 -m venv env
```
```
. venv/bin/activate
```

Обновите менеджер пакетов (pip) и установите зависимости из файла requirements.txt:

```
(venv) python3 -m pip install --upgrade pip
```
```
(venv) pip install -r requirements.txt
```
___
## Запуск сервеса:
Создать файл .env

* Если у вас Linux/MacOS
```
touch .env
```

* Если у вас Windows
```
type nul > .env
```
Заполнить файл .env:

```
FLASK_APP=opinions_app
FLASK_ENV=development
DATABASE_URI=sqlite:///db.sqlite3
SECRET_KEY=YOUR_SECRET_KEY
```
Создать базу данных:
```
flask shell
```
```
from yacut import db
db.create_all()
exit()
```
Выполнить миграции:
```
flask db upgrade
```
Выполнить запус сервиса:
```
flask run
```
___
## Доступ к сервису:
Сервис будет доступен по адресу http://localhost:5000/
image.png
### Дополнительно
Документация по API доступна по адрессу: http://localhost:5000/swagger
___
### Автор
Selivanov Dmitry