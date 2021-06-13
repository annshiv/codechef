max_score = 1000000
MOD = 1000000009
s_history = [0] * (max_score + 1)

s_history[2] = 1
s_history[3] = 1
for score in range(4, max_score + 1):
    s_history[score] = (s_history[score - 2] + s_history[score - 3]) % MOD

for _ in range(int(input())):
    print(s_history[int(input())])
