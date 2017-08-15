#! /usr/bin python
# -*- coding:utf-8 -*-

import cv2


resim = cv2.imread('dybala.jpg', 1)

pixel = resim[200, 300]

print(pixel)

resim[200, 300] = [100, 180, 200]

print(resim[200, 300])

print(resim.shape)

# image ROI işlemleri

kafa = resim[45:200, 365:485]

resim[200:355, 100:220] = kafa




cv2.imshow('dybala', resim)
if cv2.waitKey(0) &0xFF == ord('s'):
    cv2.imwrite('dybala_roi.jpg', resim)
    cv2.destroyAllWindows()



