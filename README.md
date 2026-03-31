# URL Shortener (FastAPI)

Простой сервис сокращения ссылок на базе FastAPI и PostgreSQL.

## Стек

* Python
* FastAPI
* PostgreSQL
* Docker

---

## Запуск проекта

### 1. Клонировать репозиторий

```bash
git clone <repo_url>
cd <repo>
```

---

### 2. Поднять базу данных

```bash
docker compose up -d
```

PostgreSQL будет доступен на:

```
localhost:6432
```

---

### 3. Создать виртуальное окружение

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

---

### 4. Установить зависимости

```bash
pip install -r requirements.txt
```

---

### 5. Запустить приложение

```bash
uvicorn src.main:app --reload
```

---

## API

### Создать короткую ссылку

```
POST /short_url
```

Body:
```json
{
  "long_url": "https://example.com"
}
```

---

### Редирект

```
GET /{slug}
```

---

## База данных

Используется PostgreSQL в Docker.

Конфигурация:
* DB: postgres
* User: postgres
* Password: postgres
* Port: 6432
