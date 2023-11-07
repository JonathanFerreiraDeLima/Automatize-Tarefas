def collatz(number):
    if number % 2 == 0: 
        result = number // 2
    else:
        result = 3 * number + 1   
    return result

print('Digite um Número inteiro: ')
num = input()
num = int(num)

print(collatz(num))
