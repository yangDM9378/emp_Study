N = int(input())

friends = []
for i in range(N):
    friends.append(input())

connected = [[0] * N for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if friends[i][j] == "Y" or (friends[i][k] == "Y" and friends[k][j] == "Y"):
                connected[i][j] = 1

result = 0

for con in connected:
    result = max(sum(con), result)

print(result)