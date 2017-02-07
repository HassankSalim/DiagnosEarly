# adaptive threshold
# threshold = cv2.adaptiveThreshold(gauss, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 201, 2)

# window opteration

# screen_res = 640, 360
# scale_width = screen_res[0] / img.shape[1]
# scale_height = screen_res[1] / img.shape[0]
# scale = min(scale_width, scale_height)
# window_width = int(img.shape[1] * scale)
# window_height = int(img.shape[0] * scale)
# cv2.namedWindow('result', cv2.WINDOW_NORMAL)
# cv2.resizeWindow('result', window_width, window_height)

# --------------------------------------------------------
# finding the center of the lesions
# main_contour_moments = cv2.moments(main_contour)
# centerX = int(main_contour_moments['m10']/main_contour_moments['m00'])
# centerY = int(main_contour_moments['m01']/main_contour_moments['m00'])

# #finding and drawing the min cirlce
# (x, y), radius = cv2.minEnclosingCircle(main_contour)
# cv2.circle(result, (centerX, centerY), int(radius)+15, (0, 255, 0), 1)

# # extracting the pts of the min circle
# ret, threshold_green = cv2.threshold(result[:, :, 1], 250, 255, cv2.THRESH_BINARY)
# _, green_contour_pts, _ = cv2.findContours(threshold_green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# green_contour_pts = green_contour_pts[1]
# print len(green_contour_pts)
# #dict {'theta' : 'intensity'}
# theta_B12 = {}

# # finding B12 markers
# for index, i  in enumerate(green_contour_pts):
# 	tx, ty = i[0]
# 	intensity = sum(map(lambda x : img[x[0], x[1], 0], get_line((centerX, centerY), (tx, ty))))
# 	theta_B12[index] = intensity

# print theta_B12
# plt.plot(theta_B12.keys(), theta_B12.values())
# plt.show()
# --------------------------------------------------------


# print green_contour_pts
# interval = int((1 / 360.0) * green_contour_pts.shape[0])
# if not interval:
	# interval = 1

# cv2.drawContours(img, [second_contour], 0, (255, 0, 0), 3)
# isSysmetric = cv2.isContourConvex(second_contour)
# print isSysmetric

# display result
# print area_1
# print area_2
