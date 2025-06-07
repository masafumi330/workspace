n = int(input())
t = list(input())
a = list(input())
for i in range(n):
    if t[i] == "o" and a[i] == "o":
        print("Yes")
        exit()

print("No")
