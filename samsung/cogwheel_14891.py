import sys
from collections import deque

def checkRight(start, dirs):
    # start가 범위를 넘어서거나 마지막 톱니바퀴인데 3번째 톱니랑 접점 극이 같을 때
    if (start > 4) or gears[start - 1][2] == gears[start][6]: 
        return
    
    if gears[start - 1][2] != gears[start][6]:
        checkRight(start + 1, -dirs)
        gears[start].rotate(dirs)
        
def checkLeft(start, dirs):
    if start < 1 or gears[start][2] == gears[start + 1][6]:
        return # 가장 왼쪽 톱니 바퀴이거나 오른쪽 톱니바퀴와 맞닿는 부분의 극이 같을 때
    
    if gears[start + 1][6] != gears[start][2]:
        checkLeft(start - 1, -dirs) # 왼쪽 톱니 체크할 때 현 톱니의 반대 방향으로 회전
        gears[start].rotate(dirs) # 넘겨 받은 dirs로 rotate 메서드 회전한다.
        
gears = {}

for i in range(1, 5): # 4개 톱니바퀴 상태
    gears[i] = deque(list(map(int, list(sys.stdin.readline().replace("\n", "")))))
    # gears[i] = deque([1, 0, 1, 0, 1, 1, 1, 1]), gears[i + 1] = ...
    # gears = {i : deque([1, 0, 1, 0, 1, 1, 1, 1]), ...}
n = int(sys.stdin.readline())

for i in range(n):
    num, dirs = map(int, sys.stdin.readline().split())
    checkRight(num + 1, -dirs)
    checkLeft(num - 1, -dirs)
    gears[num].rotate(dirs)
    
result = 0
for i in range(4):
    result += (2 ** i) * gears[i + 1][0] 
    # 인덱스 0번째가 12시 방향
    # 인덱스 커질수록 1, 2, 4, 8처럼 2배 지수
print(result)
