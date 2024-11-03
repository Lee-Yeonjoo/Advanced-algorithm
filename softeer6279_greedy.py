import sys
input = sys.stdin.readline

N, K = map(int, input().split())
str = input().rstrip()

line = []
for i in range(N):
    line.append(str[i])

cnt = 0 
for i in range(N):    #입력받은 배열 탐색
    if line[i] == "P":
        for j in range(i-K, i+K+1):  # K 범위 내의 H를 탐색
            if j < 0 or j >= N:
                continue

            if line[j] == "H":
                line[j] = "X"
                cnt += 1
                break
print(cnt)