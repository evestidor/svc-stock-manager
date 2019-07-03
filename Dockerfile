FROM python:3.7

WORKDIR /app

ENV PYTHONUNBUFFERED 1

COPY Pipfile* /app/

RUN pip install pipenv

RUN pipenv install --system --deploy --dev

COPY . .

CMD python manage.py runserver 0.0.0.0:8000
