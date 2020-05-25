'''
* 🙆‍♂️ Created by wwlee94 on 2020.05.25
https://programmers.co.kr/learn/courses/30/lessons/12980

- 문제 풀이 접근 -
문제를 유심히 보고 생각해보니 아래와 같은 결과를 얻을 수 있었다.
1. 2의 제곱근에 해당되는 수의 결과는 무조건 1이 나온다.
2. 수를 2로 나누어 0 또는 1이 될때까지 수를 나눈다.
    단, 홀수에서 나눌경우 (기존 수 - 1)을 해주고 -> 다시 짝수로 만들어버림
    (점프수 + 1)을 해준다. -> 해당 경우에 점프를 했으니 + 1
'''

def solution(n):
    answer = 1
    # 2의 제곱수이면 바로 1반환
    if not (n & (n - 1)):
        return answer
    
    while 1:
        if n == 0 or n == 1:
            break
        # 홀수
        if n % 2 != 0:
            n -= 1
            answer += 1
        n = n // 2
    
    return answer

# 더 개선된 풀이
def solution(n):
    return list(bin(n)).count('1')