def generate_spiral(n, clockwise=True):
    matrix = [[0] * n for _ in range(n)]
    num = 1
    layers = (n + 1) // 2

    for layer in range(layers):
        if clockwise:
            # Top row
            for i in range(layer, n - layer):
                matrix[layer][i] = num
                num += 1
            # Right column
            for i in range(layer + 1, n - layer):
                matrix[i][n - layer - 1] = num
                num += 1
            # Bottom row
            for i in range(n - layer - 2, layer - 1, -1):
                matrix[n - layer - 1][i] = num
                num += 1
            # Left column
            for i in range(n - layer - 2, layer, -1):
                matrix[i][layer] = num
                num += 1
        else:
            # Left column
            for i in range(layer, n - layer):
                matrix[i][layer] = num
                num += 1
            # Bottom row
            for i in range(layer + 1, n - layer):
                matrix[n - layer - 1][i] = num
                num += 1
            # Right column
            for i in range(n - layer - 2, layer - 1, -1):
                matrix[i][n - layer - 1] = num
                num += 1
            # Top row
            for i in range(n - layer - 2, layer, -1):
                matrix[layer][i] = num
                num += 1

    # Format output
    width = len(str(n * n))
    for row in matrix:
        print(" ".join(f"{val:>{width}}" for val in row))


n = int(input("Enter matrix size (n ≥ 2): "))
direction = input("Clockwise spiral? (yes/no): ").strip().lower()
generate_spiral(n, clockwise=(direction == "yes"))
