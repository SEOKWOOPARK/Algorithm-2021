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
    # wordList를 list(set[])으로 선언한 이유
    # maxValue의 인덱스 값으로 wordList에서 바로 해당 글자를 조회할 수 있다.

