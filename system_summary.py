def view_summary():
    print("     ===SYSTEM SUMMARY===")
    try:
        with open("rooms.txt", "r") as f:
            all_rooms = f.readlines()

    except FileNotFoundError:
        print("rooms.txt file doesn't exist sorry")


    while True:
        print("=="*16)
        print("""press the following to view the system summary:
        1.total booking 
        2.occupancy rate
        3.income.
        4.to EXIT""")
        choice_choice = int(input("Enter your choice for the following: "))
        if choice_choice == 1:
         view_booking()
        elif choice_choice == 2:
         view_occupancy()
        elif choice_choice == 3:
         check_income()
        elif choice_choice == 4:
            print("Exiting the program")
            break

def view_booking():
    print("=== VIEW TOTAL BOOKING ===")
    count_for_checked_in = 0
    count_for_checked_out = 0
    try:
        with open("bookings.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if parts[5] == "CHECKED_IN":
                    count_for_checked_in += 1
                else:
                    count_for_checked_out += 1
    except FileNotFoundError:
        print("bookings.txt does not exist")
        return
    print(f"TOTAL BOOKING: {count_for_checked_in}")
    print(f"check out: {count_for_checked_out}")

def view_occupancy():
    print("=== VIEW OCCUPANCY ===")
    total_rooms_ = 0
    occupied_rooms_ = 0
    try:
        with open("rooms.txt", "r") as f:
            for line in f:
                if line.strip() == "":
                    continue
                parts = line.strip().split(",")
                total_rooms_ += 1
                status = parts[5].strip()
                if status == "OCCUPIED":
                 occupied_rooms_ += 1

    except FileNotFoundError:
        print("rooms.txt file doesn't exist sorry")
        return
    if total_rooms_ > 0:
        rate = (occupied_rooms_ / total_rooms_) * 100
    else:
        rate = 0

    print("==" * 12)
    print(f"TOTAL ROOMS     : {total_rooms_}")
    print(f"OCCUPIED ROOMS  : {occupied_rooms_}")
    print(f"OCCUPANCY RATE  : {rate:.2f}%")
    print("==" * 12)






def check_income():
    print("=== INCOME CHECK ===")
    total_income = 0.0
    try:
        with open("payments.txt", "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("payments.txt file doesn't exist sorry")
        return
    for line in lines:
        line = line.strip()
        if line == "":
            continue
        each_detail = line.split(",")
        amount_per_room = each_detail[1].strip()
        status = each_detail[3].strip()

        if status == "Paid":
            try:
                total_income += float(amount_per_room)
            except ValueError:
                print("ERROR AMOUNT:", amount_per_room)

    print(f"TOTAL INCOME: RM {total_income:.2f}")






