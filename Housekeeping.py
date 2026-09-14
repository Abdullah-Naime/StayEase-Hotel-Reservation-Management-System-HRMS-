"""

    The housekeeping application is only authorized for the Admin and Housekeepers only

"""

"""
    - The function below take in its parameter, a file path, and a set of key(s) inside a tuple to read files easily.
    - The function reads each lines of a file, and uses the keys contained inside the tuple to create dictionaries.
    - Each record is assigned into a dictionary, making it easier to manipulate values inside the file.
    - Finally, these arrays of dictionaries are appended to a list and returned by value.
"""

def return_key_values(file_path, tuple_of_keys):
    list_of_values = [] # Empty list

    try:
        with open(file_path, 'r') as housekeeping_file: # File opened for read
            list_of_records = housekeeping_file.read().splitlines()
            for record in list_of_records:
                dictionary_of_values = { } # Empty dictionary

                # Code below assigns the values in each record to its matching Key Pairs from the Keys inside the tuple
                for i in range(0, len(tuple_of_keys)): # Loops through the tuple to reference Keys

                    tuple_key = tuple_of_keys[i] # Key
                    value = record.split(',')[i] # Value
                    dictionary_of_values.update({tuple_key:value}) # Uses the keys from the tuple and assigns the value

                list_of_values.append(dictionary_of_values) # Appends the dictionary to the list of values
    except FileNotFoundError:
        print(f"File at {file_path} was not found")
    return list_of_values

#=======================================================================================================================

"""
    
    - The function below take in its parameter, a file path, a tuple of values to add to file, the specified Open Mode, 
        and the Success Message.
    - The function, depending on the open mode, will write or append the values in a comma separated format.
    - The values are concatenated together separated by a comma and are appended or overwritten in the file.
    
"""

def set_key_values(file_path, tuple_of_values, open_mode, success_message):
    try:
        if open_mode == 'a': # If requested Open Mode is 'append'
            with open(file_path, open_mode) as housekeeping_file:

                for values in tuple_of_values:
                    record = []
                    for key, value in values.items():
                        record.append(value)
                    housekeeping_file.writelines(','.join(record) + '\n')

        elif open_mode == 'w': # If requested Open Mode is 'Write'
            with open(file_path, open_mode) as housekeeping_file:

                for values in tuple_of_values:
                    record = []
                    for key, value in values.items():
                        record.append(value)
                    housekeeping_file.writelines(','.join(record) + '\n')

    except FileNotFoundError:
        print(f"File at {file_path} was not found")
    print(success_message)

#=======================================================================================================================

"""

    - The function below validates the room number.
    - The function uses the room number passed as an argument and gets record of rooms.
    - The room id passed as an argument is compared to the rooms in extracted record and checks if room exist.
    - Returns True if the comparison exists, and false if it doesn't.

"""

def room_validation(room_id): # Room Number passed as an argument
    records = return_key_values('Room_Cleaning_Status.txt', ('RoomId', 'Cleaned')) # Gets file records as a list of dictionaries

    for record in records:
        if record['RoomId'] == room_id: # Compares records of rooms with passed room number
            return True
    return False

#=======================================================================================================================

"""

    - The function below validates that the input date matches the given format (yyyy-MM-dd).
    - Function returns false if the dates at specific locations of the string can be cast as integer, 
        the length of string provided is 10 characters long and there are exactly 2 '-' symbols.
    - Function returns true if this criteria is met.
    
"""

def date_validation(date):
    try: # Exception to catch value error if integer cast fails
        if len(date) == 10 and int(date[0:4]) and int(date[5:7]) and int(date[-2:]) and date.count('-') == 2:
            return True
        else:
            return False
    except ValueError:
        return False

#=======================================================================================================================

"""
    
    - The function below allows the user to Report any Maintenance Issues.
    - The function takes today's date as a parameter, asks the user to enter a valid room number and the maintenance 
        issue.
    - Those details are assigned to a dictionary stored inside a tuple so it can be sent to the maintenance log file.
    - This is so that the value inside the tuple cannot be altered when sent to the function.
    
"""

def send_to_maintenance_log(date):

    room_number = input('Enter the room number: ') # Asks for valid room number
    while not room_validation(room_number):
        room_number = input('Room Number does not exist!\nEnter the room number: ')

    maintenance_issue = input('What seems to be the issue?\n') # Asks the user to enter maintenance issue

    # The line below assigns these data to a dictionary inside a tuple.
    tuple_with_values = ({'Date': date, 'RoomId': room_number, 'Comment': maintenance_issue},)

    # The line below calls set_key_values with parameters File Path, values to be stored, Open Mode (Append) and the message when operation is successful
    set_key_values('Maintenance_Log.txt', tuple_with_values, 'a', 'Maintenance issue was successfully reported')

#=======================================================================================================================

"""

    - The function below changes the status of rooms from False (Uncleaned) to True (Cleaned)
    - The function calls return_key_values to retrieve values from file as a list of dictionaries.
    - Asks the user to enter a valid room number and lookup through the list of records for the requested room number
    - If the status of the room was False (Uncleaned), the status is changed to True (Cleaned), otherwise, no actions 
        are performed.
    - The function then casts the list of dictionaries into a tuple, so the value doesn't change, and writes these
        records to the file.
    - Moreover, the function then logs this event into the cleaning log as a proof of action
    
"""

