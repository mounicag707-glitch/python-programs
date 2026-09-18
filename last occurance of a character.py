text=input("enter a string")
ch=input("enter a character:")
position=text.rfind(ch)
if position!=-1:
  print("last occurance at index",position)
else:
  print("character not found")
