import collections

def solution(participant, completion):
    answer = ''
    answer = collections.Counter(participant) - collections.Counter(completion)
    
    return list(answer.keys())[0]