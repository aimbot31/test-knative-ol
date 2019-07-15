#!/usr/bin/env python3
from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return f"Hello " + requests.get("https://api.adviceslip.com/advice").json()["slip"]["advice"]