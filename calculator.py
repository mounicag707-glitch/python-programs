a=int(input("enter first value:"))
b=int(input("enter second value:"))
op=input("enter operator(+,-,*,/):")
if op=="+":
  print("addition=",a+b)
elif op=="-":
  print("subtraction=",a-b)
elif op=="*":
  print("multiplication=",a*b)
elif op=="/":
  print("division=",a/b)
else:
  print("invalid operators")
