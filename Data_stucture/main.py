# dilivery, Total, dilivery-1 = 1$, product_price, Total_dilivery
# shop information = 3 quantity_dilivery = 5
# Prepare in table or invoice = 5 
# total amount, transter shop, transfer to driver, End Balance
total_com1 = 0
total_product1 = total_product2 = total_product3 = 0
transfer_balance = 0
diliver1 = diliver2 = diliver3 = 0
i = 0
Dara = Sokha = John = 0
price_out1 = price_out2 = price_out3 = 0
print(f"{' ':<20}Welcome to Delivery Service")
print(f"{'':<10} {'='*50}")
print("""Shop_Name
        1. Coffee shop
        2. Clothe shop
        3. Drink Coffee shop
        4. Macha Coconute shop
        5. Shoes Shop""")
print("""Dilivery Name:
        1. Dara Driver
        2. Sokha Driver
        3. John Driver""")
print(f"{'':<10} {'='*50}")
while i < 100:
# ============================================================================company 1
    shop_name = int(input("Enter Name shop by number: "))
    if shop_name == 1:
        dilivery_name = int(input("Enter dilivery name by number: "))
        if dilivery_name == 1:
            product_price  = int(input("Please input product price: "))
            price_out1 = product_price + 1.5
            transfer_balance = price_out1 - product_price
            transfer_balance1 = price_out1 - product_price
            print(f"Price Sale : {price_out1} $")

            print(f"{'':<10} {'='*50}")
            Dara = int(transfer_balance1/1.5)
        elif dilivery_name == 2:
            product_price  = int(input("Please input product price: "))
            price_out1 = product_price + 1.5
            transfer_balance = price_out1 - product_price
            transfer_balance2 = price_out1 - product_price
            print(f"Price Sale : {price_out1} $")
     
            print(f"{'':<10} {'='*50}")
            Sokha = int(transfer_balance2/1.5)
        elif dilivery_name == 3:
            product_price  = int(input("Please input product price: "))
            price_out1 = product_price + 1.5
            transfer_balance = price_out1 - product_price
            transfer_balance3 = price_out1 - product_price
            print(f"Price Sale : {price_out1} $")
   
            print(f"{'':<10} {'='*50}")
            John = int(transfer_balance3/1.5)
        
# ============================================================================company 2
    elif shop_name == 2:
        dilivery_name = int(input("Enter dilivery name by number: "))
        if dilivery_name == 1:
            product_price  = int(input("Please input product price: "))
            price_out2 = product_price + 1.5
            transfer_balance = price_out2 - product_price
            transfer_balance1 = price_out2 - product_price
            print(f"Price Sale : {price_out2} $")

            print(f"{'':<10} {'='*50}")
            Dara = int(transfer_balance1/1.5)
        elif dilivery_name == 2:
            product_price  = int(input("Please input product price: "))
            price_out2 = product_price + 1.5
            transfer_balance = price_out2 - product_price
            transfer_balance2 = price_out2 - product_price
            print(f"Price Sale : {price_out2} $")
     
            print(f"{'':<10} {'='*50}")
            Sokha = int(transfer_balance2/1.5)
        elif dilivery_name == 3:
            product_price  = int(input("Please input product price: "))
            price_out2 = product_price + 1.5
            transfer_balance = price_out2 - product_price
            transfer_balance3 = price_out2 - product_price
            print(f"Price Sale : {price_out2} $")
   
            print(f"{'':<10} {'='*50}")
            John = int(transfer_balance3/1.5)
        
# ============================================================================company 3
    elif shop_name == 3:
        dilivery_name = int(input("Enter dilivery name by number: "))
        if dilivery_name == 1:
            product_price  = int(input("Please input product price: "))
            price_out3 = product_price + 1.5
            transfer_balance = price_out3 - product_price
            transfer_balance1 = price_out3 - product_price
            print(f"Price Sale : {price_out3} $")

            print(f"{'':<10} {'='*50}")
            Dara = int(transfer_balance1/1.5)
        elif dilivery_name == 2:
            product_price  = int(input("Please input product price: "))
            price_out3 = product_price + 1.5
            transfer_balance = price_out3 - product_price
            transfer_balance2 = price_out3 - product_price
            print(f"Price Sale : {price_out3} $")
     
            print(f"{'':<10} {'='*50}")
            Sokha = int(transfer_balance2/1.5)
        elif dilivery_name == 3:
            product_price  = int(input("Please input product price: "))
            price_out3 = product_price + 1.5
            transfer_balance = price_out3 - product_price
            transfer_balance3 = price_out3 - product_price
            print(f"Price Sale : {price_out3} $")
   
            print(f"{'':<10} {'='*50}")
            John = int(transfer_balance3/1.5)
           
# ============================================================================9
    elif shop_name == 9:
        break
i += 1
total_product1 += price_out1
total_com1 += transfer_balance

total_product2 += price_out2
total_com1 += transfer_balance
    
total_product3 += price_out3
total_com1 += transfer_balance
diliver1 += Dara
diliver2 += Sokha
diliver3 += John
print(f"{'':<10} {'='*50}")
print(f"{'':<10}SHOP         {' ':<10} Quantity{'':<10}Price")
print(f"{'':<10}Coffee shop  {' ':<11}{int(total_com1/1.5)}   {'':<14}{total_product1} $")
print(f"{'':<10}Clothe shop  {' ':<11}{int(total_com1/1.5)}   {'':<14}{total_product2} $")
print(f"{'':<10}Drink Coffee shop {' ':<6}{int(total_com1/1.5)}   {'':<14}{total_product3} $")
# print(f"{'':<10}Macha Coconute shop  {' ':<3}{int(total_com1/1.5)}   {'':<14}{total_product1} $")
# print(f"{'':<10}Shoes Shop  {' ':<12}{int(total_com1/1.5)}   {'':<14}{total_product1} $")
print(f"{'':<10} {'='*50}")
print(f"Dara diliver {diliver1} time")
print(f"Sokha diliver {diliver2} time")
print(f"John diliver {diliver3} time")
        

        



























































