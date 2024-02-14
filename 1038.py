"""p = [4.00,4.50,5.00,2.00,1.50]
X, Y = map(int,input().split())
if X==1:
    X = p[0]
elif X==2:
    X = p[1]
elif X==3:
    X =p[2]
elif X==4:
    X = p[3]
elif X==5:
    X = p[4]
T = X*Y
print(f"Total: R$ {(T):.2f}")"""

product_table = {
    1: 4.00,
    2: 4.50,
    3: 5.00,
    4: 2.00,
    5: 1.50
}
X, Y = map(int,input().split())
total_value = product_table[X] * Y
print("Total: R$ {:.2f}".format(total_value))
