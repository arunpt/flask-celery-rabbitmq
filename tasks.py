import time
import random
from celery import Celery

app = Celery('tasks', broker='amqp://guest:guest@rabbitmq')

@app.task()
def task1():
    time.sleep(random.randint(1, 10))
    return "task completed"


app.autodiscover_tasks()