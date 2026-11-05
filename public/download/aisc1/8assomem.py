
import numpy as np


class AssociativeMemory:

    def train(self, patterns):
        size = len(patterns[0])

        # Initialize the weight matrix
        weights = np.zeros((size, size))

        # Store each pattern using Hebbian learning
        for pattern in patterns:
            weights += np.outer(pattern, pattern)

        # Remove self-connections
        np.fill_diagonal(weights, 0)

        return weights

    def recall(self, pattern, weights):
        # Calculate weighted sum
        total = np.dot(pattern, weights)

        # Apply sign activation function
        output = np.where(total >= 0, 1, -1)

        return output


# Main program

# Define training patterns
patterns = np.array([
    [1, 1, 1, -1, -1, -1],
    [1, -1, 1, -1, 1, -1]
])

# Create the associative memory model
memory = AssociativeMemory()

# Train the network
weights = memory.train(patterns)

# Display the weight matrix
print("\nWeight Matrix:")
print(weights)

# Define the test pattern
test_pattern = np.array([1, 1, -1, -1, -1, -1])

# Recall the stored pattern
recalled_pattern = memory.recall(test_pattern, weights)

# Display results
print("\nTest Pattern:")
print(test_pattern)

print("\nRecalled Pattern:")
print(recalled_pattern)

# Compare with stored patterns
print("\nAssociative Memory Result:")

if np.array_equal(recalled_pattern, patterns[0]):
    print("Pattern 1 Recalled Successfully.")
elif np.array_equal(recalled_pattern, patterns[1]):
    print("Pattern 2 Recalled Successfully.")
else:
    print("Pattern Could Not Be Recalled Exactly.")
