class Calculator():

    def __init__(self):
        self.balance = 0
        self.debts = []
        self.entry = ["SALARIO", "COMISSOES"]
        self.exit = ["ALUGUEL", "CARTAO"]

    def debt(self, nome):
        if nome in self.entry:
            tipo = "ENTRY"
        elif nome in self.exit:
            tipo = "EXIT"
        else: #REGISTRA UM NOVO TIPO DE DÉBITO CASO NÃO TENHA
            option = str(input(f"{nome} is ENTRY or EXIT? ")).upper().strip()
            if option == "ENTRY":
                tipo = "ENTRY"
                self.entry.append(nome)
                print(f"{nome} Registration completed successfully in ENTRY")
            elif option == "EXIT":
                tipo = "EXIT"
                self.exit.append(nome)
                print(f"{nome} Registration completed successfully in EXIT")
            else:
                print("Please choose only the options provided")
            return self.exit, self.entry
        valor = float(input("Enter value: "))
        if valor <= 0:
            print("The value must be positive")
            return self.balance, self.debts
        self.debts.append({"name": nome, "type": tipo, "value": valor})
        match tipo:
            case "ENTRY":
                self.balance += valor
            case "EXIT":
                self.balance -= valor

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
