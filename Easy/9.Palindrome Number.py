# Scrieti o functie care primeste ca si parametru un numar x si returneaza true daca acesta este palindrom
# in caz contrar returneaza false

# ex1: Input: 121 -> Output: true
# ex2: Input: -121 -> Output: false
# ex3: Input: 10 -> Output: false

def is_palindrome(x):
    str_x = str(x)
    reversed_str = ''

    if x < 0:
        return False

    for i in range(len(str_x)):
        reversed_str = str(str_x[i]) + reversed_str

    reversed_int = int(reversed_str)
    if reversed_int == x:
        return True
    else:
        return False


output = is_palindrome(121)
print(output)