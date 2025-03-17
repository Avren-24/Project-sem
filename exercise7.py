studentNames = ["Lisa", "Liam", "Leo", "Larry", "Linda"]

for name in studentNames:
    print(f"{name} Evans")

new_name = input("enter a name: ")
studentNames.append(new_name)

print("\nthe list updated:")
for name in studentNames:
    print(f"{name} Evans")
