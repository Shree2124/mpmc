
import math


# K-Means Clustering
class KMeans:

    # Calculate Euclidean distance
    def distance(self, point1, point2):
        total = 0

        for i in range(len(point1)):
            total += (point1[i] - point2[i]) ** 2

        return math.sqrt(total)

    # Train the K-Means model
    def train(self, data, k, max_iterations=100):

        # Initialize the first K data points as centroids
        centroids = [data[i][:] for i in range(k)]
        clusters = [0] * len(data)

        print("\nTraining Started...\n")

        for iteration in range(1, max_iterations + 1):

            # Assign each point to its nearest centroid
            for i in range(len(data)):
                distances = []

                for centroid in centroids:
                    distances.append(
                        self.distance(data[i], centroid)
                    )

                clusters[i] = distances.index(min(distances))

            # Calculate new centroids
            new_centroids = []

            for cluster in range(k):
                cluster_points = []

                for i in range(len(data)):
                    if clusters[i] == cluster:
                        cluster_points.append(data[i])

                # Keep the old centroid if the cluster is empty
                if len(cluster_points) == 0:
                    new_centroids.append(centroids[cluster])
                    continue

                dimensions = len(data[0])
                new_centroid = []

                for j in range(dimensions):
                    total = 0

                    for point in cluster_points:
                        total += point[j]

                    new_centroid.append(
                        total / len(cluster_points)
                    )

                new_centroids.append(new_centroid)

            print(
                f"Iteration {iteration} - "
                f"Centroids: {new_centroids}"
            )

            # Stop if centroids have not changed
            if new_centroids == centroids:
                print("\nClustering Completed Successfully.")
                centroids = new_centroids
                break

            centroids = new_centroids

        # Reassign points using the final centroids
        for i in range(len(data)):
            distances = [
                self.distance(data[i], centroid)
                for centroid in centroids
            ]
            clusters[i] = distances.index(min(distances))

        return clusters, centroids


# Main program
if __name__ == "__main__":

    # Input data points
    data = [
        [1, 2],
        [2, 1],
        [3, 2],
        [8, 9],
        [9, 8],
        [8, 8]
    ]

    # Number of clusters
    k = 2

    # Create K-Means model
    kmeans = KMeans()

    # Train the model
    clusters, centroids = kmeans.train(data, k)

    # Display final centroids
    print("\nFinal Centroids:")

    for i in range(k):
        print(f"Cluster {i + 1}: {centroids[i]}")

    # Display cluster assignments
    print("\nCluster Assignments:")

    for i in range(len(data)):
        print(
            f"Point {i + 1}: {data[i]} "
            f"-> Cluster {clusters[i] + 1}"
        )
