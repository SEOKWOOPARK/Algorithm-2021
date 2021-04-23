from collections import deque
import sys

def change(d, c): # d -> 방향, c -> times = {X : C} 구조에서 C(방향)
    if c == "L": # 왼쪽 회전(시계방향 90도, 상 -> 좌 -> 하 -> 우)
        d = (d - 1) % 4
    else: # 오른쪽 회전(반시계 90도, 상 -> 우 -> 하 -> 좌)
        d = (d + 1) % 4
    return d

dy = [-1, 0, 1, 0] # 상 우 하 좌
dx = [0, 1, 0, -1]

def start():
    direction = 1 #초기 방향
    time = 1 # 시간
    y, x = 0, 0 # 문제에서 뱀 위치 초기화 상단 맨좌측
    visited = deque([[y, x]])
    arr[y][x] = 2 # 방문한 좌표는 2
    
    while True:
        y, x = y + dy[direction], x + dx[direction]
        if (0 <= y < N) and (0 <= x < N) and (arr[y][x] != 2):
            if not arr[y][x] == 1: # 사과 없어서 몸통 길이 유지할 때
                tempY, tempX = visited.popleft() # 가장 처음에 추가된 좌표 -> 뱀 꼬리
                arr[tempY][tempX] = 0 # 꼬리 있던 자리 비워주기
            arr[y][x] = 2 # 여기서 y,x는 while문의 이동 갱신된 y, x
            visited.append([y, x]) # 뱀 머리추가
            if time in times.keys():
                direction = change(direction, times[time])
            time += 1 
            # time이 1씩 커지다가 주어진 X가 times의 key값과 일치할 때 위의 if문을 따른다.
        else: # 벽이나 같은 몸통끼리 부딪힌 경우
            return time 

N = int(input())
K = int(input())
arr = [[0] * N for _ in range(N)]

for i in range(K):
    a, b = map(int, input().split())
    arr[a - 1][b - 1] = 1 # 주어진 사과 위치 설정

L = int(input())
times = {}

for i in range(L):
    X, C = input().split()
    times[int(X)] = C
    
print(start())