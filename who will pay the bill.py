import random
names=input("enter names separated with comma")
names_list=names.split(",")
print(names_list)
person_selected=random.choice(names_list)
print(f"{random.choice(names_list)} will pay the bill")
