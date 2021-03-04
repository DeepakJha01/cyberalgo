
def mmi(mi,ki,ind):

    a = mi
    m = ki

    y = 1
    while(True):
        val = (a*y) % m
        print(f"y{ind} = {y};\t{a}*{y} mod{m} = {val}")
        if val==1:break
        y+=1

    print(f"Therefore, y{ind} = {y}\n")
    return y



###############
print("\nCalculating value of x using CRT ...\n")

n = int(input("Enter number of equations available : "))

a = []
k = []

for _ in range(n):
    a0, k0 = map(int,input("Enter a & k for the form x ≡ a (mod k) : ").split())
    a.append(a0)
    k.append(k0)

d = 1
s = ""
for i in k:
    d*=i
    s+=(str(i)+" * ")
print(f"\nValue of d = {s} = {d}\n")

print("Calculating Mi ...")
m = []
for i in range(n):
    val = int(d/k[i])
    m.append(val)
    print("M"+str(i+1)+" = d/k"+str(i+1)+" = "+str(val))

print("\nFinding yi...\nMiyi ≡ 1 mod ki\n")
y = []
for i in range(n):
    print(f"{m[i]}y{i+1} ≡ 1 mod {k[i]}")
    ans = mmi(m[i],k[i],i+1)
    y.append(ans)

print("Calculating x...")
print("x = Σ[ai * Mi * yi] mod d")

x = 0
s = "x = ["
for i in range(n):
    val = a[i]*m[i]*y[i]
    x+=val
    s += ("(" + str(a[i]) + " * " + str(m[i]) + " * " + str(y[i]) + ") + ")
s+="]"

print(s + "mod " + str(d))
x = x%d
print("\nANSWER : x = ",x)

