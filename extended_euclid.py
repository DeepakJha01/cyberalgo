
from pandas import  *

def display(matrix):
    print('\n')
    df = pandas.DataFrame(matrix)
    print(df.to_string(index=False, header=False))


print("\nEXTENDED EUCLID'S ALGORITHM")
print("Calculating MMI(a mod m) and GCD(a,m) ...\n")

a = int(input("Enter a : "))
m = int(input("Enter m : "))

A1,A2,A3 = 1,0,m
B1,B2,B3 = 0,1,a
matrix = []
blank = None
row = [blank,A1,A2,A3,B1,B2,B3,blank,blank,blank]
matrix.append(['Q','A1','A2','A3','B1','B2','B3','T1','T2','T3'])
matrix.append(row)


while(B3!=0 and B3!=1):
    Q = int(A3/B3)
    T1 = A1 - Q*B1
    T2 = A2 - Q*B2
    T3 = A3 - Q*B3

    A1,A2,A3 = B1,B2,B3
    B1,B2,B3 = T1,T2,T3

    row = [Q, A1, A2, A3, B1, B2, B3, T1, T2, T3]
    matrix.append(row)


GCD, MMI = "Invalid", "Invalid"

if(B3==0):
    GCD = A3
if(B3==1):
    GCD = B3
    MMI = B2

display(matrix)

print(f"\n\nGCD of {a} and {m} = {GCD}")
print(f"MMI of {a} and {m} = {MMI}")

