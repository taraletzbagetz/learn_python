temperature = int(input("Please input your temperature reading: "))
forecast = "rainy"

if temperature > 80:
    print("It's too hot!")
    print("Stay indide!")
elif temperature < 60:
    print("It's too cold!")
    print("Stay indide!")
else:
    print("Enjoy the outdoors")  

if not forecast == "rainy":
    print("Go outside!")

