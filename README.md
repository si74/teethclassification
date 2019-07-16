# teethclassification
Using keras and CNNs to classify teeth.

## Background

## The problem

## Setup && Installation

Ensure that you have a version of python 3.6.0 or higher. Keras and tensorflow require this version of python at a minimum to work.

Other prereqs include:
- numpy
- opencv-python
- homebrew (MacOS)

# Mac OSx

1. Install pipenv and pyenv.

```
$ brew install pyenv
$ brew install pipenv
```

2. Install the required version of python.
```
$ pyenv install 3.6.0
# Set the global python
$ pyenv global 3.6.0
# Set the local python
$ pyenv local 3.6.0
```

3. Install prereqs and important packages ensuring you are using python 3.6.0.
```
$ pipenv install numpy --python /usr/local/var/pyenv/shims/python
$ pipenv install opencv-python --python /usr/local/var/pyenv/shims/python
$ pipenv install keras --python /usr/local/var/pyenv/shims/python
$ pipenv install tensorflow --python /usr/local/var/pyenv/shims/python
```

# Windows

## Resources

1. How to leverage pyenv and pipenv:
- https://hackernoon.com/reaching-python-development-nirvana-bb5692adf30c

2. How to use tensorflow and keras:
- https://www.analyticsvidhya.com/blog/2019/01/build-image-classification-model-10-minutes/
- https://www.geeksforgeeks.org/python-image-classification-using-keras/
- https://medium.com/nybles/create-your-first-image-recognition-classifier-using-cnn-keras-and-tensorflow-backend-6eaab98d14dd

3. Keras documentation:
- https://keras.io/models/sequential/#predict
- https://keras.io/preprocessing/image/
