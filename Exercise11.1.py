fin = open('words.txt')
w_dict = dict()
count = 0

for line in fin:
    word = line.strip()
    w_dict[word] = count + 1

if 'aba' in w_dict:
    print(True)



