from config import Calculator

calc = Calculator() #chamando a classe

while True:
    print((("[1] Finance Control\n"
    "[2] Dream Planning\n"
    "[3] Show Table\n"
    "[4] Exit")))
    try:
        choices = int(input("Choice you option: "))
        if choices == 4:
            print("Tanks for using my application")
            break
        elif choices == 2 and calc.balance == 0:
            print("I need to know about your finances first 😢")
            continue
        calc.options(choices)
    except ValueError:
        print("Please, choice a valid option")
        continue