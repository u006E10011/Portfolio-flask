# Portfolio Web App

Веб-приложение на Flask для создания и демонстрации портфолио разработчиков. Проект включает в себя систему аутентификации, профили пользователей, управление проектами и живой поиск по именам пользователей.

## Основные возможности

- Аутентификация и верификация: Регистрация с подтверждением через Яндекс Почту (5-значный код).
- Безопасность: Блокировка аккаунта на 5 минут после 5 неудачных попыток входа.
- Профиль пользователя: Аватар, био, список навыков и ссылки на социальные сети.
- Управление проектами: Создание и редактирование проектов, загрузка нескольких скриншотов, выбор обложки через Drag-and-Drop.
- Поиск: Живой поиск пользователей по @username.
- Интерфейс: Темная тема в стиле GitHub на базе Bootstrap 5.

## Технологический стек

- Backend: Flask, Flask-SQLAlchemy, Flask-Migrate, Flask-Login, Flask-WTF, Flask-Mail.
- Database: PostgreSQL.
- Frontend: Jinja2, Bootstrap 5, SortableJS.
- DevOps: Docker, Docker Compose.

## Установка и запуск

### Предварительные требования

- Docker и Docker Compose.
- Почтовый ящик на Яндексе и "Пароль приложения" для работы SMTP.

### Настройка окружения

1. Склонируйте репозиторий.
2. Создайте файл `.env` на основе `.env.example`:

```env
DB_USER=postgres
DB_PASSWORD=postgres
DB_NAME=portfolio_db
SECRET_KEY=your_secret_key
MAIL_USERNAME=your_email@yandex.ru
MAIL_PASSWORD=your_yandex_app_password
```

### Запуск через Docker Compose

1. Соберите и запустите контейнеры:

```bash
docker-compose up -d --build
```

2. Выполните миграции базы данных:

```bash
docker-compose exec web flask db init
docker-compose exec web flask db migrate -m "Initial migration"
docker-compose exec web flask db upgrade
```

Приложение будет доступно по адресу `http://localhost:5000`.

## Структура проекта

- `app.py`: Основной файл приложения и маршрутизация.
- `models.py`: Модели данных SQLAlchemy (User, Project, ProjectImage).
- `forms.py`: Формы Flask-WTF и валидация.
- `templates/`: HTML-шаблоны Jinja2.
- `static/`: Статические файлы (css, js, img).
- `Dockerfile` & `docker-compose.yml`: Конфигурация контейнеризации.
