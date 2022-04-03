from termcolor import colored

def prime(num):
    for n in range(2,num):
        if num % n == 0:
            return False
    return True

x = int(input('[!] Until which number do you wish to calculate: '))

a = 0
primelist = []
for i in range(2,x+1):
  if prime(i) == True:
    primelist.append(i)
    a += 1

print(colored(primelist, 'yellow'))

print(colored(f'[{a} prime numbers detected]','red'))