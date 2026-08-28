weight=int(input("enter weight in kg:"))
height=int(input("enter height in meter:"))
bmi=(weight)/(height**2)
if bmi<18:
    print(f"your bmi is {bmi} so your are under weight")
elif bmi<=25:
    print(f"your bmi is {bmi} so your are normal xweight")
elif bmi<=35:
    print(f"your bmi is{bmi} so your are over weight")
else:
    print(f"your bmi is{bmi} so your are obese")
