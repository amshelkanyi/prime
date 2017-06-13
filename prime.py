def list_primes(N):
    if not isinstance(N, int):
        return 'Only Integers are allowed'
    elif N<1:
        return 'Positive numbers only'
    else:
        primes=[]
        for num in range(2, (N+1)):
           if N > 1:
               for i in range(2, num):
                   if num % i == 0:
                       break
               else:
                   primes.append(num)
        return primes
print(list_primes(10))
