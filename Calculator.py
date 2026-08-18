a=float(input("enter first number:"))
b=float(input("enter second nmber:"))
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
choice=int(input("enter your choice:"))
if choice==1:
  print("Result=",a+b)
elif choice==2:
  print("Result=",a-b)
elif choice==3:
  print("Result=",a*b)
elif choice==4:
  print("Result=",a/b)
else:
  print("cannot divide by zero")
else:
  print("Invalid choice")
  
