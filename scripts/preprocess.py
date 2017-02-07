import cv2
import numpy as np
from drawLine import get_line
from b12_mib import find_b12
import matplotlib.pyplot as plt

# loading image and convert to gray_scale
img = cv2.imread('../mole8.jpg', 1)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# applying gaussian filter and ostu's binarilization
gauss = cv2.GaussianBlur(gray_img, (5,5), 0)
ret, threshold = cv2.threshold(gauss, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# bitwise operation 
threshold_inv = cv2.bitwise_not(threshold)
result = cv2.bitwise_and(img, img, mask = threshold_inv)

# contour operations 
img_contour, contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
area_of_contours = map(cv2.contourArea, contours)
sorted_contour_area = sorted(area_of_contours, reverse = True)
top_contours =  sorted_contour_area[1:3]

# print top_contours
contour_list = []
for i in contours:
	area = cv2.contourArea(i)
	if area == top_contours[0]:
		main_contour = i
	if area in top_contours:
		cv2.drawContours(img, [i], 0, (0,255,0), 3)
		contour_list.append(i)

# values from find_b12 function
b12_details = find_b12(img, main_contour, result, 0)
print b12_details['min'], '-', b12_details['max']

cv2.drawContours(img, contour_list, -1, (0, 0, 255), 3)
cv2.imshow('result_wihout_hull', img)
hull_list = map(cv2.convexHull, contour_list)

# print hull
cv2.drawContours(img, hull_list, 0, (255,255,255), 3)
cv2.imshow('result_with_hull', img)

cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()

