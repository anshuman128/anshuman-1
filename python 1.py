import numpy as np

# Generate new gene
def create_gen(panjang_target):
    random_number = np.random.randint(32, 126, size=panjang_target)
    gen = ''.join([chr(i) for i in random_number])
    return gen

# Calculate fitness of gene
def calculate_fitness(gen, target, panjang_target):
    fitness = 0
    for i in range(panjang_target):
        if gen[i] == target[i]:
            fitness += 1
    fitness = (fitness / panjang_target) * 100
    return fitness

# Create population
def create_population(target, max_population, panjang_target):
    populasi = {}
    for i in range(max_population):
        gen = create_gen(panjang_target)
        genfitness = calculate_fitness(gen, target, panjang_target)
        populasi[gen] = genfitness
    return populasi

# Example usage
if __name__ == "__main__":
    target = "hello"
    max_population = 100
    panjang_target = len(target)

    population = create_population(target, max_population, panjang_target)

    # Print the generated population and their fitness
    for gen, fitness in population.items():
        print(f"Gene: {gen}, Fitness: {fitness:.2f}%")