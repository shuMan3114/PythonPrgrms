def fib(n,f0=1,f1=1):
    if(n):
        print(f0)
        new_f1 = f0 + f1
        f0 = f1
        f1 = new_f1
        n -= 1
        return fib(f0,f1,n)

n = int(input("enter num(>0): "))
fib(n)
