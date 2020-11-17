from assertion import assert_sorted
from utility import random_list

from matlab import dump_sorting_function

def quick_sort(array):
    quick_sort_internal(array, 0, len(array) - 1)


def quick_sort_internal(array, left, right):
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
        quick_sort_internal(array, left, i - 1)
        quick_sort_internal(array, i + 1, right)
    return array


dummy = random_list(100)

print(dummy)

quick_sort(dummy)

print(dummy)

assert_sorted(dummy, lambda l, r: l <= r)

dump_sorting_function("퀵정렬", quick_sort, range(1, 1000, 10))
