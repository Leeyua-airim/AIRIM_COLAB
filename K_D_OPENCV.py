import cv2

img_file = 'C:/github/AIRIM_DEEP/image/JORDY.jpg'

img = cv2.imread(img_file)

if img is not None:
    cv2.imshow("IMG", img)
    cv2.waitKey()
    cv2.destroyAllWindows()
else:
    print("이미지 인식 못함")
