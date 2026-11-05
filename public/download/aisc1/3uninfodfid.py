
# Goal node
GOAL = 'H'

# Graph representation
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['H'],
    'F': [],
    'G': [],
    'H': []
}


# Depth-Limited Search (DLS)
def depth_limited_search(node, goal, depth, path):
    path.append(node)

    # Check if the goal is reached
    if node == goal:
        return True

    # Stop searching when depth limit is reached
    if depth == 0:
        path.pop()
        return False

    # Explore neighboring nodes
    for neighbor in graph[node]:
        if depth_limited_search(
            neighbor, goal, depth - 1, path
        ):
            return True

    # Remove node if the goal is not found in this branch
    path.pop()
    return False


# Depth First Iterative Deepening (DFID)
def dfid(start, goal, max_depth):
    for depth in range(max_depth + 1):
        path = []

        print(f"Searching with depth limit: {depth}")

        if depth_limited_search(start, goal, depth, path):
            return path, depth

    return None, -1


# Main program
def main():
    start = 'A'

    print("DEPTH FIRST ITERATIVE DEEPENING (DFID)")
    print("Starting Node:", start)
    print("Goal Node:", GOAL)
    print()

    path, depth = dfid(start, GOAL, 5)

    if path:
        print("\nGoal Node Found:", GOAL)
        print("Depth:", depth)
        print("Path:", " -> ".join(path))
    else:
        print("\nGoal Node Not Found")


if __name__ == "__main__":
    main()
