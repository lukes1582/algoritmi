#!/usr/bin/env python3

"""
l0m1s
lukes1582@gmail.com
algoritmo selection sort sviluppato per Python
"""

arr = [5,4,3,1,2,11,9,8,0]
print("Array in origine ")
print(arr)
print ("Lunghezza dell'array "+ str(len(arr)))
print(50*"x")

for i in range(len(arr)):
    min_idx = i
    for j in range(i+1, len(arr)):
        if arr[min_idx] > arr[j]:
            min_idx = j
    print(arr)
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
