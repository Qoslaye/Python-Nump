import numpy as np 

original = np.array([1,2,3,4,5]) 

# copied = original.copy() 
# copied[0] = (20) 

veiwed_array = original.view() 
veiwed_array[0] = (20) 

print("original array : " , original) 
print("veiwed array : " , veiwed_array )
