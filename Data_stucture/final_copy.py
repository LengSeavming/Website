
print(f"{'='*10}Welcome to Parking Service{'='*10}")
print('==='*18)

def print_receipt(id, parking_details, total_payment):
    print(f"ID: {id}")
    print("\n====================Receipt========================")
    for detail in parking_details:
        print(f"""Shift: {detail['shift']}, Vehicle: {detail['vehicle_type']}
Count: {detail['count']}, Payment: {detail['payment']} Riel""")
    print(f"\nTotal Amount: {total_payment} Riel")
    print("======================Thank You======================")

def main():

    student_parking_data = {}

    while True:
        print("\n1-Parking Option")
        print("2-Receipt")
        print("3-Exit")
        
        choice = input("\n=>Please Choice the opption: ")
        if choice == '1':
            print("\n====================Parking System====================")

            id = input("Enter ID: ")
            if not id:
                print("ID cannot be empty. Try again.\n")
                continue

            print("\nParking Shift:")
            print("1-Morning")
            print("2-Afternoon")
            print("3-Evening")
            
            shift_choice = input("\n* Please Enter Your Shift Choice: ")
            shift = {"1": "Morning", "2": "Afternoon", "3": "Evening"}.get(shift_choice, "Invalid")

            if shift == "Invalid":
                print("Invalid Shift Choice. Try Again.\n")
                continue

            print("\nPlease Choose Vehicle Type:")
            print("1-Bicycle = 500 Riel")
            print("2-Motorbike = 1000 Riel")
            print("3-Car = 2000 Riel")
            
            vehicle_choice = input("* Please Enter Your Vehicle Choice: ")
            vehicle_data = {
                "1": ("Bicycle", 500),
                "2": ("Motorbike", 1000),
                "3": ("Car", 2000)
            }
            vehicle_info = vehicle_data.get(vehicle_choice, ("Invalid", 0))

            if vehicle_info[0] == "Invalid":
                print("Invalid Vehicle Choice. Try Again.\n")
                continue

            vehicle_type, price_per_shift = vehicle_info

            try:
                count = int(input(f"Enter The Number of {vehicle_type}s: "))
                if count <= 0:
                    print("Count Must Be Greater Than 0. Try Again.\n")
                    continue
            except ValueError:
                print("Invalid Input For Count. Try Again.\n")
                continue

            payment = count * price_per_shift

            if id not in student_parking_data:
                student_parking_data[id] = []

            student_parking_data[id].append({
                "shift": shift,
                "vehicle_type": vehicle_type,
                "count": count,
                "payment": payment
            })

            print(f"Parking recorded for ID: {id}\n")

        elif choice == '2':
            id = input("Enter ID To View Receipt: ")
            if id not in student_parking_data:
                print("No Parking Records Found\n")
                continue

            parking_details = student_parking_data[id]
            total_payment = sum(detail['payment'] for detail in parking_details)
            print_receipt(id, parking_details, total_payment)

        elif choice == '3':
            print("Exiting The System.")
            print("Thank You!")
            break
        else:
            print("Invalid Choice. Please Try Again.\n")

main()