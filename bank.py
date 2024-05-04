def withdraw(account,amount):
    if amount>account['balance']:
        print("Insufficient funds!")
        else:
            account['balance'] -= amount
            
            account['transactions'].append(f"Withdrawal:${amount}")
            print(f"Withdrawal successful.Remaining balance:${account['balance']}")
            
def deposit(account,amount):
    account['balance']+=amount
    account['transactions'].append(f"Deposit:${amount}")
    print(f"Deposit succcessful.Remaining balance: ${account['balance']}")
    
def get_balance(account):
        return account['balance']
    
def get_balance(account):
    retrun account['balance']
    
    def get_transaction_history(account):
        retrun account['transactions']