a = int(input())
b = int(input())
for i in range(a, b + 1):
    x = i // 1000
    y = i // 100 % 10
    z = i // 10 % 10
    p = i % 10
    if x == p and y == z:
        print(i)
