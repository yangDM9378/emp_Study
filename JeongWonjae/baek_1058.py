def find_friend(start, current, end):
    for cur_index in range(start + 1, end):
        c = friends[current][cur_index]
        if not visited[cur_index] and c == "Y":
            visited[cur_index] = True
            dist[start] += 1
            find_friend(start, cur_index, end)

N = int(input())

dist = [0] * 10
visited = [False] * 10
friends = []
for i in range(N):
    friends.append(input())

print(friends)
for i in range(N):
    if not visited[i]:
        visited[i] = True
        find_friend(i, i, N)

print(dist)