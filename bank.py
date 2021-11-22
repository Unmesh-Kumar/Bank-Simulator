class Account:
    dollars=0
    cents=0
    
    def __init__(self) -> None:
        self.dollars=0
        self.cents=0
    
    def add_money(self,dollars,cents):
        modified_dollars=self.dollars+dollars
        modified_cents=self.cents+cents
        
        modified_dollars+=modified_cents//100
        modified_cents%=100
        
        if modified_dollars>10**9 or modified_dollars<-1*10**9:
            print('Operation cannot be performed since it voilates the account limits')
        else:
            self.dollars=modified_dollars
            self.cents=modified_cents
            print('Successful!')
            
    def withdraw_money(self,dollars,cents):
        modified_dollars=self.dollars-dollars
        modified_cents=self.cents-cents
        
        modified_dollars+=modified_cents//100
        modified_cents%=100
        
        if modified_dollars>10**9 or modified_dollars<-1*10**9:
            print('Operation cannot be performed since it voilates the account limits')
        else:
            self.dollars=modified_dollars
            self.cents=modified_cents
            print('Done')
            
    def fetch_balance(self):
        if self.cents==0:
            return f'Current Balance is {self.dollars}D'
        elif self.dollars==0:
            return f'Current Balance is {self.cents}C'
        else:
            return f'Current Balance is {self.dollars}D {self.cents}C'  


def display_the_welcome_screen():
    print('Select an option:')
    print('1. Credit')
    print('2. Debit')
    print('3. Check Balance')
    print('4. Exit')
    
def show_balance(user_account):
    print(user_account.fetch_balance())
    
def handle_credit(user_account):
    print('Enter Amount')
    entered_text=input()
    dollars=0
    cents=0
    
    for units in entered_text.split():
        if units[-1]=='D':
            dollars=int(units[:-1])
        else:
            cents=int(units[:-1])
            
    user_account.add_money(dollars,cents)
        
    
    
def handle_debit(user_account):
    print('Enter Amount')
    entered_text=input()
    dollars=0
    cents=0
    
    for units in entered_text.split():
        if units[-1]=='D':
            dollars=int(units[:-1])
        else:
            cents=int(units[:-1])
            
    user_account.withdraw_money(dollars,cents)



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
    
    