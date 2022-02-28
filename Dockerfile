FROM python:3.10-alpine
WORKDIR /app

RUN python -m pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# RUN python manage.py migrate
# RUN python manage.py collectstatic
