n, s = map(int, input().split())
t = list(map(int, input().split()))
if t[0] > s:
    print("No")
    exit()
for i in range(1, n):
    if t[i] - t[i - 1] > s:  # 寝るか判定
        print("No")
        exit()  # プログラムを終了
print("Yes")