def set_cleaning_status():

    # Line below retrieves all records of room cleaning status as a list of dictionaries, with the Key RoomId & Cleaned
    record_of_statuses = return_key_values('Room_Cleaning_Status.txt', ('RoomId', 'Cleaned'))

    room_number = input('Enter the room number: ') # Asks user for valid Room Number
    while not room_validation(room_number):
        room_number = input('Room Number does not exist!\nEnter the room number: ')

    for record in record_of_statuses: # Loops through the list of dictionaries
        if record['RoomId'] == room_number and record['Cleaned'] == 'False': # Checks if room number matches and not cleaned
            print("This part was reached")
            record['Cleaned'] = 'True' # Sets cleaning status to True (Cleaned)


    tuple_with_values = tuple(record_of_statuses) # Casts list of dictionaries to a tuple of dictionaries

    # The line below calls set_key_values with parameters File Path, values to be stored, Open Mode (Append) and the message when operation is successful
    set_key_values('Room_Cleaning_Status.txt', tuple_with_values, 'w', f'Room {room_number} cleaning status was changed to Clean')

    # The code below calls send_to_cleaning_log() to log this change to the cleaning log
    today_date = input('Enter the date of today (yyyy-MM-dd): ') # Asks user for valid date
    while not date_validation(today_date):
        today_date = input('Invalid Date Format!\nEnter the date of today(yyyy-MM-dd): ')

    send_to_cleaning_log(today_date, room_number)

#=======================================================================================================================

"""

    - The function below logs any cleaning events to the Cleaning_Log.txt text files.
    - The function takes Today's date as a parameter, asks the user to enter a valid room number and the log comment.
    - The function stores these values into a dictionary inside a tuple and appends it to the Cleaning_Log.txt file.

"""

def send_to_cleaning_log(date, room_number):

    cleaning_comments = input('Enter the comment: ') # Asks user for comments

    tuple_with_values = ({'Date': date, 'RoomId': room_number, 'Comment': cleaning_comments},) # Creates a dictionary inside tuple

    # The line below calls set_key_values with parameters File Path, values to be stored, Open Mode (Append) and the message when operation is successful
    set_key_values('Cleaning_Log.txt', tuple_with_values, 'a', f'Cleaning status was changed for {room_number}')

#=======================================================================================================================

"""

    - The function below displays a list of rooms with the statuses Not Cleaned and Cleaned.
    - The function retrieves records as a list of dictionaries with the Keys RoomId and Cleaned.
    - The function loops through the list and displays all the Uncleaned Rooms and Cleaned Rooms separately.

"""

def get_daily_cleaning_schedule():

    # Line below retrieves all records of room cleaning status as a list of dictionaries, with the Key RoomId & Cleaned
    records = return_key_values('Room_Cleaning_Status.txt', ('RoomId', 'Cleaned'))

    # The Loop below goes through the list of dictionaries and displays the Uncleaned Rooms in a formal format
    for record in records:
        if record['Cleaned'] == 'False': # Checks if room is Not Cleaned
            print(f"Room: {record['RoomId']}\t\tCleaning Status: Not Cleaned") # Displays the Room Number and Status

    print("\n")

    # The Loop below goes through the list of dictionaries and displays the Cleaned Rooms in a formal format
    for record in records:
        if record['Cleaned'] == 'True': # Checks if room is Cleaned
            print(f"Room: {record['RoomId']}\t\tCleaning Status: Cleaned") # Displays the Room Number and Status

#=======================================================================================================================

"""

    - The function below is the main stem of the housekeeping section
    - The function below displays a menu of option, allowing the user to enter their choice
    - The function validates the choice and calls their respected function or exits the program when Choice = 4

"""

def housekeeping_menu():

    while True:
        try: # Exception prevents program from crashing if user does not enter an integer

            # The code below displays the main menu
            print("\n\nWELCOME TO HOUSEKEEPING")
            print("=" * 40)
            print("1. Update Cleaning Status")
            print("2. Report Maintenance Issue")
            print("3. View Daily Cleaning Schedule")
            print("4. Exit")
            print("=" * 40)

            choice = int(input("Enter your choice: "))

            if choice == 1:
                # Calls set_cleaning_status()
                set_cleaning_status()

            elif choice == 2:

                today_date = input('Enter the date of today (yyyy-MM-dd): ') # Asks user for a valid date
                while not date_validation(today_date):
                    today_date = input('Invalid Date Format!\nEnter the date of today(yyyy-MM-dd): ')

                # Calls send_to_maintenance_log() with the dates as parameters
                send_to_maintenance_log(today_date)

            elif choice == 3:
                # Calls get_daily_cleaning_schedule()
                get_daily_cleaning_schedule()

            elif choice == 4:
                # Exits the program
                print("Thank You for using Housekeeping!\nExiting Housekeeping...")
                break

            else:
                # Displays error message if the choice does not exist
                print("Invalid Choice!")

        except ValueError:
            print("Please use numbers to select your choice!")


