from PIL import Image, ImageFilter
import matplotlib as plt
import cv2


mitzi = cv2.imread("C:\\Users\\sharong\\Desktop\\git_example\\mitzi_the_idiot.jpg",1)
height, width = mitzi.size
neg = (255-mitzi)
cv2.imshow('image',neg)
new = mitzi.filter(ImageFilter.SMOOTH_MORE)
mitzi = mitzi.tobitmap()
mitzi.show()
r, g, b = new.split()
w=1



