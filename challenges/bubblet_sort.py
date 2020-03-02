



def bubble_sort(array):

	size = len(array)

	for i in range(0,size):
		for j in range(i,size):
			if array[i] > array[j]:
				tmp = array[i]
				array[i] = array[j]
				array[j] = tmp
				print 'Despues de cambio',i, array

		print 'Temporal',i, array

	return array


def bubble_sort3(array):
    size = len(array)
    for i in range(0,size):
        for j in range(0,size-1):
            if array[j] > array[j+1]:
                tmp = array[j]
                array[j] = array[j+1]
                array[j+1] = tmp
                print 'Despues de cambio',i, array
                
        print 'Temporal',i, array
    return array




def bubble_sort2(array):

	size = len(array)
	ordered = False
	k = 0
	change = False
	while(not ordered):

		for i in range(0, size-1-k):
			j = i+1
			if array[i] > array[j]:
				tmp = array[i]
				array[i] = array[j]
				array[j] = tmp
				print 'Despues de cambio',i, array
				change = True

		if not change:
			ordered = True

		change = False

	return array




print bubble_sort3([5,4,3,2,1,0])
#print bubble_sort2([5,4,3,2,1,0])
