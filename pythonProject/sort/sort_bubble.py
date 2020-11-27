"""
good for almost-sorted file
"""


def bubble_sort(array, size_of_array):
    for i in range(size_of_array - 1, 0, -1):   # 배열 원소 수만큼 내림차순으로 라운드가 있어(0부터 원소 수-1이니까 맞지?)
        for j in range(0, i):                   # 0부터 현재 라운드까지 반복이야
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


input_array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
bubble_sort(input_array, len(input_array))
print(input_array)
