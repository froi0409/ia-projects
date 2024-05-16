import random


class Neuron:
    def __init__(self, value=0, max_integer_weight=0, decimals=4):
        self.value = value
        self.weight = round(random.random(), decimals)
        # if decimals > 0:
        #     self.weight = round(random.random(), decimals)
        # if max_integer_weight > 0:
        #     self.weight = random.randint(-max_integer_weight)
        self.inputs = []
        self.outputs = []