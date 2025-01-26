def print_receipt(student_id, parking_details, total_payment):
    print("\n--- University Parking Receipt ---")
    print(f"Student ID: {student_id}")
    print("Details:")
    for detail in parking_details:
        print(f"  - Shift: {detail['shift']}, Vehicle: {detail['vehicle_type']}, Count: {detail['count']}, Payment: {detail['payment']} Riel")
    print(f"Total Payment: {total_payment} Riel")
    print("---------------------------------")

def main():
    print("Welcome to University Parking Management System\n")
    student_parking_data = {}

    while True:
        print("1. Parking")
        print("2. Receipt")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        if choice == '1':
            print("\n--- Parking ---")

            student_id = input("Enter Student ID: ")
            if not student_id:
                print("Student ID cannot be empty. Try again.\n")
                continue

            print("Choose Shift:")
            print("1. Morning")
            print("2. Afternoon")
            print("3. Evening")
            
            shift_choice = input("Enter your shift choice: ")
            shift = {"1": "Morning", "2": "Afternoon", "3": "Evening"}.get(shift_choice, "Invalid")

            if shift == "Invalid":
                print("Invalid shift choice. Try again.\n")
                continue

            print("\nChoose Vehicle Type:")
            print("1. Bicycle = 500 Riel/shift")
            print("2. Motorbike = 1000 Riel/shift")
            print("3. Car = 2000 Riel/shift")
            
            vehicle_choice = input("Enter your vehicle choice: ")
            vehicle_data = {
                "1": ("Bicycle", 500),
                "2": ("Motorbike", 1000),
                "3": ("Car", 2000)
            }
            vehicle_info = vehicle_data.get(vehicle_choice, ("Invalid", 0))

            if vehicle_info[0] == "Invalid":
                print("Invalid vehicle choice. Try again.\n")
                continue

            vehicle_type, price_per_shift = vehicle_info

            try:
                count = int(input(f"Enter the number of {vehicle_type}s: "))
                if count <= 0:
                    print("Count must be greater than 0. Try again.\n")
                    continue
            except ValueError:
                print("Invalid input for count. Try again.\n")
                continue

            payment = count * price_per_shift

            if student_id not in student_parking_data:
                student_parking_data[student_id] = []

            student_parking_data[student_id].append({
                "shift": shift,
                "vehicle_type": vehicle_type,
                "count": count,
                "payment": payment
            })

            print(f"Parking recorded for Student ID: {student_id}\n")

        elif choice == '2':
            student_id = input("Enter Student ID to view receipt: ")
            if student_id not in student_parking_data:
                print("No parking records found for this Student ID.\n")
                continue

            parking_details = student_parking_data[student_id]
            total_payment = sum(detail['payment'] for detail in parking_details)
            print_receipt(student_id, parking_details, total_payment)

        elif choice == '3':
            print("Exiting the system. Have a nice day!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
