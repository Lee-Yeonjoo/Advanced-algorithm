import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]  # 각 인덱스 = 노드 번호(0번 인덱스는 사용x)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)

S, T = map(int, input().split())

visited = [[False] * 2 for _ in range(n+1)]  # 방문 여부 표시를 위한 2차원 리스트 - 0열은 출근길, 1열은 퇴근길 방문 여부

def dfs(node, status, end):
    if len(graph[node]) == 0:
        return
    
    visited[node][status] = True

    if node == end:
        return

    for i in graph[node]:
        if visited[i][status] == False:
            dfs(i, status, end)

dfs(S, 0, T)
dfs(T, 1, S)

cnt = 0
for i in range(1, n+1):
    if visited[i][0] and visited[i][1]:
        cnt += 1

print(cnt-2)