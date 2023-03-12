def solution(n, m, section):
    answer = 0

    walls = [0] * (n + 1)
    
    for s in section:
        walls[s] = 1
    
    index = 1
    while index <= n:
        if walls[index]:
            index += m
            answer += 1
        else:
            index += 1
            
        
    
    return answer