import sys

def dfs(x, y):
    res = 1
    visited[x][y] = True
    for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
        nx, ny = x + dx, y + dy
        if (nx < 0) or (nx >= n) or (ny < 0) or (ny >= m):
            continue # 범위 N x M 배열 넘는지 확인
        if not(visited[nx][ny] or board[nx][ny]): # 방문 안한 장소 방문
            res += dfs(nx, ny) # dfs를 통해 전파된 바이러스 갯수의 누적 값
    return res 

def solve(start, wall):
    global n, m, numVirus, visited
    if wall == 3:
        count = 0
        visited = [[False] * m for _ in range(n)]
        for x, y in virus:
            count += dfs(x, y)
        numVirus = min(numVirus, count)
        return
    for i in range(start, n * m):
        x = i // m
        y = int(i % m)
        if board[x][y] == 0:
            board[x][y] = 1
            solve(i + 1, wall + 1)
            board[x][y] = 0

n, m = map(int, input().split())
board = [list(map(int, input().split())) for i in range(n)]
visited = [[False] * m for i in range(n)] # 방문여부 표시
virus = [] # 바이러스(2) 위치 배열
numVirus = 9999
safe = -3

for i in range(n):
    for j in range(m):
        if board[i][j] != 1:
            safe += 1
        if board[i][j] == 2:
            virus.append((i, j))
            
solve(0, 0)
print(safe - numVirus)