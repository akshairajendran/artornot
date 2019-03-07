# [START gae_python37_app]
from flask import Flask, flash, redirect, render_template, request, url_for
import requests
from io import BytesIO
import os
import matplotlib as mpl
mpl.use('TkAgg')
from fastai.vision import *


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)

MODEL_PATH = os.path.dirname(os.path.abspath(__file__))
learn = load_learner(MODEL_PATH)
artists = [(" ").join([s.capitalize() for s in a.split("_")]) for a in learn.data.classes]

@app.route('/')
def index(data=[], error=None, image_url=None):
    """Returns index page"""
    pred_str = None
    pred_pct = 0
    if image_url:
      try:
        response = requests.get(image_url)
        img = open_image(BytesIO(response.content))
        pred_class,pred_idx,outputs = learn.predict(img)
        pred_str = (" ").join([s.capitalize() for s in pred_class.__str__().split("_")])
        pred_pct = round(float(outputs[pred_idx]),3) * 100
      except Exception as e:
        error = repr(e)

    return render_template('index.html', data=data, error=error, image_url=image_url, 
                                         pred_str=pred_str, pred_pct=pred_pct, artists=artists)

@app.route('/result', methods=['POST'])
def result():
    """Takes post request and returns index with appropriate data"""
    data = []
    error = None
    _image_url = request.form.get('image_url')

    if _image_url:
      pass
    else:
      error = "No url provided!"
    
    return index(data=data, error=error, image_url=_image_url)


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
