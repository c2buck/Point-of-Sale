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
    while True:
        apartment_ID = input("Enter the apartment ID, example Unit 12 Swan building = U12swan: ")
        if apartment_ID.startswith("U"):
            return apartment_ID
        else:
             print ("Error: Apartment ID must start with U for Unit")
                    
apartment_ID = get_apartment_ID()   

