import sys
print(sys.version)
print("tes script")

from PIL import Image
import cv2
  
originalImage = cv2.imread(r'person.jpeg')
grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY) 
(thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 70, 255, cv2.THRESH_BINARY)
 
cv2.imshow('Black white image', blackAndWhiteImage)




filename = 'new.png'
cv2.imwrite(filename, blackAndWhiteImage)
print("saved")
im1 = Image.open(r'/Users/ilse/Downloads/image0.jpeg')
im1.save(r'/Users/ilse/Downloads/image0.png')

cv2.destroyAllWindows()