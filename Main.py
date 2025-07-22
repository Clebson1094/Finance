from config import Calculator

calc = Calculator()

while True:
    carteira = calc.config()

    print(f"Saldo atual: {carteira}")