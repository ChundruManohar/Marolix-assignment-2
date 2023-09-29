#Write a function that checks if a given number is prime.
 #Prime number are 2,3,5,7

def prime(num):
    for i in range(2,num):
      if num % i == 0:
        return print('its not a prime number')
      else:
        return print ('its is a prime number ')

num = int(input('Enter a number '))

prime(num)


