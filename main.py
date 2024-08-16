from datetime import datetime
import math

guest_name = ["Alyssa", "luigi"]
guest_number = []
apartment_ID = ["U12swan", "U209duck", "U49goose"]
checkin_date = []
checkout_date = []
length_of_stay = []
total_cost = []
reward_points = [20, 32]

item_id = {
    'car_park': {'price': 25, 'description': 'per night'},
    'breakfast': {'price': 21, 'description': 'per person'},
    'toothpaste': {'price': 5, 'description': 'per tube'},
    'extra_bed': {'price': 50, 'description': 'per night'}
}


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

#create a guest list to add supp purchases
guests = {
    guest_name: {
        "supp_items": []
    }
}
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
            #check if the following characters are digits within range 1-300
            number_part = ''
            for i in range(1,  len(apartment_ID)):
                if apartment_ID[i].isdigit():
                    number_part += apartment_ID[i]
                else:
                    break
            if number_part.isdigit() and 1 <= int(number_part) <= 300:
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
def get_total_cost(apartment_ID, length_of_stay):
    apartment_rate = {
        "U12swan": 95.0,
        "U209duck": 106.6,
        "U49goose": 145.2
    }
    rate = apartment_rate.get(apartment_ID)
    if rate is None:
        print(f"Error: No rate found for apartment ID '{apartment_ID}")
        return 0

    total_cost = rate * length_of_stay
    print(f"Length of stay is {length_of_stay} night(s) = ${total_cost:.2f}")
    return total_cost

total_cost = get_total_cost(apartment_ID, length_of_stay)

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
    print("\nThankyou foir your booking! We hope you will have an enjoyable stay.")
    print("=" * 81)  # End of receipt
    
# Now, call display_receipt with all the necessary arguments
display_receipt(guest_name, guest_number, apartment_ID, checkin_date, checkout_date, length_of_stay, total_cost, reward_points)

#PART 2 item  2 - supp order

def request_supp_item():
    while True:
        supp_item = input("Do you want to order a supplementary item? (y/n): ")
        if supp_item == "y":
            for item, details in item_id.items():
                price = details['price']
                description = details['description']
                print(f"Item: {item}, Price: ${price} {description}")
            break
        elif supp_item == "n":
            print("Thankyou for your business")
            break
        else:
            print("Please enter 'y' for yes or 'n' for no.")

request_supp_item()

def add_supp_item():
    while True:
        supp_item = input("Which item would you like to add? ").strip().lower()
        if supp_item in item_id:
            confirmation = input(f"Are you sure you want to add {supp_item} to your purchase? ")
            if confirmation == 'y':
                print(f"{supp_item} has been added to your purchase.")
                guests[guest_name]["supp_items"].append(supp_item) # Add the item to the guest's list of supplementary items
                
                continue_ordering = input("Would you like to order another supplementary item? (y/n): ").strip().lower()
                if continue_ordering != 'y':
                    print(f"Thank you for your purchase, {guest_name}.")
                    break  # Exit the loop when the user is done  
        else:
            print("Item not found. Please choose from the available items below:")
            request_supp_item()

        # Ask if the user wants to continue ordering supplementary items

add_supp_item()


# Check what was added for the guest supp order
print(f"{guest_name} ordered the following supplementary items: {guests[guest_name]['supp_items']}")

# Display receipt
def display_receipt(guest_name):
    print("=" * 81)
    print("\n\t\tServices Apartments - Supplementary item Receipt\n")
    print("=" * 81)

    supp_items = guests[guest_name]['supp_items']
    total_cost = 0
    
    if supp_items:
        for item in supp_items:
            price = item_id[item]['price']
            description = item_id[item]['description']
            print(f"Item: {item.capitalize()}, Price: ${price} {description}")
            total_cost += price

        print("-" * 40)
        print(f"Total Cost: ${total_cost:.2f}")
    else:
        print("=" * 40)

    print("=" * 40)

display_receipt(guest_name)