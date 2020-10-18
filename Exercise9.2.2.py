fin = open('words.txt')
for line in fin:
    word = line.strip()
    letter = 'e'
    if letter not in word:
        print(word)
    
