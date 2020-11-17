import random, time


def merge_sort(arr):
    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        temp = []
        l, h = low, mid

        while l < mid and h < high:
            if arr[l] < arr[h]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h += 1

        while l < mid:
            temp.append(arr[l])
            l += 1
        while h < high:
            temp.append(arr[h])
            h += 1

        for i in range(low, high):
            arr[i] = temp[i - low]

    return sort(0, len(arr))


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
merge_sort(array)

end_time = time.time() - start_time
print('정렬 실행 시간 (N= %d) : %0.3f' % (N, end_time))
