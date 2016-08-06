# -*- coding: utf-8 -*-

from flask import request, render_template, jsonify
from blog import *

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
