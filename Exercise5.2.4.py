def check_fermat(a, b, c, n):
    if n <= 2:
        print("The value of n must be greater than 2")
    else:
        if a**n + b**n == c**n:
            print("Holy smokes, Fermat was wrong!")
        else:
            print("No, that doesn't work.")


def user_input():
    """ Asks for user input for variables a, b, c, and n."""
    a = int(input("Enter a value for variable a: "))
    b = int(input("Enter a value for variable b: "))
    c = int(input("Enter a value for variable c: "))
    n = int(input("Enter a value greater than 2 for variable n: "))
    check_fermat(a, b, c, n)

user_input()
