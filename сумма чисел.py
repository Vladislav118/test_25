a = int(input())
b = int(input())


def sum_el(arr):
    total = 0
    for x in arr:
        total += x
    return total


print(sum_el([a, b]))
