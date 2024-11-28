n = int(input("Enter the number till you want the series: "))
a = 0
b = 1
print(a)
print(b)
fib = 0
for i in range(n):
    fib = a + b
    print(fib)
    a,b = b, fib
