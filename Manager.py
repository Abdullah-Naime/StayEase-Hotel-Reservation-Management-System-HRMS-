from Managing_rooms import managing_rooms
from system_summary import view_summary
from Monthly_daily_reports import view_report
def manager_menu():
    while True:
        print("""WELCOME TO MANAGER MENU
            1.MANAGE ROOM RECORDS
            2.VIEW SYSTEM SUMMARY
            3.GENERATE DAILY AND MONTHLY PERFORMANCE REPORT
            4.EXIT""")
        try:
            Choice = int(input("Enter your choice for the following command: "))
            if Choice == 4:
                print("exiting the program")
                break
            elif Choice == 3:
                view_report()
            elif Choice == 2:
                view_summary()
            elif Choice == 1:
                managing_rooms()
            else:
                print("Invalid choice please try enter another value")
        except ValueError:
            print("Invalid choice please try entering a number instead")


manager_menu()

