a = int(input('enter a natural number ='))
b= int(input('enter second natural number ='))

def computeGCD(x, y):

    if x > y:
        csen = y
    else:
        csen = x
    for i in range(1, csen+1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i

    return gcd

print ("The gcd of first number and second number is : ",end="")
print (computeGCD(a,b))
