# dataset_setup

import numpy as np
import os
import cv2
import jax.numpy as jnp

def dataset_setup(data_path):
    """
    Load and preprocess the dataset from the given path.

    Args:
        data_path (str): The path to the dataset directory.

    Returns:
        tuple: A tuple containing the image data array and the class names.
    """
    img_data_array = []
    class_name = []

    # Iterate over the subdirectories in the data path
    for dir1 in os.listdir(data_path):
        # Iterate over the files in each subdirectory
        for file in os.listdir(os.path.join(data_path, dir1)):
            image_path = os.path.join(data_path, dir1, file)
            # Read and resize the image
            image = cv2.imread(image_path, cv2.COLOR_BGR2RGB)
            image = cv2.resize(image, (64, 64))
            image = jnp.array(image)

            # Skip images with incorrect shape
            if len(image.shape) < 3:
                continue

            # Assign class labels based on the directory name
            if dir1 == "Leaf":
                img_data_array.append(image)
                class_name.append(1)
            elif dir1 == "Noise":
                img_data_array.append(image)
                class_name.append(0)

    # Convert the lists to JAX arrays
    img_data_array = jnp.stack(img_data_array, axis=0)
    class_name = jnp.stack(class_name, axis=0)

    return img_data_array, class_name

               