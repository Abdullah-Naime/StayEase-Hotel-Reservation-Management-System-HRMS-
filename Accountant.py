#Accountant - TP091840

PAYMENTS_FILE = "payments.txt"
BOOKINGS_FILE = "bookings.txt"
DAILY_LOGS_FILE = "daily_logs.txt"

def accountant_menu():
    while True:#loops forever until exit option chosen.
        print("\n=== ACCOUNTING SYSTEM ===")
        print("1. Record Payment")
        print("2. Generate Income Report")
        print("3. View Outstanding Payments")
        print("4. Generate Monthly Financial Summary")
        print("5. Exit Accounting System")

        choice = input("Enter your choice: ")#asks user to enter choice

        if choice == "1":#calls a different function for every number between 1 and 5 chosen
            record_payment()
        elif choice == "2":
            generate_income_report()
        elif choice == "3":
            view_outstanding_payments()
        elif choice == "4":
            monthly_financial_summary()
        elif choice == "5":
            print("Exiting Accounting System...")
            break
        else:
            print("Invalid choice. Try again.")
def record_payment():
    print("\n=== RECORD PAYMENT ===")

    booking_id = input("Enter Booking ID: ")

    booking_found = False #sets booking to not found until a file is found
    try:
        with open(BOOKINGS_FILE, "r") as file:
            for line in file:
                if line.startswith(booking_id + ","):
                    booking_found = True
                    break
    except FileNotFoundError: #if the booking file is not found, error is shown
        print("Bookings file not found.")
        return

    if not booking_found: #if booking record is not found, error is shown
        print("Booking ID not found.")
        return

    amount = input("Enter Payment Amount: ")
    while not amount.isdigit(): #checks if the amount entered is a number, error displayed if not.
        amount = input("Invalid amount. Enter numbers only: ")

    status = input("Enter Payment Status (Paid/Unpaid): ").capitalize()
    while status not in ["Paid", "Unpaid"]: #only valid characters entered are Paid or Unpaid
        status = input("Enter Paid or Unpaid only: ").capitalize()

    date = input("Enter Payment Date (YYYY-MM-DD): ")

    with open(PAYMENTS_FILE, "a") as file: #writes the payment details in certain order
        file.write(f"{booking_id},{amount},{date},{status}\n")

    with open(DAILY_LOGS_FILE, "a") as log: #writes into daily logs file in a certain order
        log.write(f"{date},PAYMENT,{booking_id},Payment RM {amount} recorded\n")

    print("Payment successfully recorded.") #messege shown when record added into payment and daily_logs file
def generate_income_report():
    print("\n=== GENERATING INCOME REPORT ===")

    total_income = 0 #variable declared to print later

    try:
        with open(PAYMENTS_FILE, "r") as file: #opens the file as reading access
            for line in file: #goes line by line
                booking_id, amount, date, status = line.strip().split(",") #removes white spaces and recognises separate fields with a comma
                if status == "Paid":
                    total_income += int(amount) #added the amount if the status is 'paid'
    except FileNotFoundError:
        print("Payments file not found.")#if the payments file not found, error shown
        return

    print("Total Income Collected: RM", total_income)
def view_outstanding_payments():
    print("\n=== OUTSTANDING PAYMENTS ===")
    found = False #sets the outstanding payments as not found until found

    try:
        with open(PAYMENTS_FILE, "r") as file: #opens the file as reading access
            for line in file:
                booking_id, amount, date, status = line.strip().split(",")#removes white spaces and recognises separate fields with a comma
                if status == "Unpaid":
                    print("Booking ID:", booking_id)
                    print("Amount Due: RM", amount)
                    print("Date Recorded:", date)
                    print("-------------------------")
                    found = True #this is set to true when the outstanding payments are found
    except FileNotFoundError:
        print("Payments file not found.")
        return

    if not found:
        print("No outstanding payments.")
def monthly_financial_summary():
    print("\n=== MONTHLY FINANCIAL SUMMARY ===")

    selected_month = input("Enter Month (YYYY-MM): ")

    paid_total = 0 #declares variables to use later
    unpaid_total = 0

    try:
        with open(PAYMENTS_FILE, "r") as file: #opens file with reading access
            for line in file:
                booking_id, amount, date, status = line.strip().split(",")#removes white spaces and recognises separate fields with a comma

                if date.startswith(selected_month):
                    if status == "Paid":
                        paid_total += int(amount) #added to paid total if status is paid
                    else:
                        unpaid_total += int(amount) #added to unpaid total if status is unpaid
    except FileNotFoundError:
        print("Payments file not found.")#if file not found,error is shown
        return

    print("Monthly Summary for", selected_month) #prints all details
    print("Total Paid: RM", paid_total)
    print("Total Unpaid: RM", unpaid_total)

