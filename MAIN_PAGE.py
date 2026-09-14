

from Manager import manager_menu
from Receptionist import receptionist_menu
from Housekeeping import housekeeping_menu
from Accountant import accountant_menu
from Guest import guest_menu

def MAIN_PAGE():

    while True:
        print("=="*16)
        print(""" WELCOME TO THE STAY EASE HOTEL
        1. Management  
        2. Receptionist  
        3. Accountant 
        4. Housekeeping  
        5. Guest                             
        6. Exit""")
        print("==" * 16)
        enter_choice = int(input("Enter your choice for the following command: "))
        try:
            if enter_choice == 6:
                print("Exiting the Program")
                break
            elif enter_choice == 5:
                guest_menu()
                pass
            elif enter_choice == 4:
                housekeeping_menu()
                pass
            elif enter_choice == 3:
                accountant_menu()
                pass
            elif enter_choice == 2:
                receptionist_menu()
                pass
            elif enter_choice == 1:
                manager_menu()
                pass
            else:
                print("Invalid Choice")
                print("Please enter a valid choice")
        except ValueError:
            print("Invalid Choice")
            print("Please enter a valid choice")

MAIN_PAGE()







