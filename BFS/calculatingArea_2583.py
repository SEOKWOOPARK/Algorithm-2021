from collections import deque

def bfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    count = 1

    queue = deque()
    queue.append((x, y))

    graph[x][y] = 1

    while queue:
        now = queue.popleft()

        for i in range(4):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]

            if (0 <= nx < M) and (0 <= ny < N):
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    queue.append((nx, ny))
                    count += 1
    return count

M, N, K = map(int, input().split())
graph = [[0] * N for _ in range(M)]
result = []
total = 0

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            total += 1
            result.append(bfs(i, j))  

result.sort()
print(total)
print(*result)

