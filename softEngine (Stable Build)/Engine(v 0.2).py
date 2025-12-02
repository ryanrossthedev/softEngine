user = input("Enter a username: ")

print(user, "logged in.")

while True:
    mode = input("Enter your desired mode (Big Back or Stickman): ")

    if mode == 'Big Back':
        Message = input("What is your favourite KFC bundle??")

        CrazyMATHZ = (user, " likes ", Message)
        print("Result:", CrazyMATHZ)

    elif mode == 'Stickman':
        Message2 = input("What is your favourite small sized dish?")

        CrazyMATHZm = (user, " likes ", Message2)
        print("Result:", CrazyMATHZm)

    else:
        print("ERROR: Mode not recognised. Input *is* case sensitive.")

