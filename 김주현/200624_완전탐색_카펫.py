def solution(brown, yellow):
    answer = []
    
    # (brown + yellow) = sero * garo
    
    # brown = 2*garo + 2*(sero-2)
    # sero = brown/2-garo+2
    
    for garo in range(3, brown-2):
        if (brown/2 - garo + 2) == (brown + yellow)/garo:
            return [int((brown + yellow)/garo), garo]
        

    return answer
