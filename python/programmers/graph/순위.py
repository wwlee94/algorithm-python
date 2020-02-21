'''
* 🙆‍♂️ Created by wwlee94 on 2020.02.16
https://programmers.co.kr/learn/courses/30/lessons/49191

- 문제 풀이 접근 -
([A, B]는 A 선수가 B 선수를 이겼다는 의미 == [B, A]는 A 선수가 B 선수에게 졌다는 의미) -> 그래프에서 간선이 존재 한다는 의미 
따라서 이 문제에서 승자와 패자로 나눈다면 A->B가 1(승자)이라면, B->A는 -1(패자)라고 인접 행렬을 만들 수 있다.
여기서 끝나는 것이 아니라 만약 [A, B], [B, C]라면 A->C 도 성립 해야하기 때문에 'B'를 거쳐서 가는 경우도 고려 해주어야한다. (플로이드)

기존의 인접 행렬에서 각각의 노드를 거쳐가는 경우를 모두 갱신해주면 끝 ! 
Tip: 방향이 존재한다고 가정하고 진행해야한다. -> 특정 정점을 거쳐간다면([i][k] -> [k][j]) 각각의 값이 1인 상태이어야 거쳐갈 수 있다는 뜻 ([i][k] + [k][j] == 2)
score[i][j] == 0 -> 이 문제는 승자가 패자로 바뀌는 경우는 없으니 0인 부분만 위의 조건을 확인해주면 끝 !
'''
def solution(n, results):
    answer = 0
    score = [[0 for _ in range(n)] for _ in range(n)]
    for r in results:
        score[r[0]-1][r[1]-1] = 1
        score[r[1]-1][r[0]-1] = -1
        
    # k: 거쳐가는 노드
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i==j: score[i][j] = 9999
                if score[i][j] == 0 and score[i][k] + score[k][j] == 2: # 1이 이동 할 수 있는 표시
                    score[i][j] = 1 # i->j 이김
                    score[j][i] = -1 # j->i 짐

    answer = list(map(lambda x: True if 0 not in x else False, score)).count(True) # 0: 빠진 정보 -> 빠진 정보가 있는건 False, 모든 정보가 있다면 True
    return answer