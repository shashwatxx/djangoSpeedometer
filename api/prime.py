def prime(number):
    if number==2 or number==3:
        return True
    for i in range(2,number/2):
        
        if number%i==0:
            return False
            break
        else:
            continue
    return True
print(prime(4))