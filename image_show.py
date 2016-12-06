#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import os
import re
import sys
import subprocess

# First wrote by Yun Zhao on 2013.10.24
# Last editted by Yun Zhao on 2013.10.27


##### read selected diffraction pattern with geometrical file #####

def read_image():
    """ Show the selected image with hdfsee """
    """ Input are the image list file and the order of image which you want to see"""
    filename =sys.argv[1]
    nth_image = int(sys.argv[2])
    f = open (filename)
    lines = f.readlines()
    f.close()
    print lines[nth_image]
    image_show='hdfsee '+lines[nth_image].strip()+' -g june24-v2.geom'
    print image_show
    subprocess.call(image_show,shell=True)



###############    Show predicted bragg spots #########################
def peak_prediction():
    """ Check the predicted spots in nth frame """
    """ Input file: stream file """
#    filename = sys.argv[0]
    filename = 'good_data01.stream'
    f = open (filename)
    fo = open ('listfile.tmp','w')
    start = 0
    for line in f:
#        imagenamematch = re.search('Image filename: ',line.strip())
#        if imagenamematch:
#           imagepath = line.strip()
        if line.startswith('Image filename: '):
           imagepath = line[len('Image filename: '):]
           print imagepath
        if line.strip() == 'Peaks from peak search':
           start = 1
        if line.strip() == 'End of peak list':
           start = 0
           fo.close()
        if start == 1:
           fo.write(line)
        else:
           fo.close
        image_show='hdfsee '+imagepath.strip()+' -g june24-v2.geom'+' --peak-overlay=listfile.tmp'
        subprocess.call(image_show,shell=True)
        os.unlink('listfile.tmp')
        fo=open('listfile.tmp','w')
        start = 0


def peak_check():
    """ Check those spots identified as a peak in imosflm """





def stat_plot():
    """ plot the statistics of indexing results (lattice constant and angles) """




    




