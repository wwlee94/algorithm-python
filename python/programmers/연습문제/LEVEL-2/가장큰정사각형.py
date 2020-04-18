'''
* 🤷‍♂️ Created by wwlee94 on 2020.04.17
https://programmers.co.kr/learn/courses/30/lessons/12905
# 프로그래머스 LV2

- 문제 풀이 접근 -
이 문제를 완전 탐색(Brute-force)으로 푼다고 생각해보면 
board의 모든 인덱스를 확인해야하고, 정사각형이 가장 작은 1부터 최대 크기의 정사각형까지 확인하게 된다면 시간 복잡도는 O(n^3)이 되어 시간 초과
따라서, 주어진 문제를 여러 개의 부분 문제로 나누어 푼 뒤, 그 결과를 토대로 주어진 문제를 푸는 DP 알고리즘을 사용해야함
문제를 나누어서 푼다는 점에서 분할 정복과 비슷하지만, 한 가지 다른 점이 있음
분할 정복은 문제를 분할 했을 때 겹치는 문제가 발생하지 않지만, DP는 겹치는 문제가 발생함 
따라서, DP에서는 메모이제이션(memoization)이라는 기법을 통해 반복으로 인한 계산을 줄여주는 과정이 추가적으로 필요합니다.

'''

def solution(board):
    height = len(board)
    width = len(board[0])
    for x in range(1,height):
        for y in range(1,width):
            if board[x][y] == 1:
                board[x][y] = min(board[x-1][y-1], min(board[x-1][y], board[x][y-1])) + 1
    return max([item for row in board for item in row])**2 # board의 모든 요소 중 최대값

# 풀이 2
# def solution(board):
#     r = 0 # 사각형의 한 변의 길이 r
#     for i in range(len(board)):
#         for j in range(len(board[0])):
#             if board[i][j]:
#                 are = min(board[i-1][j-1], board[i-1][j], board[i][j-1])
#                 if are and i and j: # 세점이 1이상이면
#                     board[i][j] = are + 1 # 가장 작은 수 + 1
#                 if board[i][j] > r: # r보다 큰 수 있으면
#                     r = board[i][j] # 갱신
#     return r*r