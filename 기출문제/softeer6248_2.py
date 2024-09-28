import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]  # 각 인덱스 = 노드 번호(0번 인덱스는 사용x)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)

S, T = map(int, input().split())

visited = [0] * (n+1)  # 방문 여부 표시를 위한 리스트

def dfs_from_S(node, end):
    if node == end or len(graph[node]) == 0:
        return
    
    visited[node] = 1

    for i in graph[node]:
        if visited[i] == 0:
            dfs_from_S(i, end)

def dfs_from_T(node, end):
    if node == end or len(graph[node]) == 0:
        return

    if visited[node] == 1:
        visited[node] = 3
    else:
        visited[node] = 2
    
    for i in graph[node]:
        if visited[i] != 2 and visited[i] != 3:
            dfs_from_T(i, end)

dfs_from_S(S, T)
dfs_from_T(T, S)

cnt = 0
for i in range(1, n+1):
    if visited[i] == 3:
        cnt += 1

print(cnt)