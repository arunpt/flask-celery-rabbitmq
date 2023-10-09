from flask import Flask
from celery import Celery

app = Flask(__name__)
celery_app = Celery("myapp", broker="amqp://guest:guest@rabbitmq")


@app.get("/")
def index():
    celery_app.send_task("tasks.task1")
    return "Server is running"

