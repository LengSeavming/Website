i = 0
Atotal = Btotal = Ctotal = Dtotal = Etotal = qtytotala = qtytotalb  = qtytotalc =qtytotald =qtytotale = 0
Asale = Bsale = Csale = Dsale = Esale = Aqty = Bqty = Cqty = Dqty = Eqty = Adtc= Bdtc= Cdtc = Ddtc = Edtc = Adt= Bdt  = Cdt = Ddt = Edt =0
Adili = Bdili = Cdili = Ddili = Edili = Bdilivercom = Adilivercom  = Cdilivercom = Ddilivercom = Edilivercom = 0
driver_A = driver_B = driver_C = 0
A = B = C = 0
print(f"{' ':<10}Welcome to Delivery Service")
print(f"{'='*50}")
print("""Shop_Name
        1. Shop A
        2. Shop B
        3. Shop C
        4. Shop D
        5. Shop E""")
print("""Dilivery Name:
        1. Driver-A
        2. Driver-B
        3. Driver-C""")
print(f"{'='*50}")
while i < 100:
    shop_name = int(input("Choose Shop (1-5) (get invoice = 9): "))
    if shop_name == 1:
        Adilivery = int(input("Choose Diliver (1-3): "))
        if Adilivery == 1:
            Aproductp  = int(input("Enter product(price): "))
            
            Aqty = int(input("Quantity: "))
            Asale = (Aproductp*Aqty + 1.5)
            print(f"Price Sale : {Asale} $")
            
            print(f"{'='*50}")
            Adilivercom = 0.5
            Adili = 1
            driver_A = 1
        elif Adilivery == 2:
            Aproductp  = int(input("Enter product(price): "))
        
            Aqty = int(input("Quantity: "))
            Asale = (Aproductp*Aqty + 1.5)
            print(f"Price Sale : {Asale} $")
            print(f"{'='*50}")
            Adilivercom = 0.5
            Adili = 1
            driver_B = 1
        elif Adilivery == 3:
            Aproductp  = int(input("Enter product(price): "))
        
            Aqty = int(input("Quantity: "))
            Asale = (Aproductp*Aqty + 1.5)
            print(f"Price Sale : {Asale} $")
            print(f"{'='*50}")
            Adilivercom = 0.5
            Adili = 1
            driver_C = 1
    elif shop_name == 2:
        Bdilivery = int(input("Choose Diliver (1-3): "))
        if Bdilivery == 1:
            Bproductp  = int(input("Enter product(price): "))
            
            Bqty = int(input("Quantity: "))
            Bsale = (Bproductp*Bqty + 1.5)
            print(f"Price Sale : {Bsale} $")

            print(f"{'='*50}")
            Bdilivercom = 0.5
            Bdili = 1
            driver_A = 1
        elif Bdilivery == 2:
            Bproductp  = int(input("Enter product(price): "))
           
            Bqty = int(input("Quantity: "))
            Bsale = (Bproductp*Bqty + 1.5)
            
            print(f"Price Sale : {Bsale} $")
            print(f"{'='*50}")
            Bdilivercom = 0.5
            Bdili = 1
            driver_B = 1
        elif Bdilivery == 3:
            Bproductp  = int(input("Enter product(price): "))
           
            Bqty = int(input("Quantity: "))
            Bsale = (Bproductp*Bqty + 1.5)
            
            print(f"Price Sale : {Bsale} $")
            print(f"{'='*50}")
            Bdilivercom = 0.5
            Bdili = 1
            driver_C = 1
    elif shop_name == 3:
        Cdilivery = int(input("Choose Diliver (1-3): "))
        if Cdilivery == 1:
            Cproductp  = int(input("Enter product(price): "))
            
            Cqty = int(input("Quantity: "))
            Csale = (Cproductp*Cqty + 1.5)
            print(f"Price Sale : {Csale} $")

            print(f"{'='*50}")
            Cdilivercom = 0.5
            Cdili = 1
            driver_A = 1
        elif Cdilivery == 2:
            Cproductp  = int(input("Enter product(price): "))
           
            Cqty = int(input("Quantity: "))
            Csale = (Cproductp*Cqty + 1.5)
            
            print(f"Price Sale : {Csale} $")
            print(f"{'='*50}")
            Cdilivercom = 0.5
            Cdili = 1
            driver_B = 1
        elif Cdilivery == 3:
            Cproductp  = int(input("Enter product(price): "))
           
            Cqty = int(input("Quantity: "))
            Csale = (Cproductp*Cqty + 1.5)
            
            print(f"Price Sale : {Csale} $")
            print(f"{'='*50}")
            Cdilivercom = 0.5
            Cdili = 1
            driver_C = 1
    elif shop_name == 4:
        Ddilivery = int(input("Choose Diliver (1-3): "))
        if Ddilivery == 1:
            Dproductp  = int(input("Enter product(price): "))
            
            Dqty = int(input("Quantity: "))
            Dsale = (Dproductp*Dqty + 1.5)
            print(f"Price Sale : {Dsale} $")

            print(f"{'='*50}")
            Ddilivercom = 0.5
            Ddili = 1
            driver_A = 1
        elif Ddilivery == 2:
            Dproductp  = int(input("Enter product(price): "))
           
            Dqty = int(input("Quantity: "))
            Dsale = (Dproductp*Dqty + 1.5)
            
            print(f"Price Sale : {Dsale} $")
            print(f"{'='*50}")
            Ddilivercom = 0.5
            Ddili = 1
            driver_B = 1
        elif Ddilivery == 3:
            Dproductp  = int(input("Enter product(price): "))
           
            Dqty = int(input("Quantity: "))
            Dsale = (Dproductp*Dqty + 1.5)
            
            print(f"Price Sale : {Dsale} $")
            print(f"{'='*50}")
            Ddilivercom = 0.5
            Ddili = 1
            driver_C = 1
    elif shop_name == 5:
        Edilivery = int(input("Choose Diliver (1-3): "))
        if Edilivery == 1:
            Eproductp  = int(input("Enter product(price): "))
            
            Eqty = int(input("Quantity: "))
            Esale = (Eproductp*Eqty + 1.5)
            print(f"Price Sale : {Esale} $")

            print(f"{'='*50}")
            Edilivercom = 0.5
            Edili = 1
            driver_A = 1
        elif Edilivery == 2:
            Eproductp  = int(input("Enter product(price): "))
           
            Eqty = int(input("Quantity: "))
            Esale = (Eproductp*Eqty + 1.5)
            
            print(f"Price Sale : {Esale} $")
            print(f"{'='*50}")
            Edilivercom = 0.5
            Edili = 1
            driver_B = 1
        elif Edilivery == 3:
            Eproductp  = int(input("Enter product(price): "))
           
            Eqty = int(input("Quantity: "))
            Esale = (Eproductp*Eqty + 1.5)
            
            print(f"Price Sale : {Esale} $")
            print(f"{'='*50}")
            Edilivercom = 0.5
            Edili = 1
            driver_C = 1
    elif shop_name == 9:
        break    
    else:
        print("choose the number (1-5)")
        continue
    Atotal += Asale
    Btotal += Bsale
    Ctotal += Csale
    Dtotal += Dsale
    Etotal += Esale
    qtytotala += Aqty
    qtytotalb += Bqty
    qtytotalc += Cqty
    qtytotald += Dqty
    qtytotale += Eqty
    Adtc += Adilivercom
    Bdtc += Bdilivercom
    Cdtc += Cdilivercom
    Ddtc += Ddilivercom
    Edtc += Edilivercom
    Adt += Adili
    Bdt += Bdili
    Cdt += Cdili
    Ddt += Ddili
    Edt += Edili
    A += driver_A
    B += driver_B
    C += driver_C
    Asale = Bsale = Csale = Dsale = Esale = Aqty = Bqty = Cqty = Dqty = Eqty = Adili = Bdili = Cdili = Ddili = Edili = Bdilivercom = Adilivercom  = Cdilivercom =Ddilivercom = Edilivercom= 0   
    driver_A = driver_B = driver_C = 0
i +=1
totalAmount = Adtc + Bdtc + Cdtc + Ddtc + Edtc
totaldili = Adt + Bdt + Cdt + Ddt + Edt
print(f"{'='*50}")
print("*"*50)
print(f"                Invoice          ")
print("*"*50)
print(f"   SHOP         Quantity       Price      Quantity_dilivery")
print(f"1 (Shop A):     {qtytotala:<15}$ {Atotal:<10}{Adt} time(s)")
print(f"2 (Shop B):     {qtytotalb:<15}$ {Btotal:<10}{Bdt} time(s)")
print(f"4 (Shop C):     {qtytotalc:<15}$ {Dtotal:<10}{Cdt} time(s)")
print(f"4 (Shop D):     {qtytotald:<15}$ {Dtotal:<10}{Ddt} time(s)")
print(f"5 (Shop E):     {qtytotale:<15}$ {Etotal:<10}{Edt} time(s)")
print("*"*50)
print(f"Total payment to Dilivery company: ${totalAmount}")
print(f"Total payment to dilivers: ${totaldili}")
print("*"*50)
print(f"Driver A get ${A}")
print(f"Driver B get ${B}")
print(f"Driver C get ${C}")