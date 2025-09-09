# LeafGAN (CitrusGAN)

This project is a Deep Convolutional Generative Adversarial Network (DCGAN) designed to generate images of citrus leaves. It was developed as an experiment to work with a simpler dataset compared to the CarGAN project.

## Model

The model is a DCGAN implemented using TensorFlow and Keras. The `CitrusGAN.ipynb` notebook includes a log of various experiments with the model's architecture and hyperparameters, which provides insights into the development process.

## Dataset

The model is trained on a dataset of citrus leaf images, which is expected to be located in a Google Drive folder. The notebook is configured to load the dataset from `/content/drive/MyDrive/LeafDataset/Leaves/Leafdataset/Training/Leaf/`.

## Results

The project showed some initial success, with "Leafish" shapes being generated after about 80 epochs. Further improvements and more training would be needed to generate more realistic images.

## Implementation

The Jupyter Notebook `CitrusGAN.ipynb` contains the full implementation of the model, including:

*   The generator and discriminator network architectures.
*   The training loop.
*   Functions for saving model checkpoints and generating sample images during training.
*   A log of experiments and observations.

## How to Use

1.  Upload the citrus leaf dataset to your Google Drive in the specified path.
2.  Open the `CitrusGAN.ipynb` notebook in Google Colab.
3.  Run the cells to mount your Google Drive, load the dataset, and start the training process.
