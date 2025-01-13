# web_application

Problem Set I - Regex

Write a regex to extract all the numbers with orange color background from the below text in italics (Output should be a list).


{"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10},{"id":11},{"id":648},{"id":649},{"id":650},{"id":651},{"id":652},{"id":653}],"errors":[{"code":3,"message":"[PHP Warning #2] count(): Parameter must be an array or an object that implements Countable (153)"}]}


# to complete the problem 1 i have used python

import re

text = '''{"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},
{"id":10},{"id":648},{"id":649},{"id":650},{"id":651},{"id":652},{"id":653}], "errors":[{"code":3,
"message":"[PHP Warning #2] count(): Parameter must be an array or an object that implements Countable [153]"}]}
'''


matches = re.findall(r'(?<="id":)(\d+)', text)

numbers = list(map(int, matches))
print(numbers)

output = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 648, 649, 650, 651, 652, 653]
# regex(regular expression) is pattern matchinh tool used to search, validate, extract and manipulate data efficiently
# regex is used for 
# data validation, search and validation, web scraping, file manupulation


Problem Set 2 - A functioning web app with API

# functioning_webapp 
Documentation for Functioning Web Application

Project Setup

1. Create a Virtual Environment

Create a virtual environment using the following command:
python -m venv env

Activate the virtual environment:
Windows:
env\Scripts\activate


2. Install Django
Install Django and other dependencies using:
pip install django

3. Create a Django Project
Create the project using one of the following commands:
django-admin startproject web_app
OR
python -m django startproject web_app

4. Navigate to the Project Directory
Change directory to the project folder:
cd web_app

5. Create Django Apps
Create an app for admin functionality:
python manage.py startapp admin

Only the admin has the access to post the apps.
Create an app for user functionality:

python manage.py startapp user

6. Include Apps in Project Settings

Add the created apps to the INSTALLED_APPS list in settings.py:
INSTALLED_APPS = [
    ...
    'admin',
    'user',
    'rest_framework',  # For REST framework
]

7. Add URLs

Include the app URLs in the project's urls.py file:
from django.urls import include, path

urlpatterns = [
    path('admin/', include('admin.urls')),
    path('', include('user.urls')),
]

Database Models

Models for Admin and User are written in their respective models.py files within the admin and user apps.

Views and Logic
Admin App Views
Logic in views.py includes functionalities for:
Register
Login
Adding apps
Getdata
Deletedata

User App Views
Logic in views.py includes functionalities for:
Register
Login
Profile
Points
Tasks

Templates
Created templates for the following purposes:
Admin
App
Home
Index
Login
Points
Profile
Register
Task

Code for each template is written in its respective .html file, tailored to the application’s requirements.

Data Handling with REST Framework

Installed Django REST framework:

pip install djangorestframework

Added rest_framework to INSTALLED_APPS in settings.py.

Used serializers from the REST framework to handle GET and DELETE functionality during development.

Requirements Freeze

Freezed the dependencies into a requirements.txt file:

Problem Set 3
Please answer the below questions:

A. Write and share a small note about your choice of system to schedule periodic tasks (such as downloading a list of ISINs every 24 hours). Why did you choose it? Is it reliable enough; Or will it scale? If not, what are the problems with it? And, what else would you recommend to fix this problem at scale in production?

ANSWER
Choice of System for Scheduling Periodic Tasks
System Chosen: Celery with a Message Broker (e.g., RabbitMQ/Redis) and a Scheduler like Celery Beat
Why Did I Choose It?
1.Ease of Use: Celery is a proper task queue system for python, making it straightforward to schedule and excute periodic tasks.
2.Flexibility: with celery beat, you can schedule tasks dynamically without restarting the service and use Cron-like scheduling.
3.Reliabilty:Celery ensures task execution with retries in case of failure, using message brokers like redis or RabbitMQ  to queue the tasks.
4.Scalability: Celery supports distributed task execution, making it suitable for systems with growing workloads.

Is It Reliable Enough?
Yes, it is reliable for small to medium-scale systems due to its mature ecosystem, active community, and robust error handling. However, its reliability depends on:

The configuration of the message broker (e.g., Redis/RabbitMQ).
The system's ability to handle message persistence and retries during downtime.

Will It Scale?
Celery scales well for moderate workloads by adding workers and supporting distributed task execution. However, at large scales, it may face bottlenecks in message broker capacity, task coordination, and monitoring, making it less ideal for high-throughput systems.

Problems with Celery at Scale
Celery may face bottlenecks in message brokers (Redis/RabbitMQ), limited monitoring (e.g., Flower), increased task latency for high-throughput systems, and challenges in recovering from broker or worker failures.    

Recommendations for Scaling in Production
Airflow: For complex workflows with dependencies.
Kubernetes CronJobs: For simple, periodic tasks that need scalability.
Kafka: For large-scale, event-driven systems.
Monitoring & Optimization: Track performance and fine-tune task settings for efficiency.