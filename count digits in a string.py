text=input("enter a string:")
count=0
for ch in text:
  if ch.isdigit():
    count +=1
print("number of digits=",count)
