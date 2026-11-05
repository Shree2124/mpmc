
class FuzzyFanController:

    def triangular(self, x, a, b, c):
        if x <= a or x >= c:
            return 0.0
        elif x == b:
            return 1.0
        elif x < b:
            return (x - a) / (b - a)
        else:
            return (c - x) / (c - b)

    def control(self, temperature):

        # Calculate temperature membership values
        low = self.triangular(temperature, 0, 10, 20)
        medium = self.triangular(temperature, 15, 25, 35)
        high = self.triangular(temperature, 30, 40, 50)

        # Fan speed representative values
        low_speed = 30
        medium_speed = 60
        high_speed = 100

        # Apply fuzzy rules
        rule1 = low
        rule2 = medium
        rule3 = high

        # Weighted average defuzzification
        total_membership = rule1 + rule2 + rule3

        if total_membership == 0:
            fan_speed = 0
        else:
            fan_speed = (
                rule1 * low_speed
                + rule2 * medium_speed
                + rule3 * high_speed
            ) / total_membership

        return low, medium, high, fan_speed


# Main program

fuzzy = FuzzyFanController()

temperature = float(input("Enter room temperature (°C): "))

low, medium, high, fan_speed = fuzzy.control(temperature)

print("\nFuzzy Control System Output:\n")

print(f"Temperature: {temperature:.2f} °C")
print(f"Low Membership: {low:.4f}")
print(f"Medium Membership: {medium:.4f}")
print(f"High Membership: {high:.4f}")
print(f"Calculated Fan Speed: {fan_speed:.2f}%")
