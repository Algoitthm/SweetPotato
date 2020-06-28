def solution(begin, target, words):
    # 예외 케이스
    if target not in words:
        return 0
    # 0. list에 시작 단어 및 이동 거리 넣기
    bfs_list = []
    bfs_list.append([begin, 0])
    # 0. list 맨 앞 단어부터 팝 하며 루프
    current_word, count = bfs_list.pop(0)
    visited_word = []

    while(current_word != target):
        # 1. 반문하지 않은 words 중에 이동 가능한 단어 찾기
        for word in words:
            if word not in visited_word and is_possible(current_word, word):
                bfs_list.append([word, count+1])
                visited_word.append(word)
        if bfs_list:
            current_word, count = bfs_list.pop(0)
        else:
            return 0
    return count

def is_possible(word1, word2):
    flg = 0
    for i, j in zip(word1, word2):
        if i == j:
            continue
        else:
            flg += 1
    if flg > 1:
        return False
    else:
        return True


if __name__ == "__main__":
    solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) # 4