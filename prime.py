def list_primes(N):
    primes=[]
    for num in range(1, (N+1)):
       if N > 1:
           for i in range(2, num):
               if num % i == 0:
                   break
           else:
               primes.append(num)
    return primes
