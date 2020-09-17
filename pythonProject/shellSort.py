def shell_sort(array, n):
    h = 1
    while h < n:
        h = 3 * h + 1
    while h > 0:
        for i in range(h + 1, n + 1):
            v, j = array[i], i
            while j > h and array[j - h] > v:
                array[j] = array[j - h]
                j -= h
            array[j] = v
        h = int(h / 3)
    return array