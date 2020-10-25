english_text = 'the report was due the next day but she still chose to procrastinate'
french_text = 'le rapport devait être remis le lendemain mais elle a quand même choisi de tergiverser'
italian_text = 'il rapporto doveva essere consegnato il giorno successivo ma lei scelse comunque di procrastinare'

def most_frequent(text):
    text = text.replace(" ", "")
    dictionary = dict()
    count = 0
    result = []
    for letter in text:
        dictionary[letter] = dictionary.get(letter, 0) + 1
    
    for letter, count in dictionary.items():
        result += [(count, letter)]
    result.sort(reverse=True)

    for count, letter in result:
        print(letter, count)

     
print('English Letter Frequency:')
most_frequent(english_text)
print(" ")


print('French Letter Frequency:')
most_frequent(french_text)
print(" ")

print('Italian Letter Frequency:')
most_frequent(italian_text)
    
