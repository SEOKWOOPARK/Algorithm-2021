import sys

N = int(sys.stdin.readline())
words = []

for i in range(N):
    word = input().strip()
    length = len(word)
    words.append((word, length)) # 튜플로 단어, 단어 길이 순으로 넣어준다.

words = list(set(words)) # set => 중복 없애기, list => 정렬 용도
words.sort(key = lambda x: (x[1], x[0])) 
# x[1] => 길이 정렬, x[0] => 길이가 같을 땐 단어를 사전순 정렬

for i in range(len(words)):
    print(words[i][0])
