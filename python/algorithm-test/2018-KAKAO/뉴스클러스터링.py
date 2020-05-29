'''
* 🙆‍♂️ Created by wwlee94 on 2020.05.29
https://programmers.co.kr/learn/courses/30/lessons/17677

- 문제 풀이 방법 -
1. 문자열을 두 글자씩 끊어 다중 집합을 만들어야한다.
2. 다중 집합을 구현하려면 각 두 문자열의 리스트를 다음과 같이 만든다.
   temp = set(set_A | set_B)
   그리하면 두 문자열의 모든 종류가 담긴다.
3. 나온 모든 종류를 순회하며 각 문자열의 개수를 세어 dict로 만든다.
   개수가 작은 것은 추후 교집합이 되고 큰 것은 합집합에 포함된다.
4. 나온 교집합과 합집합을 문제의 조건에 맞게 계산하여 결과를 출력한다.
'''
import re
def solution(str1, str2):
    p = re.compile('[a-z]{2}')
    
    # 문자열을 두 글자씩 끊어 리스트로 만들어주는 메서드
    def multi_set(string):
        leng = len(string)
        string = string.lower()
        i = 0 ; j = 1
        arr = []
        for _ in range(leng-1):
            res = string[i] + string[j]
            if p.match(res):
                arr.append(res)
            i += 1
            j += 1
        return arr
            
    multi_A = multi_set(str1)
    multi_B = multi_set(str2)
    
    # 다중 집합의 교집합
    set_A = set(multi_A)
    set_B = set(multi_B)
    temp = set(set_A | set_B)
    
    inter_dic = {}
    union_dic = {}
    for t in temp:
        a_count = multi_A.count(t)
        b_count = multi_B.count(t)
        _min = min(a_count, b_count)
        _max = max(a_count, b_count)
        inter_dic[t] = _min
        union_dic[t] = _max
    
    # 다중 집합의 교집합
    intersection = []
    for key in inter_dic:
        for i in range(inter_dic[key]):
            intersection.append(key)
    
    # 다중 집합의 합집합
    union = []
    for key in union_dic:
        for i in range(union_dic[key]):
            union.append(key)

    inter_len = len(intersection)
    union_len = len(union)
    answer = 0
    if union_len == 0:
        answer = 1
    elif inter_len == 0:
        answer = 0
    else:
        answer = inter_len / union_len
    return int(answer * 65536)