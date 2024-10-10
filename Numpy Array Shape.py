import numpy as np 

array_1d = np.array([1,2,3,4,5]) 
array_2d = np.array([[1,2,3] ,[4,5,6]])
array_3d = np.array([[[1,2] ,[3,4] ,[5,6] ,[7,8]]])

print("shape of 1D array : " , array_1d )
print("shape of 2D array : " , array_2d )
print("shape of 3D array : " , array_3d )

arr = np.array([1,2,3,4] , ndmin=5) 
print(arr) 
print("shape of array : " , arr.shape)