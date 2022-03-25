def get_factorial(n,factorial = 1):
    if(n):
        factorial *=n
        n -= 1
        return get_factorial(n,factorial)
    else:
        return factorial

n = int(input("enter a num(>0): "))
print(get_factorial(n))