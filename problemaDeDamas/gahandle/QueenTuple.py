import random


class QueenTuple:
    def __init__(self, queens=None):
        self.queens = []
        if queens is None:
            self.generate_queens()
        else:
            self.queens = queens
        self.fitness_value = self.get_fitness_function()

    def __str__(self):
        output = ""
        for i in range(len(self.queens)):
            output += str(self.queens[i]) + " "
        output += " -- fitness function: " + str(self.fitness_value)
        return output

    def generate_queens(self, size=8):
        for i in range(size):
            self.queens.append(random.randint(1, 8))

    def get_fitness_function(self):
        total_queens = 28
        for i in range(1, 8):
            cont = 0
            for j in range(i, 8):
                cont += 1
                if j != 8 and (self.queens[i-1] == self.queens[j] or self.queens[i-1] == (self.queens[j] + cont) or self.queens[i-1] == (self.queens[j] - cont)):
                    total_queens -= 1
        return total_queens

    def set_fitness_value(self):
        self.fitness_value = self.get_fitness_function()