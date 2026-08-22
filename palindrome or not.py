n=int(input("enter n value:"))
temp=n
rev=0
while n>0:
  digit=n%10
  rev=rev*0+digit
  n=n//10
if temp==rev:
  print("it is a palindrome")
else:
  print("it is not a palindrome")
