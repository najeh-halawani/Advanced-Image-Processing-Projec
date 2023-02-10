import cv2 as cv
from PIL import Image, ImageFilter
from matplotlib import pyplot as plt
import PIL
import numpy as np
import random



def adaptveThreshholding(Image):
    image = cv.imread(Image)
    img = cv.cvtColor(image,cv.COLOR_RGB2GRAY)
    img= cv.resize(img,(700,700))
    _,result=cv.threshold(img,0,190,cv.THRESH_BINARY)
    #  the last two value can be changed depending ont the pic but abl e5er wehde have to always be ODD
    adaptiveIMG = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)
    # adaptiveIMG=cv.resize(adaptive,(700,700))
    titles = ['Original Image', 'Enhanced Image']
    images = [image,adaptiveIMG]
    # path = 'C:\\Desktop\\Output',random.randint(1,15),'.jpg'
    cv.imwrite('C:\\Desktop\\Output.jpg',adaptiveIMG)
    cv.imshow('Enhanced Image', adaptiveIMG)
    for i in range(2):
        plt.subplot(1, 2, i+1), plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()
    cv.waitKey(0)
    cv.destroyAllWindows()
    
def enhancement_save(Image):
    image = cv.imread(Image)
    
    img = cv.cvtColor(image,cv.COLOR_RGB2GRAY)
    img= cv.resize(img,(700,700))
    _,result=cv.threshold(img,0,190,cv.THRESH_BINARY)
    #  the last two value can be changed depending ont the pic but abl e5er wehde have to always be ODD
    adaptive = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)
    adaptiveIMG=cv.resize(adaptive,(700,700))
    path = 'C:\\Desktop\\Output',random.randint(10),'.jpg'
    cv.imwrite(path,adaptiveIMG)





