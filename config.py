class Calculator():
#Temos a majestosa classe
    def __init__(self):#Aqui onde tudo inicia independente da ordem que ocorre as funções (EU ACHO)
        self.balance = 0
        self.debts = []
        self.entry = ["SALARIO", "COMISSOES"]
        self.exit = ["ALUGUEL", "CARTAO"]

    def debt(self, nome, valor): #Essa função basicamente irá identificar o que é entrar e somar, ou saída subtrair
        if nome in self.entry:
            tipo = "ENTRY"
        elif nome in self.exit:
            tipo = "EXIT"
        else:
            return self.balance, self.debts  # Não faz nada se não encontrar

        self.debts.append({"name": nome, "type": tipo, "value": valor}) #Aqui é a estrutura do dicionário
        match tipo:
            case "ENTRY":
                self.balance += valor #Se identificar como entrada soma
            case "EXIT":
                self.balance -= valor #Se identificar como saída subtrai
        return self.balance, self.debts #Se não for entrada nem saída, não faz nada

    def planning_dream(self, value_dream, months, balance): #Esse é um conceito muito bom de plano para o futuro, porém irei melhorar 200% dessa lógica
        real_dream = value_dream / months #Aqui pega o valor do seu sonho e divide pelos meses que você quer conquistar
        recommendation = value_dream / (balance * 30 / 100) #Aqui serve para ser uma alternativa melhor, no caso fazer um planejamento seguro, pegando apenas 30% do seu saldo liquido mensal
        if recommendation > real_dream:#Se ele recomendar um valor maior em menos prazo, te mostra
            print(f"To reach you goal {real_dream:.2f} for month")
            print(f"For safety i recommend {balance * 30 / 100:.2f} for month, during {recommendation:.2f}")
        else:
            print(f"To reach you goal {real_dream:.2f} for month") #Caso contrario, somente o valor bruto mesmo

    def show_table(self): #Essa função foi meu brother GUANABARA PAI DA CIÊNCIA que me ensinou, utilizando um FOR para printar meu dicionário
        if bool(self.debts) == True: #Eu gosto de booleano
            print("TABLE")
            for debt in self.debts:
                print(f"Name: {debt['name']} | Type: {debt['type']} | Value: R$:{debt['value']:.2f}")
            print(f"Final Balance: {self.balance:.2f} ")
            return self.balance, self.debts
        else: #Se a lista de dicionários tiver vazia, printa isso
            print("No items in your financial table 😢")

    def cadastro(self, nome, option): #Essa função cadastra o nome e o tipo de entrada ou saída financeira que você tem
        if option == "ENTRY":
            tipo = "ENTRY"
            self.entry.append(nome)
            return tipo
        elif option == "EXIT":
            tipo = "EXIT"
            self.exit.append(nome) 
            return tipo
        return self.exit, self.entry #Se não for entrada nem saída, retorna nadinha

    def remove_debt(self, nome): #Aqui removemos os débitos cadastrados e ainda devolvemos o valor devolta ao saldo
        for debt in self.debts:
            if debt['name'] == nome and debt['type'] == "ENTRY":
                self.balance -= debt['value']
            elif debt['name'] == nome and debt['type'] == "EXIT":
                self.balance += debt['value']
            self.debts.remove(debt)
        else:
            print(f"{nome} not found in your debts")