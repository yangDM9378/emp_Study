def find_friend(start, current, end, cnt):
    if cnt == 2:
        return
    for cur_index in range(end):
        if start != cur_index and friends[current][cur_index] == "Y":
            connected[start][cur_index] = 1
            find_friend(start, cur_index, end, cnt + 1)

N = int(input())
connected = [[0] * N for _ in range(N)]
friends = []

for i in range(N):
    friends.append(input())

for i in range(N):
    find_friend(i, i, N, 0)

result = 0

for con in connected:
    result = max(result, sum(con))
    
print(result)