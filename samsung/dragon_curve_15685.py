import sys

input = sys.stdin.readline
dx = [0, -1, 0, 1] # 남, 서, 북, 동 방향
dy = [1, 0, -1, 0] # dx, dy => 시작방향 0(x+), 1(y-), 2(x-), 3(y+) 표현
n = int(input())
s = [[0] * 101 for i in range(101)] # s는 100 x 100 격자판
result = 0

for i in range(n): # 방향 0, 1, 2, 3 => 동, 북, 서, 남
    y, x, d, g = map(int, input().split()) # y:행, x:열, d: 시작방향, g: 진행할 목표 세대
    s[x][y] = 1 # 시작점 채우고 시작
    points = [d] # 점들의 방향 배열. 초기화
    directions = [d] # 각 세대의 방향. 초기화
    for j in range(g + 1): # 0부터 g세대까지 반복문
        for k in directions:
            x += dx[k]
            y += dy[k]
            s[x][y] = 1 # s[column][row] 꼴
        # 다음 j를 위한 방향 갱신
        directions = [(p + 1) % 4 for p in points] # 점들로 이루어진 각 선분의 이동방향 배열
        directions.reverse() # 이동방향 배열 뒤집기(핵심 규칙성)
        points = points + directions # 지나온 각 점의 좌표 누적

for i in range(100):
    for j in range(100):
        if s[i][j] and s[i][j + 1] and s[i + 1][j] and s[i + 1][j + 1]:
            result += 1

print(result)