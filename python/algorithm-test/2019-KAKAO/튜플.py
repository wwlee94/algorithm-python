'''
* 🙆‍♂️ Created by wwlee94 on 2020.05.06
https://programmers.co.kr/learn/courses/30/lessons/64065

2019년 카카오 개발자 겨울 인턴십 LEVEL 2 문제
- 문제 풀이 접근 -
{{2}, {2, 1}, {2, 1, 3}, {2, 1, 3, 4}}
{{2, 1, 3, 4}, {2}, {2, 1, 3}, {2, 1}}
{{1, 2, 3}, {2, 1}, {1, 2, 4, 3}, {2}}
위와 같은 집합의 원소를 (2,1,3,4) 라는 튜플로 바꾸어야 하는 문제이다.
핵심은 길이가 작은 원소부터 돌면서 이전 원소와 set의 '-' 연산을 통해 다음 원소를 하나씩 구해가도록 접근!

1. 가장 먼저, 문제 자체가 string으로 주어졌기 때문에 이를 parsing 해야한다.
2. 정규식과 split을 통해서 원하는 형태로 parsing한 후
3. 해당 원소들을 len을 기준으로 오름차순 정렬 시킨다.
4. 마지막으로 for문을 돌면서 이전 원소와 set의 '-' 연산을 통해 answer에 나온 값을 추가한다.
'''

import re
def solution(s):
    answer = []
    arr = []
    
    s = s.lstrip('{').rstrip('}').split('},{')
    for string in s:
        val = list(map(int, string.split(','))) # 정수형 배열로
        arr.append(val)
    arr.sort(key = len)
    
    answer.append(arr[0][0])
    for i in range(1, len(arr)):
        val = set(arr[i]) - set(arr[i-1])
        answer.append(val.pop()) # set에서 값 하나 가져오기
    return answer