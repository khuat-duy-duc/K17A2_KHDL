#1
a = float(input("Nhập số cần tính bình phương: "))
if a > 0:
    b =a**2
    print(f"Bình phương của {a} là {b}")
else:
    print("Số bạn nhập không phải số dương.")
#2
n=int(input("Nhập 1 số nguyên bất kỳ:"))
print("các số nguyên từ 1 đến ",n,"là:")
for i in range(1,n+1):
    print(i)
#3
m = int(input("Nhập số tự nhiên m:"))
n = int(input("Nhập số tự nhiên n (n>m):"))
if m>= n:
    print("Vui lòng nhập m<n.")
else:
    print(f"Các số chia hết cho m trong khoảng từ 1 đến {n} là:")
    for i in range(1, n+1):
        if i % m ==0:
            print(i)
#4
number1 = float(input("Nhập số thứ nhất:"))
number2 = float(input("Nhập số thứ hai:"))
number3 = float(input("Nhập số thứ ba:"))
max_number = max(number1, number2, number3)
print("Số lớn nhất trong ba số là:", max_number)
#5
def ucln(a, b):
    while b:
        a, b = b, a % b
    return a
def bcnn(a, b):
    return a * b // ucln(a, b)
num1 = int(input("Nhập số thứ nhất: "))
num2 = int(input("Nhập số thứ hai: "))
result_bcnn = bcnn(num1, num2)
print(f"Bội chung nhỏ nhất của {num1} và {num2} là: {result_bcnn}")
#6
#Giả hệ phương trình bậc nhất
#Sơ đồ khối
   +-----------------------+
      |                       |
      v                       |
    Nhập a, b                |
      |                       |
      v                       |
    Nếu a = 0               |
    |                        |
    Hiển thị "Vô số nghiệm"  |
    |                        |
    Kết thúc                 |
      |                       |
      v                       |
    Nghiệm x = -b/a          |
      |                       |
      v                       |
    Hiển thị nghiệm x        |
      |                       |
      +-----------------------+
#Giải mã:

Nhập hai số a và b từ người dùng.
Nếu a bằng 0, hiển thị "Vô số nghiệm" và kết thúc.
Nếu a khác 0, tính nghiệm x = -b/a và hiển thị kết quả.

#Tính số ngày của một tháng một năm nào đó
#Sơ đồ khối
   +-----------------------+
      |                       |
      v                       |
    Nhập tháng, năm          |
      |                       |
      v                       |
    Nếu tháng không hợp lệ  |
    |                        |
    Hiển thị "Tháng không hợp lệ"|
    |                        |
    Kết thúc                 |
      |                       |
      v                       |
    Nếu là tháng 2          |
    |                        |
    Nếu năm nhuận            |
    |                        |
    Hiển thị "29 ngày"       |
    |                        |
    Ngược lại                |
    |                        |
    Hiển thị "28 ngày"       |
    |                        |
    Kết thúc                 |
      |                       |
    Ngược lại                |
    |                        |
    Nếu tháng là 1, 3, 5, 7, 8, 10, hoặc 12|
    |                        |
    Hiển thị "31 ngày"       |
    |                        |
    Ngược lại                |
    |                        |
    Hiển thị "30 ngày"       |
      |                       |
      +-----------------------+
#Giải mã:

Nhập tháng và năm từ người dùng.
Kiểm tra xem tháng có hợp lệ không.
Nếu là tháng 2, kiểm tra xem năm là năm nhuận hay không.
Dựa vào kiểm tra trên, hiển thị số ngày của tháng tương ứng.

#Thuật toán tìm ước số chung lớn nhất
#Sơ đồ khối
   +-----------------------+
      |                       |
      v                       |
    Nhập a, b                |
      |                       |
      v                       |
    Trong khi b khác 0       |
    |                        |
    |   Tính r = a % b        |
    |                        |
    |   Gán a = b            |
    |   Gán b = r            |
    |                        |
    Kết thúc                 |
      |                       |
      v                       |
    Hiển thị "UCLN là a"      |
      |                       |
      +-----------------------+
#Giải mã:

Nhập hai số a và b từ người dùng.
Trong khi b khác 0, thực hiện các bước sau:
Tính phần dư r = a % b.
Gán a = b, b = r.
Hiển thị "UCLN là a".
#7
def tinh_tong_chu_so(N):
    chuoi_so = str(N)
    tong = 0
    for chu_so in chuoi_so:
        tong += int(chu_so)

    return tong

so_nguyen = int(input("Nhập số nguyên N:"))
ket_qua = tinh_tong_chu_so(so_nguyen)
print("Tổng các chữ số của", so_nguyen, "là:", ket_qua)




