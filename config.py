class Calculator():

    def __init__(self):
        self.balance = 0
        self.debts = []
        self.entry = ["SALARIO", "COMISSOES"]
        self.exit = ["ALUGUEL", "CARTAO"]

    def debt(self, nome, valor):
        if nome in self.entry:
            tipo = "ENTRY"
        elif nome in self.exit:
            tipo = "EXIT"
        else:
            return self.balance, self.debts  # Não faz nada se não encontrar

        self.debts.append({"name": nome, "type": tipo, "value": valor})
        match tipo:
            case "ENTRY":
                self.balance += valor
            case "EXIT":
                self.balance -= valor
        return self.balance, self.debts

    def planning_dream(self, value_dream, months, balance):
        real_dream = value_dream / months
        recommendation = value_dream / (balance * 30 / 100)
        if recommendation > real_dream:
            print(f"To reach you goal {real_dream:.2f} for month")
            print(f"For safety i recommend {balance * 30 / 100:.2f} for month, during {recommendation:.2f}")
        else:
            print(f"To reach you goal {real_dream:.2f} for month")

    def show_table(self):
        if bool(self.debts) == True:
            print("TABLE")
            for debt in self.debts:
                print(f"Name: {debt['name']} | Type: {debt['type']} | Value: R$:{debt['value']:.2f}")
            print(f"Final Balance: {self.balance:.2f} ")
            return self.balance, self.debts
        else:
            print("No items in your financial table 😢")

    def cadastro(self, nome, option):
        if option == "ENTRY":
            tipo = "ENTRY"
            self.entry.append(nome)
            return tipo
        elif option == "EXIT":
            tipo = "EXIT"
            self.exit.append(nome) 
            return tipo
        return self.exit, self.entry

    def remove_debt(self, nome):
        for debt in self.debts:
            if debt['name'] == nome and debt['type'] == "ENTRY":
                self.balance -= debt['value']
                print(f"{nome} removed successfully")
            elif debt['name'] == nome and debt['type'] == "EXIT":
                self.balance += debt['value']
                print(f"{nome} removed successfully")
            self.debts.remove(debt)
        else:
            print(f"{nome} not found in your debts")