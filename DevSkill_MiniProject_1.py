

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
    Pending Task: Adding the current amount with the previous amount and validate
    -----------------------------------------------------------------------------
'''
def deposit():
    try:
        deposit= float(input('Enter the ammount that you would like to deposit: '))

    except:
        print('Invalid User Input ')
   

# this function will ask the user regarding the amount for withdraw
'''
    --------------------------------------------------------------------------------------
    Pending Task: 1. checking the current available amount, 
                  2. validate regarding the user is allowed to withdraw the desired amount
    --------------------------------------------------------------------------------------
'''
def withdraw():
    try:
        withdraw= float(input('Enter the ammount that you would like to withdraw: '))

    except:
        print('Invalid User Input ')


# this function will show the current balance
'''
    --------------------------------------------------------------------------------------
    Pending Task: 1. function which is holds all users current balance information 
                  
    --------------------------------------------------------------------------------------
'''
def available_balance():
    print('Your current balance is: ')

# testing the functionality of the function
Home_Screen()
deposit()