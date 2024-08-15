# Enter Guests Name
def get_guest_name():
    while True:
        guest_name = input("Enter Guests Name: ")
        if guest_name.isalpha():
            return guest_name        
        else:
            print("Error: Name should only contain alphabetric characters. Please try again.")

guest_name = get_guest_name()
print(f"Welcome, {guest_name}!")

# Enter number of guests
def get_number_of_guests():
    while True:
        guest_number = input("Enter Number of Guests: ")
        if guest_number.isdigit():
            return guest_number
        else:
            print("Error: Number should only contain numeric values. Please try again.")

guest_number = get_number_of_guests()  # Get the numeric value

#enter apartment ID

def get_apartment_ID():
    apartment_names = ["swan", "goose", "duck"]
    
    while True:
        apartment_ID = input("Enter the apartment ID, example Unit 12 Swan building = U12swan: ")
        if apartment_ID.startswith("U"):
            #check if the following characters are digits within range 1-99
            number_part = ''
            for i in range(1,  len(apartment_ID)):
                if apartment_ID[i].isdigit():
                    number_part += apartment_ID[i]
                else:
                    break
            if number_part.isdigit() and 1 <= int(number_part) <= 99:
                # extract the building name part
                bldname = apartment_ID[len(number_part) +1:].lower()   # Get the remaining part of the string and convert to lowercase             
                if bldname in apartment_names:
                    return apartment_ID  
                else:
                    print("Error: Apartment building must be either swan, goose or duck") 
            else:
                print("Error: The digits following "U" must be between 1 and 99.")
        else:
             print ("Error: Apartment ID must start with U for Unit, Unit number and building name for example: 'U12sawn'")
                    
apartment_ID = get_apartment_ID()   

from datetime import datetime
# Enter checkin date
def get_checkin_date():
    while True:
        checkin_date = input("Enter checkin date in format DD.MM.YYYY: ").strip()
        print(f"Received input: {checkin_date}")  # Debugging print statement
        try:
            # try to parse the input string to a date
            parsed_date = datetime.strptime(checkin_date, "%d.%m.%Y")
            return parsed_date
        except ValueError as e:
            print(f"Error: {e}")
            print("Error: Please enter a valid date in format DD.MM.YYYY.")

checkin_date = get_checkin_date()  # Get the numeric value
print(f"Valid checkin date entered: {checkin_date.strftime('%d.%m.%Y')}")

# Enter checkout  date
def get_checkout_date():
    while True:
        checkout_date = input("Enter checkout date in format DD.MM.YYYY: ").strip()
        print(f"Received input: {checkout_date}")  # Debugging print statement
        try:
            # try to parse the input string to a date
            parsed_date = datetime.strptime(checkout_date, "%d.%m.%Y")
            return parsed_date
        except ValueError as e:
            print(f"Error: {e}")
            print("Error: Please enter a valid date in format DD.MM.YYYY.")

checkout_date = get_checkout_date()  # Get the numeric value
print(f"Valid checkout date entered: {checkout_date.strftime('%d.%m.%Y')}")

#length of stay

def get_length_of_stay():
    while True:
        length_of_stay = input("Please enter length of stay: ")
        if length_of_stay.isdigit() and int(length_of_stay) >= 1:
            return length_of_stay
        else:
            print("Error: Must be at least one night stay") 

length_of_stay = get_length_of_stay()
