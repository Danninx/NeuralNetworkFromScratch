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
[NumPy](https://numpy.org/) 
to stress a "library free" syntax that forces a raw understanding of neural networking concepts.

***

## About the MNIST dataset

The dataset used can be downloaded 
[here](https://www.kaggle.com/datasets/oddrationale/mnist-in-csv),
and contains:

- 60,000, 28x28 pixel images of hand-drawn images. This set of images is called the "training" set, and each image contains a label with its associated number for training purposes.
- 10,000, 28x28 pixel images. This set of images is called the "testing" set, and contrary to the training set, this set contains no labels, which the model is meant to give to the set following its training.

Example images:
![](https://machinelearningmastery.com/wp-content/uploads/2019/02/Plot-of-a-Subset-of-Images-from-the-MNIST-Dataset.png)

The format for this particular version of the dataset is as follows:
> Training Set:
> 
> [label, p<sub>1</sub>, p<sub>2</sub>, p<sub>3</sub> ... , p<sub>784</sub>]
> 
> ***
> 
> Testing Set:
> 
> [p<sub>1</sub>, p<sub>2</sub>, p<sub>3</sub> ... , p<sub>784</sub>]

where p<sub>i</sub> represents the i<sup>th</sup> pixel in a given image.
(Pixels numbers are ordered left to right, and then top to bottom)
***

## Notes
This project is going to, for the most part, follow along with the 
[YouTube series by sentdex](https://www.youtube.com/watch?v=Wo5dMEP_BbI&list=PLQVvvaa0QuDcjD5BAw2DxE6OF2tius3V3), 
and as such may not followed structured project. For example, the series starts with building single neurons, and as such the project will also do that, but it 
may be deleted later for a more clean, readable approach when more steps are added. Certain commits may be used not
necessarily for adding important features, but as a sort of "save point" when I'm switching between computers or videos.