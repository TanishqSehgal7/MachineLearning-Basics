# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#NumPy is a library in python which provides a multidimentional array with many built in functions
import numpy as np 
import matplotlib.pyplot as plt

a=np.array([(1,2,3),(2,3,4)])
print("Dimension of the array is:")
print(a.ndim)               #prints the dimension of the array
print("The size of the array is:")
print(a.itemsize)
print("The datatype of the array is:")
print(a.dtype)
print(a.shape)  #tells th number of rows and columns in array
print(a.size)   # tells the number of elements in the array
#reshaping and slicing of array
a=a.reshape(3,2)
print(a)
a=a.reshape(2,3)
print("\n")
print(a)
#slicing in numpy array
print(a[0,2])
print("\n")
print((a[0:,2]))
A=np.linspace(1,3,10) #gives 10 equispaced values between 1 and 3 -> syntax- np.linespace(start,end,number of values)
print(A)
#minimum, maximum and sum of numpy array
array1=np.array([(1,2,3),(4,5,6),(7,8,9)])
print(array1.min())  #prints the minimum element in the array
print("\n")
print(array1.max()) #prints the maximum element in the array
print("\n")
print(array1.sum())
print("\n")
print(array1)
print("\n")
#sum of the axis 
 #if axis=0 -> vertical sum of values and if axis=1-> horizontal sum of values is obtained
print(array1.sum(axis=0))  
print("\n")
print(array1.sum(axis=1)) # horizontal sum of values 

#some more mathematical operations in numpy 

#finding the square root of each element
print(np.sqrt(array1))
print("\n")

#standard deviation of the array
print(np.std(array1))

#additon multiplication and subtraction in numpy array
# addition of arrays
array2=np.array([(2,3,4),(4,5,6),(6,7,8)])
print("Final array after addition is:")
print(array1+array2)
print("\n")
#multiplication of arrays
print("Final array after multiplication is:")
print(array1*array2)
print("\n")
#division of arrays
#print("Final array after division is:\n")
#print(array1/array2)
#print("\n")
#print("Printing vertical stack of both arrays:")
#print(np.vstack(array1,array2))
#print("\n")
#print("Printing horizontal stack of both arrays:\n")
#print(np.hstack((array1,array2)))
#print("Printing vertical stack of both arrays:\n")
#print(np.vstack((array1,array2)))

#converting an array into a single column
print(array1.ravel())
print("\n")
#special functions in numpy-> done using matplotlib
#sine function
x=np.arange(0,3*np.pi,0.1)
print("Printing sine function graph:\n")
y=np.sin(x)
plt.plot(x,y)
plt.show()
print("\n")
#cosine function
print("Printing cosine function graph:\n")
z=np.cos(x)
plt.plot(x,z)
plt.show()
print("\n")
#tan function
print("Printing tan function graph:\n")
t=np.tan(x)
plt.plot(x,t)
plt.show()
print("\n")
#expotential function
print("Printing exponential values of array1:\n")
print(np.exp(array1))
print("\n")
#logarithmic function
print(np.log(array1)) # this gives the natural log -> (ln)
print("\n")
print(np.log10(array1)) # this gives logarithmic values with base 10

