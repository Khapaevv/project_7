Треккер Привычек
Описание проекта
Этот проект представляет собой API для отслеживания привычек, который позволяет пользователям создавать, редактировать и удалять свои привычки, а также получать напоминания через Telegram. API предоставляет возможность работать с полезными и приятными привычками, а также управлять их периодичностью и вознаграждениями.

Документация
GET /swagger/: Документация в формате Swagger UI.
GET /redoc/: Документация в формате ReDoc.
Используемые технологии:
Python 3.12
Django 4.2.2
PostgreSQL
Django REST Framework
Celery
Redis
Telegram API
Установка
Клонируйте репозиторий:
git clone https://github.com/Khapaevv/project_7/tree/main
Установите зависимости с помощью Poetry:
poetry install
Настройте переменные окружения. Создайте файл .env и добавьте необходимые переменные, такие как:
SECRET_KEY=
NAME=
BD_USER=
PASSWORD=
HOST=
PORT=
TELEGRAM_TOKEN=
LOCATION=
LOCALHOST=
