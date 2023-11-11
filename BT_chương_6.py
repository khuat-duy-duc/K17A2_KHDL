#1.1
print("** ** ******    **      **     ** ****")
print("** ** **        **      **     **   **")
print("***** ******    **      **     **   **")
print("** ** **        **      **     **   **")
print("** ** ** ****   ******  ****** *******")
#1.2
x=10
y=5
tong=x+y
hieu=x-y
tich=x*y
thuong=x/y
print('Tổng của hai số    ', x, '+', y, '=',tong)
print('Hiệu của hai số    ', x, '-', y, '=',hieu)
print('Tích của hai số    ', x, '*', y, '=',tich)
print('Thuong của hai số  ', x, '/', y, '=',thuong)
#1.3
ten_hang = "Sữa hộp Vinamilk"
so_luong = 5
don_gia = 25000
tien_phai_tra = so_luong * don_gia
print("Tên hàng:", ten_hang)
print("Số lượng:", so_luong)
print("Tiền phải trả:", tien_phai_tra)
#1.4
x=(5-3)//2
print("(5-3)//2","=",x)
y=(8-3)*(2-(1+1))
print("(8-3)*(2-(1+1))","=",y)
#1.5
so_luong=int(input("Nhập số lượng :"))
don_gia=int(input("Nhập đơn giá :"))
print("Thành tiền =",so_luong,"*",don_gia,"=",so_luong*don_gia)
#1.7
C=int(input("Nhập độ C :"))
F=(C*9/5)+32
print(C,"độ C","=",F,"độ F")
#1.8
s1=input("nhap chuoi s1=")
s2=input("nhap chuoi s2=")
s3=input("nhap chuoi s3=")
a=int(input("nhap diem dau:"))
b=int(input("nhap diem cuoi:"))
print("chieu dai cua chuoi s1 la :",len(s1))
print("chieu dai cua chuoi s2 la :",len(s2))
print("chieu dai cua chuoi s3 la :",len(s3))
print("chuoi s4 =",s1[a:b])
print("chui s2 lap lai 2 lan =",s2*a)
#1.9
lai_suat=float(input("Lãi suất 1 năm (%) :"))
tien_gui=int(input("Số tiền gửi :"))
so_thang_gui=int(input("Số tháng gửi :"))
tien_lai=(tien_gui*so_thang_gui)*(lai_suat/12)
tong_so_tien=tien_gui+tien_lai
print("tiền lãi =",tien_lai)
print("Tiền vốn + Lãi =",tong_so_tien)