def my_div(a):
    sup = 0
    for i in range(a // 2, 0, -1):
        if a % i == 0:
            sup = i
            break
    if sup != 1:
        return sup
    else:
        return a


a = int(input())
b = my_div(a)
print(b)
