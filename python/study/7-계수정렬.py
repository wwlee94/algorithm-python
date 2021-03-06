'''
'크기를 기준으로 개수를 세면 어떨까?'

지금까지 여러 정렬 기법에 대해 알아보았습니다.
O(N*logN)의 시간복잡도를 가지는 퀵 정렬, 병합 정렬, 힙 정렬 보다 더욱 빠르게 정렬을 해야 한다면 어떻게 할까요?

다음의 5이하 자연수 데이터들을 오름차순 정렬하세요.
1 3 2 4 3 2 5 3 1 2 3 4 4 3 5 1 2 3 5 2 3 1 4 3 5 1 2 1 1 1

이번 예시는 정렬할 데이턱의 개수가 30개입니다.
다만 모든 데이터가 1부터 5 사이에 속한다는 특징을 가집니다.
바로 이처럼 '범위 조건'이 있는 경우에 한해서 굉장이 빠른 알고리즘이 존재합니다.
그 속도는 무려 O(N)을 가진 '계수 정렬(Counting Sort)' 입니다.

지금까지는 모든 데이터를 위치를 바꾸어가면서 정렬하는 알고리즘이였지만
이번 계수 정렬은 위치를 바꿀 필요 없이 '크기를 기준으로' 개수만 세주면 되기 때문에 모든 데이터에 한 번씩만 접근하면 됩니다.

- 알고리즘 동작 방식 -
# 초기
크기=1 / 크기=2 / 크기=3 / 크기=4 / 크기=5
  0       0       0       0       0

# 1번째 상태
크기=1 / 크기=2 / 크기=3 / 크기=4 / 크기=5
  1       0       0       0       0

# 2번째 상태
크기=1 / 크기=2 / 크기=3 / 크기=4 / 크기=5
  1       1       0       0       0

...

# 최종!
크기=1 / 크기=2 / 크기=3 / 크기=4 / 크기=5
  8       6       8       4       4

1을 8번 출력하고, 2를 6번 출력하고 ...
이런식으로 출력하면 정렬과 동일한 효과를 얻을 수 있습니다.

- 특징 - 
1. 사용 : 정렬하는 숫자가 특정한 범위 내에 있을 때 사용
2. 장점 : O(n) 의 시간복잡도
3. 단점 : 배열 사이즈 N 만큼 돌 때, 증가시켜주는 Counting 배열의 크기가 큼.
(메모리 낭비가 심함)


# 기수 정렬 - Radix Sort
다르지만 비슷한 알고리즘
데이터를 구성하는 기본 요소 (Radix) 를 이용하여 정렬을 진행하는 방식

장점 : 문자열, 정수 정렬 가능

- 단점 - 
1. 자릿수가 없는 것은 정렬할 수 없음. (부동 소숫점)
2. 중간 결과를 저장할 bucket 공간이 필요함.
'''

data = [1, 3, 2, 4, 3, 2, 5, 3, 1, 2, 3, 4, 4, 3,
        5, 1, 2, 3, 5, 2, 3, 1, 4, 3, 5, 1, 2, 1, 1, 1]
size = len(data)

count = {}

# 개수 세서 dict에 저장하기 !
for i in range(size):
    if data[i] not in count:
        count[data[i]] = 1
    else:
        count[data[i]] += 1

# 키값으로 sort한 후
results = sorted(count.items())

# 출력 !
for result in results:
    for _ in range(result[1]):
        print(f'{result[0]}', end=' ')
print()
