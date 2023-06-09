# Garbage Control Project
The Garbage Control Project is a project focused on image processing and garbage object segmentation. It involves a range of functions that perform different tasks related to image manipulation and data processing.

## Project Description
One important aspect of the project is the preprocessing of images. The images are stretched to a square shape that is a multiple of 32. This step prepares the images for further processing using a specific model. The stretched images are then used for subsequent tasks.

To simplify the image data, a process is implemented to convert the images from a three-channel representation to a one-channel representation. This conversion reduces the complexity of the data while preserving important information.

The project also includes functions for saving and loading arrays from files. This allows for efficient storage and retrieval of data during the processing pipeline.

Another crucial aspect of the project is the segmentation of garbage objects in the images. The project includes processes to extract relevant information from metadata files, such as the ID and dimensions of specific objects. This information is used to locate and segment the corresponding objects in the images.

The segmentation process involves converting a list of polygons into binary masks. These masks represent the presence or absence of the objects within the image. The masks are used to isolate and identify the garbage objects.

Once the segmentation is complete, the project provides functionality to save the segmented images in a specific format. This ensures that the segmented data can be easily accessed and utilized for further analysis or visualization.

Lastly, the project includes functions to split the data into different sets, such as training, validation, and test sets. This division enables proper evaluation and training of models using the segmented data.

Overall, the Garbage Control Project aims to process and manipulate garbage object images and segmentations using various functions. The project involves tasks such as image preprocessing, data simplification, file storage and retrieval, segmentation using metadata information, binary mask generation, saving segmented images, and data splitting for model training and evaluation.

## Requirements
- Python (version 3.6 or higher)
- TensorFlow (version 2.12.0 or higher)
- Keras-Applications (version 1.0.8 or higher)
- Keras-Preprocessing (version 1.1.2 or higher)

The majority of experiments were performed on the Colaboratory cloud platform for deep learning, specifically using a T4 GPU with 12.7GB of memory.

The script will evaluate the model using the test dataset and print the evaluation metrics.

## Results

## Contributions

## Authors
- [Leonardo Catello](https://github.com/Leonard2310) 
- [Daiana Cipollaro](https://github.com/Dad-cip)

## License
This project is licensed under the [GNU General Public License v3.0]. Refer to the LICENSE file for more information.

## Acknowledgments
The Garbage Control Project builds upon the following works and datasets:

- [Dataset]()
