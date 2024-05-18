import cv2


img = cv2.imread("solar-system.jpg")


cv2.putText(img, "Sun", (20, 300), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
cv2.putText(img, "Mercury", (110, 250), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
cv2.putText(img, "Venus", (190, 250), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
cv2.putText(img, "Earth", (290, 250), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
cv2.putText(img, "Mars", (390, 250), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
cv2.putText(img, "Jupiter", (490, 250), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
cv2.putText(img, "Saturn", (690, 250), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
cv2.putText(img, "Uranus", (890, 250), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
cv2.putText(img, "Neptune", (1090, 250), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)


cv2.imshow("output", img)
cv2.waitKey(0)


cv2.imwrite("Solar_systemwithname.jpg", img)
