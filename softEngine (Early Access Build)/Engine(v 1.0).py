user = input("Enter a username: ")

print(user, "logged in.")

while True:
    mode = input("Enter your desired mode (Addition, Subtraction, Multiplication, Division.): ")

    if mode == 'Addition':
        Message1p1 = int(input("Enter Value A"))
        Message1p2 = int(input("Enter Value B"))

        CrazyMATHZ = (Message1p1 + Message1p2)
        print("Result:", CrazyMATHZ)

    elif mode == 'Subtraction':
        Message2p1 = int(input("Enter Value A"))
        Message2p2 = int(input("Enter Value B"))

        CrazyMATHZ2 = (Message2p1 - Message2p2)
        print("Result:", CrazyMATHZ2)

    elif mode == 'Multiplication':
        Message3p1 = int(input("Enter Value A"))
        Message3p2 = int(input("Enter Value B"))

        CrazyMATHZ3 = (Message3p1 * Message3p2)
        print("Result:", CrazyMATHZ3)

    elif mode == 'Division':
        Message4p1 = int(input("Enter Value A"))
        Message4p2 = int(input("Enter Value B"))

        CrazyMATHZ4 = (Message4p1 / Message4p2)
        print("Result:", CrazyMATHZ4)
        
    else:
        print("ERROR: Mode not recognised. Input *is* case sensitive.")
        
