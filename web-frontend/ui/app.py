import os
from datetime import datetime

import subprocess

# Upgrade Jinja2 package to a specific version
subprocess.check_call(['pip', 'install', 'jinja2==2.11.3'])


from flask import Flask, redirect, render_template, request, url_for
import streamlit as st
from model import initialize_index

app = Flask(__name__)
index = None

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/get")
def get_bot_response():
    query_text = request.args.get("msg", None)
    if query_text is None:
        return "Invalid input"
    response = index.query(query_text)
    return str(response), 200

if __name__ == "__main__":
    index = initialize_index("index.json")
    app.run(debug=True)
