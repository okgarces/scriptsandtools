def get_freq(list_i):
    hash_r = {}
    count_i = 0
    for i in range(0, len(list_i)):
        for j in range(0, len(list_i)):
            if list_i[i] == list_i[j]:
                count_i+=1
        hash_r[list_i[i]] = count_i
        count_i = 0
    return hash_r

def get_missing_numbers(hash_a, hash_b):
    array_r = []
    hash_a_keys = hash_a.keys()
    hash_b_keys = hash_b.keys()
    for i in range(0, len(hash_b_keys)):
        # Si el key no esta en el dict lo aegrega a los numeros perdidos.
        if not hash_b_keys[i] in hash_a_keys:
            array_r.append(hash_b_keys[i])
        else:
            # Si el key esta revisar que se encuentren en la misma frecuencia
            if hash_b[hash_b_keys[i]] != hash_a[hash_b_keys[i]]:
                array_r.append(hash_b_keys[i])
    array_r.sort()
    return (' ').join(array_r)

numberA = raw_input()
listA = raw_input()
numberB = raw_input()
listB = raw_input()

listA = listA.split(' ')
listB = listB.split(' ')

hash_a = get_freq(listA)
hash_b = get_freq(listB)

print(get_missing_numbers(hash_a, hash_b))
