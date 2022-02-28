FROM ubuntu
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SUPERUSER_USERNAME=testuser
ENV DJANGO_SUPERUSER_PASSWORD=testpass
WORKDIR /code
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y python3.8 python3-pip python3.8-dev unixodbc-dev
RUN pip install --upgrade pip
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate --run-syncdb
RUN python3 manage.py loaddata fixtures/DB.json
#RUN echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@myproject.com', 'password')" | python3 manage.py shell
RUN python3 manage.py createsuperuser --noinput
EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000" ]
