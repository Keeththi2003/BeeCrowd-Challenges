code_pro1,uni_pro1,price_pro1 = map(float,input().split())
code_pro2,uni_pro2,price_pro2 = map(float,input().split())
S = (uni_pro1*price_pro1+uni_pro2*price_pro2)
print("VALOR A PAGAR: R$","{:.2f}".format(S))

