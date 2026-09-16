height=int(input("enter height:"))
if height>=3:
  print("can ride")
  age=int(input("enter age:"))
  if age<12:
    print("ticket price is 50 rs")
  elif age<=18:
    print("ticket price is 150 rs")
  else:
    print("ticket price is 250 rs")
else:
  print("cant ride")
