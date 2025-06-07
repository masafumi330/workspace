n = int(input())
a = list(map(int, input().split()))
for x in range(n, -1, -1):
    count = 0
    for a_v in a:
        if a_v >= x:
            count += 1
    if count >= x:
        print(x)
        exit()
