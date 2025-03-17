age = int(input("enter your age: "))

if age <= 19:
    print("Discount for students:")
elif 20 <= age <= 54:
    print("no discount:")
else:
    print("Discount for the old:")
