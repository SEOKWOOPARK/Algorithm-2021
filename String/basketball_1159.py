import sys

N = int(sys.stdin.readline())
words = []
alphabet = set([])
counting = []

for i in range(N):
    a = input()
    words.append(a[0]) # 빈도수까지 고려한다.
    alphabet.add(a[0]) # 성의 첫 글자 종류만 고려한다.

for i in alphabet: 
    c = words.count(i) # 문자별 빈도 체크
    if c >= 5:
        counting.append(i) # 5개 이상이면 해당 문자 push

counting.sort() # 사전순 출력

if len(counting):
    print(''.join(counting))
else:
    print('PREDAJA')
