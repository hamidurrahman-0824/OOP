class BankAccount:
    customer = 0
    accounts = []
    def __init__(self,name,id,origin,baln= 0):
        self.name = name 
        self.id = id 
        self.origin = origin
        self.baln = baln
        BankAccount.customer += 1
#        BankAccount.customer = BankAccount.customer
        BankAccount.accounts.append(self)
      
    def add(self,amount):
        if amount>0:
            self.baln += amount
            return f'Succesfully added {amount}, current balance {self.baln}'
        else:
            return f'Invalid amount.'
    def withdraw(self,amount):
        
        if self.baln >= amount:
            self.baln -= amount
            return f'Succesfully withdrew {amount}, current balance {self.baln}'
        else:
            return f'Insufficient Fund'
    def __str__(self):
        return f'Name :{self.name}\
            ID :{self.id}\
                Origin : {self.origin}'
    @classmethod
    def richest(cls):
        if not cls.accounts:
            return "No accounts in the bank"
        richest_acc = max(cls.accounts, key = lambda acc : acc.baln)  
        return f"The largest amount is {richest_acc.baln} (Owner: {richest_acc.name})"
customer1 = BankAccount('MAk',1001, 'Dhaka')
customer2 = BankAccount('MAkk',1002, 'Dhaka')
customer3 = BankAccount('MAkkk',1003, 'Dhaka')
print(customer1.add(100))
print(customer2.add(300))
print(customer1.add(400))
print(BankAccount.customer)
print(BankAccount.richest())
print(customer1)
