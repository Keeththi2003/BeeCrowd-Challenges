A, B, C = map(float,input().split())
if A+B>C and A+C>B and C+B>A:
    perimeter = A+B+C
    print(f"Perimetro = {perimeter:.1f}")
else:
    area = 1/2*(A+B)*C
    print(f"Area = {area:.1f}")