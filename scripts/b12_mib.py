import cv2
import numpy as np
from drawLine import get_line
import matplotlib.pyplot as plt


def find_b12(img, main_contour, extracted_lesion, channel):
	
	# finding the center of the lesions
	main_contour_moments = cv2.moments(main_contour)
	centerX = int(main_contour_moments['m10']/main_contour_moments['m00'])
	centerY = int(main_contour_moments['m01']/main_contour_moments['m00'])

	#finding and drawing the min cirlce
	(x, y), radius = cv2.minEnclosingCircle(main_contour)
	cv2.circle(extracted_lesion, (centerX, centerY), int(radius)+15, (0, 255, 0), 1)
	
	# extracting the pts of the min circle
	ret, threshold_green = cv2.threshold(extracted_lesion[:, :, 1], 250, 255, cv2.THRESH_BINARY)
	_, green_contour_pts, _ = cv2.findContours(threshold_green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	green_contour_pts = green_contour_pts[1]
	
	# dict {'theta' : 'intensity'}
	theta_B12 = {}

	# finding B12 markers
	for index, i  in enumerate(green_contour_pts):
		tx, ty = i[0]
		pts = get_line((centerX, centerY), (tx, ty))
		intensity = sum(map(lambda x : img[x[0], x[1], channel], pts))
		non_zero_pixels = len(filter(lambda x : img[x[0], x[1], 0] != 0, pts)) 
		theta_B12[index] = intensity/non_zero_pixels

	# plotting	
	plt.plot(theta_B12.keys(), theta_B12.values())
	plt.show()
	return { 'max': max(theta_B12.values()), 'min' : min(theta_B12.values()) }