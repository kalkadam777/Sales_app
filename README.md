# 📌 Sales & Trading App

🚀 **Sales & Trading App** — это мощное веб-приложение для управления продажами, торговыми операциями и аналитикой. Оно сочетает Django и Django REST Framework на бэкенде, а также использует Bootstrap для фронтенда.

---

## Демо

-   Ссылка на Deploy: [Sales_app](https://sales-app-qwi6.onrender.com)
-   Ссылка на видео: [Youtube]

---

## 🌟 Функциональность

✅ **Аутентификация и авторизация** (JWT)  
✅ **Управление пользователями** (регистрация, вход, профиль)  
✅ **Торговая площадка** (покупка/продажа товаров)  
✅ **Система аналитики** (графики, отчеты)  
✅ **Роли пользователей** (администратор, трейдер, покупатель)  
✅ **Реактивный UI** с Bootstrap 5  
✅ **Swagger-документация API**

---

## ⚡ Технологии

🔹 **Backend:** Django, Django REST Framework, PostgreSQL  
🔹 **Frontend:** Django Templates (Jinja2), Bootstrap 5  
🔹 **Аутентификация:** JWT (Simple JWT)  
🔹 **Фоновые задачи:** Celery + Redis (если потребуется)  
🔹 **Документация API:** drf-yasg (Swagger UI)  
🔹 **DevOps:** Docker, CI/CD

---

## 🔧 Установка

### 1️⃣ Клонирование репозитория

```bash
git clone https://github.com/username/sales-trading-app.git
cd sales-trading-app
```

### 2️⃣ Создание виртуального окружения

```bash
python -m venv venv
source venv/bin/activate  # для macOS/Linux
venv\Scripts\activate  # для Windows
```

### 3️⃣ Установка зависимостей

```bash
pip install -r requirements.txt
```

### 4️⃣ Настройка базы данных

```bash
python manage.py migrate
```

### 5️⃣ Создание суперпользователя

```bash
python manage.py createsuperuser
```

### 6️⃣ Запуск сервера

```bash
python manage.py runserver
```

Приложение будет доступно по адресу:  
🔗 **http://127.0.0.1:8000/**

---

## 📌 API Endpoints

### 🔑 Аутентификация

| Метод  | URL                   | Описание             |
| ------ | --------------------- | -------------------- |
| `POST` | `/api/token/`         | Получение JWT-токена |
| `POST` | `/api/token/refresh/` | Обновление токена    |

### 👥 Пользователи

| Метод  | URL                    | Описание                        |
| ------ | ---------------------- | ------------------------------- |
| `GET`  | `/api/users/`          | Список пользователей            |
| `POST` | `/api/users/register/` | Регистрация нового пользователя |
| `GET`  | `/api/users/<id>/`     | Детали профиля                  |

### 📊 Торговля

| Метод  | URL                    | Описание                 |
| ------ | ---------------------- | ------------------------ |
| `GET`  | `/api/trading/`        | Список торговых операций |
| `POST` | `/api/trading/create/` | Создание сделки          |
| `GET`  | `/api/trading/<id>/`   | Детали сделки            |

---

## 🔥 Скриншоты

### 🔹 Главная страница

![Главная](https://via.placeholder.com/800x400?text=Главная+страница)

### 🔹 Личный кабинет

![Профиль](https://via.placeholder.com/800x400?text=Личный+кабинет)

---

## 🛠 Дополнительные настройки

### Запуск с Docker

```bash
docker-compose up --build
```

### Запуск Celery (если есть фоновая обработка)

```bash
celery -A sales_trading_app worker --loglevel=info
```
