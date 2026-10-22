n=int(input("Enter a number: "))
multi=1
total=0
for x in range(1, n + 1):
    multi *= x
    
print(f"the factorial of {n} is {multi}")
