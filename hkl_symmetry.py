#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import os
import re
import sys
import subprocess

# First wrote by Yun Zhao on 2013.10.24
# Last editted by Yun Zhao on 2014.3.31
# Yun Zhao is awesome!


########### common usage of this code: examples #################
# python -c 'import hkl_symmetry; print hkl_symmetry.full_hkl_P63()' full-30A.hkl
# python -c 'import hkl_symmetry; print hkl_symmetry.full_hkl_P43212()' full-30A.hkl
# 
#################################################################################

#####################     hkl file format for P1    #########################
def full_hkl_P1():
    """ convert the P1 hkl list to full reciprocal space """
    """ Last editted by Yun Zhao at Nov 6,2013 """
    filename = sys.argv[1]
    f1 = open(filename)
    f2 = open('full.hkl','w')
    for line in f1:
        f2.write(line)
        if re.search("[0-9]",line):
           reflection=line.split()
           h =-int(reflection[0])
           k =-int(reflection[1])
           l =-int(reflection[2])
           intensity = float(reflection[3]) # Friedel pair share the same intensity
           phase =360-float(reflection[4]) # Friedel pair have the opposite phase
#          print h,"\n",k,"\n",l,"\n",intensity,"\n", phase
#          reflection = ' {0} {1} {2} {3} {4} {5} {6} {7} {8}'.format(h,k,l,intensity,phase,0.0,1,0.0,0.0)
           reflection = "%(h)3i %(k)3i %(l)3i %(intensity)10.2f %(phase)8.2f %(sigma_I)10.2f %(counts)7i %(fs)6.1f %(ss)6.1f\n" % {"h":h,"k":k,"l":l,"intensity":intensity, "phase":phase, "sigma_I":0.0,"counts":1,"fs":0,"ss":0}
           f2.write(reflection)
    f1.close()
    f2.close()

#####################     hkl file format for P63    #########################
def full_hkl_P63():
    """ convert the P63 hkl list from gen-sfs to full reciprocal space """
    """ Last editted by Yun Zhao at Nov 6,2013 """
# usage example: python -c 'import image_show; print image_show.full_hkl_P63()' full-30A.hkl
    filename = sys.argv[1]
    f1 = open(filename)
    f2 = open('full.hkl','w')
    for line in f1:
        f2.write(line)
        if re.search("[0-9]",line):
                reflection=line.split()
                h =int(reflection[0])
                k =int(reflection[1])
                l =int(reflection[2])
                intensity = float(reflection[3]) # Friedel pair share the same intensity
# 1st equivalent I(h,k,l)= I(-h,-k,-l)          
                phase =360-float(reflection[4]) # Friedel pair have the opposite phase
                reflection_1 = "%(h)3i %(k)3i %(l)3i %(intensity)10.2f %(phase)8.2f %(sigma_I)10.2f %(counts)7i %(fs)6.1f %(ss)6.1f\n" % {"h":-h,"k":-k,"l":-l,"intensity":intensity, "phase":phase, "sigma_I":0.0,"counts":1,"fs":0,"ss":0}
                f2.write(reflection_1)

# 2nd equivalent I(h,k,l)=I(h,k,-l)
                phase =360-float(reflection[4]) # Friedel pair have the opposite phase
                reflection_1 = "%(h)3i %(k)3i %(l)3i %(intensity)10.2f %(phase)8.2f %(sigma_I)10.2f %(counts)7i %(fs)6.1f %(ss)6.1f\n" % {"h":h,"k":k,"l":-l,"intensity":intensity, "phase":phase, "sigma_I":0.0,"counts":1,"fs":0,"ss":0}
                f2.write(reflection_1)

# 3rd equivalent I(h,k,l)= I(-h,-k,l)
                phase =360-float(reflection[4]) # Friedel pair have the opposite phase
                reflection_1 = "%(h)3i %(k)3i %(l)3i %(intensity)10.2f %(phase)8.2f %(sigma_I)10.2f %(counts)7i %(fs)6.1f %(ss)6.1f\n" % {"h":-h,"k":-k,"l":l,"intensity":intensity, "phase":phase, "sigma_I":0.0,"counts":1,"fs":0,"ss":0}
                f2.write(reflection_1)

