#bài 1
def sign(x):
    if x<0:
        return -1
    elif x==0:
        return 0
    else:
        return 1
 #............................
print(sign(8))
print(sign(-8))
print(sign(0))
#bài 3
def tinh_bmi(can_nang,chieu_cao):
    BMI=can_nang/(chieu_cao*chieu_cao)
    if BMI < 18.5:
        return "Gầy"
    elif 18.5 <= BMI < 24.9:
        return "Bình thường"
    elif BMI>=25:
        return "Thừa cân"
 #...........................
a=float(input("Nhập cân nặng : "))
b=float(input("Nhập chiều cao :"))
bmi= tinh_bmi(a,b)
print(bmi)
#bài 4
def tinh_S(n,x):
    S=(x**2+1)**2
    return S
 #............................
a=int(input("Nhập a : "))
b=int(input("Nhập b : "))
ham_so=tinh_S(a,b)
print(ham_so)
#bài 5
def tinh_A(n,x):
    A=(x**2+x+1)**n+(x**2-x+1)**n
    return A
 #.........................
a=int(input("Nhập a : "))
b=int(input("Nhập b : "))
gia_tri=tinh_A(a,b)
print(gia_tri)
#bài 6
def so_nguyen_to(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True
 #............. 
x = int(input("Nhập một số: "))
if so_nguyen_to(x):
    print(x,"là số ngueyen tố")
else:
    print(x, "không phải là số nguyên tố.")
#bài 7
def phần_nguyên(a,b)->int:
    return a//b
 #................... 
a=int(input("nhập vào một số a :"))
b=int(input("Nhập vào một số b :"))
print("phần nguyên của hai số",a ,b ,"là ")