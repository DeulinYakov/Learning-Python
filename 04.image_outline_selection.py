import cv2
from matplotlib import pyplot as plt

img = cv2.imread('/home/yakov/Изображения/1614761033_156-p-belii-krug-na-chernom-fone-198.jpg', 0)
print(img.shape)
plt.figure(figsize=(24, 24))

j=100
for i in range(799):
    if img[j][i] < 128 and img[j+1][i+1] > 128:
        img[j][i] = 255
        i += 1
    elif img[j][i] > 128 and img[j+1][i+1] < 128:
        img[j][i] = 0
        i += 1
    else:
        img[j][i] = 0
        i += 1
plt.imshow(img, cmap='gray')
plt.show()