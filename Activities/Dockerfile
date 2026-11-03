# Build from Lab8 with: docker build -f Activities/Dockerfile --target <target> ..
FROM python:3.12-alpine AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app

WORKDIR /app
COPY Lab5/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY Lab5/app.py Lab5/database.py ./
COPY Lab5/database.db /data/database.db

# Lab 5 stores database.db relative to its current working directory.
WORKDIR /data

FROM base AS lab5
COPY Lab8/Activities/run_lab5.py /app/
EXPOSE 5000
CMD ["python", "/app/run_lab5.py"]

FROM base AS names
COPY Lab8/Activities/names_app.py /app/
EXPOSE 3000
CMD ["python", "/app/names_app.py"]
