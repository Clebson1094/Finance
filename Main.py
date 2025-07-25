from config import Calculator

calc = Calculator() #chamando a classe

def options(choice):
    while True:
        if choice not in [1, 2, 3, 4]:
            print("Please, choose a valid option: ")
        else:
            break
        return choice
    match choice:
        case 1:
            nome = str(input("Enter name "))
            tipo = str(input("Entry or Exit: ")).upper().strip()
            calc.debt(nome, tipo) #chamando as funções que estão dentro da Classe
            calc.show_debts()
        case 2:
            value_dream = float(input("Enter value you dram"))
            months = int(input("For months?"))
            calc.planning_dream(value_dream, months, calc.balance)

while True:
    try:
        choices = int(input("Choice you option: "))
        options(choices)
    except ValueError:
        print("Repeat")
        continue