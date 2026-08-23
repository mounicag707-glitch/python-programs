def calculate(a,b):
  sum=a+b
  difference=a-b
  product=a*b
  return sum,difference,product
a=int(input("enter a value:"))
b=int(input("enter b value:"))
sum,difference,product=calculate(a,b)
print("sum=",sum)
print("difference=",difference)
print("product=",product)
