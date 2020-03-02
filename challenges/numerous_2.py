numberA = raw_input()
listA = raw_input()
numberB = raw_input()
listB = raw_input()

listA = listA.split(' ')
listA.sort()
listB = listB.split(' ')
listB.sort()

list_r = []

for i in range(0, len(listB)):
    if len(listA)-1 < i:
        listA = listA + [0]
    if listB[i] != listA[i]:
        if not listB[i] in list_r:
            list_r.append(listB[i])
        listA = listA[:i] + [listB[i]] + listA[i:]
print (' ').join(list_r)
