def find_x_mas_patterns(text):
    # Convert the single string input into a 2D grid
    lines = text.strip().splitlines()
    grid = [list(line.strip()) for line in lines]
    rows, cols = len(grid), len(grid[0])
    pattern_count = 0

    def is_valid_position(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def check_x_mas(center_x, center_y):
        # Ensure the center is 'A'
        if grid[center_x][center_y] != 'A':
            return 0

        # Check the diagonals for two "MAS" patterns
        diagonals = [
            [(-1, -1), (1, 1)],  # Top-left to bottom-right
            [(-1, 1), (1, -1)]   # Top-right to bottom-left
        ]
        count = 0

        for diagonal in diagonals:
            chars = []
            for dx, dy in diagonal:
                nx, ny = center_x + dx, center_y + dy
                if is_valid_position(nx, ny):
                    chars.append(grid[nx][ny])
                else:
                    chars.append(None)
            
            # Check if the diagonal forms "MAS" (in any order)
            if chars[0] and chars[1] and set(chars) == {'M', 'S'}:
                count += 1

        return 1 if count == 2 else 0  # Both diagonals must match

    # Iterate over every cell in the grid
    for r in range(rows):
        for c in range(cols):
            pattern_count += check_x_mas(r, c)

    return pattern_count


# Read the input text file
with open("words.txt", "r") as file:
    text = file.read()

result = find_x_mas_patterns(text)
print(f"Total X-MAS patterns found: {result}")
