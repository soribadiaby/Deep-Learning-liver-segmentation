# Deep-Learning-liver-segmentation-project
 <em>Final project of the Deep Learning course followed at <a href='https://www.imt-atlantique.fr/en'>IMT Atlantique</a>.</em></br></br>
<p>The code of this project is largely inspired by that of <a href='https://github.com/jocicmarko/ultrasound-nerve-segmentation'> this repository</a>, a tutorial for a kaggle competition about ultrasound image nerve segmentation. The goal of this project is to adapt the code to the segmentation of liver images as described in this article https://arxiv.org/pdf/1702.05970.pdf.
 </p>

## Data
The data to be used are available in NifTi format <a href='https://www.dropbox.com/s/hx3dehfixjdifvu/ELU-502-ircad-dataset.zip?dl=0'>here</a>. 
This dataset consists of 20 medical examinations in 3D, we have the source image as well as a mask of segmentation of the liver for each of these examinations. We will use the nibabel library (http://nipy.org/nibabel/) to read associated images and masks.

## Model

