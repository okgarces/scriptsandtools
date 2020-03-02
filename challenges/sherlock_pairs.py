import sys
from collections import defaultdict

sys.setrecursionlimit(100000)

num_test = int(input())

factorial = lambda x: x*factorial(x-1) if x>1 else 1

def count_array(array):
    dictn = {}
    for i in array:
        a = 0
        count = reduce(lambda count, x: count+1 if x==i else count, array, 0)
        dictn[i] = count
    return dictn

def count_array_on(string):
    dictn = defaultdict(int)
    for i in string.split():
        dictn[i] += 1
    return dictn

def calculate_permutation(dictn):
    calculo = 0
    for k, freq in dictn.iteritems():
        if(freq>1):
            # permutación = (factorial(freq) / (factorial(freq - 2)))
            # Pero simplificando da freq*(freq-1).    
            calculo = calculo + (freq*(freq-1))
    return calculo


for i in range(num_test):
    num_array = int(input())
    array = raw_input()
    #array = map(lambda x: int(x), array.split())
    print(calculate_permutation(count_array_on(array)))
