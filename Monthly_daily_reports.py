
def view_report():
    while True:
        print("""PRESS FOR THE FOLLOWING PLEASE
           1 FOR DAILY REPORTS
           2 FOR MONTHLY REPORTS
           3 FOR EXIT""""")
        choice = input("Enter Choice for: ")
        if choice == "1":
            generate_daily_reports()
        elif choice == "2":
            generate_monthly_reports()
        elif choice == "3":
            print("Exiting the program")
            break
        else:
            print("Wrong Choice please try again")

def generate_daily_reports():
    target_date = input("Enter the date (YYYY-MM-DD): ").strip()
    print(f"\n===== DAILY REPORT: {target_date} =====")
    total_bookings = 0
    try:
        with open("bookings.txt", "r") as f:
            for line in f:
                line = line.strip()
                if line == "":
                    continue
                parts = line.split(",")
                check_in_date = parts[3]
                status = parts[5]
                if check_in_date == target_date and status == "CHECKED_IN":
                    total_bookings += 1
    except FileNotFoundError:
        print("bookings.txt not found!")
    total_income = 0.0
    try:
        with open("payments.txt", "r") as f:
            for line in f:
                line = line.strip()
                if line == "":
                    continue
                parts = line.split(",")
                pay_date = parts[2]
                status = parts[3]
                if pay_date == target_date and status == "Paid":
                    total_income += float(parts[1])
    except FileNotFoundError:
        print("payments.txt not found!")
    print(f"Total Bookings: {total_bookings}")
    print(f"Total Income (RM): {total_income:.2f}")





def generate_monthly_reports():
    target_month = input("Enter the month (YYYY-MM): ").strip()
    print(f"\n===== MONTHLY REPORT: {target_month} =====")
    monthly_bookings = 0
    try:
        with open("bookings.txt", "r") as f:
            for line in f:
                line = line.strip()
                if line == "":
                    continue
                parts = line.split(",")
                check_in_date = parts[3]
                status = parts[5]
                if check_in_date.startswith(target_month) and status == "CHECKED_IN":
                    monthly_bookings += 1
    except FileNotFoundError:
        print("bookings.txt not found!")
    monthly_income = 0.0
    try:
        with open("payments.txt", "r") as f:
            for line in f:
                line = line.strip()
                if line == "":
                    continue
                parts = line.split(",")
                pay_date = parts[2]
                status = parts[3]
                if pay_date.startswith(target_month) and status == "Paid":
                    monthly_income += float(parts[1])
    except FileNotFoundError:
        print("payments.txt not found!")
    except ValueError:
        pass
    print(f"Total Bookings: {monthly_bookings}")
    print(f"Total Income (RM): {monthly_income:.2f}")











