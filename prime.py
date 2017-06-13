def list_primes(N):
    for num in range(0,N+1):
       if num > 1:
           for i in range(2,num):
               if num % i == 0:
                   break
           else:
               print (num)
