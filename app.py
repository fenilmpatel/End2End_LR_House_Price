# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 14:53:34 2020

@author: fenil
"""

from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_flask():
    return 'Hello flask user, How are you?'

port = os.environ.get('PORT',5000)

if __name__ == '__main__':
    
    app.run(debug=1,host='0.0.0.0',port=port)