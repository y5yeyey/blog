# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, jsonify
import simplejson as json
from datetime import datetime
import pandas as pd

app = Flask(__name__)

@app.route('/')
@app.route('/about')
def homepage():
    return render_template("about.html")

@app.route('/projects')
def report():
    return render_template("projects.html")

@app.route('/resume')
def resume():
    return render_template("resume.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

