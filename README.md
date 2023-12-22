# NeuralNetworkFromScratch

Based largely on the 
[YouTube series by sentdex](https://www.youtube.com/watch?v=Wo5dMEP_BbI&list=PLQVvvaa0QuDcjD5BAw2DxE6OF2tius3V3), 
this project aims to build a neural network without using machine-learning focused libraries like Tensorflow and PyTorch.
Like many other elementary neural networking projects, this project will use the [MNIST database](https://en.wikipedia.org/wiki/MNIST_database) to train a neural network to recognize hand-drawn digits.
Although the series stresses other libraries such as 
[pandas](https://pandas.pydata.org/), 
[matplotlib](https://matplotlib.org/) and 
[scikit-learn](https://scikit-learn.org/) 
for data analysis, this project will be limited to 
[numpy](https://numpy.org/) 
to stress a "library free" syntax that forces a raw understanding of neural networking concepts.

***

## About the MNIST dataset

The dataset can be downloaded 
[here](https://drive.google.com/file/d/1eEKzfmEu6WKdRlohBQiqi3PhW_uIVJVP/view),
and contains:

- 60,000, 28x28 pixel images of hand-drawn images. This set of images is called the "training" set, and each image contains a label with its associated number for training purposes.
- 10,000, 28x28 pixel images. This set of images is called the "testing" set, and contrary to the training set, this set contains no labels, which the model is meant to give to the set following its training.

## Notes