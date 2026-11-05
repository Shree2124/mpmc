
import heapq

# Goal state of the 15-puzzle
GOAL = (
    (1, 2, 3, 4),
    (5, 6, 7, 8),
    (9, 10, 11, 12),
    (13, 14, 15, 0)
)


# Calculate Manhattan Distance
def heuristic(state):
    distance = 0

    for i in range(4):
        for j in range(4):
            value = state[i][j]

            if value != 0:
                goal_x = (value - 1) // 4
                goal_y = (value - 1) % 4

                distance += abs(i - goal_x) + abs(j - goal_y)

    return distance


# Find the position of the blank tile (0)
def find_blank(state):
    for i in range(4):
        for j in range(4):
            if state[i][j] == 0:
                return i, j


# Generate all valid neighboring states
def get_successors(state):
    x, y = find_blank(state)

    directions = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]

    successors = []

    for dx, dy in directions:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < 4 and 0 <= ny < 4:
            board = [list(row) for row in state]

            # Move the adjacent tile into the blank space
            board[x][y], board[nx][ny] = (
                board[nx][ny],
                board[x][y]
            )

            new_state = tuple(tuple(row) for row in board)
            successors.append(new_state)

    return successors


# Check whether the puzzle is solved
def is_goal_state(state):
    return state == GOAL


# Check whether a 15-puzzle configuration is solvable
def is_solvable(state):
    tiles = [
        value
        for row in state
        for value in row
        if value != 0
    ]

    inversions = 0

    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            if tiles[i] > tiles[j]:
                inversions += 1

    # Row number counted from the bottom (starting at 1)
    blank_row_from_bottom = 4 - find_blank(state)[0]

    # For a 4x4 puzzle, inversions + blank row must be odd
    return (inversions + blank_row_from_bottom) % 2 == 1


# A* Search Algorithm
def a_star(start):
    # Priority queue entries: (f_cost, g_cost, state)
    priority_queue = []

    g_cost = {start: 0}
    parent = {}

    heapq.heappush(
        priority_queue,
        (heuristic(start), 0, start)
    )

    while priority_queue:
        f, g, current = heapq.heappop(priority_queue)

        # Skip outdated queue entries
        if g != g_cost.get(current):
            continue

        # Goal reached: reconstruct the path
        if is_goal_state(current):
            path = []

            while current != start:
                path.append(current)
                current = parent[current]

            path.append(start)
            path.reverse()

            return path

        # Explore all valid next states
        for next_state in get_successors(current):
            new_g = g + 1

            if new_g < g_cost.get(next_state, float("inf")):
                g_cost[next_state] = new_g
                parent[next_state] = current

                h = heuristic(next_state)
                f = new_g + h

                heapq.heappush(
                    priority_queue,
                    (f, new_g, next_state)
                )

    return None


# Display a puzzle board
def print_board(state):
    for row in state:
        print(" ".join(
            "_" if value == 0 else f"{value:2}"
            for value in row
        ))
    print()


# Main program
def main():
    print("15-PUZZLE SOLVER USING A* SEARCH")
    print("Enter 16 numbers from 0 to 15.")
    print("Use 0 to represent the blank space.\n")

    try:
        numbers = list(map(
            int,
            input("Enter the puzzle row-wise: ").split()
        ))

        if len(numbers) != 16 or set(numbers) != set(range(16)):
            print("Invalid input! Enter each number from 0 to 15 once.")
            return

        start = tuple(
            tuple(numbers[i:i + 4])
            for i in range(0, 16, 4)
        )

        print("\nInitial State:")
        print_board(start)

        if not is_solvable(start):
            print("This puzzle configuration is not solvable.")
            return

        print("Solving the puzzle using A* Search...")
        solution = a_star(start)

        if solution is None:
            print("No solution found.")
            return

        print("\nSolution Path:")

        for step, state in enumerate(solution):
            print(f"Step {step}:")
            print_board(state)

        print("Total moves:", len(solution) - 1)
        print("Total states in path:", len(solution))
        print("Puzzle solved successfully!")

    except ValueError:
        print("Invalid input! Enter 16 integers from 0 to 15.")


if __name__ == "__main__":
    main()