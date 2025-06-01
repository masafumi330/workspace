
n = int(input())
a = list(map(int, input().split()))
s = set(a)
ans = list(s)
ans.sort()
print(len(ans))
print(*ans)
