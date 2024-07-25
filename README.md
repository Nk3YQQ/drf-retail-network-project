# Результаты тестирования

![Workflow Status](https://github.com/Nk3YQQ/drf-retail-network-project/actions/workflows/main.yml/badge.svg)
[![Coverage Status](coverage/coverage.svg)](coverage/coverage-report.txt)

# Структура проекта

```
drf-retail-network-project/
    |—— config/ # Настройки проекта
        |—— __init__.py
        |—— asgi.py
        |—— settings.py
        |—— urls.py
        |—— wagi.py
    |—— coverage/ # Результаты тестрования
    |—— network/ # Приложение сети
        |—— migrations/
        |—— __init__.py
        |—— admin.py
        |—— apps.py
        |—— models.py
        |—— serializers.py
        |—— services.py
        |—— urls.py
        |—— views.py
    |—— nginx/ # Настройки для Nginx
    |—— tests/ # Тесты для приложений
        |—— __init__.py
        |—— test_network_node.py
        |—— test_network_node_contact.py
        |—— test_network_node_products.py
        |—— test_user.py
    |—— users/ # Приложение пользователей
        |—— migrations/
        |—— __init__.py
        |—— admin.py
        |—— apps.py
        |—— models.py
        |—— permissions.py
        |—— serializers.py
        |—— services.py
        |—— urls.py
        |—— views.py
    |—— .dockerignore
    |—— .env.sample
    |—— .flake8
    |—— .gitignore
    |—— docker-compose.dev.yml
    |—— docker-compose.yml
    |—— Dockerfile
    |—— gunicorn_config.py
    |—— LICENSE
    |—— Makefile
    |—— manage.py
    |—— poetry.lock
    |—— pyproject.toml
    |—— README.md
    |—— requirements.txt
```

# Результаты работы

- ### Реализована модель сети по продаже электроники
- ### Сделан вывод в админ-панели созданных объектов
- ### Создан CRUD для модели поставщика
- ### Добавлена возможность фильтрации объектов по определенной стране
- ### Настроены права доступа к API так, чтобы только активные сотрудники имели доступ к API
- ### API задокументирована в Swagger и Redoc

# Основной стек проекта:

- ### Python 3.10
- ### Django 4.2
- ### Django REST Framework
- ### DRF Spectacular (OpenAPI)
- ### PostgreSQL 11
- ### Django ORM
- ### Docker
- ### unittest
- ### GitHub Actions (CI)

# Как пользоваться проектом

## 1) Скопируйте проект на Ваш компьютер

```
git clone git@github.com:Nk3YQQ/drf-retail-network-project.git
```

## 2) Добавьте файл .env для переменных окружения

Чтобы запустить проект, понадобятся переменные окружения, которые необходимо добавить в созданный Вами .env файл.

Пример переменных окружения необходимо взять из файла .env.sample

## 3) Запустите проект

Запуск проекта

```
make run
```

Остановка проекта

```
make stop
```