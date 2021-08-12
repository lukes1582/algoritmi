#!/usr/bin/env python3

"""
l0m1s
lukes1582@gmail.com
algoritmo counting sort sviluppato per Python
"""

arr = [50, 1000, 0, 43, 8, 5, 1, 10]

print(arr)

maxElement = int(max(arr))
minElement = int(min(arr))
rangeOfElements = maxElement - minElement + 1

"""
per prima cosa assegno 0 a tutti gli elementi dell'array count_arr che è esattamente
lungo quanto calcolato in precedenza
"""
count_arr = [0 for _ in range(rangeOfElements)] 
"""
poi procedo ad assegnare 0 a tutti gli elementi dell'array output_arr che ha una grandezza
paritetica a quella dell'array da ordinare
"""
output_arr = [0 for _ in range(len(arr))]


for h in range(0, len(arr)):
    count_arr[arr[h]-minElement] += 1  # assegno 1 nel count_arr nella posizione definita dal valore preso dell'arr - il valore minimo 

for k in range(1, len(count_arr)):
    count_arr[k] += count_arr[k-1]

for j in range(len(arr)-1, -1, -1):
    output_arr[count_arr[arr[j] - minElement] - 1] = arr[j]
    count_arr[arr[j] - minElement] -= 1

print(output_arr)

for w in range(0, len(arr)):
    arr[w] = output_arr[w]

print(arr)
 
