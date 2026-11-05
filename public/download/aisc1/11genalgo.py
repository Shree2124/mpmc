
import random


class GeneticAlgorithm:

    def __init__(
        self,
        population_size=10,
        chromosome_length=8,
        generations=20,
        mutation_rate=0.1
    ):
        self.population_size = population_size
        self.chromosome_length = chromosome_length
        self.generations = generations
        self.mutation_rate = mutation_rate

    def create_chromosome(self):
        return [
            random.randint(0, 1)
            for _ in range(self.chromosome_length)
        ]

    def create_population(self):
        return [
            self.create_chromosome()
            for _ in range(self.population_size)
        ]

    def fitness(self, chromosome):
        return sum(chromosome)

    def selection(self, population):
        population.sort(
            key=self.fitness,
            reverse=True
        )

        return population[:self.population_size // 2]

    def crossover(self, parent1, parent2):
        point = random.randint(
            1,
            self.chromosome_length - 1
        )

        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]

        return child1, child2

    def mutation(self, chromosome):
        for i in range(self.chromosome_length):
            if random.random() < self.mutation_rate:
                chromosome[i] = 1 - chromosome[i]

        return chromosome

    def run(self):
        population = self.create_population()

        for generation in range(self.generations):

            selected = self.selection(population)

            new_population = selected.copy()

            while len(new_population) < self.population_size:
                parent1, parent2 = random.sample(selected, 2)

                child1, child2 = self.crossover(
                    parent1,
                    parent2
                )

                child1 = self.mutation(child1)
                child2 = self.mutation(child2)

                new_population.append(child1)

                if len(new_population) < self.population_size:
                    new_population.append(child2)

            population = new_population

            best = max(population, key=self.fitness)

            print(
                f"Generation {generation + 1}: "
                f"{best} | Fitness = {self.fitness(best)}"
            )

        best = max(population, key=self.fitness)

        return best, self.fitness(best)


# Main program

ga = GeneticAlgorithm(
    population_size=10,
    chromosome_length=8,
    generations=20,
    mutation_rate=0.1
)

best_solution, best_fitness = ga.run()

print("\nFinal Result:")
print("Best Chromosome:", best_solution)
print("Best Fitness:", best_fitness)
