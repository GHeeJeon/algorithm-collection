def insert_sort(array, n):
    for i in range(2, n + 1):
        v, j = array[i], i
        while array[j - 1] > v:
            array[j] = array[j - 1]
            j -= 1
        array[j] = v
    return array