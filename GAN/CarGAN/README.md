# CarGAN

This project is a Deep Convolutional Generative Adversarial Network (DCGAN) for generating images of cars.

## Model

The model is based on the architecture described in the paper: [Unsupervised Representation Learning with Deep Convolutional Generative Adversarial Networks](https://arxiv.org/pdf/1511.06434.pdf). It is implemented using TensorFlow and Keras.

## Dataset

The model is trained on a dataset of car images, which is expected to be located in a Google Drive folder. The notebook is configured to mount a Google Drive and load the dataset from `/content/drive/MyDrive/CarsDataset/`. and can be downloaded from [Stanford cars dataset](https://www.kaggle.com/datasets/eduardo4jesus/stanford-cars-dataset)

## Implementation

The Jupyter Notebook `CarGAN.ipynb` contains the full implementation of the model, including:

*   The generator and discriminator network architectures.
*   The training loop.
*   Functions for saving model checkpoints and generating sample images during training.

## How to Use

1.  Upload the car dataset to your Google Drive in the specified path.
2.  Open the `CarGAN.ipynb` notebook in Google Colab.
3.  Run the cells to mount your Google Drive, load the dataset, and start the training process.
