def sum_of_digits(num):
    sum = 0
    while num > 0:
        digit = num % 10
        sum += digit
        num /= 10
    return sum

def to_digits(num):
    lst = [None] * 100
    count = 0
    while num > 0:
        digit = num % 10
        lst[count] = digit
        count += 1
        num /= 10
    return lst


def to_number(digits):
    step = 1
    num = 0
    for i in range(0, len(digits)):
        digit = digit[i]
        num += step*digit
        step *= 10
    return num


def count_vowels(str):
    str = str.lower()
    count = 0
    for i in range(0, len(str)+1):
        digit = str % 10
        # check if digit is vowel
        if is_vowel(digit):
            count += 1
        str /= 10
    return count

def is_vowel(char):
    if char == "a":
        return True
    elif char == "e":
        return True
    elif char == "i":
        return True
    elif char == "o":
        return True
    elif char == "y":
        return True
    elif char == "u":
        return True
    else:
        if char < "a":
            print(char)
            return True
        elif char > "z":
            print(char)
            return True
        else:
            return False

def count_consonants(str):
    count = 0
    str = str.lower()
    for i in range(0, len(str)):
        letter = str[i]
        if is_vowel(letter) == False:
            count += 1
    return count

def prime_number(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# def fact_digits(n):
#     pass

# def fibonacci(n):
#     pass
#
#
# def fib_number(n):
#     pass
#
# def palindrome(n):
#     pass
#
# def char_histogram(string):
#     pass
#

