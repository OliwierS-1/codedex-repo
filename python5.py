gryffindor = 0
hufflepuff = 0
ravenclaw = 0
slytherin = 0

question1 = int(input('Q1) Do you like Dawn or Dusk? \n1) for Dawn\n2) for Dusk: '))

if question1 == 1:
    gryffindor += 1
    ravenclaw += 1
elif question1 == 2:
    hufflepuff += 1
    slytherin += 1
else:
    print("Invalid input. Please enter 1 or 2.")

question2 = int(input('Q2) When I\'m dead, I want people to remember me as: \n1) The Good\n2) The Great\n3) The Wise\n4) The Bold: '))

if question2 == 1:
    hufflepuff += 2
elif question2 == 2:
    slytherin += 2
elif question2 == 3:
    ravenclaw += 2
elif question2 == 4:
    gryffindor += 2
else:
    print("Invalid input. Please enter a number between 1 and 4.")

question3 = int(input('Q3) Which kind of instrument most pleases your ear? \n1) The violin\n2) The trumpet\n3) The piano\n4) The drum: '))

if question3 == 1:
    slytherin += 4
elif question3 == 2:
    hufflepuff += 4
elif question3 == 3:
    ravenclaw += 4
elif question3 == 4:
    gryffindor += 4
else:
    print("Invalid input. Please enter a number between 1 and 4.")

if gryffindor > hufflepuff and gryffindor > ravenclaw and gryffindor > slytherin:
    print("You belong to Gryffindor!")
elif hufflepuff > ravenclaw and hufflepuff > slytherin:
    print("You belong to Hufflepuff!")
elif ravenclaw > slytherin:
    print("You belong to Ravenclaw!")
else:
    print("You belong to Slytherin!")