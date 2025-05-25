FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# 1️⃣  Спершу залежності – під root
COPY requirements.txt .
RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# 2️⃣  Тепер створюємо некореневого користувача
RUN adduser --disabled-password --gecos "" fastapi
USER fastapi

# 3️⃣  Додаємо решту коду
COPY --chown=fastapi . .

EXPOSE 8000
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "main:app", "--bind", "0.0.0.0:8000"]
