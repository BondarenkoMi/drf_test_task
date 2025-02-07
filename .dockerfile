
FROM python:3.10

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN pip install gunicorn

EXPOSE 8000

CMD ["python", "manage.py", "runserver"]
