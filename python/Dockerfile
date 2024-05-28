FROM python:3.10-bullseye
WORKDIR /app
LABEL authors="admin"

RUN python -m venv ./.venv

COPY dependencies.txt .

RUN . ./.venv/bin/activate && \
    pip install -r dependencies.txt

COPY . .

EXPOSE 8080

CMD [".venv/bin/uvicorn", "spaceship.main:app", "--host=0.0.0.0", "--port=8080"]