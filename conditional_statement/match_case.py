a = int(input("Enter a lucky number between 1 to 10:"))

match a:
    case 1:
        print("You won  a charger")

    case 2:
        print("You won  a chipsr") 

    case 3:
        print("You won  a candy") 

    case 4:
        print("You won a lighter")

    case 5:
        print("You won a bicycle")

    case 6:
        print("You won a camera")

    case 7:
        print("You won a lottary")

    case _:
        print("Better luck next time")