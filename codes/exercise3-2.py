# Write a program that reads 2 integers, say, a and b, then produce a sequence of 9 evenly distributed values in the
# range of \\( [a, b] \\), formatted as a 3 x 3 integer array (values should be floored/truncated). (Hint: use
# linspace())


import numpy as np
a = int(input())
b = int(input())
arr = np.linspace(a, b, 9, dtype=int)
list1 = arr[0: 3]
list2 = arr[3: 6]
list3 = arr[6: 9]
arrList1 = list1.tolist()
arrList2 = list2.tolist()
arrList3 = list3.tolist()
myList = np.zeros((3, 3), dtype=int)
myList[0] = arrList1
myList[1] = arrList2
myList[2] = arrList3
print(myList)
