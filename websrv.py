#!/usr/bin/env python

''' By Ryan Gao, 2014 '''

from flask import Flask, request
import subprocess as subp
import os, sys
from sp import load_by_firefox, url as th_url
import requests

app = Flask(__name__)

@app.route("/")
def hello():
    if '_escaped_fragment_' in request.args:
        return load_by_firefox('#' + request.args.get('_escaped_fragment_'))
    return "Hello World!"

@app.route("/<path:path>")
def get_everything(path):
    print 'Getting everything: ', path
    r = requests.get(th_url.format(path))
    return (r.content, r.status_code)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
