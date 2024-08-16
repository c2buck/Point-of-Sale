from datetime import datetime
import math

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
            return int(length_of_stay)
        else:
            print("Error: Must be at least one night stay") 

length_of_stay = get_length_of_stay()

# Enter booking date
def get_booking_date():
    while True:
        booking_date = input("Enter booking date in format DD.MM.YYYY: ").strip()
        print(f"Received input: {booking_date}")  # Debugging print statement
        try:
            # try to parse the input string to a date
            parsed_date = datetime.strptime(booking_date, "%d.%m.%Y")
            return parsed_date
        except ValueError as e:
            print(f"Error: {e}")
            print("Error: Please enter a valid date in format DD.MM.YYYY.")

booking_date = get_booking_date()  # Get the numeric value
print(f"Valid booking date entered: {booking_date.strftime('%d.%m.%Y')}")

#calculate total cost
def get_total_cost(length_of_stay):
    apartment_rate = 200
    total_cost = apartment_rate * length_of_stay
    print(f"Length of stay is {length_of_stay} night(s) = ${total_cost}")
    return total_cost

total_cost = get_total_cost(length_of_stay)

#calculate reward points
def get_reward_points(total_cost):
    reward_points = math.ceil(total_cost)
    print(f"Reward Points earned: {reward_points}")
    return reward_points

reward_points = get_reward_points(total_cost)

# Display receipt
def display_receipt_header():
    print("=" * 81)
    print("\n\t\tServices Apartments - Booking Receipts\n")
    print("=" * 81)

def display_receipt(guest_name, guest_number, apartment_ID, checkin_date, checkout_date, length_of_stay, total_cost, reward_points):
    display_receipt_header()
    
    # Print the guest details and booking information
    print(f"Guest Name: {guest_name}")
    print(f"Number of Guests: {guest_number}")
    print(f"Apartment ID: {apartment_ID}")
    print(f"Check-in Date: {checkin_date.strftime('%d.%m.%Y')}")
    print(f"Check-out Date: {checkout_date.strftime('%d.%m.%Y')}")
    print(f"Length of Stay: {length_of_stay} night(s)")
    print("-" * 81)
    print(f"Total Cost: ${total_cost}")
    print(f"Reward Points Earned: {reward_points}")
    print("=" * 81)  # End of receipt
    
# Now, call display_receipt with all the necessary arguments
display_receipt(guest_name, guest_number, apartment_ID, checkin_date, checkout_date, length_of_stay, total_cost, reward_points)