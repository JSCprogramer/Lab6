num=int(input("Enter the starting number: "))
MAX=int(input("How high should I go? "))

print("Number \t Square")
print("----------------")
for x in range(num, MAX +1):
    sqr= x**2
    print(f'{x}\t{sqr}')
    
