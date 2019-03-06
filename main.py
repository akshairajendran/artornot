# [START gae_python37_app]
from flask import Flask, flash, redirect, render_template, request, url_for
from PIL import Image
import requests
from io import BytesIO


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/')
def index(data=[], error=None, image_url=None):
    """Returns index page"""
    if image_url:
      response = requests.get(image_url)
      img = Image.open(BytesIO(response.content))
    return render_template('index.html', data=data, error=error, image_url=image_url)

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
