user = input("Enter a username: ")

print(user, "logged in.")

while True:
    mode = input("Enter your desired mode (Addition or Multiplication): ")

    if mode == 'Addition':
        ValA = int(input("Enter your desired number for Value A: "))
        ValB = int(input("Enter your desired number for Value B: "))

        CrazyMATHZ = ValA + ValB
        print("Result:", CrazyMATHZ)

    elif mode == 'Multiplication':
        ValAM = int(input("Enter your desired number for Value A: "))
        ValBM = int(input("Enter your desired number for Value B: "))

        CrazyMATHZm = ValAM * ValBM
        print("Result:", CrazyMATHZm)

    else:
        print("ERROR: Mode not recognised. Input *is* case sensitive. Ensure correct spelling.")

