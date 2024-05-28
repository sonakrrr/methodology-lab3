FROM python:alpine

WORKDIR /app

COPY requirements/backend.in ./requirements/

RUN apk add --no-cache musl-dev g++ gcc lapack-dev

RUN pip install -r ./requirements/backend.in

COPY . .

CMD ["uvicorn", "spaceship.main:app", "--host=0.0.0.0", "--port=8080"]