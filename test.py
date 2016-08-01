import input_data
import cv2

cv2.namedWindow('plane')
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
cv2.waitKey()
