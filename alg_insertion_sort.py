#!/usr/bin/env python3

"""
l0m1s
lukes1582@gmail.com
algoritmo insertion sort sviluppato per Python
"""

arr = [5,4,3,1,2,11,9,8,0]
print("Array in origine ")
print(arr)
print ("Lunghezza dell'array "+ str(len(arr)))
print(50*"x")

for i in range(1, len(arr)):
    key = arr[i]

    j = i-1
    while j >=0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
    arr[j+1] = key

print ("l'array ordinato risulta essere: ")
for x in range(len(arr)):
	print ("%d" %arr[x])

