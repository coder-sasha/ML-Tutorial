"""
This script uses matplotlib library to demonstrate basic data visualization technic
"""

# this is a set of images we will display
from tensorflow.keras.datasets import mnist
from sklearn.datasets import load_digits

# pandas dataframe as data buffer
import pandas as pd
# math operations
import numpy as np
# matplotlib for plotting
import matplotlib.pyplot as plt

# load sklearn dataset with digit images
digits = load_digits()

title = f"SKLEARN Digits Set has {len(digits)} images"
fig, ax = plt.subplots(3, 3, figsize=(6, 6))
for i, axi in enumerate(ax.flat):
    axi.imshow(digits.images[i], cmap='binary')
    axi.set(xticks=[], yticks=[])

fig.suptitle(title)
plt.show()

# load dataset with digit images and their labels
(x_train, train_labels), (_, _) = mnist.load_data()

# shape of training data
ttl_img, l_img, w_img = x_train.shape

# print the data' statistics
title = f"MNIST Dataset has {ttl_img} images"

# create 3 rows and 3 columns
img_per_row = 3
n_rows = 3

# create a figure with 3 rows and 3 columns, using a compact figure size
fig, ax = plt.subplots(nrows=n_rows, ncols=img_per_row,
                       figsize=(9, 9),  # smaller figure for a compact view
                       subplot_kw=dict(xticks=[], yticks=[]))

# loop through the grid, display each image and set its title with the corresponding label
for row in range(n_rows):
    for col in range(img_per_row):
        index = row * img_per_row + col
        ax[row, col].imshow(x_train[index], cmap='gray')
        ax[row, col].set_title(f" {train_labels[index]}")

# Apply tight layout to optimize spacing
fig.suptitle(title)
fig.tight_layout()
plt.show()

