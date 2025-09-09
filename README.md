# Experiments_and_Improvements

This repository was created to include programs that serve certain applications and are built with various libraries, for the purpose of learning how the programs function and how to use the libraries.

This repository contains two main directories:

## GAN (Generative Adversarial Networks)

This directory contains two Generative Adversarial Network (GAN) projects. Both are implemented using TensorFlow and Keras.

### CarGAN

*   **Objective**: To generate images of cars.
*   **Model**: This project is based on the DCGAN (Deep Convolutional Generative Adversarial Network) architecture, as described in the paper: [Unsupervised Representation Learning with Deep Convolutional Generative Adversarial Networks](https://arxiv.org/pdf/1511.06434.pdf).
*   **Dataset**: The model is trained on a dataset of car images, which is loaded from Google Drive.
*   **Implementation**: The implementation can be found in `GAN/CarGAN/CarGAN.ipynb`. It includes the generator and discriminator models, the training loop, and functions for saving checkpoints and generating images.

### LeafGAN (CitrusGAN)

*   **Objective**: To generate images of tree leaves. This was an experiment to work with a simpler and smaller dataset compared to the CarGAN project.
*   **Model**: This is also a DCGAN implementation.
*   **Dataset**: The dataset consists of citrus leaf images, loaded from Google Drive.
*   **Results**: The project showed some initial success, with "Leafish" shapes being generated after about 80 epochs. Further improvements and more training would be needed to generate more realistic images. The notebook `GAN/LeafGAN/CitrusGAN.ipynb` contains a log of various experiments with the model's architecture and hyperparameters.

## JAX

This directory contains programs built using the JAX library. The main goal of this project was to learn and experiment with JAX, which offers superior performance and speed compared to NumPy, while having a similar API.

### JAX Neural Network

*   **Objective**: To build a neural network for image classification using JAX.
*   **Model**: A feed-forward neural network for classifying citrus leaf images.
*   **Dataset**: The same citrus leaf dataset from the LeafGAN project is used here.
*   **Implementation**: The notebook `JAX/my_network(JAX).ipynb` contains the implementation of the neural network, including the model definition, training loop, and a record of experiments with different hyperparameters (learning rate, regularization) and network architectures. The notebook `JAX/my_network.ipynb` appears to be a similar implementation, likely using NumPy or another library for comparison. `Dense_noise_leaf_detector.ipynb` seems to be another variant of the leaf detector. `Dataset_setupWithJAX.py` is likely a utility script for preparing the dataset.
