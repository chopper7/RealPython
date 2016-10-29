inp = input('Enter a positive integer: ')

def find_factors(num):
    for n in range(1, round(num/2)+1):
        if num % n == 0:
            print('{} is a divisor of {}'.format(n, num))
    print('{0} is a divisor of {0}'.format(num))

find_factors(int(inp))
