import cv2 
import numpy as np
image1 = cv2.imread('odspweb.png') 
image2 = cv2.imread('faultypage.png') 

if image1.shape == image2.shape:
    print("images are equal in size")
else:
    print("Not in equal size")

res = cv2.absdiff(image1, image2)
#--- convert the result to integer type ---
res = res.astype(np.uint8)

#--- find percentage difference based on number of pixels that are not zero ---
percentage = (np.count_nonzero(res) * 100)/ res.size

print("Pecentage difference : ", percentage)
difference = cv2.subtract(image1,image2)
#cv2.imshow("difference",difference)


#cv2.imshow("diff", image1)
#cv2.imshow("diff2", image2)
cv2.waitKey(0)
cv2.destroyAllWindows()