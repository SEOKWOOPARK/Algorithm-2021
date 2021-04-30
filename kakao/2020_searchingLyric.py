# 해시로 탐색 시간을 줄여보려 했으나 역부족.
def solution(words, queries):
    answer = []
    dic = {}
    
    for x in range(len(words)):
        length = len(words[x])
        if length not in dic:
            dic[length] = [words[x]]
        elif length in dic:
            dic[length].append(words[x])
    
    for i in range(len(queries)):
        letter = queries[i]
        idx = []
        c = 0
        
        for j in range(len(letter)):
            if letter[j] != '?':
                idx.append(j)
                
        start = idx[0]
        end = idx[-1]
        
        if len(letter) in dic:
            for k in dic[len(letter)]:
                if letter[start : end + 1] == k[start : end + 1]:
                    c += 1
                    
        answer.append(c)
    
    return answer

