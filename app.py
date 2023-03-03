a= float(input("Tham số a "))
b= float(input("Tham số b "))
if a==0 and b==0:
    print('PT vô số nghiệm')
elif a==0 and b!=0:
    print('PT vô nghiệm')
else:
    print('x=%.1f'%(-b/a))