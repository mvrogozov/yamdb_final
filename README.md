![example workflow](https://github.com/mvrogozov/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

# yamdb_final
yamdb_final

# Проект Yamdb.
***
Проект YaMDb собирает отзывы пользователей на различные произведения.
***

## Возможности.

* Добавление отзыва.
* Выставление оценки.
* Комментирование отзыва.
* Контроль доступа к контенту.
***

## Установка.
***
Клонировать репозиторий и перейти в него в командной строке.

```
git clone git@github.com:mvrogozov/api_yamdb.git
```
```
cd api_yamdb
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Перейти в папку api_yamdb

```
cd api_yamdb
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

## Алгоритм регистрации пользователей
***
1. Пользователь отправляет POST-запрос на добавление нового пользователя с параметрами email и username на эндпоинт ```/api/v1/auth/signup/```

2. YaMDB отправляет письмо с кодом подтверждения (confirmation_code) на адрес email.
3. Пользователь отправляет POST-запрос с параметрами username и confirmation_code на эндпоинт  ```/api/v1/auth/token/```, в ответе на запрос ему приходит token (JWT-токен).
4. При желании пользователь отправляет PATCH-запрос на эндпоинт ```/api/v1/users/me/``` и заполняет поля в своём профайле (описание полей — в документации).

### Примеры запросов

Получение списка всех категорий:
```
GET http://127.0.0.1:8000/api/v1/categories/
```
Добавление категорий:
```
POST http://127.0.0.1:8000/api/v1/categories/
{
	"name": "string",
	"slug": "string"
}
```
Получение списка всех жанров:
```
GET http://127.0.0.1:8000/api/v1/genres/
```
Добавление жанра:
```
POST http://127.0.0.1:8000/api/v1/genres/
{
	"name": "string",
	"slug": "string"
}
```
Получение списка всех произведений:
```
GET http://127.0.0.1:8000/api/v1/titles/
```
Добавление произведения:
```
POST http://127.0.0.1:8000/api/v1/titles/
{
  "name": "string",
  "year": "int",
  "description": "string",
  "genre": [
    "string"
  ],
  "category": "string"
}
```
Получение информации о произведении:
```
GET http://127.0.0.1:8000/api/v1/titles/{titles_id}/
```
Получение списка всех отзывов:
```
GET http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/
```
Получение списка всех комментариев к отзыву:
```
GET http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/
```
Получение комментария к отзыву:
```
GET http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/
```
***
## Документация к API:
```
http://127.0.0.1:8000/redoc/
```

## Возможен запуск в контейнерах Docker:

Необходимые файлы лежат в папке infra.
Настройки сервера nginx лежат в файле nginx/nginx.conf.
На сервер скопировать файлы docker-compose.yml и nginx.conf, запустить docker-compose:
```
sudo docker-compose up
```
Переменные окружения, необходимые для запуска:

* DB_ENGINE - настройка ENGINE для БД в django.settings
* DB_HOST - имя хоста с БД (в проекте - 'db')
* DB_NAME - имя БД (в проекте - 'postgres')
* DB_PORT - порт для БД
* POSTGRES_PASSWORD - пароль БД
* POSTGRES_USER - пользователь БД
***

Автор:
* Рогозов Михаил