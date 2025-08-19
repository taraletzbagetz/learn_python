age = input("How old are you?")

decades = int(age) // 10
years = int(age) % 10

print("You're " + str(decades) + " decades and " + str(years)+ " years old.")