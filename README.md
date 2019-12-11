# Liver segmentation project
<p>Purpose : the objective is to automatically delineate liver on patient scans by computer vision. The method used is from the research paper <a href="https://arxiv.org/pdf/1505.04597.pdf">"U-Net: Convolutional Networks for Biomedical
Image Segmentation"</a></p>
<p>In this project we apply the method to the segmentation of liver images as described in this research paper https://arxiv.org/pdf/1702.05970.pdf.
 </p>

## Data
The data is available in NifTi format <a href='https://www.dropbox.com/s/8h2avwtk8cfzl49/ircad-dataset.zip?dl=0'>here</a>. 
This dataset consists of 20 medical examinations in 3D, we have the source image as well as a mask of segmentation of the liver for each of these examinations. We use the nibabel library (http://nipy.org/nibabel/) to read associated images and masks.

## Model
<p>We train a U-net architecture, a fully convolutional network. The principle of this architecture is to add to a usual contracting network, layers with upsampling operators instead of pooling. This allow the network to learn context (contracting path), then localization (expansive path). Context information is propagated to higher resolution layers thanks to skip-connexions. So we have images of the same size as input</p>


<p align="center"><img src="img/u-net-architecture.png" style></img></p>


<p>in the data.py script, we perform axial cuts of our 3D images. So 256x256 images are input to the network</p>

## Evaluation

As metric we use the <a href='https://en.wikipedia.org/wiki/S%C3%B8rensen%E2%80%93Dice_coefficient'>Dice coefficient</a> (which is quite similar to the Jaccard coefficient)

## How it works
<ol><li>First download the data whose link has been given previously</li>
<li>Create a 'raw' folder
<li>In the 'raw' folder, create a 'test' folder, and a 'train' folder
<li>Then separate the data in two sets (train and test, typically we use 13 samples for the train set and 7 for the test set) and put them in the corresponding directories that you can find in the 'raw' folder</li>
<li>Run data.py , this will save the train and test data in npy format</li>
<li>Finally launch the notebook, you can observe a curve of the Dice coef according to the number of epochs and visualize your predictions in the folder 'preds'</li>
 </ol>
 (Feel free to play with the parameters : learning rate, optimizer etc.)
 
 ## Some results
 
 
<p>Finally we get this kind of predictions for a particular cut (you can reproduce this with the notebook), we delineate the liver with a yellow marker</p>
<p align="center"><img src="img/segmentation-example1.png"></img></p>

<p>The evolution of the Dice coef for 20 epochs, this plot shows that we have consistent results and a test Dice coef reaching almost 0.87</p>
<p align="center"><img src="img/dice-20epochs-example.png"></img></p>

## Acknowledgments

* <a href='https://github.com/jocicmarko/ultrasound-nerve-segmentation'>Ultrasound nerve segmentation</a>
* <a href='https://www.ircad.fr/fr/'>Institut de recherche contre les cancers de l'appareil digestif</a>
