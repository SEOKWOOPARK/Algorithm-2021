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

# -------------------------------------------------------

from collections import defaultdict

# Trie 자료구조안에 위치하고 있는 노드 정의
class Node(object):
    def __init__(self, key, passnumber=None, isEnd=None):
        self.key = key
        # 해당 노드를 지나간 길이 별 단어 갯수
        self.passnumber = defaultdict(int)  
        self.isEnd = False
        self.children = {}

# Trie(문자열 + 트리) 자료구조 활용
class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curNode = self.head
        curNode.passnumber[len(string)] += 1
        for char in string:
            if char not in curNode.children:
                curNode.children[char] = Node(char)

            curNode = curNode.children[char]
            curNode.passnumber[len(string)] += 1

        curNode.isEnd = True

    def search(self, query):
        curNode = self.head
        for q in query:
            if q == "?":
                break
            if q in curNode.children:
                curNode = curNode.children[q]
            else:
                return 0

        return curNode.passnumber[len(query)]


def solution(words, queries):
    trie = Trie()
    r_trie = Trie()
    r_words = [w[::-1] for w in words]
    dic = {}
    answer = []

    for word in words:
        trie.insert(word)
    for word in r_words:
        r_trie.insert(word)
    for query in queries:
        if query in dic:
            answer.append(dic[query])
            continue
        if query.endswith("?"):
            result = trie.search(query)
            answer.append(result)
            dic["query"] = result

        else:
            result = r_trie.search(query[::-1])
            answer.append(result)
            dic["query"] = result

    return answer