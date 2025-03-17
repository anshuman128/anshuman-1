# Selection process
def selection(populasi):
    pop = dict(populasi)  # Create a copy of the population dictionary
    parent = {}
    for i in range(2):
        gen = max(pop, key=pop.get)  # Select the gene with the highest fitness
        genfitness = pop[gen]
        parent[gen] = genfitness
        if i == 0:
            del pop[gen]  # Remove the selected gene for the first iteration to avoid duplicate selection
    return parent

# Example usage
if __name__ == "__main__":
    # Example population
    population = {
        'abc': 50,
        'def': 70,
        'ghi': 65,
        'jkl': 80
    }

    # Perform selection
    parents = selection(population)

    print("Selected Parents:")
    for gen, fitness in parents.items():
        print(f"Gene: {gen}, Fitness: {fitness:.2f}%")