# 4th equivalent I(h,k,l) = I(-k,h+k,l)
                phase =360-float(reflection[4]) # Friedel pair have the opposite phase
                reflection_1 = "%(h)3i %(k)3i %(l)3i %(intensity)10.2f %(phase)8.2f %(sigma_I)10.2f %(counts)7i %(fs)6.1f %(ss)6.1f\n" % {"h":-k,"k":h+k,"l":l,"intensity":intensity, "phase":phase, "sigma_I":0.0,"counts":1,"fs":0,"ss":0}
                f2.write(reflection_1)

# 5th equivalent I(h,k,l)= I(k,-h-k,-l)
                phase =360-float(reflection[4]) # Friedel pair have the opposite phase
                reflection_1 = "%(h)3i %(k)3i %(l)3i %(intensity)10.2f %(phase)8.2f %(sigma_I)10.2f %(counts)7i %(fs)6.1f %(ss)6.1f\n" % {"h":k,"k":-h-k,"l":-l,"intensity":intensity, "phase":phase, "sigma_I":0.0,"counts":1,"fs":0,"ss":0}
                f2.write(reflection_1)

# 6th equivalent I(h,k,l) = I(k,-h-k,l)
                phase =360-float(reflection[4]) # Friedel pair have the opposite phase
                reflection_1 = "%(h)3i %(k)3i %(l)3i %(intensity)10.2f %(phase)8.2f %(sigma_I)10.2f %(counts)7i %(fs)6.1f %(ss)6.1f\n" % {"h":k,"k":-h-k,"l":l,"intensity":intensity, "phase":phase, "sigma_I":0.0,"counts":1,"fs":0,"ss":0}
                f2.write(reflection_1)

# 7th equivalent I(h,k,l) = I(-k,h+k,-l)
                phase =360-float(reflection[4]) # Friedel pair have the opposite phase
                reflection_1 = "%(h)3i %(k)3i %(l)3i %(intensity)10.2f %(phase)8.2f %(sigma_I)10.2f %(counts)7i %(fs)6.1f %(ss)6.1f\n" % {"h":-k,"k":h+k,"l":-l,"intensity":intensity, "phase":phase, "sigma_I":0.0,"counts":1,"fs":0,"ss":0}
                f2.write(reflection_1)

# 8th equivalent I(h,k,l) = I(h+k,-h,l)
                phase =360-float(reflection[4]) # Friedel pair have the opposite phase
                reflection_1 = "%(h)3i %(k)3i %(l)3i %(intensity)10.2f %(phase)8.2f %(sigma_I)10.2f %(counts)7i %(fs)6.1f %(ss)6.1f\n" % {"h":h+k,"k":-h,"l":l,"intensity":intensity, "phase":phase, "sigma_I":0.0,"counts":1,"fs":0,"ss":0}
                f2.write(reflection_1)

# 9th equivalent I(h,k,l) = I(-h-k,h,-l)
                phase =360-float(reflection[4]) # Friedel pair have the opposite phase
                reflection_1 = "%(h)3i %(k)3i %(l)3i %(intensity)10.2f %(phase)8.2f %(sigma_I)10.2f %(counts)7i %(fs)6.1f %(ss)6.1f\n" % {"h":-h-k,"k":h,"l":-l,"intensity":intensity, "phase":phase, "sigma_I":0.0,"counts":1,"fs":0,"ss":0}
                f2.write(reflection_1)

# 10th equivalent I(h,k,l)=I(-h-k,h,l)
                phase =360-float(reflection[4]) # Friedel pair have the opposite phase
                reflection_1 = "%(h)3i %(k)3i %(l)3i %(intensity)10.2f %(phase)8.2f %(sigma_I)10.2f %(counts)7i %(fs)6.1f %(ss)6.1f\n" % {"h":-h-k,"k":h,"l":l,"intensity":intensity, "phase":phase, "sigma_I":0.0,"counts":1,"fs":0,"ss":0}
                f2.write(reflection_1)

# 11th equivalent I(h,k,l)= I(h+k,-h,-l)
                phase =360-float(reflection[4]) # Friedel pair have the opposite phase
                reflection_1 = "%(h)3i %(k)3i %(l)3i %(intensity)10.2f %(phase)8.2f %(sigma_I)10.2f %(counts)7i %(fs)6.1f %(ss)6.1f\n" % {"h":h+k,"k":-h,"l":-l,"intensity":intensity, "phase":phase, "sigma_I":0.0,"counts":1,"fs":0,"ss":0}
                f2.write(reflection_1)
    f1.close()
    f2.close()


#####################     hkl file format for P43212    #########################
def full_hkl_P43212():
    """ convert the P43212 hkl list to full reciprocal space """
    """ Last editted by Yun Zhao at Jan 17,2014 """
