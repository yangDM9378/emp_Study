from collections import deque

def bfs(y, x):
    global visited
    q = deque()
    q.append([y, x])
    size = 0
    while q:
        size += 1
        now = q.popleft()
        y, x = now
        dy = [0, 1, 0, -1]
        dx = [1, 0, -1, 0]
        for k in range(4):
            ny, nx = y+dy[k], x+dx[k]
            if ny > N-1 or nx > N-1 or ny < 0 or nx < 0: continue
            if visited[ny][nx] == 1: continue
            if arr[ny][nx]==0: continue
            visited[ny][nx]=1
            q.append([ny, nx])
    return size

N = int(input())
arr = [list(map(int, input()))for _ in range(N)]
visited = [[0]*N for _ in range(N)]
cnt=0
cnt_list = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and visited[i][j] == 0:
            cnt+=1
            visited[i][j] = 1
            cnt_list.append(bfs(i,j))
print(cnt)
sort_cnt_list = sorted(cnt_list)
for z in sort_cnt_list:
    print(z)
