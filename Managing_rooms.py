


def managing_rooms():
        while True:
            print("\n===== MANAGER ROOM MANAGEMENT =====")
            print("1. Add Room")
            print("2. Update Room")
            print("3. Remove Room")
            print("4. View Rooms")
            print("5. Exit")
            choice = input("Enter your choice to change the rooms: ")
            if choice == "1":
                add_room()
            elif choice == "2":
              update_room()
            elif choice == "3":
               remove_room()
            elif choice == "4":
                view_rooms()
            elif choice == "5":
                print("Exit")
                break
            else:
                print("wrong choice please put a valid choice")


def add_room():
    print("===== ADD ROOM =====")
    floor_number = input("Enter the floor from 1 to 4: ").strip()
    room_type_ = input("Enter room type (STD-S / STD-Q / DLX-Q / DLX-T / DLX-3 / FAM) to add: ").strip().upper()
    number_of_room = int(input("Enter room number: "))
    if room_type_ == "STD-S":
        occupancy, rate = "Single", 109
    elif room_type_ == "STD-Q":
        occupancy, rate = "Queen", 125
    elif room_type_ == "DLX-Q":
        occupancy, rate = "Queen", 159
    elif room_type_ == "DLX-T":
        occupancy, rate = "Twin", 167
    elif room_type_ == "DLX-3":
        occupancy, rate = "Triple", 189
    elif room_type_ == "FAM":
        occupancy, rate = "Family", 200
    else:
        print("Wrong choice. Please enter a valid room type.")
        return
    room_id = f"F{floor_number}{room_type_}{number_of_room}"
    status = "AVAILABLE"
    with open("rooms.txt", "a") as f:
        f.write(f"{room_id},{room_type_},{occupancy},{floor_number},{rate},{status}\n")
    print(f"Room {room_id} added to the rooms.txt file")


def update_room():
    print("===== UPDATE ROOM =====")
    room_to_update = input("Enter room ID to update: ").strip()
    try:
        with open("rooms.txt", "r") as f:
            all_rooms = f.readlines()
    except FileNotFoundError:
        print("rooms.txt file doesn't exist sorry")
        return
    updated_lines = []
    found = False
    for line in all_rooms:
        each_detail = line.strip().split(",")
        if each_detail[0] == room_to_update:
            current_status = each_detail[5]
            print(f"Room {room_to_update} found. Current status: {current_status}")
            print("PLEASE ALTER THE ROOM STATUS based on the liking:")
            print("1. AVAILABLE")
            print("2. UNDER MAINTENANCE")
            print("3. OCCUPIED")
            change_option = input("Enter your choice (1/2/3): ").strip()
            if change_option == "1":
                new_status = "AVAILABLE"
            elif change_option == "2":
                new_status = "UNDER MAINTENANCE"
            elif change_option == "3":
                new_status = "OCCUPIED"
            else:
                print("Wrong choice please put a valid choice.")
                return
            updated_line = f"{each_detail[0]},{each_detail[1]},{each_detail[2]},{each_detail[3]},{each_detail[4]},{new_status}\n"
            updated_lines.append(updated_line)
            found = True
        else:
            updated_lines.append(line)
    if not found:
        print("Room not found.")
        return
    with open("rooms.txt", "w") as f:
        f.writelines(updated_lines)
    print("Room status updated successfully to the room.txt file")


def remove_room():
    room_to_remove = input("Enter Room ID to remove (e.g., F1STD-S1): ").strip()

    try:
        with open("rooms.txt", "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("rooms.txt file doesn't exist sorry")
        return

    new_lines = []
    found = False
    for line in lines:
        if line.strip() == "":
            continue
        if line.split(",")[0].strip() == room_to_remove:
            found = True
        else:
            new_lines.append(line)
    if not found:
        print(f"Room {room_to_remove} not found.")
    else:
        with open("rooms.txt", "w") as f:
            f.writelines(new_lines)
        print(f"{room_to_remove} removed.")


def view_rooms():
    print("=== VIEW ALL THE ROOMS===\n")
    try:
        with open("rooms.txt", "r") as f:
            print("all room details as shown below")
            print(f.read())
    except FileNotFoundError:
        print("rooms.txt file doesn't exist sorry")
        print("please try again")















