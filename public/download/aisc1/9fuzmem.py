 
import math


class FuzzyMembership:

    def triangular(self, x, a, b, c):
        # Calculate triangular membership
        if x <= a or x >= c:
            return 0.0
        elif x == b:
            return 1.0
        elif x < b:
            return (x - a) / (b - a)
        else:
            return (c - x) / (c - b)

    def trapezoidal(self, x, a, b, c, d):
        # Calculate trapezoidal membership
        if x <= a or x >= d:
            return 0.0
        elif b <= x <= c:
            return 1.0
        elif x < b:
            return (x - a) / (b - a)
        else:
            return (d - x) / (d - c)

    def gaussian(self, x, c, sigma):
        # Calculate Gaussian membership
        return math.exp(
            -((x - c) ** 2) / (2 * sigma ** 2)
        )


# Main program

# Define input values
values = [10, 20, 30, 40, 50]

# Create fuzzy membership model
fuzzy = FuzzyMembership()

# Define membership function parameters
triangular_parameters = (10, 30, 50)
trapezoidal_parameters = (10, 20, 40, 50)
gaussian_parameters = (30, 10)

# Display membership values
print("\nFuzzy Membership Values:\n")

for value in values:

    triangular = fuzzy.triangular(
        value, *triangular_parameters
    )

    trapezoidal = fuzzy.trapezoidal(
        value, *trapezoidal_parameters
    )

    gaussian = fuzzy.gaussian(
        value, *gaussian_parameters
    )

    print(f"Input: {value}")
    print(f"Triangular Membership: {triangular:.4f}")
    print(f"Trapezoidal Membership: {trapezoidal:.4f}")
    print(f"Gaussian Membership: {gaussian:.4f}")
    print()
