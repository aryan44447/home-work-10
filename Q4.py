numb = int(100000)
print ('Printing armstrong numbers below',numb)
for num in range(0,numb):
    sum=0
    n=num
    while num !=0:
        sum= sum +pow(num%10,len(str(n)))
        num=int(num/10)
    if n==sum:
        print (n,'is an armstrong number')