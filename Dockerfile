# FROM python:3
# RUN pip install django
# COPY . .

# RUN python manage.py migrate
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

FROM python:3.11

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt
RUN python manage.py migrate
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]