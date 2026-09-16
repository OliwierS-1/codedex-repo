height = input("Enter your height in cm: ")
credits = input("Enter your credits: ")

height = float(height)
credits = int(credits)

if height >= 137 and credits >= 10:
    print("You can ride the roller coaster!")
elif height < 137 and credits >= 10:
    print("You are too short to ride the roller coaster.")
elif height >= 137 and credits < 10:
    print("You do not have enough credits to ride the roller coaster.")
else:
    print("You are too short and do not have enough credits to ride the roller coaster.")