"""
We will create a decision tree and a simple neural network - a multi-layer perceptron.
We train both to classify handwritten digits in the MNIST dataset.
"""

from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.utils import check_random_state
from sklearn import tree
from sklearn.neural_network import MLPClassifier

import matplotlib.pyplot as plt
import numpy as np
import random

# read MNIST dataset, using Sklearn database
X, y = fetch_openml('mnist_784', version=1, return_X_y=True)

# next, divide the dataset into a training set and test set, randomly selecting 5000 examples for training
train_samples = 5000

# convert to numpy from pandas DataFrame
X = np.array(X)
y = np.array(y)

# shaffle training data
random_state = check_random_state(0)
permutation = random_state.permutation(X.shape[0])
X = X[permutation]
y = y[permutation]
X = X.reshape((X.shape[0], -1))

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    train_size=train_samples,
    test_size=1000)

# print out some items in the dataset and its label.
items = [13, 21, 42, 666, 777]

fig, axes = plt.subplots(1, 5, figsize=(12, 4))
for i, it in enumerate(items):
    # Extract label and image, reshape image to 28x28
    img = np.array(X_train[it]).reshape(28, 28)

    # Display the image on the subplot axis
    axes[i].imshow(img, cmap='gray', vmin=0, vmax=255)
    axes[i].set_title(f"Item {it} is digit {y_train[it]}")
    axes[i].axis('off')  # Hide axis ticks

plt.tight_layout()
plt.show()

# let's see how a decision tree with 200 decision rules performs by training it and printing its accuracy
clf = tree.DecisionTreeClassifier(max_leaf_nodes=200)
clf = clf.fit(X_train, y_train)
correct = 0
for i in range(len(X_test)):
    if clf.predict([X_test[i]]) == y_test[i]:
        correct = correct + 1

acc = 100.0 * correct / len(X_test)
print(f"Accuracy= {acc:.2f}%")

# let's try a simple neural network: a multi-layer perceptron with no hidden layers
clf = MLPClassifier(hidden_layer_sizes=[], max_iter=10000, activation='identity')
# train a network
clf.fit(X_train, y_train)

# get results
score = clf.score(X_test, y_test)
print(f"score = {score:.2f}%")

# now, add one hidden layer and expand the number of hidden units from 10 to 200 in intervals of 10
# print the accuracy of each model given the number of hidden units
for i in range(1, 21):
    nhidden = i * 10
    clf = MLPClassifier(hidden_layer_sizes=[nhidden], max_iter=10000)
    # train network
    clf.fit(X_train, y_train)
    score = clf.score(X_test, y_test)
    print(f"Number of hidden layers: {nhidden}, score={score}")

# the model is trained now and should be able to recognize images
nhidden = 180
clf = MLPClassifier(hidden_layer_sizes=[nhidden], max_iter=10000)
clf.fit(X_train, y_train)

print('ready...')

items = [13, 21, 42, 666, 777]
results = []
for it in items:
    res = clf.predict([X_test[it]])
    results.append(res)
    print(f"model says that item {y_test[it]} is {res}")

fig, axes = plt.subplots(1, 5, figsize=(12, 4))

for i, it in enumerate(items):
    # extract label and image, reshape image to 28x28
    img = np.array(X_test[it]).reshape(28, 28)

    # display the image on the subplot axis
    axes[i].imshow(img, cmap='gray', vmin=0, vmax=255)
    axes[i].set_title(f"Model says that {y_test[it]} is {results[i]}")
    axes[i].axis('off')  # Hide axis ticks

plt.tight_layout()
plt.show()
