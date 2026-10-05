n=int(input("Enter a limit: "))
a, b=0, 1
print("Fibinacci series: ")
while a<=n:
    print(a, end=" ")
    a, b= b, a+b
print()
