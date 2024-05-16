from utilities.Model import Model
from utilities.Input import Input
from colorama import init, Fore

init()


def start():
    print(Fore.YELLOW + "Modelo en entrenamiento..." + Fore.RESET)

    model = Model()
    # model.input_model = [
    #     Input(x1=0, x2=1, y=0),
    #     Input(x1=1, x2=0, y=0),
    #     Input(x1=0, x2=0, y=0),
    #     Input(x1=1, x2=1, y=1)
    # ]
    model.train_model()

    print(Fore.YELLOW + "Modelo Entrenado con éxito." + Fore.RESET)
    print("\nIngrese sus percepciones")
    x1 = input("x1: ")
    x2 = input("x2: ")

    print("Resultado: " + str(model.calculate(x1, x2)))


if __name__ == '__main__':
    start()