# usage example: python -c 'import image_show; print image_show.full_hkl_P43212()' full-30A.hkl
    filename = sys.argv[1]
    f1 = open(filename)
    f2 = open('full.hkl','w')
    for line in f1:
        f2.write(line)
        if re.search("[0-9]",line):
                reflection=line.split()
                h =int(reflection[0])
                k =int(reflection[1])
                l =int(reflection[2])
                intensity = float(reflection[3]) # Friedel pair share the same intensity
# 1st equivalent I(h,k,l)= I(-h,-k,-l)          
                phase =360-float(reflection[4]) # Friedel pair have the opposite phase
                reflection_1 = "%(h)3i %(k)3i %(l)3i %(intensity)10.2f %(phase)8.2f %(sigma_I)10.2f %(counts)7i %(fs)6.1f %(ss)6.1f\n" % {"h":-h,"k":-k,"l":-l,"intensity":intensity, "phase":phase, "sigma_I":0.0,"counts":1,"fs":0,"ss":0}
                f2.write(reflection_1)

# 2nd equivalent I(h,k,l)=I(-k,h,l)
                phase =360-float(reflection[4]) # Friedel pair have the opposite phase
                reflection_1 = "%(h)3i %(k)3i %(l)3i %(intensity)10.2f %(phase)8.2f %(sigma_I)10.2f %(counts)7i %(fs)6.1f %(ss)6.1f\n" % {"h":-k,"k":h,"l":l,"intensity":intensity, "phase":phase, "sigma_I":0.0,"counts":1,"fs":0,"ss":0}
                f2.write(reflection_1)

# 3rd equivalent I(h,k,l)= I(k,-h,-l)
                phase =360-float(reflection[4]) # Friedel pair have the opposite phase
                reflection_1 = "%(h)3i %(k)3i %(l)3i %(intensity)10.2f %(phase)8.2f %(sigma_I)10.2f %(counts)7i %(fs)6.1f %(ss)6.1f\n" % {"h":k,"k":-h,"l":-l,"intensity":intensity, "phase":phase, "sigma_I":0.0,"counts":1,"fs":0,"ss":0}
                f2.write(reflection_1)

# 4th equivalent I(h,k,l) = I(-h,-k,l)
                phase =360-float(reflection[4]) # Friedel pair have the opposite phase
                reflection_1 = "%(h)3i %(k)3i %(l)3i %(intensity)10.2f %(phase)8.2f %(sigma_I)10.2f %(counts)7i %(fs)6.1f %(ss)6.1f\n" % {"h":-h,"k":-k,"l":l,"intensity":intensity, "phase":phase, "sigma_I":0.0,"counts":1,"fs":0,"ss":0}
                f2.write(reflection_1)

# 5th equivalent I(h,k,l)= I(h,k,-l)
                phase =360-float(reflection[4]) # Friedel pair have the opposite phase
                reflection_1 = "%(h)3i %(k)3i %(l)3i %(intensity)10.2f %(phase)8.2f %(sigma_I)10.2f %(counts)7i %(fs)6.1f %(ss)6.1f\n" % {"h":h,"k":k,"l":-l,"intensity":intensity, "phase":phase, "sigma_I":0.0,"counts":1,"fs":0,"ss":0}
                f2.write(reflection_1)
# 6th equivalent I(h,k,l) = I(k,-h,l)
                phase =360-float(reflection[4]) # Friedel pair have the opposite phase
                reflection_1 = "%(h)3i %(k)3i %(l)3i %(intensity)10.2f %(phase)8.2f %(sigma_I)10.2f %(counts)7i %(fs)6.1f %(ss)6.1f\n" % {"h":k,"k":-h,"l":l,"intensity":intensity, "phase":phase, "sigma_I":0.0,"counts":1,"fs":0,"ss":0}
                f2.write(reflection_1)

# 7th equivalent I(h,k,l) = I(-k,h,-l)
                phase =360-float(reflection[4]) # Friedel pair have the opposite phase
                reflection_1 = "%(h)3i %(k)3i %(l)3i %(intensity)10.2f %(phase)8.2f %(sigma_I)10.2f %(counts)7i %(fs)6.1f %(ss)6.1f\n" % {"h":-k,"k":h,"l":-l,"intensity":intensity, "phase":phase, "sigma_I":0.0,"counts":1,"fs":0,"ss":0}
                f2.write(reflection_1)

