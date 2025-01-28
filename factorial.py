a = int(input("Enter the number: "))
i = 1
res = 1
while i <= a:
    res *= i  
    i += 1
print(f"Factorial of {a} is {res}")
