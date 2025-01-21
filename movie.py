import datetime
while(True):
    print("Available Movies:\n 1.Interstellar\n 2.Empuran\n 3.Rekhachithram ")
    movie = int(input("Select Movie (1 - 3) :").strip())
    ticket_No = int(input("Enter number of Tickets : ").strip())
    types = int(input("Select Ticket Type :\n 1.Premium 2.Normal").strip())
    print("Select showtime")
    timing = int(input("1. 10.00 AM\t2. 2:00 PM\t3. 5:00 PM\n").strip())
    premium = 200
    normal = 150
    if types == 1:
        totalCost = premium*ticket_No
    else:
        totalCost = normal*ticket_No
    if ticket_No >= 5:
        totalCost -= totalCost * .10
    totalCost = int(totalCost)
    print("===========================================================")
    print("Ticket Details : ")
    if movie == 1:
        print("Movie : Interstellar")
    elif movie == 2:
        print("Movie : Empuran")
    else:
        print("Movie : Rekhachithram")
    print("Number Of Tickets : "+str(ticket_No))
    if types == 1:
        print("Ticket Type : Premium")
    else:
        print("Ticket Type : Normal")
    if timing == 1:
        print("Showtime : 10:00 AM")
    elif timing == 2:
        print("Showtime : 2:00 PM")
    else:
        print("Showtime : 5:00 PM")
    day = datetime.datetime.now()
    formatted_datetime = day.strftime("%A %d-%m-%Y")
    print("Day : "+formatted_datetime)
    Total = totalCost
    print(f"Total: Rs. {Total:.2f}")
    print("===========================================================")
    exitPage = input("Do you want to book other ticket or not (YES/NO) : ").upper()
    if exitPage == "NO":
        print("\nThank you for using the Online Movie Ticket Booking System. Goodbye!")
        break


1


