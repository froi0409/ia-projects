from utilities.Input import Input
from colorama import init, Fore

init()


class Model:
    def __init__(self, input_model=None):
        if input_model is None:
            self.input_model = [
                Input(x1=0, x2=1, y=1),
                Input(x1=1, x2=0, y=1),
                Input(x1=0, x2=0, y=0),
                Input(x1=1, x2=1, y=1)
            ]
        else:
            self.input_model = input_model

        self.w1 = 0.2
        self.w2 = 0.6
        self.umbral = 0.4
        self.lambda_value = 0.2
        self.bias = self.get_bias()

    def get_bias(self):
        return self.umbral * -1

    def train_model(self):
        iteration = 1
        while True:
            print(Fore.GREEN + "Iteration " + str(iteration))
            errors = False
            for element in self.input_model:
                print(Fore.CYAN + "element: " + str(element.x1) + " - " + str(element.x2) + Fore.RESET)
                self.bias = self.get_bias()
                z = (element.x1 * self.w1) + (element.x2 * self.w2) + self.bias
                activation = 1 if z >= 0 else 0
                error_value = element.y - activation

                print("z: " + str(z))
                print("activation: " + str(activation))
                print("error_value: " + str(error_value))

                if error_value != 0:
                    umbral_diff = -(self.lambda_value * error_value)
                    self.umbral = self.umbral + umbral_diff
                    print("umbral_diff: " + str(umbral_diff))
                    print("new_umbral: " + str(self.umbral))

                    w1_diff = self.lambda_value * error_value * element.x1
                    self.w1 = self.w1 + w1_diff
                    w2_diff = self.lambda_value * error_value * element.x2
                    self.w2 = self.w2 + w2_diff
                    print("w1_diff: " + str(w1_diff))
                    print("new_w1: " + str(self.w1))
                    print("w2_diff: " + str(w2_diff))
                    print("new_w2: " + str(self.w2))

                    if element.y != 0:
                        percent_error = abs(((activation - element.y) / element.y) * 100)
                    else:
                        percent_error = abs((activation - element.y) * 100)
                    print("percent_error: " + str(percent_error))

                    if percent_error > 1:
                        errors = True

            if errors is False:
                break
            iteration = iteration + 1
