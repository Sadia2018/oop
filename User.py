class User:

    def __init__(self, name):
        self.name = name
        self.amount = 0

    def make_deposit(self, amount):
        self.amount += amount

    def make_withdrawal(self,amount):
        self.amount -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")

    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()


sadia = User("Sadia")
sam = User("Mr. Sam")
samira = User("Samira")

sadia.make_deposit(100).make_deposit(200).make_deposit(200).make_withdrawal(45).display_user_balance()
# sadia.make_deposit(200)
# sadia.make_deposit(50)
# sadia.make_withdrawal(45)
# sadia.display_user_balance()

sam.make_deposit(1000)
sam.make_deposit(1000)
sam.make_withdrawal(500)
sam.make_withdrawal(300)
sam.display_user_balance()

samira.make_deposit(1500)
samira.make_withdrawal(1000)
samira.make_withdrawal(5000)
samira.make_withdrawal(3000)
samira.display_user_balance()


sam.transfer_money(400, sadia)


