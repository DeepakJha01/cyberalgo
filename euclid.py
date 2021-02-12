
print("\nEUCLID THEOREM")
print("Calculating GCD(a,b) ...")

A = int(input("\nEnter a : "))
B = int(input("Enter b : "))

print()

while(B!=0):
    C = A%B
    print(f"A = {A}\tB = {B}\tC = {C}")
    A = B
    B = C

print(f"A = {A}\tB = {B}\tSTOP\n")

print(f"GCD({A},{B}) = {A}")