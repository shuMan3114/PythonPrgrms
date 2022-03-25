n = int(input("enter a number(>0): "))
sum_of_squares = sum([i**2 for i in range(1,n+1)])
print(sum_of_squares)

sum_of_cubes = sum([i**3 for i in range(1,n+1)])
print(sum_of_cubes)