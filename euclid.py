
print("\nEUCLID THEOREM")
print("Calculating GCD(a,b) ...")

A0 = int(input("\nEnter a : "))
B0 = int(input("Enter b : "))

A,B = A0,B0

print()

while(B!=0):
    C = A%B
    print(f"A = {A}\tB = {B}\tC = {C}")
    A = B
    B = C

print(f"A = {A}\tB = {B}\tSTOP\n")

print(f"GCD({A0},{B0}) = {A}")
