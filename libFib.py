def fib(n):   
    a, b = 0, 1 
    # a = 0
    # b = 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
        #temporal = a 
        #a = b
        #b = temporal + b
    print()