import sys

def search_max(array_cw):
    return max(array_cw)

def search_min(array_cw):
    return min(array_cw)

suma_by = lambda y,max,array: map(lambda x: x+y if x + y <= max else x, array)



####################################################################
num_test = int(input())
num_coworkers = 0
coworkers = []

by_5 = 5
by_2 = 2
by_1 = 1

for i in xrange(num_test):
    num_coworkers = int(input())
    coworkers = map(lambda x: int(x), raw_input().split())
    max_cow = search_max(coworkers)
    min_cow = search_min(coworkers)
    count = 0
    while(not max_cow - min_cow == 0):
        if(max_cow - min_cow >= by_5):
            coworkers = suma_by(by_5,max_cow,coworkers)
        else:
            if((max_cow - min_cow) < by_5 and (max_cow - min_cow) >= by_2):
                coworkers = suma_by(by_2,max_cow,coworkers)
            else:
                coworkers = suma_by(by_1,max_cow,coworkers)
        print coworkers
        max_cow = search_max(coworkers)
        min_cow = search_min(coworkers)
        count += 1
    print(count)
