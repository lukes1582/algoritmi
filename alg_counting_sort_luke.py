#!/usr/bin/env python3

"""
l0m1s
lukes1582@gmail.com
algoritmo counting sort sviluppato per Python
"""
# funziona solo con valori interi positivi
arr = [50, 1000, 2, 43, 0, 343, 5100, 10]

print(arr)

maxElement = int(max(arr))
minElement = int(min(arr))
rangeOfElements = maxElement - minElement + 1

"""
per prima cosa assegno 0 a tutti gli elementi dell'array count_arr che è esattamente
lungo quanto calcolato in precedenza
"""
count_arr = ["0" for _ in range(rangeOfElements)] 
"""
poi procedo ad assegnare 0 a tutti gli elementi dell'array output_arr che ha una grandezza
paritetica a quella dell'array da ordinare
"""
output_arr = [0 for _ in range(len(arr))]


for h in range(0, len(arr)):
    count_arr[arr[h]-minElement] = "x"  # assegno 1 nel count_arr nella posizione definita dal valore preso dell'arr - il valore minimo 

index = 0
for j in range(0,len(count_arr)):
    if(count_arr[j]!="0"):
        output_arr[index] = j
        index += 1

print(output_arr)
 
