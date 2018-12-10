from __future__ import print_function

import os
import numpy as np
import nibabel
from skimage.io import imsave, imread

data_path = 'raw/'

image_rows = int(512/2)
image_cols = int(512/2) #we will undersample our training 2D images later (for memory and speed)


def create_train_data():
    train_data_path = os.path.join(data_path, 'train')
    images = os.listdir(train_data_path)

    imgs_train=[]  #training images
    imgsliv_train=[] #training masks (corresponding to liver)
    print('-'*30)
    print('Creating training images...')
    print('-'*30)
    a=[]
    b=[]
    for k in range(len(images)):
        if k%2==0:
            a.append(np.sort(images)[k]) #file names corresponding to training masks
        else:
            b.append(np.sort(images)[k]) #file names corresponding to training images
        
    for liver,orig in zip(a,b):
        imgl=nibabel.load(os.path.join(train_data_path,liver)) #we load 3D training mask
        imgo=nibabel.load(os.path.join(train_data_path,orig)) #we load 3D training image
        for k in range(imgl.shape[2]):
            dimgl=np.array(imgl.get_data()[::2,::2,k]) #axial cuts are made along the z axis with undersampling
            dimgo=np.array(imgo.get_data()[::2,::2,k])
            if len(np.unique(dimgl))!=1: #we only recover the 2D sections containing the liver
                imgsliv_train.append(dimgl)
                imgs_train.append(dimgo)
            
                
    imgs = np.ndarray((len(imgs_train), image_rows, image_cols), dtype=np.uint8)
    imgs_mask = np.ndarray((len(imgsliv_train), image_rows, image_cols), dtype=np.uint8)
    for index,img in enumerate(imgs_train):
        imgs[index,:,:]=img
    for index,img in enumerate(imgsliv_train):
        imgs_mask[index,:,:]=img


    np.save('imgs_train.npy', imgs)
    np.save('imgsliv_train.npy', imgs_mask)
    print('Saving to .npy files done.')


def load_train_data():
    imgs_train = np.load('imgs_train.npy')
    imgs_mask_train = np.load('imgsliv_train.npy')
    return imgs_train, imgs_mask_train


def create_test_data():
    test_data_path = os.path.join(data_path, 'test')
    images = os.listdir(test_data_path)
    print('-'*30)
    print('Creating training images...')
    print('-'*30)
    imgs_test=[]
    imgsliv_test=[]
    for image_name in images:
        print(image_name)
        img=nibabel.load(os.path.join(test_data_path,image_name))
        print(img.shape)
        for k in range(img.shape[2]):  
            dimg=np.array(img.get_data()[::2,::2,k])
            if 'liver' in image_name:
                imgsliv_test.append(dimg)
            
            elif 'orig' in image_name:
                imgs_test.append(dimg)
                
   
    
    imgst= np.ndarray((len(imgs_test), image_rows, image_cols), dtype=np.uint8)
    imgs_maskt= np.ndarray((len(imgsliv_test), image_rows, image_cols), dtype=np.uint8)
    for index,img in enumerate(imgs_test):
        imgst[index,:,:]=img
    for index,img in enumerate(imgsliv_test):
        imgs_maskt[index,:,:]=img

    np.save('imgs_test.npy', imgst)
    np.save('imgsliv_test.npy', imgs_maskt)
    print('Saving to .npy files done.')
    


def load_test_data():
    imgst = np.load('imgs_test.npy')
    imgs_id = np.load('imgs_id_test.npy')
    return [imgst, imgs_id]

if __name__ == '__main__':
    create_train_data()
    create_test_data()
