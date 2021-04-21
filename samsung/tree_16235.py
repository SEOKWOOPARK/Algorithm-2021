import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())

# N 활용 -> A(영양분), tree 배열 
A = [list(map(int, input().split())) for i in range(N)]
tree = [[[] for _ in range(N)] for _ in range(N)]
ground = [[5] * N for i in range(N)] # 기본 양분 5씩 셋팅

for i in range(M): # 크리티컬한 부분. 나무 나이 대소비교를 위한 장치
    x, y, z = map(int, input().split())
    tree[x - 1][y - 1].append(z) # 나이를 배열에 넣는다

for x in range(K):
    # 봄
    for i in range(N):
        for j in range(N):
            if len(tree[i][j]) <= 0:
                continue
            tree[i][j].sort() # 가장 어린 나무에게 양분 공급용
            idx = 0
            
            while idx < len(tree[i][j]):
                if tree[i][j][idx] <= ground[i][j]:
                    ground[i][j] -= tree[i][j][idx]
                    tree[i][j][idx] += 1 # 트리 나이 한살 먹기
                    idx += 1 # 그 다음 나이 많은 나무로 반복문 진행
                else:
                    die = tree[i][j][idx:] # 양분 부족 -> 못먹은 나무들 
                    for t in die:
                        ground[i][j] += (t // 2)
                    tree[i][j] = tree[i][j][:idx] # 살아 있는 나무만 그 칸에 남긴다.
                    break
    # 가을
    di = [[-1, 0], [0, -1], [1, 0], [0, 1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
    for i in range(N):
        for j in range(N):
            c = 0
            if tree[i][j]: # tree[i][j]번째에 존재하는 모든 나무들 조회
                for now in tree[i][j]:
                    if now % 5 == 0:
                        c += 1
            if c > 0:
                for k in range(8): # 주변 8개 구역 나무 번식 
                    ni = i + di[k][0]
                    nj = j + di[k][1]
                    # 항상 범위, 구역 넘는지 체크하는거 중요
                    if (0 <= ni < N) and (0 <= nj < N):
                        for y in range(c): # 그 자리에 나무기 있는 갯수(m) 만큼 새로운 나무를 추가한다.
                            tree[ni][nj].append(1) # 나이 1살짜리 나무 추가
    # 겨울                            
    for i in range(N):
        for j in range(N):
            ground[i][j] += A[i][j]
            
answer = 0
for i in range(N):
    for j in range(N):
        answer += len(tree[i][j])
        
print(answer)