from django.apps import AppConfig
from flask import Flask

class ApiConfig(AppConfig):
    name = 'api'

app = Flask("_main_")
app.run()