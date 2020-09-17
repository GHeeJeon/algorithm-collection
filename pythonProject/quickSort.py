def quick_sort(array, l, r):
    if r > l:
        v, i, j = array[r], l - 1, r
        while True:
            i += 1
            while array[i] < v:
                i += 1
            j -= 1
            while array[j] > v:
                j -= 1
            if i >= j:
                break
            array[i], array[j] = array[j], array[i]
        array[i], array[r] = array[r], array[i]
        quick_sort(array, l, i - 1)
        quick_sort(array, i + 1, r)
    return array
