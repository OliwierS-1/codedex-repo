import random

question = input("Enter a question: ")

choices = random.randint(1, 9)

if choices == 1:
    print("Yes - definitely.")
elif choices == 2:
    print("It is decidedly so.")
elif choices == 3:
    print("Without a doubt.")
elif choices == 4:
    print("Reply hazy, try again.")
elif choices == 5:
    print("Ask again later.")
elif choices == 6:
    print("Better not tell you now.")
elif choices == 7:
    print("My sources say no.")
elif choices == 8:
    print("Outlook not so good.")
else:
    print("Very doubtful.")