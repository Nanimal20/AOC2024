def find_xmas_in_file(filename, word="XMAS"):
    # Read the grid from the file
    with open(filename, "r") as file:
        grid = [line.strip() for line in file]

    rows, cols = len(grid), len(grid[0])
    directions = [
        (0, 1),  # Horizontal (right)
        (0, -1),  # Horizontal (left)
        (1, 0),  # Vertical (down)
        (-1, 0),  # Vertical (up)
        (1, 1),  # Diagonal (down-right)
        (-1, -1),  # Diagonal (up-left)
        (1, -1),  # Diagonal (down-left)
        (-1, 1)   # Diagonal (up-right)
    ]

    def in_bounds(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def search(x, y, dx, dy):
        for i in range(len(word)):
            nx, ny = x + i * dx, y + i * dy
            if not in_bounds(nx, ny) or grid[nx][ny] != word[i]:
                return False
        return True

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == word[0]:  # Start from matching first letter
                for dx, dy in directions:
                    if search(r, c, dx, dy):
                        count += 1
    return count

# Example usage
filename = "words.txt"
result = find_xmas_in_file(filename)
print(f"Total occurrences of 'XMAS': {result}")
