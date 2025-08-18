#31
# def power(base, exp):
#     return base ** exp

# print(power(2, 3))

#32
# def is_palindrome(s):
#     rev_str = s[::-1]
#     return s ==  rev_str

# print(is_palindrome("radar"))

#33
# def sum_even(n):
#     return sum([num for num in range(2,n + 1,2)])

# print(sum_even(4))

#34
# def factorial(n):
#     dact = 1
#     for num in range(2,n + 1):
#         dact *= num
#     return dact

# print(factorial(4))

#35
# def count_vowels(s):
#     vowels = ['а', 'А', 'е', 'Е', 'ё', 'Ё', 'и', 'И', 'о', 'О', 'у', 'У', 'ы', 'Ы', 'э', 'Э', 'ю', 'Ю']
#     i = 0
#     for char in s:
#         if char in vowels:
#             i+=1
#     return i

# print(count_vowels('Привет'))

#36
# def swap(a, b):
#     return f'({b}, {a})'

#37

# def is_prime(n):
#     if n <= 1:
#         return False
#     if n % 2 == 0:
#         return False
#     if n == 2:
#         return True
#     for i in range(3, int(n **0.5) + 1, 2):
#         if n % i == 0:
#             return False
#     return True

# print(is_prime(8))

#38
def gcd(a, b):
    if b % a == 0 or a % b == 0:
        return min(a , b)
    n = []
    min_num = min(a,b)
    for i in range(2, int(min_num ** 0.5) + 1):
        if min_num % i == 0:
            n.append(min_num / i)
    