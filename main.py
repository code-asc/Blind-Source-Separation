import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import math
import cv2
import cv

def merge(pathOne, pathTwo):
    s1 = cv2.imread(pathOne, cv2.IMREAD_GRAYSCALE)
    s2 = cv2.imread(pathTwo, cv2.IMREAD_GRAYSCALE)
     
    # singular value decomposition
    A = np.array([[1, 0.2], [1/2, 2/3]])


    # mixed images
    x1 = A[0][0] * s1 + A[0][1] * s2
    x2 = A[1][0] * s1 + A[1][1] * s2
    return (s1, s2, x1, x2)

s1, s2, x1, x2 = merge("im1.jpg", "im2.jpg")

plt.figure(figsize=(8,8))

plt.subplot(3,2,1)
plt.imshow(s1)

plt.subplot(3,2,2)
plt.imshow(s2)

plt.subplot(3,2,3)
plt.imshow(x1)

plt.subplot(3,2,4)
plt.imshow(x2)



m,n = x1.shape

# reshaping matrics
x1 = x1.reshape(m*n, 1)
x2 = x2.reshape(m*n, 1)

# We assume that the data has a mean 0
x1 = (x1 - np.mean(x1))/(m*n)
x2 = (x2 - np.mean(x2))/(m*n)

# rotate out PC direction
theta0 = 0.5 * math.atan(-2*np.sum(np.multiply(x1,x2)) / np.sum(np.subtract(np.multiply(x1,x1), np.multiply(x2,x2))))
Us = np.array([[math.cos(theta0), math.sin(theta0)], [-math.sin(theta0), math.cos(theta0)]])

# undo scaling of singular matrix
sig1 = np.sum(np.square(x1 * math.cos(theta0) + x2 * math.sin(theta0)))
sig2 = np.sum(np.square(x1 * math.cos(theta0 - math.pi/2) + x2 * math.sin(theta0 - math.pi/2)))

Sigma = np.array([[1/math.sqrt(sig1), 0], [0, 1/math.sqrt(sig2)]])

# make probability densit seperable
temp1 = Us[0][0] * x1 + Us[0][1] * x2 
temp2 = Us[1][0] * x1 + Us[1][1] * x2 

x1bar = Sigma[0][0] * temp1
x2bar = Sigma[1][1] * temp2


phi0 = 0.25 * math.atan(-np.sum(2 * np.multiply(np.power(x1bar,3), x2bar - 2 * np.multiply(np.power(x2bar,3), x1bar))))/np.sum(3 * np.multiply(np.power(x1bar,2), np.power(x2bar,2)) - 0.5 * np.power(x1bar,4) - 0.5 * np.power(x2bar,4))

v = np.array([[math.cos(phi0), math.sin(phi0)], [-math.sin(phi0), math.cos(phi0)]])

s1bar = v[0][0] * x1bar + v[0][1] * x2bar
s2bar = v[1][0] * x1bar + v[1][1] * x2bar

plt.subplot(3,2,5)
plt.imshow(s1bar.reshape(m,n))

plt.subplot(3,2,6)
plt.imshow(s2bar.reshape(m,n))

plt.show(block=False)
