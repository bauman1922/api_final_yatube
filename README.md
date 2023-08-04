# api_final_yatube
#### Описание проекта
Разработан API для проекта социальной сети. Реализована возможность добавления, удаления и изменения постов и комментариев. Настроена пагинация, пермишены.

#### Технологии
 - Python 3.8, Django 3.2, DRF, JWT + Djoser
#### Как запустить проект:
- Клонировать репозиторий и перейти в него в командной строке:
```
git clone ...
```
```
cd api_final_yatube
```
- Cоздать и активировать виртуальное окружение:
```
python -m venv venv
```
```
source venv/Scripts/activate
```
- Установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
- Выполнить миграции:
```
python manage.py migrate
```
- Запустить проект:
```
python manage.py runserver
````
- Документация REDOC будет доступна по ссылке: 
http://127.0.0.1:8000/redoc/

#### Примеры запросов

```
GET  http://127.0.0.1:8000/api/v1/posts/
```
````
[
    {
        "id": 1,
        "author": "newbor",
        "text": "Hey",
        "pub_date": "2022-08-08T18:41:19.125087Z",
        "image": null,
        "group": null
    },
    {
        "id": 2,
        "author": "newbor",
        "text": "Тестовый пост",
        "pub_date": "2022-08-09T13:23:43.516385Z",
        "image": null,
        "group": null
    }
]
````
````
POST  http://127.0.0.1:8000/api/v1/follow/
````
Данные запроса:
````
{
  "following": "leo"
}
`````
Вывод:
````
{
    "id": 1,
    "following": "leo",
    "user": "newbor"
}
````


