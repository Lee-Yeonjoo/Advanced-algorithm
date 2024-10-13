from collections import deque

def bfs(n, computers, x, visited):
    visited[x] = True  #시작 노드 방문처리
    queue = deque()
    queue.append(x)  #큐에 시작노드 넣기

    while queue:
        v = queue.popleft()  #큐에서 제일 앞의 노드 pop

        for i in range(n):   #v의 이웃 노드에 대해 반복
            if computers[v][i] == 1 and visited[i] == False:
                queue.append(i)  
                visited[i] = True  #이웃 노드 방문 처리

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for i in range(n):
        if visited[i] == False:
            bfs(n, computers, i, visited)
            answer += 1

    return answer

n = 3
computers = [
    [1,1,0],
    [1,1,1],
    [0,1,1]
]

print(solution(n, computers))