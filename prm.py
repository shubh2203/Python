for num in range(1,20):
    prime = True
    for i in range(2,num):
        if (num%i==0):
            prime = False
    if prime:
       print(num)

