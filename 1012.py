A,B,C = map(float,input().split())
pi = 3.14159
triangle  = 1/2*A*C
circle  = pi*C*C
trapezium = 1/2*(A+B)*C
square = B*B
rectangle = A*B
print("TRIANGULO:","{:.3f}".format(triangle))
print("CIRCULO:","{:.3f}".format(circle))
print("TRAPEZIO:","{:.3f}".format(trapezium))
print("QUADRADO:","{:.3f}".format(square))
print("RETANGULO:","{:.3f}".format(rectangle))




