import random, time
import checkSort

N = int(input("N의 값 입력: "))
array = []
for i in range(N):
    array.append(random.randint(1, N))
start_time = time.time()
#add sort function here
end_time = time.time() - start_time
print('정렬 실행 시간 (N= %d) : %0.3f'%(N, end_time))
checkSort(array, N)