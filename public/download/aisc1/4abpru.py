
# Infinity values for MAX and MIN players
MAX = float('inf')
MIN = float('-inf')

# Game tree with leaf node values
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': 3,
    'E': 5,
    'F': 6,
    'G': 9
}


# Alpha-Beta Pruning Algorithm
def alpha_beta(node, depth, alpha, beta, maximizing_player):

    # Base case: leaf node or depth limit reached
    if depth == 0 or not isinstance(tree[node], list):
        return tree[node]

    if maximizing_player:
        max_eval = MIN

        for child in tree[node]:
            evaluation = alpha_beta(
                child, depth - 1, alpha, beta, False
            )

            max_eval = max(max_eval, evaluation)
            alpha = max(alpha, max_eval)

            # Prune remaining branches
            if alpha >= beta:
                print("Pruning at node:", node)
                break

        return max_eval

    else:
        min_eval = MAX

        for child in tree[node]:
            evaluation = alpha_beta(
                child, depth - 1, alpha, beta, True
            )

            min_eval = min(min_eval, evaluation)
            beta = min(beta, min_eval)

            # Prune remaining branches
            if beta <= alpha:
                print("Pruning at node:", node)
                break

        return min_eval


# Main program
def main():
    root = 'A'
    depth = 2

    print("ALPHA-BETA PRUNING")
    print("Root Node:", root)
    print("Search Depth:", depth)

    best_value = alpha_beta(
        root, depth, MIN, MAX, True
    )

    print("Optimal Value:", best_value)


if __name__ == "__main__":
    main()
