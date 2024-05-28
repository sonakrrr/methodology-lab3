FROM python:3.10-bullseye

WORKDIR /app

COPY . .

RUN pip install -r ./requirements/backend.in

CMD ["uvicorn", "spaceship.main:app", "--host=0.0.0.0", "--port=8080"]