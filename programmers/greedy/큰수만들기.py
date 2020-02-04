'''
* 🤷‍♂️ Created by wwlee94 on 2020.02.03

- 문제 풀이 접근 - 
    number      k
EX) '1924'      2 -> 10의 자리수는 1,9,2 중 가장 큰 값임 -> 9가 가장 크므로 9를 선택 ! -> 1의 자리수는 선택도니 9 이후 숫자인 2, 4 중 하나 ! -> 4를 선택 ! => '94'
첫 자리수 == 가장 큰 자리수를 구하는 법은 (0 ~ k+1) 사이 수들 중 하나
일반화하면 (idx ~ k+1+i) -> idx는 각 자리수로 선택된 숫자의 index

TIP) '99999999999' 인 경우 각 자리수의 최대값은 9보다 클 수 없으니 값이 9가 나오면 바로 그 수를 선택하도록해야 효율성 테스트 패스 가능
'''
def solution(number, k):
    answer = ''
    l = len(number) - k
    idx = 0
    
    for i in range(l):
        _max = '-99'
        max_idx = -1
        for j in range(idx, k+1+i):
            if _max < number[j]: 
                _max = number[j]
                max_idx = j
            if _max == '9': break # 매우 중요 !
        
        idx = max_idx + 1
        # number = number.replace(_max, ' ', 1)
        answer += _max
    return answer