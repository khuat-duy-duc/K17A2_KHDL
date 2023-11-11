#1
print("Bài toán tìm số lớn nhất và nhỏ nhất.")
a=eval(input("Nhập số a:"))
b=eval(input("Nhập số b:"))
c=eval(input("Nhập số c:"))
d=eval(input("Nhập số d:"))
g=0
h=0
while(g<a)or(g<b)or(g<c)or(g<d):
    g+=1
h=g
while(h>a)or(h>b)or(h>c)or(h>c):
    h-=1
print("max =",g)
print("min =",h)  

#2
a=eval(input("Nhập số:"))
print("Giá trị tuyệt đối của",a,"là:","|",a,"|=",abs(a))

#3
print("Giải phương trình ax+b=0")
a = int(input("Nhập số a:"))
b = int(input("Nhập số b:"))
if a == 0:
    if b == 0:
        print("Phương trình vô số nghiệm.")
    else: print("Phương trình vô nghiệm.") 
else: 
    print('Nghiệm của phương trình là: x = ', -b/a)

    #4
    a = eval(input("nhap do dai canh a: "))
b = eval(input("nhap do dai canh b: "))
c = eval(input("nhap do dai canh c: "))
if a+b<c and b+c<b:
    print("day khong phai la tam giac")
else:
    print("day la mot tam giac")
    import math
    p=(a+b+c)/2
    S= math.sqrt(p*(p-a)*(p-b)*(p-c))
    print("Dien tich tam giac tren la: ",S)

#5
a = int(input("Nhập năm: "))
if ((a%4==0) and (a%100!=0) or (a%400==0)):
    print("năm", a, "là năm nhuận")
else:
    print("năm", a, "không phải là năm nhuận")

    #6
    loai_xe=int(input("Cho biết loại xe là 4/7 ?"))
so_km=float(input("Nhập số km chạy bằng = "))
time_cho=float(input("Cho biết thời gian chờ (phút chờ) = "))
tien_cuoc=float(0)
tien_di_chuyen=float(0)
if time_cho >=5:
    tien_cho=(time_cho-5)*0.8
else:
    tien_cho=0
if loai_xe==4:
    if so_km <=0.8:
        tien_di_chuyen=0.8*11000
    elif so_km <=20:
        tien_di_chuyen=0.8*11000+(20-so_km)*12100
    else:
        tien_di_chuyen=0.8*11000+(20-0.8)*12100+(so_km-20)*10000
    tien_cuoc=tien_cho+tien_di_chuyen
    print("Cước phí xe taxi 4 chỗ của quý khách là %0.2f"%tien_cuoc)
if loai_xe==7:
    if so_km <=0.8:
        tien_cuoc+tien_cho+0.8*13000
    elif so_km <=30:
        tien_cuoc=tien_cho+0.8*13000+(30-so_km)*14100
    else:
        tien_cuoc=tien_cho+0.8*13000+(30-0.8)*14100+(so_km-30)*12000
    tien_cuoc=tien_cho+tien_di_chuyen
    print("Cước phí xe taxi 7 chỗ của quý khách là %0.2f"%tien_cuoc)

    #7
    a=eval(input("Nhập số KWh tiêu thụ:"))
if a>=0:
    if a<=50:
       print("Tổng số tiền phải trả là:",a*1678,"đồng.")
    elif a<=100:
       print("Tổng số tiền phải trả là:",50*1678+(a-50)*1734,"đồng.")
    elif a<=200:
       print("Tổng số tiền phải trả là:",50*(1678+1734)+(a-100)*2014,"đồng.")
    elif a<=300:
       print("Tổng số tiền phải trả là:",50*(1678+1734+2014)+(a-200)*2536,"đồng.")
    elif a<=400:
       print("Tổng số tiền phải trả là:",50*(1678+1734+2014+2536)+(a-300)*2834,"đồng.")
    else:
       print("Tổng số tiền phải trả là:",50*(1678+1734+2014+2536+2834)+(a-400)*2927,"đồng.")     
else:
   print("Số KWh không hợp lệ.")

   #8
   print("Các mã loại phòng cho bạn:")
print("1-Standard")
print("2-Superior Garden View")
print("3-Superior Ocean View")
print("4-Garden View Bungalow")
print("5-Pool View Bungalow")
print("6-Family Room")
print("7-Beach Front Bungalow")
print("8-VIP sea View")
a=eval(input("Nhập mã loại phòng:"))
b=eval(input("Nhập số đêm:"))
if a>0&a<=8:
    if a==1: c=1260000
    elif a==2: c=1550000
    elif a==3: c=1830000
    elif a==4: c=1830000
    elif a==5: c=2120000
    elif a==6: c=2120000
    elif a==7: c=2540000
    elif a==8: c=4800000
    else: 
        print("Vui lòng chọn lại mã loại phòng.")
else: print("Vui lòng chọn lại mã loại phòng.") 
if b==1:
    print("Giá  tiền phải trả là:",c,"đồng.")
elif b==2:
    print("Giá  tiền phải trả là:",c*b*0.75,"đồng.") 
elif b==3:
    print("Giá  tiền phải trả là:",c*b*0.75,"đồng.") 
elif b>=4:
    print("Giá  tiền phải trả là:",c*b*0.7,"đồng.")       
else:
    print("Vui lòng nhập lại số đêm.")

    #9
    a = int(input("nhap so a: "))
for i in range(a,0,-1):
    print(i)

    #10
    print("Nhập n:")
n=eval(input(""))
print("Nhập x:")
x=eval(input(""))
s=(x*x+1)**n
print("(S=x*x+1)^n =",s)

#11
print("Nhập n:")
n=eval(input(""))
print("Nhập x:")
x=eval(input(""))
A=(x*x+x+1)**n + (x*x-x+1)**n
print("A=(x*x+x+1)^n+(x*x-x+1)^n=",A)

#12
n = int(input("Nhập số n = "))
flag = True 
if n < 2 :
    print(n, "Không nguyên tố !!!")
else:
    for i in range(2, n):
        if n%i == 0:
            flag = False
            break
    if flag:
        print(n, " là số nguyên tố")
    else:
        print(n, " không phải là số nguyên tố!!!")