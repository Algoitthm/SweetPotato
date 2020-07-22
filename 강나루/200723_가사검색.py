#####
## KAKAO BLIND RECRUITMENT :: 가사검색
####

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

### 1단계(나루풀이) :: 원시적으로 3중 포문을 썼음. 근데 이렇게 풀면 효율성 테스트 통과못함.
# 더 간단하게 풀 수 있는 방법은 찾아봐야 함!
for i in range(0, len(queries)): ####  i : Query 단위
    query = queries[i]
    result = []

    for j in range(0, len(words)):   #### j : Word 단위
        word = words[j]
        check_list_1 = []        # word 단위로 매치가능한지 여부 List

        if len(word) == len(query):
            check_list_2 = []  # letter 단위로 매치하는지 여부 List

            ##  Step1) word -- query 일치여부 확인
            for k in range(0, len(word)): #### k : Letter 단위
                if query[k] == "?":
                    check_list_2.append(True)
                    print(word[k], check_list_2)
                else:
                    check_list_2.append(word[k] == query[k])
                    print(word[k], check_list_2)

            ## Step2) 일치 여부 확인해서 모두 일치하면 True라고 넣고, 아니면 False라고 넣음
            if sum(check_list_2) == len(word):
                check_list_1.append(True)
            else:
                check_list_1.append(False)
            print(i, "/", j, ":", check_list_1)

        else:  # 길이가 다르면 걍 False 로 추가
            check_list_1.append(False)
            print(i, "/", j, ":", check_list_1)
    result.append(sum(check_list_1))

print(result)

### 2단계 :: Trie 구조로 푸는방법.. ( 아래는 나루코드 아님 주의.. 코드를 이해해보려고 노력해볼 것))

class Node:
    def __init__(self, w = ""):
        self.word = w
        self.cList = {}#자식 노드를 저장한 사전
        self.length = 0

class Trie:
    def __init__(self):
        self.root = Node("")
        self.keyList = {}#이미 입력된 단어와 그 길이를 저장한 사전(중복 검색 방지)

    def create(self, words, reverse = False):#단어들을 받아 Trie 구축, reverse가 True인 경우 단어들을 뒤집음
        for word in words:
            if(reverse):
                word = word[::-1]
            if(word not in self.keyList):
                self.keyList[word] = len(word)
                cur_node = self.root
                for w in word:
                    if(w not in cur_node.cList):
                        cur_node.cList[w] = Node(w)
                    cur_node = cur_node.cList[w]
                cur_node.length = len(word)

    def search(self, word):
        num = 0#매칭되는 단어의 개수
        cur_node = self.root
        for w in word:
            if(w not in cur_node.cList):
                if(w == '?'):#현재 문자가 '?'인 경우
                    stack = []#DFS를 위한 스택
                    l = len(word)
                    nQ = word.count("?")#검색 키워드에서 ?의 개수
                    if(nQ == l):#검색 키워드가 모두 '?'로 이루어진 경우
                        for i in self.keyList.values():
                            if(i == l):
                                num += 1
                        break
                    for node in cur_node.cList.values():#현재 노드의 자식 노드를 스택에 삽입
                        stack.append((node, 1))#스택(노드, 깊이)
                    while(stack):
                        cur_node, cur_depth = stack.pop()#cur_depth: 현재 노드의 깊이
                        if(cur_node.length == len(word) and cur_depth == nQ):
                            num+=1#현재 노드가 단어의 끝을 나타내는 노드, 깊이가 ?의 개수와 같음 => 매칭
                        if(cur_depth < nQ):#현재 깊이가 ?의 개수보다 적은 경우
                            for node in cur_node.cList.values():
                                stack.append((node, cur_depth+1))
                    break
                else:
                    break
            cur_node = cur_node.cList[w]
        return num

def solution(words, queries):
    answer = []
    dic = {}
    trie = Trie()#정상 Trie
    trie.create(words, False)
    r_trie = Trie()#뒤집은 Trie
    r_trie.create(words, True)
    for q in queries:
        if(q not in dic):
            if(q.startswith('?')):
                answer.append(r_trie.search(q[::-1]))
            else:
                answer.append(trie.search(q))
            dic[q] = answer[-1]
        else:
            answer.append(dic[q])
    return answer
