fin = open('words.txt')
total = 0
count = 0

for line in fin:
    word = line.strip()
    letter = 'e'
    total = total + 1
    if letter not in word:
        print(word)
        count = count + 1

print(count/total * 100)


