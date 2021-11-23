from .account import Account

def display_the_welcome_screen():
    print('Select an option:')
    print('1. Credit')
    print('2. Debit')
    print('3. Check Balance')
    print('4. Exit')
    
def show_balance(user_account: Account):
    print(user_account.fetch_balance())
    
def parse_dollars_and_cents():
    print('Enter Amount')
    entered_text=input()
    dollars=0
    cents=0
    
    for units in entered_text.split():
        if units[-1]=='D':
            dollars=int(units[:-1])
        else:
            cents=int(units[:-1])
            
    return dollars,cents
    
    
def handle_debit(user_account: Account):
    dollars,cents=parse_dollars_and_cents()
    user_account.withdraw_money(dollars,cents)
    
    
def handle_credit(user_account: Account):
    dollars,cents=parse_dollars_and_cents()
    user_account.add_money(dollars,cents)


if __name__ == "__main__":
    user_account=Account()
    
    while True:
        display_the_welcome_screen()
        response = input()
        if response== '1':
            handle_credit(user_account)
        elif response == '2':
            handle_debit(user_account)
        elif response == '3':
            show_balance(user_account)
        else:
            print('Thank You!')
            break 
    
    