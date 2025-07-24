from config import Calculator

calc = Calculator() #chamando a classe

while True:
    nome = str(input("Enter name "))
    tipo = str(input("Entry or Exit: ")).upper().strip()
    calc.debt(nome, tipo) #chamando as funções que estão dentro da Classe
    calc.show_debts()