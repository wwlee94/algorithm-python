'''
* 🤷‍♂️ Created by wwlee94 on 2020.04.07
https://programmers.co.kr/learn/courses/30/lessons/49993
# 프로그래머스 LV2

- 문제 풀이 접근 -
1. 각 스킬의 위치를 찾는다.
2. 만약 스킬이 없으면 스킬 길이의 제한값인 26보다 큰 수로 넣어준다.
3. 해당 스킬 순서의 배열이 정렬되어 있으면 가능한 스킬트리 정렬이 안되어 있으면 불가능한 스킬트리이다.
'''
def solution(skill, skill_trees): 
    answer = 0 
    for skill_tree in skill_trees: 
        pre_idx = [] 
        for i in range(len(skill)): 
            if skill_tree.find(skill[i]) == -1: 
                pre_idx.append(30) # 핵심 1
            else: 
                pre_idx.append(skill_tree.find(skill[i])) 

        if sorted(pre_idx) == pre_idx: # 핵심 2
            answer += 1 
    return answer