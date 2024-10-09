def max_of(a):
    maximum = a[0]
    max_turn = 0

    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]
            max_turn = i
    return maximum, max_turn+1

n = [int(input()) for _ in range(9)]

maximum, max_turn = max_of(n)
print(f"{maximum}")
print(f"{max_turn}")