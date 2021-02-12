from pandas import *

def display(matrix):
    print('\n')
    df = pandas.DataFrame(matrix)
    print(df.to_string(index=False, header=False))


def isPrime(n):
    if (n <= 1):
        return False
    if (n <= 3):
        return True
    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6

    return True


print("\nFinding Primitive roots ...")

n = int(input("\nEnter n : "))
if not isPrime(n):
    exit()

roots = []
matrix = []
row0 = ["a\i"]
for i in range(1,n):
    row0.append("a^"+str(i))
matrix.append(row0)

for a in range(1,n):
    col0 = "a="+str(a)
    row = [col0]
    for i in range(1,n):
        val = (a**i) % n
        row.append(val)
    matrix.append(row)
    if sorted(row[1:]) == [j for j in range(1,n)]:
        roots.append(a)


display(matrix)

print("\nPrimitive roots are  = ",roots)