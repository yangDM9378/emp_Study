A, B = map(int, input().split())

prime = [False] + [True] * B
prime[1] = False

end = int(B * 0.5)
for i in range(2, end+1):
    if prime[i]:
        for j in range(i+i, B+1, i):
            prime[j] = False

dp = [0] * (B+1)

for i in range(2, B+1):
    if prime[i]:
        dp[i] = 1

for i in range(2, B+1):
    for j in range(2, B+1):
        if i * j > B:
            break
        dp[i*j] = dp[i] + 1

answer = 0
for i in range(A, B+1):
    if prime[dp[i]] :
        answer += 1
        
print(answer)