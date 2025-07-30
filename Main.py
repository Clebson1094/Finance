from config import Calculator

calc = Calculator() #chamando a classe

while True:
    print((("[1] Finance Control\n"
    "[2] Dream Planning\n"
    "[3] Show Table\n"
    "[4] Remove regisered debt\n"
    "[5] Exit\n")))
    try:
        choices = int(input("Choice you option: "))
        if choices not in [1, 2, 3, 4, 5]:
            print("Please, choose a valid option: ")
            continue
        if choices == 2 and calc.balance == 0:
            print("I need to know about your finances first 😢")
            continue
        match choices:
            case 5:
                print("Tanks for using my application")
                break
            case 1:
                nome = str(input("Enter name "))
                calc.debt(nome)
            case 2:
                value_dream = float(input("Enter value you dram"))
                months = int(input("For months?"))
                calc.planning_dream(value_dream, months, calc.balance)
            case 3:
                calc.show_table()
                continue
            case 4:
                if bool(calc.debts) == True:
                    nome = str(input("Enter name to remove: "))
                    calc.remove_debt(nome)
                    continue
                else:
                    print("No items in your financial table 😢")
                    continue
    except ValueError:
        print("Please, choice a valid option")
        continue