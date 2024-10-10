import numpy as np 

origanl = np.array([1,2,3,4,5,6])
# reshaped_array = origanl.reshape(2,3) 
row_major = origanl.reshape(2,3 , order='C')
coloum_major = origanl.reshape(2,3 , order='F')

print("original array : " , origanl) 
print("row major array : " , row_major)
print("coloumn major array: " , coloum_major)

