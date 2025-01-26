i = 1
money = 0
total = 0
while i < 100:
    print(f"Please pay money for wedding")
    print(f"Specail guest")
    name = input("Enter your name: ")
    money = int(input("Your payment = "))
    total += money
    enter = input("You want to continue (Y/y or N/n): ")
    if enter == 'y' or enter == 'Y':
        continue
    elif enter == 'n' or enter == 'N':
        break
    i+=1
print("Total of wedding = ",total ,"$")