import numpy as np

arr01 = np.array([1, 2, 3])
arrtest = arr01.tobytes()
print(arrtest)
print(type([1, 2, 3]))  # list 在 list 中保存的是数据的存放的地址，即指针，并非数据。
print(arr01)  # [1 2 3]
print(type(arr01))  # <class 'numpy.ndarray'>
print(arr01.dtype)  # int32

# Upcasting
arr02 = np.array([1., 2., 3.])
print(arr02)  # [1. 2. 3.]
print(arr02.dtype)  # float64

# More than one dimension:
arr03 = np.array([[1, 2], [3, 4]])
print(arr03)
