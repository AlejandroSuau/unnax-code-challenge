# Unnax API Challenge

_This is an API Challenge developed for Unnax Company._

## Used technologies.

* [Python 3.7](https://www.python.org/downloads/release/python-370/)
* [Django 3.0](https://docs.djangoproject.com/en/3.2/releases/3.0/)
* [Django Rest Framework 3.0](https://www.django-rest-framework.org)
* [Flake8](https://flake8.pycqa.org/en/latest/)
* [Redis 3.5](https://pypi.org/project/redis/)
* [Celery 5](https://docs.celeryproject.org/en/stable/getting-started/introduction.html)
* [RabitMQ](https://www.rabbitmq.com)
* [Selenium 3](https://pypi.org/project/selenium/)

## Endpoints.

_Note: Get methods allow pagination parameters._

* \[GET\]: http://127.0.0.1:8000/api/read/
* \[POST\]: http://127.0.0.1:8000/api/read/
  * params: {"username": "x", "password": "testpass"}

## How to run.

_Note: Docker & Docker-compose expected to be installed._

```
docker-compose up --build
```
