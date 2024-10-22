import cv2 as cv
from matplotlib import pyplot as plt


img = cv.imread('Pictures/img.jpg' ,0)

_, th1 = cv.threshold(img, 50, 255, cv.THRESH_BINARY)

_, th2 = cv.threshold(img, 200, 255, cv.THRESH_BINARY_INV)

_, th3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)

_, th4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)

_, th5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)
th6adaptive = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2) #more informative
th7adaptive = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

threshold = [th1, th2, th3, th4, th5, th6adaptive, th7adaptive]
titles = ['THRESH_BINARY', 'THRESH_BINARY_INV', 'THRESH_TRUNC', 'THRESH_TOZERO', 'THRESH_TOZERO_INV', 
          'ADAPTIVE_THRESH_MEAN_C', 'ADAPTIVE_THRESH_GAUSSIAN_C']

fig, ax = plt.subplots(nrows=2, ncols=3, figsize = (15, 10))
for i in range(6):
    row = i // 3
    col = i % 3
    ax[row, col].imshow(threshold[i], 'gray')
    ax[row, col].set_title(titles[i])
    ax[row, col].axis('off')
    
plt.show()

cv.waitKey(0)

cv.destroyAllWindows() #close window