import cv2 
path_original = r'C:/out/0.bmp'
img = cv2.imread(path_original, 0) 
cv2.imshow('Image crop',img)
cv2.waitKey(0)
cv2.destroyAllWindows()