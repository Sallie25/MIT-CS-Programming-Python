def gcdIter(a,b):
    all_divisors = []
    min_value = min(a, b)
    for i in range(1, min_value + 1):
        if a % i == 0 and b % i == 0:
            all_divisors.append(i)
        else:    
            continue
    return(max(all_divisors))
           
print(gcdIter(14,28))            


            
            




















#     print(all_divisors)    

# gcd(6,12)  