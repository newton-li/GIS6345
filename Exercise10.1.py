t = [[1, 2], [3], [4, 5, 6]]
def nested_sum(t):
    total = 0
    for elem in t:
        total = total + sum(elem)
    print(total)

nested_sum(t)
