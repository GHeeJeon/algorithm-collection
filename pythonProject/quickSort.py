def quick_sort(array, left, right):
    if right > left:
        v, i, j = array[right], left - 1, right
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
        array[i], array[right] = array[right], array[i]
        quick_sort(array, left, i - 1)
        quick_sort(array, i + 1, right)
    return array