# 8th equivalent I(h,k,l) = I(h,k,-l)
                phase =360-float(reflection[4]) # Friedel pair have the opposite phase
                reflection_1 = "%(h)3i %(k)3i %(l)3i %(intensity)10.2f %(phase)8.2f %(sigma_I)10.2f %(counts)7i %(fs)6.1f %(ss)6.1f\n" % {"h":h,"k":k,"l":-l,"intensity":intensity, "phase":phase, "sigma_I":0.0,"counts":1,"fs":0,"ss":0}
                f2.write(reflection_1)

# 9th equivalent I(h,k,l) = I(-h,-k,l)
                phase =360-float(reflection[4]) # Friedel pair have the opposite phase
                reflection_1 = "%(h)3i %(k)3i %(l)3i %(intensity)10.2f %(phase)8.2f %(sigma_I)10.2f %(counts)7i %(fs)6.1f %(ss)6.1f\n" % {"h":-h,"k":-k,"l":l,"intensity":intensity, "phase":phase, "sigma_I":0.0,"counts":1,"fs":0,"ss":0}
                f2.write(reflection_1)

# 10th equivalent I(h,k,l)=I(-k,h,-l)
                phase =360-float(reflection[4]) # Friedel pair have the opposite phase
                reflection_1 = "%(h)3i %(k)3i %(l)3i %(intensity)10.2f %(phase)8.2f %(sigma_I)10.2f %(counts)7i %(fs)6.1f %(ss)6.1f\n" % {"h":-k,"k":h,"l":-l,"intensity":intensity, "phase":phase, "sigma_I":0.0,"counts":1,"fs":0,"ss":0}
                f2.write(reflection_1)

# 11th equivalent I(h,k,l)= I(k,-h,l)
                phase =360-float(reflection[4]) # Friedel pair have the opposite phase
                reflection_1 = "%(h)3i %(k)3i %(l)3i %(intensity)10.2f %(phase)8.2f %(sigma_I)10.2f %(counts)7i %(fs)6.1f %(ss)6.1f\n" % {"h":k,"k":-h,"l":l,"intensity":intensity, "phase":phase, "sigma_I":0.0,"counts":1,"fs":0,"ss":0}
                f2.write(reflection_1)

# 12th equivalent I(h,k,l)= I(k,-h,-l)
                phase =360-float(reflection[4]) # Friedel pair have the opposite phase
                reflection_1 = "%(h)3i %(k)3i %(l)3i %(intensity)10.2f %(phase)8.2f %(sigma_I)10.2f %(counts)7i %(fs)6.1f %(ss)6.1f\n" % {"h":k,"k":-h,"l":-l,"intensity":intensity, "phase":phase, "sigma_I":0.0,"counts":1,"fs":0,"ss":0}
                f2.write(reflection_1)

# 13th equivalent I(h,k,l)= I(-k,h,l)
                phase =360-float(reflection[4]) # Friedel pair have the opposite phase
                reflection_1 = "%(h)3i %(k)3i %(l)3i %(intensity)10.2f %(phase)8.2f %(sigma_I)10.2f %(counts)7i %(fs)6.1f %(ss)6.1f\n" % {"h":-k,"k":h,"l":l,"intensity":intensity, "phase":phase, "sigma_I":0.0,"counts":1,"fs":0,"ss":0}
                f2.write(reflection_1)

# 14th equivalent I(h,k,l)= I(k,h,l)
                phase =360-float(reflection[4]) # Friedel pair have the opposite phase
                reflection_1 = "%(h)3i %(k)3i %(l)3i %(intensity)10.2f %(phase)8.2f %(sigma_I)10.2f %(counts)7i %(fs)6.1f %(ss)6.1f\n" % {"h":k,"k":h,"l":l,"intensity":intensity, "phase":phase, "sigma_I":0.0,"counts":1,"fs":0,"ss":0}
                f2.write(reflection_1)

# 15th equivalent I(h,k,l)= I(-k,-h,-l)
                phase =360-float(reflection[4]) # Friedel pair have the opposite phase
                reflection_1 = "%(h)3i %(k)3i %(l)3i %(intensity)10.2f %(phase)8.2f %(sigma_I)10.2f %(counts)7i %(fs)6.1f %(ss)6.1f\n" % {"h":-k,"k":-h,"l":-l,"intensity":intensity, "phase":phase, "sigma_I":0.0,"counts":1,"fs":0,"ss":0}
                f2.write(reflection_1)


    f1.close()
    f2.close()



