#=================================================================================
#                    PYTHON ATM MACHINE SYSTEM
#=================================================================================
import time as t



print("=============================================================================")
print("                      WELCOME  TO PYTHON ATM                                 ")
print("=============================================================================")




# Account Information
account_name = "John Doe"
account_number = "1234567890"
pin = 1234
balance = 50000
opening_balance = balance




#Transaction Variables
total_deposit = 0
total_withdrawal = 0
total_transfer = 0
total_airtime = 0
total_electricity = 0
transaction_count = 0
total_water = 0



#=================================================================================
#                     ATM PIN VERIFICATION
#=================================================================================
print("\nplease insert your ATM card")
print("card detected Successfully")


attempts = 0
max_attempts = 3
pin_verified = False

while attempts < max_attempts:
    entered_pin = int(input("\nEnter Your four-digit PIN:"))
    if entered_pin == pin:
        print("\nPIN verified successfully")
        print(f"welcome, {account_name}")
        pin_verified = True
        break
    else:
        attempts = attempts + 1
        remaining_attempts = max_attempts - attempts

        print("\nIncorrect PIN!")

        if(remaining_attempts > o):
            print(f"Attempts Remaining: {remaining_attempts}")   
        else:
            print("You have exceeded your PIN attempts")    
            print("Your ATM session has been terminated")

#=================================================================================
#                    MAIN ATM MENU
#=================================================================================


