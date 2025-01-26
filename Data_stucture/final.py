class system:
    def __init__(self):
        self.bike = 0
        self.moto = 0
        self.car =  0
        self.choice = 0
        self.total = 0
    def opption(self):
        print(f"{'':<15}Vehacal types")
        print(f"""Taking of Vehacal Student (Morning Afternoon Evening)
              1. Bike (1/500r)
              2. Moto (1/1000r)
              3. Car (1/2000r)""")
    def condition(self,choice):
        self.choice = choice
        if choice == 1:
            print("bike")
        elif choice == 2:
            print("moto")
        elif choice == 3:
            print("car")
        else:
            print("Available number please try again")
    
    def invoice(self,choice):
        self.choice = choice
        
        print(f"{'':<15}Receipt")
        print("Build Bright University")
        if choice == 1:
            print("bike = 500r")
            self.bike = 500
            
        elif choice == 2:
            print("moto = 1000r")
            self.moto = 1000
        elif choice == 3:
            print("car = 2000r")
            self.car = 2000
            
        else:
            print("Available number please try again")
        self.total += self.bike
        self.total += self.moto
        self.total += self.car
        print(f"Totla = {self.total} riel")
        

i = 0
me = system()
while i < 100:
    choose = bool
    me.opption()
    choice = int(input("Please choose your vehacal types(1-3): "))
    me.condition(choice)
    choose = input('You want to continue (n/no) stop (y/yes): ')
    if choose == 'y' or choose == 'yes':
        break
    elif choose == 'n' or choose == 'no':
        continue
    else:
        print("Plese try again.")
i+=1
    
me.invoice(choice)