class Calculator():
    
    def __init__(self):   
        self.balance = 0
    
    def config(self):
        try:
            function = int(input("Options:\n[1]Add Value to your Balance\n[2]Include expense\nEnter: "))
            value = float(input("Enter your value\nEnter R$:"))
            match function:
                case 1:
                    self.balance += value
                case 2:
                    self.balance -= value
                case _:
                    print("Please select only the options")
        except ValueError:
            print("nn")
        return self.balance
