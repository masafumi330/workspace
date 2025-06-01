n, m = map(int, input().split())
guarded = {i: [] for i in range(1, n + 1)}
for i in range(1, m+1):
    l, r = map(int, input().split())
    for j in range(l, r + 1):
        guarded[j].append(i)
min_len = min(len(v) for v in guarded.values())
print(min_len)
