class bank:
    def __init__(self,bal):
        self.bal=bal
    def bank_account_balance(self,bal):
        print("Total balance Available in your account: ",*bal)
    def bank_account_withdraw(self,debit):
            for i in bal:
                if debit>0 and debit<= i:
                    print("Collect your cash: ",debit)
                    debit_bal= i- debit
                    print("Balance after withdrawal: ", debit_bal)
                    bal.clear()
                    bal.append(debit_bal)
                    break
                elif debit == 0:
                    print("Please enter amount greater than 0")
                else:
                    print("Insufficient balance")
                    quit()
    def bank_account_deposit(self, credit):
        for i in bal:
            if credit > 0:
                credit = i + credit
                print("Your total available balance after deposited amount: ", credit)
                bal.clear()
                bal.append(credit)
                break
            else:
                print("Enter Valid amount to deposit. This service is cancelled please start new service for depositing again")

print("Enter your bank account number: ")
act_num=int(input())
bal=[1000]
b=bank(bal)

while True:
    msg1="""******COIMBATORE BANK INTERNATIONAL LIMITED******
SELECT SERVICES- 
1.Show Available Balance
2.Withdraw
3.Deposit
4.Cancel
*****************THANK YOU*********************"""
    print(msg1,"\n")
    ch=int(input("Enter your choice: "))
    if ch==1:
        b.bank_account_balance(bal)
        print("\r")
    elif ch==2:
        debit=int(input("Enter amount to withdraw: "))
        b.bank_account_withdraw(debit)
        print("\r")
    elif ch==3:
        credit=int(input("Enter amount to deposit: "))
        b.bank_account_deposit(credit)
        print("\r")
    elif ch>=4:
        print("Thank You, Have a nice day!")
        quit()