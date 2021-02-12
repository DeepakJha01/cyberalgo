
print("\nCalculating x of ax mod m = 1 ...\n")

a = int(input("Enter a : "))
m = int(input("Enter m : "))

print()

x = 1
while(True):
    val = (a*x) % m
    print(f"x = {x};\t{a}*{x} mod{m} = {val}")
    if val==1:break
    x+=1

print(f"\nx = {x}")