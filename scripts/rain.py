rain = input("Is it currently raining? ")

if rain == "Yes":
    print("You should take the bus.")

elif rain == "No":
    travel = int(input("How far in km do you need to travel? "))
    if travel > 10:
        print("You should take the bus.")
    elif travel in range(2, 11):
        print("You should ride your bike.")
    elif travel < 2:
        print("You should walk.")

# if you use the range function with a if statement you use in not the equality operator
