# combinations 라이브러리 간단한 예제
from itertools import combinations

li = ["a", "b", "c", "d", "e"]
comb = combinations(li, 3)

for c in comb:
    print(c)

# ('a', 'b', 'c')
# ('a', 'b', 'd')
# ('a', 'b', 'e')
# ('a', 'c', 'd')
# ('a', 'c', 'e')
# ('a', 'd', 'e')
# ('b', 'c', 'd')
# ('b', 'c', 'e')
# ('b', 'd', 'e')
# ('c', 'd', 'e')
# combinations은 조합이기 때문에 주어진 튜플이나 배열의 원소들의 인덱스 순서(오름차순)를 지킨 상태로 
# 주어진 갯수의 케이스를 뽑아준다.

# ----------------------------------------------------------

import sys
from itertools import combinations

input = sys.stdin.readline
vowels = ['a', 'e', 'i', 'o', 'u']
L, C = map(int, input().split())
password = sorted(list(map(str, input().split())))
comb = combinations(password, L)

for c in comb: # 생성된 조합 단어에서 한 글자씩 방문
    counting = 0 # 모음 갯수를 세기 위한 장치
    for letter in c:
        if letter in vowels:
            counting += 1

    if (counting >= 1) and (counting <= L - 2): 
        # 자음이 최소 2개 있어야 하므로 L개 중에서 모음은 최소 1개고 최대 L - 2개.
        print(''.join(c))

