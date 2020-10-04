def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome('mom'))
print(is_palindrome('radar'))
print(is_palindrome('higher'))
print(is_palindrome('upper'))
print(is_palindrome('aa'))
print(is_palindrome('p'))
