def is_prime(num):
    if num > 1:  
        for n in range(2,num):  
            if (num % n) == 0:  
                return False
        return True
    else:
        return False
    
print(is_prime(56))