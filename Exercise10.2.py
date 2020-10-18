t = [1, 2, 3]
def cumsum(t):
    total = 0
    for elem in t:
        total = total + elem
        print(total)
        
cumsum(t)
