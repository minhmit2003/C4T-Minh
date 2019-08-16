a= float(input("Nhập giá trị của X^2: "))
b= float(input("Nhập giá trị của X: "))
c= float(input("Nhập giá trị của số thực trong biểu thức: "))
s= b*b-4*a*c
x1 = (-b+s)/2*a

if s < 0:
     print("Đây ko phải là phương trình bậc 2")
elif s < 1 :
    print("Giá trị của X là: ", x1)
else :
    print("ggwp)