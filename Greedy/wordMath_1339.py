import sys

input = sys.stdin.readline
n = int(input())
word = []
dic = {}

for i in range(n):
    word.append(list(input()))

for i in range(len(word)):
    for j in range(len(word[i])):
        if word[i][j] not in dic:
            dic[word[i][j]] = pow(10, len(word[i])-j-1)
            # dic에 없으면 해당 자릿수에 해당하는만큼 pow(10, x)로 등록
        else:
            dic[word[i][j]] += pow(10, len(word[i][j])-j-1)
			# 기존 dic에 있으면 해당 자릿수만큼 pow(10, x)로 누적

sortedList = sorted(dic.items(), key = lambda x: x[1], reverse = True)
result, num = 0, 9

for i in sortedList:
    result += (num * i[1])
    # result에 자릿수 내림차순으로 정렬된 값들을 9부터 맵핑시킨다.
    num -= 1

print(result)

