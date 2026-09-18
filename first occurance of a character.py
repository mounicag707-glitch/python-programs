text=input("enter a string")
ch=input("enter a character:")
position=text.find(ch)
if position!=-1:
  print("character found at index",position)
else:
  print("character not found")
