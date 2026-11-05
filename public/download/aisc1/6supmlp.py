
import numpy as np


# Multi-Layer Perceptron (MLP)
class MLP:

    def __init__(self, input_size, hidden_size, output_size):
        np.random.seed(42)

        # Initialize weights and biases
        self.weights1 = np.random.randn(input_size, hidden_size) * 0.5
        self.bias1 = np.zeros((1, hidden_size))

        self.weights2 = np.random.randn(hidden_size, output_size) * 0.5
        self.bias2 = np.zeros((1, output_size))

    # Sigmoid activation function
    def sigmoid(self, x):
        x = np.clip(x, -500, 500)
        return 1 / (1 + np.exp(-x))

    # Train the neural network
    def train(self, X, y, epochs=10000, learning_rate=0.5):

        for epoch in range(epochs):

            # Forward propagation
            hidden_input = np.dot(X, self.weights1) + self.bias1
            hidden_output = self.sigmoid(hidden_input)

            final_input = np.dot(hidden_output, self.weights2) + self.bias2
            predicted_output = self.sigmoid(final_input)

            # Calculate error
            error = predicted_output - y

            # Backpropagation
            output_delta = error * (
                predicted_output * (1 - predicted_output)
            )

            hidden_delta = np.dot(
                output_delta, self.weights2.T
            ) * (hidden_output * (1 - hidden_output))

            # Update weights and biases
            self.weights2 -= learning_rate * np.dot(
                hidden_output.T, output_delta
            ) / len(X)

            self.bias2 -= learning_rate * np.mean(
                output_delta, axis=0, keepdims=True
            )

            self.weights1 -= learning_rate * np.dot(
                X.T, hidden_delta
            ) / len(X)

            self.bias1 -= learning_rate * np.mean(
                hidden_delta, axis=0, keepdims=True
            )

            # Display training loss
            if (epoch + 1) % 2000 == 0:
                loss = np.mean(error ** 2)
                print(f"Epoch {epoch + 1}, Loss: {loss:.6f}")

    # Predict the output
    def predict(self, X):
        hidden_output = self.sigmoid(
            np.dot(X, self.weights1) + self.bias1
        )

        predicted_output = self.sigmoid(
            np.dot(hidden_output, self.weights2) + self.bias2
        )

        return (predicted_output >= 0.5).astype(int)


# Main program
if __name__ == "__main__":

    # Input data for XOR
    X = np.array([
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ], dtype=float)

    # Expected output
    y = np.array([
        [0],
        [1],
        [1],
        [0]
    ], dtype=float)

    # Create MLP model
    mlp = MLP(
        input_size=2,
        hidden_size=4,
        output_size=1
    )

    # Train the model
    print("Training Started...\n")

    mlp.train(
        X, y,
        epochs=10000,
        learning_rate=0.5
    )

    # Make predictions
    predictions = mlp.predict(X)

    # Display actual and predicted outputs
    print("\nActual Output vs Predicted Output:")

    for i in range(len(X)):
        print(
            f"Input: {X[i].astype(int)}, "
            f"Actual: {int(y[i][0])}, "
            f"Predicted: {predictions[i][0]}"
        )

    # Calculate accuracy
    accuracy = np.mean(predictions == y) * 100

    print(f"\nTraining Accuracy: {accuracy:.2f}%")
