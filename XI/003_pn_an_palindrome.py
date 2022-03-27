# Find a number is perfect number or Armstrong number or Palindrome
# Perfect number : A positive integer which is equal the sum of the proper divisors excluding itself. Ex:6=1+2+3,28=1+2+4+7+14
# Armstrong Number : The sum of its own digits raised to the power number of digits gives the number itself. Ex: 153=1**3+5**3+3**3,407
# Palindrome : The number remains same when we reverse the digits of the number. Ex: 121,12321,1345431

def perfect_number(number):
    sum = 0
    for i in range(1, number, 1):
        if number % i == 0:
            sum = sum + i
    if sum == number:
        print("{} is a Perfect number".format(number))
    else:
        print("{} is not a Perfect number".format(number))


def armstrong_number(number):
    length = len(str(number))
    sum = 0
    n = number
    while n > 0:
        dig = n % 10
        n = n // 10
        sum = sum + dig**length
    if number == sum:
        print("{} is a Armstrong number".format(number))
    else:
        print("{} is not a Armstrong number".format(number))


def palindrome_number(number):
    n = number
    rev = 0
    while n > 0:
        dig = n % 10
        rev = rev * 10 + dig
        n = n // 10
    if number == rev:
        print("{} is a Palindrome number".format(number))
    else:
        print("{} is not a Palindrome number".format(number))


n = int(input("Enter a number"))
perfect_number(n)
armstrong_number(n)
palindrome_number(n)
