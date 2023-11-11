#1
x=int(input("nhap x :"))
s=(1+x)+(x**3/3)+(x**5/5)
print(s)

#2
result=1+2
print('result',result)
original_result=result
result=result-1
print('result',result)
original_result=result
result=result*2
original_result=result
print('result',result)
result=result**3
original_result=result
print('result',result)
result=result+8
original_result=result
print('result',result)
result=result%7
original_result=result
print('result',result)
result=result//2
original_result=result
print('result',result)

#3
result=5
print('result',result)
result-=1
print('result',result)
result+=3
print('result',result)
result= - result
print('result',result)
result= True
print('result',result)

#4
x=10
y=4
print('x=%d,y=%d'%(x,y))
equivelence= x==y
print('x==y is',equivelence)
equivelence= x!=y
print('x!=y is',equivelence)
equivelence= x>y
print('x>y is',equivelence)

x=8
x=9
print('x=%d,y=%d'%(x,y))
equivelence= x>=y
print('x>=y is',equivelence)
equivelence=  x<y
print('x<y is',equivelence)
equivelence= x<=y
print('x<=y is',equivelence)

#5
x=15
y=12
print('Binary of x =',bin(x),", Binary of y =",bin(y))
print('x & y =',bin(x&y))
print('x / y =',bin(x|y))
print('x ^ y =',bin(x^y))
print('~x =',bin(~x))
print('x << 2 =',bin(x<<2))
print('y >> 2 =',bin(y>>2))

#6
x=True
y=False
print('x and y :',x and y)
print('x or y :',x or y)
print('not x :',not x)
print('x is y ',x is y)
print('x is not y :',x is not y)

#7
so_tien_muon_doi=int(input("Nhap so tien muon doi :"))
so_to_1 = so_tien_muon_doi // 500000
tien_con_lai_1 = so_tien_muon_doi % 500000
print("so_to_500000 =",so_to_1)
so_to_2 = tien_con_lai_1 // 200000
tien_con_lai_2 = tien_con_lai_1 % 200000
print("so_to_200000 =",so_to_2)
so_to_3 = tien_con_lai_2 // 100000
tien_con_lai_3 = tien_con_lai_2 % 100000
print("so_to_100000 =",so_to_3)
so_to_4 = tien_con_lai_3 // 50000
tien_con_lai_4= tien_con_lai_3 % 50000
print("so_to_50000 =",so_to_4)
print("tien_con_lai =", tien_con_lai_4)