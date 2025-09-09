# JAX Projects

This directory contains projects built using the JAX library. The primary goal of these projects was to learn and experiment with JAX, a high-performance numerical computing library with a NumPy-like API.

## JAX Neural Network for Leaf Classification

This project is a feed-forward neural network for classifying citrus leaf images.

### Model

The model is implemented in JAX and uses a feed-forward architecture. The notebook `my_network(JAX).ipynb` contains a log of experiments with different hyperparameters and architectures, including:

*   Learning rate
*   Regularization (L2)
*   Number of hidden layers and units

### Dataset

The model is trained on the same citrus leaf dataset used in the LeafGAN project. The dataset is expected to be located in a Google Drive folder. The `Dataset_setupWithJAX.py` script is used to prepare the dataset for the JAX model.

### Implementation

The main implementation is in the `my_network(JAX).ipynb` notebook, which includes:

*   The neural network model definition.
*   The training loop.
*   Functions for forward and backward propagation.
*   A record of experimental results.

Other notebooks in this directory, such as `my_network.ipynb` and `Dense_noise_leaf_detector.ipynb`, appear to be variations or earlier versions of the leaf classification project.

### How to Use

1.  Upload the citrus leaf dataset to your Google Drive.
2.  Open the `my_network(JAX).ipynb` notebook in Google Colab.
3.  Run the cells to mount your Google Drive, load the dataset, and start the training process.
