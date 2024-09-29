# Garbage Control Project
The Garbage Control Project is a comprehensive initiative that focuses on working with images and segmentations of garbage objects. It involves a set of functions designed to perform various tasks related to image processing and data manipulation.

## Project Description
The Garbage Control Project utilizes the TACO dataset. This dataset comprises a collection of images depicting litter in various environmental settings such as woods, roads, and beaches. These images are manually labeled and segmented based on a hierarchical taxonomy, enabling the training and evaluation of object detection algorithms. The dataset is continuously growing, with images hosted on Flickr, and ongoing efforts are made to collect more images and annotations at tacodataset.org. The annotations in the dataset are provided in COCO (Common Objects in Context) format, which is a widely used standard for representing object detection and segmentation annotations. This format includes detailed information about the objects present in the images, their bounding boxes and segmentation masks.

A crucial aspect of the project is image preprocessing. Images are processed to ensure they have a square shape that is a multiple of 32. This step is essential to prepare the images for subsequent processing using specific models like the UNet model. The preprocessing standardizes the image dimensions, making them compatible with the model's requirements and optimizing subsequent analysis.

Another significant function of the project is converting the images from a three-channel representation (typically red, green, and blue) to a one-channel representation. This simplifies the data by extracting the least significant bitplane from the red channel. By reducing the image to a single channel, the data's complexity is reduced while preserving relevant information necessary for further analysis.

To facilitate data storage and retrieval, the project includes functions to save and load arrays from binary files. This enables efficient handling of large datasets without the need for complex data structures. The ability to save and load arrays ensures that processed data can be easily stored and accessed for subsequent analysis or further processing steps.

The project also involves functions related to garbage object segmentation within the images. It extracts relevant information from metadata files associated with each image, such as object IDs and dimensions. By utilizing this metadata, the project accurately locates and segments the corresponding objects within the images. For segmentation, the project employs the Run-Length Encoding (RLE) technique. RLE is a compression scheme that represents a binary mask as a sequence of numbers, indicating the lengths of consecutive runs of 1s and 0s in the mask. This encoding scheme is commonly used in image segmentation tasks to efficiently represent and store binary masks.

The segmentation process converts a list of polygons representing the outlines of the garbage objects into binary masks. These masks serve as binary representations of the presence or absence of the garbage objects within the images. The masks are generated by mapping the polygons onto a binary image of the same dimensions. The pixels inside the polygons are set to 1 (indicating object presence) and the pixels outside the polygons are set to 0 (indicating background). This binary representation allows for efficient isolation and identification of the garbage objects.

Once the segmentation is complete, the project provides functionality to save the segmented images in a specific format, such as PNG. This ensures that the segmented data can be easily accessed and utilized for further analysis, visualization, or integration into other applications.

Lastly, the project includes functions to split the data into different sets, such as training, validation, and test sets. This data splitting is crucial for tasks such as model training and evaluation. By dividing the dataset into distinct subsets, the project enables the development and assessment of machine learning models using the segmented data.

The project utilizes a U-Net architecture for the segmentation task. The U-Net is a popular neural network model designed for image segmentation. It consists of an encoder path that extracts low-level features from the input image and a decoder path that reconstructs the segmented output. The backbone of the U-Net model, serving as the low-level feature extractor, is a ResNet34 neural network. ResNet34 is a widely used pre-trained model that has been trained on the large-scale ImageNet dataset, enabling it to effectively capture general features from images.

The U-Net model employed in the project has several important configurations. The model is trained to perform binary segmentation, classifying each pixel as either belonging to the garbage object or the background. The activation function used in the final layer of the model is the sigmoid function, which restricts the output values to the range of [0, 1]. This activation function ensures a more stable training process when dealing with masks in the segmentation task.

During training, the weights of the U-Net model can be initialized using pre-trained weights from ImageNet, thanks to the 'encoder_weights' parameter. To retain the pre-trained features and prevent further training of the encoder layers, the 'encoder_freeze' parameter is set to True.

The U-Net model employs upsampling in the decoder path to increase the resolution of the feature maps and generate the final segmented output. Batch normalization is utilized in the decoder layers to improve the stability and convergence of the training process.

## Requirements
- Python (version 3.6 or higher)
- Segmentation-Models (version 1.0.1 or higher)

The majority of experiments were performed on the Colaboratory cloud platform for deep learning, specifically using a Tesla K80 GPU.

The script will evaluate the model using the test dataset and print the evaluation metrics.

## Results
In summary, the Garbage Control Project aims to effectively manage and control garbage objects through advanced image analysis techniques. It utilizes the TACO dataset, employing the U-Net architecture with a ResNet34 backbone for the segmentation task. The project takes advantage of various functions for image preprocessing, data simplification, efficient data storage and retrieval, metadata handling, object segmentation, binary mask generation, saving segmented images and data splitting for model training and evaluation. These techniques contribute to improved waste management by enabling accurate segmentation and analysis of garbage objects in the images.

## Contributions
We welcome contributions and improvements to the KinDeNet project. If you would like to contribute, please submit a pull request. Make sure to discuss and plan proposed changes with the development team before starting the work.

## Authors
- [Leonardo Catello](https://github.com/Leonard2310) 
- [Daiana Cipollaro](https://github.com/Dad-cip)
- [Giovanni Bolla](https://github.com/CryptoGionni)

## License
This project is licensed under the [GNU General Public License v3.0]. Refer to the LICENSE file for more information.

## Acknowledgments
The Garbage Control Project builds upon the following works and datasets:

- [TACO Dataset](https://github.com/pedropro/TACO)
