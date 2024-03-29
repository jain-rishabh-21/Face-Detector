import cv2

face_casecade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("group.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)


faces = face_casecade.detectMultiScale(gray_img ,
scaleFactor = 1.05,
minNeighbors = 5)

print(faces)

for x, y, w, h in faces:
    img = cv2.rectangle(img,(x , y) , (x + w , y + h), (255, 255, 0), 3)

cv2.imshow("GRAY", img)
cv2.waitKey(0)
cv2.destroyAllWindows()