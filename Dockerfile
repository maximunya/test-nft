FROM 3.11.9-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app/

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN python manage.py collectstatic --no-input

RUN python manage.py migrate
RUN python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); if not User.objects.filter(username='admin').exists(): User.objects.create_superuser('admin', 'admin@example.com', 'admin')"

CMD gunicorn backend.wsgi:application --bind 0.0.0.0:8000 --workers 3