class accountHolder():
    def __init__(self, cardNumber, pin, firstname, lastname, balance):
        self.cardNumber = cardNumber
        self.pin = pin
        self.firstname = firstname
        self.lastname = lastname
        self.balance = balance
    
   
    # Method for getting user information
   
    def get_cardNumber(self):
        return self.cardNumber
    def get_pin(self):
        return self.pin
    def get_firstname(self):
        return self.firstname
    def get_lastname(self):
        return self.lastname
    def get_balance(self):
        return self.balance

    # setting user information
    def set_cardNumber(self, newValue):
        self.cardNumber = newValue
    def set_pin(self, newValue):
        self.pin = newValue
    def set_firstnamer(self, newValue):
        self.firstname = newValue
    def set_lastname(self, newValue):
        self.lastname = newValue
    def set_balance(self, newValue):
        self.balance = newValue


    def display(self):
        print( "card Number: ", self.cardNumber)
        print( "Pin: ", self.pin)
        print( "First Name: ", self.firstname)
        print( "Last Name: ", self.lastname)
        print( "Balance: ", self.balance)


# this function will ask the uuser for the reason for using ATM card 
def Home_Screen():
    print('Please select of the following options ')
    print('1. Deposit ')
    print('2. Withdraw ')
    print('3. Balance ')
    print('4. Exit ')


# this function will ask the user regarding the amount for deposit
'''
    -----------------------------------------------------------------------------
     Task: Adding the current amount with the previous amount and validate
    -----------------------------------------------------------------------------
'''
def deposit(accountHolder):
    try:
        deposit= float(input('Enter the ammount that you would like to deposit: '))
        accountHolder.set_balance(accountHolder.get_balance() + deposit)
        print('Your new balance is: ', str(accountHolder.get_balance()))
    except:
        print('Invalid User Input ')
   

# this function will ask the user regarding the amount for withdraw
'''
    --------------------------------------------------------------------------------------
     Task: 1. checking the current available amount, 
           2. validate regarding the user is allowed to withdraw the desired amount
    --------------------------------------------------------------------------------------
'''
def withdraw(accountHolder):
    try:
        withdraw= float(input('Enter the ammount that you would like to withdraw: '))
        if(accountHolder.get_balance()< withdraw):
            print('Insufficient balance: ')
        else:
            accountHolder.set_balance(accountHolder.get_balance - withdraw)
            print('Thank You')

    except:
        print('Invalid User Input ')


# this function will show the current balance
'''
    --------------------------------------------------------------------------------------
     Task: 1. function which is holds all users current balance information 
                  
    --------------------------------------------------------------------------------------
'''
def available_balance(accountHolder):
    print('Your current balance is: ', accountHolder.get_balance())

if __name__ == "__main__":
    present_user = accountHolder("", "", "", "", "")

    # User Database
    accountHolder_list = []
    accountHolder_list.append(accountHolder("100200", 1470, "Lily", "Homes", 15.58))
    accountHolder_list.append(accountHolder("300400", 2583, "Joe", "Marshal", 95.20))
    accountHolder_list.append(accountHolder("500600", 3691, "John", "Smith", 500.0))

# testing the functionality 

    # 1. Debit card number validation
    debitCardNumber = " "
    while True:
        try:
            debitCardNumber = input (" Please enter your debit card number: ")
            debitMatch = [ dnumber for dnumber in accountHolder_list if dnumber.cardNumber == debitCardNumber ]
            # for dnumber in accountHolder_list:
            #     if dnumber.cardNumber== debitCardNumber:
            #         debitMatch.append(dnumber) 
            if (len(debitMatch)>0):
                present_user = debitMatch[0]
                break
            else:
                print(" Card number not valid. Please Try again")

        except:
                print(" Card number not valid. Please Try again")

    #2. Pin validation
    while True:
        try: 
            uPin = int(input("Please enter your pin: ").strip())
            if(present_user.get_pin()== uPin):
                break
            else:
                 print(" Enter a valid pin")
        except:
            print(" Enter a valid pin")


    print( "Welcome to ATM ", present_user.get_firstname())
    options = 0
    while (options != 4):
        Home_Screen()
        try:
            options = int ( input()) 
        except:
            print("Invalid input from the user. Please try again.")
        if (options ==1):
            deposit(present_user)
        elif (options == 2):
            withdraw(present_user)
        elif (options == 3):
            available_balance(present_user)
        elif (options == 4):
            break
        else:
            options = 0
print( "Thanks for using our ATM. ")
