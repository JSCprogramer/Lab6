start=int(input("Enter starting KPH: "))
end=int(input("enter end of KPK: "))



print("KPH\tMPH")
print("-------------")
for KPH in range(start,end+1,10):
    MPH =KPH*0.6214
    print(f'{KPH}\t{MPH:.1f}')