if pin_verified:
    while True:
        print("\n=============================================================================")
        print("                      MAIN ATM MENU                              ")
        print("=============================================================================")

        print("1. Check Account Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Money")
        print("5. Pay Bills")
        print("6. Change Pin")
        print("7. View account information")
        print("8. View Transaction Summary")
        print("9. Exit")


        print("================================================================================")
        choice = input("Select an option: ")

    
        #=================================================================================
        #                      CHECK BALANCE
        #=================================================================================

        if choice == "1":
            t.sleep(2.5)
            print("\n=================ACCOUNT BALANCE =====================================")
            print(f"Account Name: {account_name}")
            print(f"Account Number: {account_number}")
            print(f"Account Balance: {balance}")

        #=================================================================================
        #       OPTION 2:   DEPOSIT MONEY
        #=================================================================================
        

        elif choice == "2":
            t.sleep(2.5)
            print("\n=================  CASH DEPOSIT ===================================")

            amount = float(input("Enter deposit amount: N"))

            if amount > 0:
                balance = amount + balance
                total_deposit = total_deposit + amount
                transaction_count = transaction_count + 1

                print("\n Deposit Sucessful!")
                print(f"Amount Deposited: N{amount}")
                print(f"New Balance: N{balance}")


                print("\n================ DEPOSIT RECIEPTS ============================")
                print("Transaction Type: Deposit")
                print(f"Account Name {account_name}")
                print(f"Account Number: {account_number}")
                print(f"Account: N{amount}")
                print(f"Balance: N{balance}")
                print("Status Successful")
                print("================================================================")
            else:
                print("Deposit amount must be greater than zero")   
        #=================================================================================
        #                OPTION 3:  WITHDRAW  MONEY
        #================================================================================= 
                
        if choice == "3":
                    t.sleep(2.5)
                    print("\n=================  CASH WITHDRAWAL ===================================")
        
                    amount = float(input("Enter withdrawal amount: N"))
        
                    if amount <= 0:
                        print("Invalid withdrawal amount")
                        
                    elif amount > balance:

                        print("insufficient Funds") 
                        print(f"Available Balance: N{balance}") 

                    else:

                        balance = balance - amount
                        total_withdrawal = total_withdrawal + amount
                        transaction_count = transaction_count + 1
        
                        print("\n Withdrawal Sucessful!")
                        print("Please collect your cash")
                        print(f"Amount Withdrawn: N{amount}")
                        print(f"Remaining Balance: N{balance}")
        
        
                        print("\n================ WITHDRAWAL RECIEPTS ============================")
                        print("Transaction Type: Withdrawal")
                        print(f"Account Name {account_name}")
                        print(f"Account Number: {account_number}")
                        print(f"Account: N{amount}")
                        print(f"Balance: N{balance}")
                        print("Status Successful")
                        print("================================================================")


        #=================================================================================
        #                OPTION 4:  TRANSFER MONEY
        #=================================================================================            
                           

        elif choice == "4":
             t.sleep(2.5)
             print("\n=================  TRANSFER MONEY ===================================")
             recipient_name = input("Enter recipient's name: ")
             recipient_account = input("Enter recipient's account: ")
             bank_name = input("Enter recipient's bank name: ")

             amount = float(input("Enter transfer amount: N"))

             if amount <= 0:

                  print("Transfer must be greater than zero")

             elif amount > balance:
                print("Insufficient funds for this transfer")
             else:  
                  confirm = input("Confirm transfer?") 

                  if confirm.lower() == "yes":
                       balance = balance - amount
                       total_transfer = total_transfer + amount
                       transaction_count = transaction_count + 1


                       print("\n Transfer Sucessful!")
                       print(f"Recipient: {recipient_name}")
                       print(f"Account Number: {recipient_account}")
                       print(f"Bank: {bank_name}")
                       print(f"Amount Transferred: N{amount}")
                       print(f"Remaining Balance: N{balance}")
                      
    
    
                       print("\n================ TRANSFER RECIEPTS ============================")
                       print("Transaction Type: Transfer")
                       print(f"Sender {account_name}")
                       print(f"Recipient: {recipient_name}")
                       print(f"Recipient_Account: N{recipient_account}")
                       print(f"Bank: {bank_name}")
                       print(f"Amount: N{amount}")
                       print("Status Successful")
                       print("================================================================")
                  else:
                       print("Transferred cancelled")   


        #=================================================================================
        #                OPTION 5:  PAY BILLS
        #=================================================================================

        elif choice == "5":
             while True:
                print("\n=============================================================================")
                print("                      PAY BILLS                              ")
                print("=============================================================================")

                print("1. Buy Airtime")
                print("2. Pay Electricity Bill")
                print("3. Pay Water Bill")
                print("4. Return to Main Menu")
                print("================================================================================")
                bill_choice = input("Select a bill payment option:  ")

                #=================================================================================
                #  BILL 1: BUY AIRTIME
                #=================================================================================

                if bill_choice == "1":

                    print("\n=================ACCOUNT BALANCE =====================================")

                    print("1. MTN")
                    print("2. AIRTEL")
                    print("3. GLO")
                    print("4. 9MOBILE")
                    print("================================================================================")

                
                    network = input("Select Your Network: ")

                    if network == "1":
                         network_name = "MTN"

                    elif network == "2":
                         network_name = "AIRTEL"

                    elif network == "3":
                         network_name = "GLO"     

                    elif network == "4":
                         network_name = "9MOBILE"

                    else:
                         network_name = "Invalid"

                    if network_name != "Invalid":
                        phone_number = input("Enter phone number: ")
                        amount = float(input("Enter airtime amount: "))

                        if amount <= 0:
                            print("Invalid airtime amount")

                        elif  amount > balance:
                            print("Insufficient funds")  

                        else :
                               balance = balance - amount 
                               total_airtime = total_airtime + amount
                               transaction_count = transaction_count + 1

                               print("\n Airtime purchase successful!")
                               print(f"Network: {network_name}")
                               print(f"Phone Number: {phone_number}")
                               print(f"Amount: N{amount}")
                               print(f"Remaining Balance: N{balance}")


                               print("\n================ AIRTIME RECIEPTS ============================")
                               print(f"Network: {network_name}")
                               print(f"Phone Number: {phone_number}")
                               print(f"Amount: N{amount}")
                               print("Status Successful")
                               print("================================================================")
                    else:
                         print("Invalid network selection")


                #=================================================================================
                #  BILL 2: ELECRICITY PAYMENT
                #=================================================================================
                
                if bill_choice == "2":

                    print("\n================= ELECTRICITY PAYMENT =====================================")

                    print("1. Prepaid Meter")
                    print("2. Postpaid Meter")


                    meter_choice = input("Select your meter type: ")

                    if meter_choice == "1":
                        meter_type = "prepaid"

                    elif meter_choice == "2":
                        meter_type = "Postpaid"

                    else:
                        meter_type = "Invalid"   

                    if meter_type != "Invalid":
                        print("1. IBDEC") 
                        print("2. EKDEC") 
                        print("3. IKDEC") 
                        print("4. AEDC") 
                        print("5. Other") 

                        provider_choice = input("Select electricity provider: ")

                        if provider_choice == "1":
                            provider = "IBDEC"

                        elif provider_choice == "2":
                            provider = "EKDEC"

                        elif provider_choice == "3":
                            provider = "IKDEC"

                        elif provider_choice == "4":
                            provider = "AEDC"

                        elif provider_choice == "5":
                            provider = input("Enter provider name: ")

                        else:
                            provider = "Invalid"

                        if provider != "Invalid":
                            meter_number = input("Enter meter number: ")
                            customer_name = (input("Enter customer name: "))
                            amount = float(input("Enter electricity bill amount: "))  

                            if amount <= 0:
                                print("Payment must be greater than zero")
                                           
                            elif  amount > balance:
                                print("Insufficient funds")

                            else:
                                confirm = input("confirm transfer?  ")

                                if confirm.lower() == "yes":

                                    balance = balance - amount
                                    total_electricity = total_electricity + amount
                                    transaction_count = transaction_count + 1

                                    print("\n Electricity bill payment successful!")
                                    print(f"Provider: {provider}")
                                    print(f"Meter Type: {meter_type}")
                                    print(f"Meter Number: {meter_number}")
                                    print(f"Customer Name: {customer_name}")
                                    print(f"Amount Paid: N{amount}")
                                    print(f"Remaining Balance: N{balance}")

                                    print("\n================ ELECTRICITY PAYMENT RECIEPTS ============================")   
                                    print(f"Provider: {provider}")
                                    print(f"Meter Type: {meter_type}")
                                    print(f"Meter Number: {meter_number}")
                                    print(f"Amount Paid: N{amount}")
                                    print(f"Status: Successful")
                                    print("================================================================")
                                else:
                                    print("Payment cancelled")
                        else:
                            print("Invalid electricity provider")      
                    else:
                        print("Invalid Meter Type")
                #=================================================================================
                #  BILL 3 : WATER PAYMENT
                #=================================================================================

                if bill_choice == "3":
                
                                    print("\n================= WATER BILL PAYMENT =====================================")
                
                                    print("1. Abeokuta water corporation")
                                    print("2. Lagos Water corporation")
                                    print("2. other provider")
                
                
                                    water_choice = input("Select your water provider: ")
                
                                    if water_choice == "1":
                                        water_provider = "Abeokuta water corporation"
                
                                    elif water_choice == "2":
                                        water_provider = "Lagos Water corporation"

                                    elif water_choice == "3":
                                        water_provider = input("Enter provider name")    
                
                                    else:
                                        water_provider= "Invalid"   
                
                                    if water_provider != "Invalid":
                                        customer_name = input("Enter water number: ")
                                        customer_number = (input("Enter customer aacount number: "))
                                        amount = float(input("Enter electricity bill amount: "))  
            
                                        if amount <= 0:
                                            print("Payment must be greater than zero")
                                                        
                                        elif  amount > balance:
                                            print("Insufficient funds")  
                
                                        else:
                                            confirm = input("confirm water bill payment  ")
            
                                            if confirm.lower() == "yes":
            
                                                balance = balance - amount
                                                total_water = total_water + amount
                                                transaction_count = transaction_count + 1
            
                                                print("\n Water bill payment successful!")
                                                print(f"Provider: {water_provider}")
                                                print(f"Customer: {customer_name}")
                                                print(f"Account Number: N{customer_number}")
                                                print(f"Amount Paid: N{amount}")
                                                print(f"Remaining Balance: N{balance}")
            
                                                print("\n================ WATER BILL RECIEPTS ============================")   
                                                print(f"Provider: {water_provider}")
                                                print(f"Customer: {customer_name}")
                                                print(f"Account Number: {customer_number}")
                                                print(f"Amount Paid: N{amount}")
                                                print(f"Status: Successful")
                                                print("================================================================")
                                            
                                            else:
                                                print("Invalid electricity provider")      
                                    else:
                                         print("Invalid Meter Type")            
                #=================================================================================
                #  RETURN TO MAIN MENU
                #=================================================================================

                elif bill_choice == "4": 
                    print("Returning to main menu")
                    t.sleep(2.5)
                    break
                else:
                     print("Invalid option. Select between 1 and 4.")

        #=================================================================================
        #  OPTION 6  :  CHANGE ATM PIN
        #=================================================================================
        elif choice =="6":
         print("\n=============================================================================")
         print("                      CHANGE ATM PIN                          ")
         print("=============================================================================")            


         old_pin = int(input("Enter your current PIN:"))

         if old_pin == pin:
            new_pin = int(input("Enter new four-digit PIN "))
            confirm_pin = int(input("confirm your new PIN:"))


            if new_pin == confirm_pin:
                if 1000 <= new_pin <= 9999:
                    if new_pin != pin:
                        pin = new_pin
                        print("PIN changed successfully from old PIN.")
                    else:
                        print("Your new PIN must differ from your PIN")   
                else:
                    print("PIN must contain exactly four digit")
            else:
                print("PINs do not match")        
         else:
             print("Incorrect current PIN")        

         # ==========================================
        # OPTION 7: ACCOUNT INFORMATION
        # ==========================================

        elif choice == "7":

            print("\n========== ACCOUNT INFORMATION ==========")

            print("Account Name:", account_name)
            print("Account Number:", account_number)
            print("Account Type: Savings")
            print("Account Status: Active")
            print("Available Balance: N¦", balance)

            print("==========================================")

        # ==========================================
        # OPTION 8: TRANSACTION SUMMARY
        # ==========================================

        elif choice == "8":

          print("\n========== TRANSACTION SUMMARY ==========")

          print("Account Name:", account_name)
          print("Opening Balance: N¦", opening_balance)
          print("Total Deposits: N¦", total_deposit)
          print("Total Withdrawals: N¦", total_withdrawal)
          print("Total Transfers: N¦", total_transfer)
          print("Total Airtime Purchases: N¦", total_airtime)
          print("Total Electricity Payments: N¦", total_electricity)
          print("Total Water Payments: N¦", total_water)
          print("Number of Transactions:", transaction_count)
          print("Current Balance: N¦", balance)

          print("==========================================")

        # ==========================================
        # OPTION 9: EXIT ATM
        # ==========================================

        elif choice == "9":

            print("\n==========================================")
            print("          THANK YOU FOR BANKING")
            print("==========================================")

            print("Account Name:", account_name)
            print("Final Balance: N¦", balance)
            print("Total Transactions:", transaction_count)

            print("\nPlease take your ATM card.")
            print("Have a wonderful day!")

            break

        # ==========================================
        # INVALID MAIN MENU OPTION
        # ==========================================

        else:

            print("\nInvalid option selected.")
            print("Please select a number between 1 and 9.")

# ==================================================
#               END OF ATM PROGRAM
# ==================================================

else:

    print("\nAccess denied.")
    print("Thank you for using Python ATM.")
