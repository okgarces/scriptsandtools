#!/bin/python
def insertion_sort(array):
    for i in range(len(array)-1,-1,-1):
        j = i-1
        temp = array[i]
        while j >= 0 and (array[i] < array[j]):
            array[i] = array[j]
            print(' '.join(str(x) for x in array))
            j = j-1
        array[j+1] = temp
    return array
m = input()
ar = [int(i) for i in raw_input().strip().split()]
print(' '.join(str(x) for x in insertion_sort(ar)))
