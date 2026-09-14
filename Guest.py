# need to display guest ID from the first section. Also display extra need to know details like "booking ID", "room ID", and "payment ID" IF possible.
# second section I should also make a print comment saying "and successfully made a reservation" and just in case if its already a booked room, make another comment stating that its "already reserved, please pick another one". Also one final adjustment, make the list of reservations tidy (format wise)
# before asking for booking ID, I should display the available booking ID made, by that specific user (probably complicated)


# VALIDATION code for entering specific data
def date_validation(date):
    try:
        if len(date) == 10 and int(date[0:4]) and int(date[5:7]) and int(date[-2:]) and date.count('-') == 2:
            return True
        else:
            return False
    except ValueError:
        return False

def room_validation(guest_ID):
    try:
        with open("rooms.txt", "r") as f:
            lines = f.read().splitlines()
            for record in lines:
                if record.split(',')[0] == guest_ID:
                    return True
    except FileNotFoundError:
        print("rooms.txt file not found")
    return False

def payment_id_validation(payment_id):
    try:
        with open("payments.txt", "r") as f:
            lines = f.read().splitlines()
            for record in lines:
                if record.split(',')[0] == payment_id:
                    return True
    except FileNotFoundError:
        print("payments.txt file not found")
    return False

def booking_id_validation(booking_id):
    try:
        with open("bookings.txt", "r") as f:
            lines = f.read().splitlines()
            for record in lines:
                if record.split(',')[0] == booking_id:
                    return True
    except FileNotFoundError:
        print("bookings.txt file not found")
    return False






#2. reservation
def append_file(filename, record):
    with open("bookings.txt", "a") as f:
        f.write(",".join(map(str, record)) + "\n")



def make_reservation():
    print("Make a reservation")

#this function displays all the available rooms
    available_rooms()


    selected_room = input("\nTo reserve, please enter your room ID: ")
    while not room_validation(selected_room):

        selected_room = input("\nPlease enter a valid room ID: ")
    print("You selected: ", selected_room)

# Get check-in/check-out dates
    checkin_date = input("Enter check-in date (YYYY-MM-DD): ")
    while not date_validation(checkin_date):
        checkin_date = input("\nInvalid date format\nPlease enter a valid date (YYYY-MM-DD): ")

    checkout_date = input("Enter check-out date (YYYY-MM-DD): ")
    while not date_validation(checkout_date):
        checkout_date = input("\nInvalid date format\nPlease enter a valid date (YYYY-MM-DD): ")

#Read bookings file
    with open("bookings.txt", "r") as f:
        bookings = f.read().splitlines()

    highest_booking_id = 0
    highest_guest_id = 0

    for booking in bookings:
        record = booking.split(",")
        booking_id = int(record[0])
        guest_id = int(record[1])

        if booking_id > highest_booking_id:
            highest_booking_id = booking_id
        if guest_id > highest_guest_id:
            highest_guest_id = guest_id


    new_booking_id = highest_booking_id + 1
    new_guest_id = highest_guest_id + 1
    append_file(
        "bookings.txt", [str(new_booking_id), str(new_guest_id), selected_room, checkin_date, checkout_date, 'CHECKED-IN'])
    room = ("rooms.txt", "w")
    print(f"You have successfully booked a reservation, your Booking ID: {new_booking_id}")

#Word difference between "booked" and "checked-in" reasoning: the guest module only reserves the status with booked while the physical status "checked-in" only applies when the customer shows up to the receptionist, which then updates to "checked-in"


#3. Cancelling reservation
def cancel_reservation():
    print("Cancel reservation(s)")

    booking_ID = input("Enter your booking ID: ")
    while not booking_id_validation(booking_ID):
        booking_ID = input("\nPlease enter a valid booking ID: ")
    print("Booking ID is", booking_ID)

    roomID = ""
    list_of_bookings = []
    list_of_rooms = []

    try:
        with open("bookings.txt", "r") as f:
            bookings = f.read().splitlines()
            for booking in bookings:
                record = booking.split(",")
                if record[0] == booking_ID:
                    record[5] = "CHECKED_OUT"

                    roomID = record[2]
                list_of_bookings.append(",".join(record))

        with open("bookings.txt", "w") as f:
            for record in list_of_bookings:
                f.writelines(record + "\n")
    except FileNotFoundError:
        print("No bookings file can be found")

    try:
        with open("rooms.txt", "r") as f:
            rooms = f.read().splitlines()
            for room in rooms:
                record = room.split(",")
                if record[0] == roomID:
                    record[5] = "AVAILABLE"
                list_of_rooms.append(",".join(record))


        with open("rooms.txt", "w") as f:
            for record in list_of_rooms:
                f.writelines(record + "\n")

        print("Successfully canceled reservation")
    except FileNotFoundError:
        print("No rooms file can be found")






#4. View billing summary
def view_billing():
    found = False

    print("View billing summary\n====================")

    booking_ID = input("Enter your Booking ID: ")

    try:
        with open("payments.txt", "r") as f:
            payments = f.read().splitlines()

            for payment in payments:
                record = payment.split(",")
                if record[0] == booking_ID:
                    found = True
                    print(
                        "Amount: ", record[1],
                        "| Date: ", record[2],
                        "| Status: ", record[3]
                    )
                    break

            if not found:
                print("Try again, this either may be invalid or is wrongfully written")


    except FileNotFoundError:
        print("No payments file can be found")

#Billing summary is a read-only function that displays payment records; payment creation is handled by another role.



#1. Viewing available rooms
def available_rooms():
    print("Available rooms")

    found = False  #this is later useful for if statement when no rooms are available


    try:
        with open("rooms.txt", "r") as f:
            for x in f:
                room = x.strip().split(",")

                if room[5] == "AVAILABLE":
                    found = True
                    print(
                        "| Room ID: ", room[0], "\t"
                        "| Occupancy:", room[2],"\t\t",
                        "| Price:", room[4],"\t\t",
                    )
    except FileNotFoundError:
        print("No rooms file can be found")
        return

    if not found:
       print("Sorry, no available rooms can be found")
 #   f.close() is NOT needed since with open() as f: automatically closes the file








# MAIN MENU
def guest_menu():

    while True:
        try:
            print("="*40,"\n")
            print("Welcome to The Guest Menu")
            print("1. View available rooms")
            print("2. Make a reservation")
            print("3. Cancel a reservation")
            print("4. View billing summary")
            print("5. Exit")

            choice = int(input("Enter your choice: "))
            print("")

            if choice == 1:
                available_rooms()
            elif choice == 2:
                make_reservation()
            elif choice == 3:
                cancel_reservation()
            elif choice == 4:
                view_billing()
            elif choice == 5:
                print("Exiting Guest Menu")
                break
            else:
                print("Invalid choice")
        except ValueError:
            print("Please enter a numeric value only")

guest_menu()


