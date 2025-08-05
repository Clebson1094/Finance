from config import Calculator
#Está importando a Classe Calculator do arquivo config

calc = Calculator() #chamando a classe

while True:
    #Iniciando o Loop infinito(Ou quase infinito)
    print((("[1] Finance Control\n"
    "[2] Dream Planning\n"
    "[3] Show Table\n"
    "[4] Remove regisered debt\n"
    "[5] Exit\n")))
    #Um menu de interatividade com o usuário em terminal
    try:
        #O try serve para evitar erros advindo dos inputs
        choices = int(input("Choice you option: "))
        if choices not in [1, 2, 3, 4, 5]:
            print("Please, choose a valid option: ")
            continue
        #Nesse bloco ele define qual vai ser a escolha do usuário
        if choices == 2 and calc.balance == 0:
            print("I need to know about your finances first 😢")
            continue
        #Se escolher 2 e não tiver nada no balance[], ele não executa
        match choices:
            #Aqui abaixo em cada case está a escolha do usuário
            case 5:
                print("Thanks for using my application")
                break
            #Aqui ele finaliza o loop
            case 1:
                nome = str(input("Enter name "))
                if nome not in calc.entry and nome not in calc.exit:
                    option = str(input(f"{nome} is ENTRY or EXIT? ")).upper().strip()
                    if option == "ENTRY" or option == "EXIT":                       
                        calc.cadastro(nome, option)
                        #Aqui se não tiver cadastrado o débito como saída ou entrada, ele irá cadastrar
                        print(f"{nome} Registration completed successfully in {option}")
                    else:
                        print("Invalid option.")
                        continue  
                valor = float(input("Enter value: "))
                if valor <= 0:
                    print("The value must be positive")
                    continue
                calc.debt(nome, valor)
                print("Successfully registered")
                #No momento está bastante bagunçado e isso me incomoda, porém está que digamos "funcional"
                #Mas ele executa a lógica principal que é cadastrar dentro da lista, e definir também se é entrada ou saída
            case 2:
                value_dream = float(input("Enter value you dream"))
                months = int(input("For months?"))
                calc.planning_dream(value_dream, months, calc.balance)
                #Executa a lógica do planejando um sonho
            case 3:
                calc.show_table()
                continue
                #Função simples para printar a tabela e o usuário não se perder
            case 4:
                if bool(calc.debts) == True:
                    #Gosto de booleano
                    nome = str(input("Enter name to remove: "))
                    calc.remove_debt(nome)
                    #Remove algum débito da lista
                    if calc.correct == True:
                        print(f"{nome} removed successfully")
                    continue
                else:
                    print("No items in your financial table 😢")
                    #Se o item não existir na lista, ele retorna para o menu
                    continue
    
    except ValueError:
        print("Please, choice a valid option")
        #Caso o usuário faça algo que não foi solicitado EX: Colocar STR em INT ou FLOAT
        continue