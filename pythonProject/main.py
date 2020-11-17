import random, time

"""
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
    
    
    def heapify(a, h, m):
    v, j = a[h], 2 * h
    while j <= m:
        if j < m and a[j] < a[j+1]:
            j += 1
        if v >= a[j]:
            break
        else:
            a[int(j/2)] = a[j]
        j *= 2
    a[int(j/2)] = v


def heapSort(a, n):
    for i in range(int(n/2), 0, -1):
        heapify(a, i, n)
    for i in range(n-1, 0, -1):
        a[1], a[i+1] = a[i+1], a[1]
        heapify(a, 1, i)
        
        
def merge_sort(array, left, right):
    if right > left:
        middle = int((right + left) / 2)
    merge_sort(array, left, middle)
    merge_sort(array, middle + 1, right)
    for i in range(middle + 1, left, -1):
        brray[i - 1] = array[i - 1]
    i -= 1
    for j in range(middle, right):
        brray[right + middle - j] = array[j + 1]
    j += 1
    for k in range(left, right + 1):
        if brray[i] < brray[j]:
            array[k] = brray[i]
            i += 1
        else:
            array[k] = brray[j]
            j -= 1
"""


def checkSort(a, n):
    is_sorted = True
    for i in range(1, n):
        if a[i] > a[i + 1]:
            is_sorted = False
        if not is_sorted:
            break
    if is_sorted:
        print("정렬 완료!")
    else:
        print("정렬 오류 발생")


N = int(input("N의 값 입력: "))

array = []
for i in range(N):
    array.append(random.randint(1, N))

start_time = time.time()
# add sort function here
end_time = time.time() - start_time
print('정렬 실행 시간 (N= %d) : %0.3f' % (N, end_time))
checkSort(array, N)
