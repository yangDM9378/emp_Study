def outChess(row, col):
    if 1 <= row <= 8 and 1 <= col <= 8:
        return False
    return True

k_position, r_position, N = input().split()
N = int(N)
k_c = ord(k_position[0]) - ord('A') + 1
k_r = int(k_position[1])
r_c = ord(r_position[0]) - ord('A') + 1
r_r = int(r_position[1])

direct = {"R" : [0, 1], "L" : [0, -1], "B" : [-1, 0], "T" : [1, 0],
          "RT" : [1, 1], "LT" : [1, -1], "RB" : [-1, 1], "LB" : [-1, -1]}

for _ in range(N):
    next_step = input()

    new_r, new_c = direct.get(next_step)
    new_k_r = new_r + k_r
    new_k_c = new_c + k_c

    # 킹이 체스판을 넘어 가는 지?
    if outChess(new_k_r, new_k_c):
        continue

    # 다음 위치에 돌이 있는 지?
    if new_k_r == r_r and new_k_c == r_c:
        new_r_r = r_r + new_r
        new_r_c = r_c + new_c

        # 돌이 체스판을 넘어 가는 지?
        if outChess(new_r_r, new_r_c):
            continue

        r_r, r_c = new_r_r, new_r_c
    
    k_r, k_c = new_k_r, new_k_c
    
print(chr(k_c + 64)+str(k_r))
print(chr(r_c + 64)+str(r_r))
