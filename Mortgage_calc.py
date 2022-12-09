#prompt the user to enter username
name = str(input("Enter your name "))

#store the correct pin used to verify users
pin_number= "345673"
attempts = 0

#Verify the name from the list of 3 users, if not prompt user to enter name again
while name not in ('Wycliffe','Damian', 'Teachops'):   
        print("Verification Failed for "+ name)
        name =str(input("Enter your name "))
        attempts += 1
        if attempts ==5:
            #if the user makes 5 unsuccessful attemps, block him fro trying further  
            print("Too many attemps! Account Locked ",
                    "Please contact your system Administrator ")
            break
else:
#if the name is coorect, prompt the user to enter the PIN
        pin = str(input("Enter your PIN "))
#check if the pin entered is correct, if not, prompt the user to enter again while showing the number of attemps made
        while(pin != pin_number):
                print ("Wrong Pin, ")
                pin = input("Attempt #" + str(attempts) + " | " + "Enter your PIN ")
#if the user makes 10 unsuccessful attempts, block them from trying again. 
                attempts += 1
                if attempts ==10:
                    print("Too many attemps! Accoount Locked ",
                    "Please contact your Administrator "  )
                    break
#If pin entered is correct then allow the user to proceed
        if pin == pin_number:
            print(f'\nWelcome {name}\n')
#prompt user to enter Loan amount
            P = int(input("Enter the Loan Amount \n"))
#prompt user to enter repayment period in years
            Y = int(input("Enter Repayment period in year \n"))
#prompt user to enter the annual interest rate
            R = float(input("Enter the Annual interest rate \n"))
#calculate the interest period in months 
            n = float(12*Y)
#calculate the monthly interest rates
            r = float(R/12)/100
#calculate the Monthly installments 
            M =P*(((r*(1 + r)**n))/(((1+r)**n)-1))
#Calculate Total amount to be paid back with interests
            A = M * n 
#Print out the Monthly installments and Total amounts 
            print(f'\nMonthly repayments = {M:.2f}\n')
            print (f'Total Repayment Amount = {A:.2f}')
           
            