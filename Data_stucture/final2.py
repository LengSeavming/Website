i = 1
aba = 1000
acilida = 1000
wing = 1000
balance = aba + acilida + wing
total_balance = total_spend = total_income = income = spend = 0
abas = abai = acilidai = acilidas = wingi = wings = total_aba = total_wing = total_acilida = 0
total_abas = total_acilidas = total_wings = total_abai = total_acilidai = total_wingi = 0
print(f"{'':<15}Your Account Data")
print('='*40)
print(f"ABA     account: {aba} $  ")
print(f"Acilida account: {acilida} $  ")
print(f"Wing    account: {wing} $  ")
print(f"Total   balance: {balance} $")
print('='*40)

while i < 100:
    print("1. Spend")
    print("2. Income")
    print("3. Balance")
    enter = int(input("Please enter by number (1-3): "))
    if enter == 1:
        print(f"{'':<10}Exspend Box.")
        print('='*40)
        print("It's time to spend money hahaha. ")
        print(f"""{'':<10}Choose Bank Account
              1. ABA Bank
              2. Acilida Bank
              3. Wing Bank""")
        choose = int(input("Choose Bank Account (1-3): "))
        if choose == 1:
            abas = int(input("Enter amount of spend: "))
            # abas = aba - spend
        elif choose == 2:
            acilidas = int(input("Enter amount of spend: "))
            # acilidas = acilida - spend
        elif choose == 3:
            wings = int(input("Enter amount of spend: "))
            # wings = wing - spend
        
        print('='*40)
    
    elif enter == 2:
        print(f"{'':<10}Income Box.")
        print(f"""{'':<10}Choose Bank Account
              1. ABA Bank
              2. Acilida Bank
              3. Wing Bank""")
        choose = int(input("Choose Bank Account (1-3): "))
        if choose == 1:
            abai = int(input("Enter amount of account earn: "))
            # abai = aba + income
        elif choose == 2:
            acilidai = int(input("Enter amount of account earn: "))
            # acilidai = acilida + income
        elif choose == 3:
            wingi = int(input("Enter amount of account earn: "))
            # wingi = wing + income
        print('='*40)
    elif enter == 3:
        break
        
    else:
        print("Number is available.")
    # total_spend += spend
    # total_income += income
    total_abas += abas
    total_acilidas += acilidas
    total_wings += wings
    total_abai += abai
    total_acilidai += acilidai
    total_wingi += wingi
    i+=1


total_aba = aba + total_abai - total_abas
total_acilida = acilida + total_acilidai - total_acilidas
total_wing = wing + total_wingi - total_wings
total_balance = total_wing + total_aba + total_acilida
print(f"{'':<15}Your Account Data")
print('='*40)
print(f"ABA     account: {total_aba} $  | Spend: {total_abas} $ | Earn: {total_abai} $")
print(f"Acilida account: {total_acilida} $  | Spend: {total_acilidas} $ | Earn: {total_acilidai} $")
print(f"Wing    account: {total_wing} $  | Spend: {total_wings} $ | Earn: {total_wingi}")
print(f"Total   balance: {total_balance} $")
print('='*40)