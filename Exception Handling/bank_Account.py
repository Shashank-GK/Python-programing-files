# This program will show exception if user tries to get money after the minimum balance.


class MinimumBalanceException(Exception):
    pass


def bank(Min_balance):
    global balance
    Choice = input("Enter 'Withdraw' or 'Deposit' to continue: \n")
    if Choice == "Deposit":
        deposit_amount = int(input("Enter the amount to deposit: \n"))
        balance = balance + deposit_amount
        print("Your Balance is Rs. ", balance)

    elif Choice == "Withdraw":
        if balance == 0:
            balance_da = int(
                input("You have a '0' balance, Enter the amount to deposit")
            )
            balance = balance + balance_da
            print("Your Balance is Rs. ", balance)
        else:
            withdraw_amount = int(input("Enter the amount to withdraw: \n"))
            balance = balance - withdraw_amount
            print("Your Balance is Rs. ", balance)
            if balance <= Min_balance:
                raise MinimumBalanceException(
                    "Your Balance is Rs. {0} with reference to minimum balance of Rs. {1} \nIf you does not maintain minimum balance, You will be charge Rs. 10/month as fine".format(
                        balance, Min_balance
                    )
                )
            else:
                print("Thank You for using our service")
    else:
        print("Invalid Choice")


Min_balance = 500
balance = 500  # This is the current balance in the account, it may change over time if the user deposits or withdraws money.

try:
    bank(Min_balance)
except MinimumBalanceException as e:
    print(e)
