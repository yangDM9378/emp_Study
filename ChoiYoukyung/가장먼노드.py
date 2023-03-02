from collections import deque
def solution(n, edge):
    g = [[] for _ in range(n+1)]
    for e in edge:
        n1, n2 = e[0], e[1]
        g[n1].append(n2)
        g[n2].append(n1)
    visited = [0] * (n+1)
    q = deque([1])
    visited[1] = 1    
    while q:
        x = q.popleft()
        for y in g[x]:
            if not visited[y]:
                q.append(y)
                visited[y] = visited[x]+1
    maxV = max(visited)
    print(maxV)
    answer = visited.count(maxV)
    return answer