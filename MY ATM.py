print("WELCOME TO CANARA BANK")

import time
import random
import os

#global name, balance, pin, acc_no, banking, read_data, my, Bank

#classes defined for the program

class banking:
    def __init__(self, name, accountno, balance,pin):
        self.name = name
        self.accountno = accountno
        self.balance = balance
        self.pin = pin

    def printing(self):
        print("Your account details are")
        print("bank name :  ", self.name)
        print("account no :  ", self.accountno)
        print("balance :  ", self.balance)
        print("                           ")


class Bank:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self):
        amount = float(input("Enter the amount to be deposited : "))
        self.balance = float(self.balance) + amount
        print("your deposit is being processed....")
        time.sleep(4)
        print("Deposit is successful and the balance is %f " % self.balance)
        return self.balance

    def withdraw(self):
        amount = float(input("Enter the amount to withdraw : "))
        print("confirm the amount by entering again")
        l = int(input())
        if float(self.balance) >= amount:
            self.balance = float(self.balance) - amount
            print("Withdraw is successful!!  the balance is %f " % self.balance)
            n = 0
            while n == 0:
                if l == amount:
                    print("Do you want to print the receipt??  :")
                    print("enter corresponding numbers to perform action")
                    print(" 1. Yes   2. No ")
                    o = int(input())
                    if o == 1:
                        print("Please wait while the transaction is being processed....")
                        time.sleep(3)
                        print("please collect the cash")
                        print("\n")
                        print("TRANSACTION RECEIPT")
                        print(" * your amount of ", l, " has been debited from the account\n"
                                                       " * your balance amount is", self.balance)

                        #perform_action_again()

                    elif o == 2:
                        print("Please wait while the transaction is being processed....")
                        time.sleep(3)
                        print("please remove the card")
                        print("please collect the cash")

                        break
                elif l != amount:
                    print("Amount doesn't match !!")
                    #perform_action_again()
            n += 1
        else:
            print("Insufficient balance !!")
        return self.balance

    def enquiry(self):
        print("Balance in the account is %s" % self.balance)
        #perform_action_again()

#getting user info and returning in the form of list
def create_account(name):
    file_handle = open("%s.txt" % name, 'w')
    pin_no, acc_no = pin()
    balance = enter_balance()
    user_data = name + '||' + str(acc_no) + '||' + str(balance) + '||' + str(pin_no)
    file_handle.write(user_data)
    account_details = banking(name, acc_no, balance, pin_no)
    print("you account is created!!")
    print("your pin is ", pin_no)
    return account_details

#checking for account existance otherwise it will create account and return
def check_account_existance(name):
    path = "C:/Users/admin/PycharmProjects/pythonProject/MYATM/"
    dir_list = os.listdir(path)
    if "%s.txt" % name in dir_list:
        print('Account Found')
        time.sleep(4)
        read_FH = open("%s.txt" % name, 'r')
        read_data = read_FH.read()
        read_data = read_data.split("||")
        print(read_data)
        my = banking(read_data[0], read_data[1], read_data[2], read_data[3])
    # acc = Bank(my.balance)
    else:
        print("You don't have an account. So it is being created....")
        time.sleep(3)
        created_account = create_account(name)
        my = created_account
        # acc = Bank(my.balance)
    return my

#code to generate pin and account number which will be returend
def pin():
    chars = "1234567890"
    chars_acc = "12345678901234567890"
    pin_no = "".join(random.sample(chars, 4))
    acc_no = "0" + "5" + "7" + "".join(random.sample(chars_acc, 10))
    return pin_no, acc_no

#getting the balance from the user > than 500
def enter_balance():
    balance = int(input("Please deposit a minimum of 500Rs the opening amount : "))
    if balance >= 500:
        return balance
    else:
        print("Min deposit should be 500Rs")
        enter_balance()


#function get the choice of the transaction selected by user
def choice(acc,account_in_use):
    m = 0
    while m == 0:
        m += 1
        print("please select the choice  :  ")
        print(" 1. Deposit"
              " 2. withdrawal"
              " 3. Account details"
              " 4. Account Balance"
              " 5. exit")
        k = int(input())

        if k == 2:
            account_in_use.balance = acc.withdraw()
            update_balance(account_in_use)
            perform_action_again(acc, account_in_use)
        elif k == 1:
            account_in_use.balance = acc.deposit()
            update_balance(account_in_use)
            perform_action_again(acc, account_in_use)
        elif k == 3:
            print(account_in_use.name, account_in_use.balance)
            account_in_use.printing()
            perform_action_again(acc, account_in_use)

        elif k == 4:
            acc.enquiry()
            perform_action_again(acc, account_in_use)

        elif k == 5:
            exit()

    m += 1


#function to offer choice of transaction again by the user
def perform_action_again(acc,account_in_use):
    print("do you want  to continue the process again??")
    print("1. yes       2. No")
    print("enter corresponding numbers to perform action")
    g = int(input())
    if g == 1:
        choice(acc,account_in_use)
    elif g == 2:
        update_balance(account_in_use)
        exit()
    else:
        update_balance(account_in_use)
        print("invlaid input")
        perform_action_again(acc,account_in_use)


#funtion to login to the account
def login(account_in_use):
    print(account_in_use.name, account_in_use.pin)
    User_name = str(input("Please enter your USER NAME  :  "))
    Password = str(input("Please enter your 4 digit pin code :  "))

    if User_name == account_in_use.name and Password == account_in_use.pin:
        print("logged in")
        return True
        # print("please select the choice  :  ")
        # print("1.Savings ""2.current")
        # j = int(input())
        # if j == 1:
        #     choice(acc,account_in_use)

        # else:
        #     print("You don't have a Current account")

    else:
        print("Your password is Incorrect"
              " please rerun the code(please remove your card and re-insert)")
        return False

def main_function():
    name = str(input("Please enter your name  :  "))
    print("The account is being verified for its existance. Please wait....")
    account_in_use = check_account_existance(name)
    acc = Bank(account_in_use.balance)
    print("\n \n")
    print("Here is your debit card\n")
    print("Login to your account")
    time.sleep(2)
    logged_in = login(account_in_use)
    if logged_in:
        choice(acc,account_in_use)
    else:
        print("not logged in, login again to continue")
        main_function()


def update_balance(account_in_use):
    file_handle = open("%s.txt" % account_in_use.name, 'w')
    new_data = account_in_use.name +'||'+ str(account_in_use.accountno) + '||' + str(account_in_use.balance) + '||' + str(account_in_use.pin)
    file_handle.write(new_data)
    return True

main_function()