import random


# Define the objective function
def objective_function(x, y):
    return x*2 + y*2  # Example objective function: minimize x^2 + y^2

# Define the parameters
num_employed_bees = 10
num_onlooker_bees = 10
num_iterations = 10
lower_bound = -10
upper_bound = 10
limit = 10  # Maximum number of trials for a bee
num_best_sites = 3

# Generate random initial solutions
solutions = []
for _ in range(num_employed_bees + num_onlooker_bees):
    x = random.uniform(lower_bound, upper_bound)
    y = random.uniform(lower_bound, upper_bound)
    fitness = objective_function(x, y)
    solutions.append((x, y, fitness))

# Define the Artificial Bee Colony algorithm
def artificial_bee_colony():
    best_solution = min(solutions, key=lambda x: x[2])
    for iteration in range(num_iterations):
        # Employed bee phase
        for i in range(num_employed_bees):
            solution = solutions[i]
            new_solution = explore_neighborhood(solution)
            if new_solution[2] < solution[2]:
                solutions[i] = new_solution
            else:
                solutions[i] = solution

        # Onlooker bee phase
        probabilities = calculate_probabilities()
        for i in range(num_onlooker_bees):
            selected_index = select_bee(probabilities)
            solution = solutions[selected_index]
            new_solution = explore_neighborhood(solution)
            if new_solution[2] < solution[2]:
                solutions[selected_index] = new_solution

        # Scout bee phase
        best_solution = min(solutions, key=lambda x: x[2])
        if best_solution[2] > limit:
            best_solution = generate_random_solution()
            solutions.append(best_solution)

        # Print the best solution in each iteration
        print("Iteration:", iteration + 1)
        print("Best solution: (x = {}, y = {})".format(best_solution[0], best_solution[1]))
        print("Best fitness:", best_solution[2])
        print()

    return best_solution

# Explore the neighborhood of a solution by adding random perturbation
def explore_neighborhood(solution):
    x = solution[0] + random.uniform(-1, 1)
    y = solution[1] + random.uniform(-1, 1)
    x = max(min(x, upper_bound), lower_bound)
    y = max(min(y, upper_bound), lower_bound)
    fitness = objective_function(x, y)
    return (x, y, fitness)

# Calculate the probabilities for the onlooker bee phase
def calculate_probabilities():
    total_fitness = sum(solution[2] for solution in solutions)
    probabilities = [solution[2] / total_fitness for solution in solutions]
    return probabilities

# Select a bee based on probabilities
def select_bee(probabilities):
    r = random.uniform(0, 1)
    cumulative_probability = 0
    for i, probability in enumerate(probabilities):
        cumulative_probability += probability
        if r <= cumulative_probability:
            return i
    return len(probabilities) - 1

# Generate a random solution
def generate_random_solution():
    x = random.uniform(lower_bound, upper_bound)
    y = random.uniform(lower_bound, upper_bound)
    fitness = objective_function(x, y)
    return (x, y, fitness)

# Run the Artificial Bee Colony algorithm
best_solution = artificial_bee_colony()

# Print the best solution and its fitness
print("Final Best solution: (x = {}, y = {})".format(best_solution[0], best_solution[1]))
print("Final Best fitness:", best_solution[2])