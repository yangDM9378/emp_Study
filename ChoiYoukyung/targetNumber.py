# dfs
def solution(numbers, target):
    answer = 0
    n = len(numbers)
    queue = [[numbers[0], 0], [-1*numbers[0], 0]]
    while queue:
        tmp, idx = queue.pop()
        idx += 1
        if idx < n:
            queue.append([tmp+numbers[idx], idx])
            queue.append([tmp-numbers[idx], idx])
        else:
            if tmp == target:
                answer += 1
    return answer

# bfs
from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque()
    n = len(numbers)
    queue.append([numbers[0], 0])
    queue.append([-1*numbers[0], 0])
    while queue:
        tmp, idx = queue.popleft()
        idx += 1
        if idx < n :
            queue.append([tmp+numbers[idx], idx])
            queue.append([tmp-numbers[idx], idx])
        else:
            if tmp == target:
                answer += 1
    return answer