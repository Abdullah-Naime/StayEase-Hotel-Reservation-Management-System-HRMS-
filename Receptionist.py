def read_file(filename):
    data = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                data.append(line.strip().split(','))
    except FileNotFoundError:
        return []
    return data


def write_file(filename, data):
    with open(filename, 'w') as file:
        for record in data:
            file.write(','.join(record) + '\n')

def append_file(filename, record):
    with open(filename, 'a') as file:
        file.write(','.join(record) + '\n')



def receptionist_menu():
    print('RECEPTIONIST MENU')
    while True:
        print("-"*20)
        print("Press 1 to register a new guest")
        print("Press 2 to update guest information")
        print("Press 3 to view room availability")
        print("Press 4 to check-in guest")
        print("Press 5 to check-out guest")
        print("Press 6 to cancel booking")
        print("Press 7 to exit Receptionist menu")

        choice = input("Enter your choice: ")

        if choice == '7':
            print("Exiting Receptionist menu.")
            break

        elif choice == '1':
            print('REGISTER NEW GUEST')
            name = input("Enter guest name: ")
            identification = input("Enter guest ID: ")
            phone = input("Enter guest phone number: ")
            email = input("Enter guest email: ")

            if name == "" or identification == "" or phone == "" or email == "":
                print("Error: All fields are required.")
            else:
                guests = read_file('guests.txt')
                highest_id = 0
                for guest in guests:
                    if int(guest[0]) > highest_id:
                        highest_id = int(guest[0])
                new_guest_id = highest_id + 1
                append_file('guests.txt', [str(new_guest_id), name, identification, phone, email])
                print(f"Guest registered successfully with Guest ID: {new_guest_id}")

        elif choice == '2':
            print('UPDATE GUEST INFORMATION')
            search_id = input("Enter Guest ID to update: ")
            guests = read_file('guests.txt')
            found = False

            for guest in guests:
                if guest[0] == search_id:
                    found = True
                    new_name = input("Enter new name (leave blank to keep current): ")
                    new_identification = input("Enter new ID (leave blank to keep current): ")
                    new_phone = input("Enter new phone (leave blank to keep current): ")
                    new_email = input("Enter new email (leave blank to keep current): ")

                    if new_name != "":
                        guest[1] = new_name
                    if new_identification != "":
                        guest[2] = new_identification
                    if new_phone != "":
                        guest[3] = new_phone
                    if new_email != "":
                        guest[4] = new_email

            if not found:
                print("Error: Guest ID not found.")
            else:
                write_file('guests.txt', guests)
                print("Guest information updated successfully.")

        elif choice == '3':
            print('VIEW ROOM AVAILABILITY')
            rooms = read_file('rooms.txt')
            for room in rooms:
                print("Room:", room[0], "| Type:", room[1], "| Price:", room[4], "| Status:", room[5])

        elif choice == '4':
            print('CHECK-IN GUEST')
            guest_id = input("Enter Guest ID: ")

            guests = read_file('guests.txt')
            guest_exists = any(guest[0] == guest_id for guest in guests)

            if not guest_exists:
                print("Error: Guest not found, register guest first.")
            else:
                rooms = read_file('rooms.txt')
                print("Available rooms:")
                for room in rooms:
                    if room[5] == 'AVAILABLE':
                        print("Room:", room[0], "| Type:", room[1], "| Price:", room[4])

                selected_room = input("Enter Room ID to assign: ")

                room_found = False
                for room in rooms:
                    if room[0] == selected_room and room[5] == 'AVAILABLE':
                        room_found = True
                        room[5] = 'OCCUPIED'

                if not room_found:
                    print("Error: Room not available.")
                else:
                    checkin_date = input("Enter check-in date (DD-MM-YYYY): ")
                    checkout_date = input("Enter expected check-out date (DD-MM-YYYY): ")

                    bookings = read_file('bookings.txt')
                    highest_booking_id = 0
                    for booking in bookings:
                        if int(booking[0]) > highest_booking_id:
                            highest_booking_id = int(booking[0])

                    new_booking_id = highest_booking_id + 1
                    append_file('bookings.txt', [str(new_booking_id), guest_id, selected_room, checkin_date, checkout_date, 'CHECKED-IN'])
                    write_file('rooms.txt', rooms)
                    print(f"Guest checked in successfully with Booking ID: {new_booking_id}")

        elif choice == '5':
            print('CHECK-OUT GUEST')
            booking_id = input("Enter Booking ID: ")

            bookings = read_file('bookings.txt')
            rooms = read_file('rooms.txt')
            found = False

            for booking in bookings:
                if booking[0] == booking_id and booking[5] == 'CHECKED-IN':
                    found = True
                    booking[5] = 'CHECKED-OUT'
                    room_id = booking[2]

                    for room in rooms:
                        if room[0] == room_id:
                            room[5] = 'AVAILABLE'
            if not found:
                print("Error: Booking ID not found or guest already checked out.")
            else:
                write_file('bookings.txt', bookings)
                write_file('rooms.txt', rooms)
                print("Guest checked out successfully. Direct guest to Accountant for billing.")

        elif choice == '6':
            print('CANCEL BOOKING')
            booking_id = input("Enter Booking ID to cancel: ")

            bookings = read_file('bookings.txt')
            rooms = read_file('rooms.txt')
            found = False

            for booking in bookings:
                if booking[0] == booking_id and booking[5] == 'CHECKED-IN':
                    found = True
                    booking[5] = 'CANCELLED'
                    room_id = booking[2]

                    for room in rooms:
                        if room[0] == room_id:
                            room[5] = 'AVAILABLE'
            if not found:
                print("Error: Booking ID not found or cannot cancel checked-out booking.")
            else:
                write_file('bookings.txt', bookings)
                write_file('rooms.txt', rooms)
                print("Booking cancelled successfully.")

