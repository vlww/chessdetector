#!/usr/bin/python3

# modules used for recognizing and loading images
import jetson.inference
import jetson.utils

# module to parse the command line
import argparse

# parse the image file name and select a network
parser = argparse.ArgumentParser()
parser.add_argument("filename", type=str, help="filename of the image to process")
parser.add_argument("--network", type=str, default="googlenet", help="model to use, can be:  googlenet, resnet-18, ect. (see --help for others)")
opt = parser.parse_args()

# load the image from the disk
img = jetson.utils.loadImage(opt.filename)
# load the recognition network as specified in the command line
net = jetson.inference.imageNet(opt.network)

# classify the image (outputs index and confidence)
class_idx, confidence = net.Classify(img)

# get the class description and print out the results
class_desc = net.GetClassDesc(class_idx)
print("image is recognized as '{:s}' (class #{:d}) with {:f}% confidence".format(class_desc, class_idx, confidence * 100))