'''
* 🤷‍♂️ Created by wwlee94 on 2020.02.01
- 문제 풀이 접근 - 
4자리 수를 만들 때, 그 수를 반복시켜 만든다

[EX]
# ex1. [6, 10, 2] # l = [[66666, '6'], [10101, '10'], [22222, '2']] 
# ex2. [3, 30, 34, 5, 9] # l = [[33333, '3'], [30303, '30'], [34343, '34'], [55555, '5'], [99999, '9']]

* 이러한 원리로 문제 접근 -> 풀이는 위와 정확히 일치하진 않음 풀이는 아래와 같은 원리
문자열 비교연산의 경우엔 첫번째 인덱스인 666[0]인 6과 101010[0]인 1과 222[0]인 2를 ascii숫자로 바꿔서 비교합니다. 물론 같으면, 다음 인덱스도 비교합니다. 비교한 결과 [6, 2, 10]의 순으로 정렬
단, n = [0,0,0,0]이면 0000이 아니라 0으로 출력해야함
'''

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True) # EX) '5'*3 -> '555'
    return str(int(''.join(numbers)))


# 2020.07.14
def solution(numbers):
    if sum(numbers) == 0: return '0'
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x:x*3, reverse=True)
    return ''.join(numbers)