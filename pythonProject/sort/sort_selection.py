def selection_sort(array, number_of_element):
    for i in range(1, number_of_element):
        min_index = i
        for j in range(i + 1, number_of_element + 1):
            if array[min_index] > array[j]:
                min_index = j
        array[min_index], array[i] = array[i], array[min_index]
    return array
