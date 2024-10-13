from collections import deque

def bfs(n, computers, x):
    computers[x][x] = 0
    queue = deque()
    queue.append(x)

    while queue:
        v = queue.popleft()

        for i in range(n):
            if computers[v][i] == 1:
                queue.append(i)
                computers[v][i] = 0  #방문 처리
                computers[i][v] = 0
                
def solution(n, computers):
    answer = 0
    
    for i in range(n):
        if computers[i][i] == 1:
            bfs(n, computers, i)
            answer += 1
                
    return answer

n = 3
computers = [
    [1,1,0],
    [1,1,1],
    [0,1,1]
]

print(solution(n, computers))