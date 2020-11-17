#TODO understand heapify

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

