#calculate the factorial of a non-negative integer.
def m(num):
    if num == 0:
        return 1
    else:
        return num * m(num-1)
    
num = int(input("Enter the number: "))
m(num)
print('the factorial is : ', m(num))

    
