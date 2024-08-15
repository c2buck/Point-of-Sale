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

