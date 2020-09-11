'''
* 🙆‍♂️ Created by wwlee94 on 2020.09.11
https://programmers.co.kr/learn/courses/30/lessons/12938

# 프로그래머스 LV3

- 문제 접근 방식 -
곱이 최대인 경우를 생각해보면 (각 원소의 차이가 가장 적은 경우를 뜻함)
차이가 가장 적은 경우를 구하려면 -> 구하고자 하는 합(s), 개수(n)에서 나눈 몫을 계속 구하면 됨

Tip: divmod(a,b) -> (a//b, a%b) 로 한번에 반환해줌
'''
def solution(n, s):
    answer = []
    
    if n > s: return [-1] # 최고의 집합이 존재하지 않는 경우
    
    while n != 0:
        q, r = divmod(s, n)
        answer.append(q)
        s -= q
        n -= 1
    return sorted(answer)