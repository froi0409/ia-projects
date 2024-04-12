from gahandle.QueenTuple import QueenTuple
import random

class Population:
    def __init__(self):
        self.population = []
        self.aux_population = []
        self.generate_population()

        self.max_value = self.get_max_value()

    def generate_population(self, size=10):
        for i in range(size):
            self.population.append(QueenTuple())

    def print_population(self):
        for i in range(len(self.population)):
            print("Entity " + str(i+1) + ": " + str(self.population[i]))

    def new_generation(self):
        for i in range(1, 5):
            parent_1 = self.get_parent()
            parent_2 = self.get_parent()

            self.crossover(parent_1, parent_2)

        self.population = self.aux_population
        self.aux_population = []
        print("\n\nNUEVA GENERACIÓN:")

    def get_parent(self):
        value = random.randint(self.population[0].fitness_value, self.max_value)
        sum = 0
        for i in range(len(self.population)):
            sum += self.population[i].fitness_value
            if (sum > value):
                return self.population[i]
        return self.population[len(self.population) - 1]

    def get_max_value(self):
        value = self.population[0].fitness_value
        for i in range(len(self.population)):
            value += self.population[i].fitness_value
        return value

    def crossover(self, queen_tuple_1_object, queen_tuple_2_object):
        queen_tuple_1 = queen_tuple_1_object.queens
        queen_tuple_2 = queen_tuple_2_object.queens

        first_child = QueenTuple(queen_tuple_1[:len(queen_tuple_1) // 2] + queen_tuple_2[len(queen_tuple_2) // 2:])
        second_child = QueenTuple(queen_tuple_2[:len(queen_tuple_2) // 2] + queen_tuple_1[len(queen_tuple_1) // 2:])

        print("De los padres")
        print(str(queen_tuple_1))
        print(str(queen_tuple_2))

        print("\nSalen")
        print(str(first_child))
        print(str(second_child))

        self.aux_population.append(first_child)
        self.aux_population.append(second_child)
