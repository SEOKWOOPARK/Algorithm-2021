import sys
input = sys.stdin.readline

def sharkMove():
    temp = [[0] * C for i in range(R)]
    for i in range(R):
        for j in range(C):
            if g[i][j] != 0:
                x, y, s, d, z = i, j, g[i][j][0], g[i][j][1], g[i][j][2]

                while s > 0: # 상어가 한 번 이동할 때 가는 거리(속도)
                    x += dx[d]
                    y += dy[d]
                    if (0 <= x < R) and (0 <= y < C): # 상어 이동경로가 격자판 범위내 진행
                        s -= 1 # 1칸 움직였으므로 속도 하나 차감
                    else:
                        x -= dx[d] # 격자판 범위 넘을 때 방향 전환
                        y -= dy[d]
                        if d == 0: d = 1
                        elif d == 1: d = 0
                        elif d == 2: d = 3
                        elif d == 3: d = 2
                        # 격자판 벽에 턴하고 방향 반대 전환
                        # 위 <-> 아래, 좌 <-> 우

                if temp[x][y] == 0: # 해당 자리에 상어 없으면 예정된 상어 끌어오기
                    temp[x][y] = [g[i][j][0], d, z]
                else: # 옮기려는 곳에 기존 상어 temp[x][y][0], temp[x][y][1], temp[x][y][2] => s, d ,z 역할
                    if temp[x][y][2] < z: # 상어 중복 때 무거운 개체 픽
                        temp[x][y] = [g[i][j][0], d, z]

    return temp

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

R, C, m = map(int, input().split())
g = [[0] * C for i in range(R)]
result = 0

for i in range(1, m + 1):
    r, c, s, d, z = map(int, input().split())
    g[r - 1][c - 1] = [s, d - 1, z]
    # d -> 위 : 1, 아래 : 2, 우 : 3, 좌 : 4
    # 방향 d를 (d - 1)로 넣은 것은 dx, dy의 인덱스 0 ~ 3으로 맵핑용

for i in range(C): # 낚시꾼은 열 기준 이동
    for j in range(R): # 가장 가까운 행부터 차례로 돌아보기
        if g[j][i] != 0: # 가장 가까운 상어 발견
            result += g[j][i][2]
            g[j][i] = 0 # 가장 가까운 상어 삭제
            break
    g = sharkMove() # 상어 포획 후 이동 및 격자판 갱신

print(result)