def solution(numbers):
    answer = ''
    s_numbers = []
    for num in numbers:
        s_numbers.append(str(num))
    
    # print(s_numbers)
    # for s in s_numbers:
    #     print(s*3)
        
    s_numbers.sort(key=lambda x: x*3, reverse=True)
    
    # print(s_numbers)
    # for s in s_numbers:
    #     print(s*3)

    return str(int(''.join(s_numbers)))
