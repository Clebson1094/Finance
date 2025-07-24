class Calculator():

    def __init__(self):
        self.balance = 0
        self.debts = []

    def debt(self, nome, tipo):

        if tipo not in ["ENTRY", "EXIT"]:
            print("Select only (ENTRY) or (EXIT)")
            return self.balance, self.debts

        try:
            valor = float(input("Enter value: "))
            if valor <= 0:
                print("The value must be positive")
                return self.balance, self.debts
        except ValueError:
            print("Invalid value, please select valid value")
            return self.balance, self.debts

        self.debts.append({"name": nome, "type": tipo, "value": valor})

        match tipo:
            case "ENTRY":
                self.balance += valor
            case "EXIT":
                self.balance -= valor

    def planning_dream(self, balance, months):

        idea = balance / months
        result = idea * 30 / 100

    def show_debts(self):
        print("TABLE")
        for debt in self.debts:
            print(f"Name: {debt['name']} | Type: {debt['type']} | Value: R$:{debt['value']:.2f}")
        print(f"Final Balance: {self.balance} ")

        return self.balance, self.debts
    
    