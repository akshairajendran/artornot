# artornot
Art or Not is a simple Flask App that takes a URL for a work of art and attempts to guess the artist. It was built based on Lessons 1 and 2 of FastAI's fantastic [Practical Deep Learning for Coders v3](https://course.fast.ai) course and uses a Resnet34 architecture pre-trained on ImageNet.

The app was trained on a small group of artists (Warhol, Lichtenstein, Haring, Caravaggio, Botticelli) and is able to guess works only by them.

## Model
I have not committed the model or training data to git for space purposes but [artornot.ipynb](artornot.ipynb) contains the process by which the model can be trained given the necessary training data. When I originally trained the model I scraped artists' images from Google using [google-images-download](https://github.com/hardikvasa/google-images-download). As mentioned above the model is a Resnet34 pre-trained on ImageNet, trained for 4 epochs with the pre-trained layers frozen and trained for another 4 epochs with the pre-trained layers unfrozen. The average training time per epoch was about 14 seconds for a total training time of just under 2 minutes.

## Deployment
This app was originally deployed on Google Cloud Platform and I have included all the necessary deployment files
