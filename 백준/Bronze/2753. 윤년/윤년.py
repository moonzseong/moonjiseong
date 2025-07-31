yun = int(input())
if yun % 4 != 0:
    print("0")
elif yun%100 != 0 or yun%400 == 0:
    print("1")
else:
    print("0")