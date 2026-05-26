print("welcome to the interactive personal data collector!\n")

name=input("please enter your name:")
age=int(input("please enter your age:"))
height=float(input("please enter your height in meters:"))
fav_number=int(input("please enter your favourite number:"))

print("your birth year is approximately:2009 based on your age of 17")

print(f"name: {name} (type:{type(name)}, memory address:{id(name)})")
print(f"age: {age} (type:{type(age)}, memory address:{id(age)})")
print(f"height: {height} {type(height)},memory addeess:{id(height)})")
print(f"favourite number:{fav_number}{type(fav_number)},memory address:{id(fav_number)})")

print("Thank you for using the personal data collector. Goodbye!")

