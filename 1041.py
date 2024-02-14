X, Y = map(float,input().split())
if X==0 and Y==0:
     print("Origem")
elif X==0:
    print("Eixo Y")
elif Y==0:
    print("Eixo X")
else:
    if X>0 and Y>0:
        print("Q1")
    elif X>0 and Y<0:
        print("Q4")
    elif X<0 and Y>0:
        print("Q2")
    elif X<0 and Y<0:
        print("Q3")    
"""
# Read coordinates
x, y = map(float, input().split())

# Check quadrant or axis
if x == 0 and y == 0:
    print("Origem")
elif x == 0:
    print("Eixo Y")
elif y == 0:
    print("Eixo X")
else:
    if x > 0:
        if y > 0:
            print("Q1")
        else:
            print("Q4")
    else:
        if y > 0:
            print("Q2")
        else:
            print("Q3")
"""