#左直角三角形
n = eval(input("請輸入數字:"))

for i in range(n+1):
    print("@"*i)

#倒左直角三角形
n = eval(input("請輸入數字:"))

for i in range(n+1):
    print("@"*(n-i))

#右直角三角形
n = eval(input("請輸入數字:"))

for i in range(n+1):
    print(" "*(n-i)+"@"*i)
#倒右直角三角形
n = eval(input("請輸入數字:"))

for i in range(n+1):
    print(" "*i+"@"*(n-i))

#正等腰三角
n = eval(input("請輸入數字:"))

for i in range(n+1):
    print(" "*(n-i)+"@"*(2*i-1))

#倒等腰三角
n = eval(input("請輸入數字:"))

for i in range(n,0,-1):
    print(" "*(n-i)+"@"*(2*i-1))

