import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

# 입력
n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]
adjR = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adjR[y].append(x)
s, t = map(int, input().split())

# dfs함수
def dfs(now, adj, visit):
    if visit[now] == 1:
        return
    
    visit[now] = 1

    for i in adj[now]:
        dfs(i, adj, visit)

fromS = [0] * (n+1)
fromS[t] = 1
dfs(s, adj, fromS)

fromT = [0] * (n+1)
fromT[s] = 1
dfs(t, adj, fromT)

toS = [0] * (n+1)
dfs(s, adjR, toS)

toT = [0] * (n+1)
dfs(t, adjR, toT)

cnt = 0
for i in range(1, n+1):
    if fromS[i] and fromT[i] and toS[i] and toT[i]:
        cnt += 1
print(cnt-2)