#Задача "Всё не так уж просто":
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = [] #только простые числа.
not_primes = [] #все не простые числа.
is_prime = True
for i in range(2, len(numbers) + 1):
    #print(i)
    for j in range(2, i):
        #print(j)
        if i % j == 0:
            is_prime = False
            not_primes.append(i)
            break
    else:
        primes.append(i)
print(f'Primes: {primes}')
print(f'Not_primes: {not_primes}')
