FROM python:3.11-slim
LABEL authors="Team 4"

COPY requirements.txt /

RUN pip3 install --upgrade pip

RUN pip3 install -r /requirements.txt

COPY . /app

WORKDIR /app

EXPOSE 80

CMD ["python", "app.py"]