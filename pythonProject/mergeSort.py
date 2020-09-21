def merge_sort(array, brray, left, right):
    if right > left:
        middle = int((right + 1) / 2)
    merge_sort(array, left, middle)
    merge_sort(array, middle + 1, right)
    for i in range(middle + 1, left, -1):
        brray[i - 1] = array[i - 1]
    i -= 1
    for j in range(middle, right):
        brray[right + middle - j] = array[j - 1]
    j += 1
    for k in range(left, right + 1):
        if brray[i] < brray[j]:
            array[k] = brray[i]
            i += 1
        else:
            array[k] = brray[j]
            j -= 1
