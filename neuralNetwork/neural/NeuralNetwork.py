import numpy as np


class NeuralNetwork:
    """
    Representa una red neuronal con la capacidad de definir la cantidad de entradas, salidas y capas ocultas, así como las funciones de activación para las capas ocultas y la capa de salida.

    Attributes:
    - total_inputs (int): El número de entradas de la red neuronal.
    - total_outputs (int): El número de salidas de la red neuronal.
    - hidden_layers (list of int): Una lista que especifica el número de neuronas en cada capa oculta. La longitud de la lista determina el número de capas ocultas.
    - activation (str): La función de activación utilizada en las capas ocultas. Puede ser 'sigmoid' o 'tanh'.
    - output_activation (str): La función de activación utilizada en la capa de salida. Puede ser 'step' o 'identity'.
    """

    SIGMOID = "sigmoid"
    TANH = "tanh"
    STEP = "step"
    IDENTITY = "identity"

    def __init__(self, total_inputs, total_outputs, hidden_layers=None, activation="sigmoid", output_activation="step"):
        """
        Inicializa una nueva red neuronal.

        Args:
        - total_inputs (int): El número de entradas de la red neuronal.
        - total_outputs (int): El número de salidas de la red neuronal.
        - hidden_layers (list of int, optional): Una lista que especifica el número de neuronas en cada capa oculta. La longitud de la lista determina el número de capas ocultas. Por defecto, se crea una red sin capas ocultas, es decir, solo una capa de entrada y una capa de salida.
        - activation (str, optional): La función de activación utilizada en las capas ocultas. Puede ser 'sigmoid' o 'tanh'. Por defecto, se utiliza 'sigmoid'.
        - output_activation (str, optional): La función de activación utilizada en la capa de salida. Puede ser 'step' o 'identity'. Por defecto, se utiliza 'step'.
        """
        self.activation = activation
        self.output_activation = output_activation
        self.total_inputs = total_inputs
        self.total_outputs = total_outputs
        if hidden_layers is None:
            self.hidden_layers = [self.total_inputs]
        else:
            self.hidden_layers = hidden_layers

        # Inicialización de pesos y sesgos
        self.weights_input_hidden = np.random.randn(self.total_inputs, self.hidden_layers[0])
        self.bias_hidden = np.zeros((1, self.hidden_layers[0]))
        self.weights_hidden_output = np.random.randn(self.hidden_layers[-1], self.total_outputs)
        self.bias_output = np.zeros((1, self.total_outputs))

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def step(self, x):
        return np.where(x >= 0, 1, 0)

    def forward_pass(self, X):
        """
        Ejecuta el forward pass, el cual no servirá para entrenar y obtener predicciones
        :param X: Entradas que serviran para predecir o evaluar el entrenamiento (Dependiendo del caso)
        :return: Salida de la prediccion o valor de entrenamiento
        """
        # Capa oculta
        if self.activation == self.SIGMOID:
            self.hidden_output = self.sigmoid(np.dot(X, self.weights_input_hidden) + self.bias_hidden)
        elif self.activation == self.TANH:
            self.hidden_output = np.tanh(np.dot(X, self.weights_input_hidden) + self.bias_hidden)

        # Capa de salida
        if self.output_activation == self.STEP:
            self.output = self.step(np.dot(self.hidden_output, self.weights_hidden_output) + self.bias_output)
        elif self.output_activation == self.IDENTITY:
            self.output = np.dot(self.hidden_output, self.weights_hidden_output) + self.bias_output

        return self.output

    def backward_pass(self, X, y, learning_rate):
        error = y - self.output

        # Calcular los gradientes para la capa de salida
        if self.output_activation == self.STEP:
            output_gradient = error
        elif self.output_activation == self.IDENTITY:
            output_gradient = error * 1  # Derivada de la identidad es 1

        # Actualizar pesos y sesgos de la capa de salida
        self.weights_hidden_output += np.dot(self.hidden_output.T, output_gradient) * learning_rate
        self.bias_output += np.sum(output_gradient, axis=0, keepdims=True) * learning_rate

        # Calcular los gradientes para la capa oculta
        if self.activation == self.SIGMOID:
            hidden_gradient = np.dot(output_gradient, self.weights_hidden_output.T) * self.sigmoid_derivative(self.hidden_output)
        elif self.activation == self.TANH:
            hidden_gradient = np.dot(output_gradient, self.weights_hidden_output.T) * (1 - np.power(self.hidden_output, 2))

        # Actualizar pesos y sesgos de la capa oculta
        self.weights_input_hidden += np.dot(X.T, hidden_gradient) * learning_rate
        self.bias_hidden += np.sum(hidden_gradient, axis=0, keepdims=True) * learning_rate

    def train(self, X, y, epochs, learning_rate):
        """
        Entrena la red neuronal utilizando el algoritmo de retropropagación.

        Args:
        - X (numpy array): Matriz de entrada de forma (número de muestras, número de características).
        - y (numpy array): Matriz de salida de forma (número de muestras, número de salidas).
        - epochs (int): Número de épocas de entrenamiento.
        - learning_rate (float): Tasa de aprendizaje del algoritmo.

        Returns:
        - None
        """
        for epoch in range(epochs):
            self.forward_pass(X)

            self.backward_pass(X, y, learning_rate)

            error = np.mean(np.abs(y - self.output))
            if epoch % 1000 == 0:
                print(f"Epoch {epoch}, Error: {error}")
