# Reviews Cars



### В проекте используется:

![version](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![version](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![version](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![version](https://img.shields.io/badge/redis-%23DD0031.svg?&style=for-the-badge&logo=redis&logoColor=white)


### Перед началом работы:

#### Установка зависимостей:

В корневой папке находится файл с зависимостями requirements.txt
```shell
pip install poetry
```
```shell
poetry install
```


#### Настройка переменных окружения:

Для работы проекта необходимо создать **.env** в корневой папке.
В нем нужно указать необходимые значения переменных:

* SECRET_KEY = **секретный ключ**
* DEBUG = **True**
* URL_PREFIX = **префикс default : api**
* DATABASE_URL = **psql://<имя пользователя>:<пароль пользователя>@<ip адрес>:<порт>/<имя базы>**
* REDIS_HOST = **хост Redis пример : redis**
* REDIS_PORT = **порт Redis пример : 6379**


(Опционально)
* GOOGLE_OAUTH2_KEY = **Ключ  Google Oauth**
* GOOGLE_OAUTH2_SECRET = **Секрет для Google Oauth**



### Запуск проекта Django:

#### Docker:
* Разворачиваем docker контейнер с проектом, запустив файл docker-compose.yml.

```shell
docker compose up --build -d
```
#### Локально:
* Перед запуском проекта локально требуется выполнить миграции на базу данных командой

```shell
python ./manage.py migrate
```
* Запуск проекта

```shell
python ./manage.py runserver
```


### Состав проекта:
* Swagger UI ``` localhost/api/docs```
* Postman дамп в корне проекта 
* Администраторский Web UI ``` localhost/admin``` тестовый аккаунт (admin@mail.com : test)
* Получение токена ``` localhost/api/auth/login``` тестовый аккаунт (test@mail.com : test)
 
* Тесты ``` pytest --cov``` 
