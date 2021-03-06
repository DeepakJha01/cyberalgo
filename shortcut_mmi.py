
def shortcut_mmi(a,m):

    print(f"\nx = (1 + (k * {m})) / {a}\n")

    k = 0
    x = 0.5

    while(x % 1 != 0):
        k+=1
        x = (1 + (k * m)) / a

        print(f"k = {k} ; x = {1+(k*m)}/{a} = {x}")

    print(f"\nTherefore, x = {int(x)} when k = {k}")


# ax = 1 mod m      or    ax mod m ≡ 1
# arguments : (a, m)
shortcut_mmi(9,67)