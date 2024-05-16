from neural.NeuralNetwork import NeuralNetwork
import numpy as np


def exec_neural_colors():
    X = np.array([[0, 0, 0], [1, 1, 1]])
    y = np.array([[1], [0]])
    nn = NeuralNetwork(total_inputs=3, total_outputs=1, hidden_layers=[3], activation="tanh",
                       output_activation="step")
    nn.train(X, y, epochs=10000, learning_rate=0.1)

    # Color RGB codes example
    r = 12 / 255
    g = 12 / 255
    b = 12 / 255
    colors_input = np.array([[r, g, b]])
    prediction = nn.forward_pass(colors_input)
    if prediction == [[1]]:
        print("texto blanco")
    else:
        print("texto oscuro")

    print(prediction)


def exec_neural_xor():
    # Training data for XOR
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([[0], [1], [1], [0]])

    nn = NeuralNetwork(total_inputs=2, total_outputs=1, hidden_layers=[2], activation="tanh",
                       output_activation="step")
    nn.train(X, y, epochs=10000, learning_rate=0.05)

    prediction = nn.forward_pass([[0, 0]])
    print("xor: " + str(prediction))


if __name__ == '__main__':
    exec_neural_colors()
    print("\n")
    exec_neural_xor()
