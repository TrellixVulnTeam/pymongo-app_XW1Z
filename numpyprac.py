import numpy as np

print("------------------------------")
arr = np.array([[1,2,3,4], [5,6,7,8]])
# arr = np.ones((2,5))
# print(arr.shape)
b = arr[0:3, 1:4]
row1 = arr[1, :]
row2 = arr[1:2, :]
# print(row1, row1.shape)
# print(row2, row2.shape)
# print(arr[arr<5])
a1 = np.array([[1,2], [1,2]], dtype=np.int64)
a2 = np.array([[1,1], [1,1]], dtype=np.int64)
# print(np.sum(a1, axis=1))
# print(a1)
# print("Transposing")
# print(a1.T)
arr2 = np.empty_like(arr)
# print(arr[0, :] + 10)
for i in range(2):
    arr2[i, :] = arr[i, :] + 10

# print(arr2)
a1 = np.tile(a1, (4, 1))
print(a1.shape)