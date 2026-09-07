text=input("enter a string:")
sub=input("enter a substring:")
position=text.find(sub)
if position!=-1:
  print("substring found at index",position)
else:
  print("substring is not found")
