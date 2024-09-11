from opencv_basic.basic import *
from numpy_basic.basic import *
import cv2
import numpy as np

def main():
    # create a numpy array
    array = np.array([1, 2, 3, 4, 5])
    # create an object of NumpyBasic class
    numpy_basic = NumpyBasic(array)
    # add 5 to the numpy array
    print(numpy_basic.add(5))
    # subtract 5 from the numpy array
    print(numpy_basic.subtract(5))
    # multiply the numpy array by 5
    print(numpy_basic.multiply(5))
    # divide the numpy array by 5
    print(numpy_basic.divide(5))
    # raise the numpy array to the power of 5
    print(numpy_basic.power(5))
    # take the square root of the numpy array
    print(numpy_basic.square_root())
    # take the natural logarithm of the numpy array
    print(numpy_basic.log())
    # take the exponential of the numpy array
    print(numpy_basic.exp())
    # take the sine of the numpy array
    print(numpy_basic.sin())
    # take the cosine of the numpy array
    print(numpy_basic.cos())
    # take the tangent of the numpy array
    print(numpy_basic.tan())
    # take the inverse sine of the numpy array
    print(numpy_basic.arcsin())
    # take the inverse cosine of the numpy array
    print(numpy_basic.arccos())
    # take the inverse tangent of the numpy array
    print(numpy_basic.arctan())
    # take the hyperbolic sine of the numpy array
    print(numpy_basic.sinh())
    # take the hyperbolic cosine of the numpy array
    print(numpy_basic.cosh())
    # take the hyperbolic tangent of the numpy array
    print(numpy_basic.tanh())
    # take the inverse hyperbolic sine of the numpy array
    print(numpy_basic.arcsinh())
    # take the inverse hyperbolic cosine of the numpy array
    print(numpy_basic.arccosh())
    # take the inverse hyperbolic tangent of the numpy array
    print(numpy_basic.arctanh())
    # create an object of OpencvBasic class

main()