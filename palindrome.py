def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome('bob'))
print(is_palindrome('sandy'))
print(is_palindrome('apple'))
print(is_palindrome('kayak'))
print(is_palindrome('elephant'))
print(is_palindrome('racecar'))
