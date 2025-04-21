FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod +x ./wait_for_it.sh ./docker_entrypoint.sh

ENTRYPOINT [ "./docker_entrypoint.sh" ]

CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:8000"]