class Account:
    # dollars can be positive and negative and can range from -10**9 and 10**9
    dollars=0
    # cents will always be non-negative
    cents=0
    
    def __init__(self) -> None:
        self.dollars=0
        self.cents=0
    
    def add_money(self, dollars: int , cents: int):
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
            
    def withdraw_money(self, dollars: int, cents: int):
        modified_dollars=self.dollars-dollars
        modified_cents=self.cents-cents
        
        modified_dollars+=modified_cents//100
        modified_cents%=100
        
        if modified_dollars>10**9 or modified_dollars<-1*10**9:
            print('Operation cannot be performed since it violates the account limits')
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