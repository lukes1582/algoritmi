#!/usr/bin/env python3

"""
l0m1s
lukes1582@gmail.com
algoritmo bubble sort sviluppato per Python
"""

arr = [5,4,3,1,2,11,9,8,0]
print("Array in origine ")
print(arr)
print ("Lunghezza dell'array "+ str(len(arr)))
print(50*"x")
n = len(arr)
for i in range(n-1):
    for j in range(0, n-i-1):
        if arr[j] > arr[j + 1] :
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(arr)




