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
    for i in range(0,len(digits)):
        digit = digit[i]
        num += step*digit
        step *= 10
    return num


def count_vowels(str):
    str = str.lower()
    count = 0
    for i in range(0, len(str)):
        digit = str % 10
        # check if digit is vowel
        if is_vowel(digit) == True:
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
        return False

def count_consonants(str):
    for i in range(0, len(str)+1):
        letter = str % 10
        count = 0
        if is_vowel(letter):
            count += 1
        str /= 10
def prime_number(n):
    if n % 2 == 1:
        return True
    else:
        return False

def fact_digits(n):
    pass

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
