text=input("enter a string:")
count=0
for ch in text:
  if ch.isalpha():
    count +=1
print("number of alphabets=",count)
