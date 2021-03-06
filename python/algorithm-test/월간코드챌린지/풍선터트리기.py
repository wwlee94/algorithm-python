'''
#  이 문제는 접근방식이 필요하는 문제

[left, right] 방식로 2개의 풍선의 기준으로 보았을 때, 제일 왼쪽의 풍선은 마지막까지 남길 수 있다. 마찬가지로 제일 오른쪽의 풍선도 마지막까지 남길 수 있다.
가운데 풍선의 경우, left와 right 중 하나가 되기 위해서는 left, right보다 숫자가 작아야 한다. (숫자가 작아야 마지막까지 남는다)

이 문제의 핵심 아이디어는 다음과 같습니다.
- 어떤 풍선에 대해, 이 풍선이 끝까지 남겨지기 위해서는 이 풍선보다 작은 풍선이 없거나, 혹은 이 풍선의 왼쪽 또는 오른쪽에 해당 풍선보다 더 큰 번호를 가진 풍선만 있어야 합니다.

왜냐하면, 인접한 두 풍선 중에서 번호가 더 작은 풍선을 터트릴 기회는 한 번밖에 없는데, 자기 왼쪽과 오른쪽에 있는 풍선들은 자기 자신이 제거되지 않는 한 서로 만날 일이 없기 때문입니다.

다시 말해, 자기 자신의 위치를 x라고 한다면, 인덱스 구간 [0,x]와 [x,end]에서 a[x]보다 작은 풍선을 최소 1번 이상은 제거해야 하는데, 양쪽 모두에 a[x]
보다 번호가 더 작은 풍선이 있다면, 인접한 두 풍선 중에서 번호가 더 작은 풍선을 터트리는 행위를 최소 2번 이상 해야 한다는 것입니다.

이제 이 핵심 아이디어를 빠르게 구현하기 위해서는 배열 a에 대한 Prefix Min과 Suffix Min을 계산하면 됩니다.
'''

# Set을 통해 left, right보다 작은 숫자를 걸러낸다.
def solution(a):
    _set = set()
    
    _min = a[0]
    for i in range(1, len(a)):
        _set.add(_min)
        _min = min(a[i], _min)
    
    _min = a[-1]
    for i in range(len(a)-1, -1, -1):
        _set.add(_min)
        _min = min(a[i], _min)
    return len(_set)