from PIL import Image
import cv2
import numpy as np
import glob
import pickle
train_x = []
train_y = []
# class 1
filelist = glob.glob('train/train1/*.png')
for fname in filelist:
    image =cv2.imread(fname, cv2.IMREAD_GRAYSCALE)
    train_x.append(image)
    train_y.append([1])
# class 2
filelist = glob.glob('train/train2/*.png')
for fname in filelist:
    image =cv2.imread(fname, cv2.IMREAD_GRAYSCALE)
    train_x.append(image)
    train_y.append([2])
# class 3
filelist = glob.glob('train/train3/*.png')
for fname in filelist:
    image =cv2.imread(fname, cv2.IMREAD_GRAYSCALE)
    train_x.append(image)
    train_y.append([3])
train_x = np.array(train_x)
train_x.dump('train_x.npy')
train_y = np.array(train_y)
train_y.dump('train_y.npy')
# To load array x back in from file:
train_x = np.load('train_x.npy', allow_pickle=True)
print(len(train_x), len(train_x))
# ////////////////////////////////////////////////////////
test_x = []
test_y = []
# class 1
filelist = glob.glob('test/test1/*.png')
for fname in filelist:
    image =cv2.imread(fname, cv2.IMREAD_GRAYSCALE)
    test_x.append(image)
    test_y.append([1])
# class 2
filelist = glob.glob('test/test2/*.png')
for fname in filelist:
    image =cv2.imread(fname, cv2.IMREAD_GRAYSCALE)
    test_x.append(image)
    test_y.append([2])
# class 3
filelist = glob.glob('test/test3/*.png')
for fname in filelist:
    image =cv2.imread(fname, cv2.IMREAD_GRAYSCALE)
    test_x.append(image)
    test_y.append([3])
test_x = np.array(test_x)
test_x.dump('test_x.npy')
test_y = np.array(test_y)
test_y.dump('test_y.npy')
# To load array x back in from file:
test_x = np.load('test_x.npy', allow_pickle=True)
print(len(train_x), len(train_x))