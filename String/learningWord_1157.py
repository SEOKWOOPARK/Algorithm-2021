word = input().lower() # 모두 소문자로 통일
wordList = list(set(word)) # set => 중복없이 문자마다 1번씩 뽑는다
wordCount = [] # 문자별 빈도 체크 용도

for i in wordList:
	counting = word.count(i) 
	wordCount.append(counting) # 해당 문자가 몇 번 나왔는지만 push

maxValue = max(wordCount) # 빈도 중 최대값 

if wordCount.count(maxValue) >= 2: 
	print('?') # 최대값이 2개 이상이면 '?'
else:
	answer = wordCount.index(maxValue)
	print(wordList[answer].upper())

