def collatz(number):
    if number == 1:
        print(number)
    elif num % 2 == 0:
        number = number // 2
        print(number)
        return collatz(number)
    elif number % 2 ==1:
        number = 3 * number + 1
        print(number)
        return collatz(number)

print('Lets test the Collatz sequence.... ')
num = int(input('Enter a number:'))
collatz(num)
