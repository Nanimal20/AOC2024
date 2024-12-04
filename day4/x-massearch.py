def find_x_mas_in_file(filename, word="MAS"):
    # Read the grid from the file
    with open(filename, "r") as file:
        grid = [line.strip() for line in file]

    rows, cols = len(grid), len(grid[0])
    word_len = len(word)

    def in_bounds(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def check_x_mas(center_x, center_y):
        # Check vertical "MAS" centered at (center_x, center_y)
        vertical = []
        for i in range(-(word_len // 2), word_len // 2 + 1):
            nx = center_x + i
            if in_bounds(nx, center_y):
                vertical.append(grid[nx][center_y])
            else:
                return False
        vertical = "".join(vertical)
        
        # Check both diagonal directions
        diagonal1, diagonal2 = [], []
        for i in range(-(word_len // 2), word_len // 2 + 1):
            nx1, ny1 = center_x + i, center_y + i
            nx2, ny2 = center_x + i, center_y - i
            if in_bounds(nx1, ny1):
                diagonal1.append(grid[nx1][ny1])
            if in_bounds(nx2, ny2):
                diagonal2.append(grid[nx2][ny2])
        diagonal1 = "".join(diagonal1)
        diagonal2 = "".join(diagonal2)

        # Check if we have a valid X-MAS pattern
        reversed_word = word[::-1]
        return (
            (vertical == word and diagonal1 == word) or
            (vertical == word and diagonal1 == reversed_word) or
            (vertical == reversed_word and diagonal1 == word) or
            (vertical == reversed_word and diagonal1 == reversed_word) or
            (vertical == word and diagonal2 == word) or
            (vertical == word and diagonal2 == reversed_word) or
            (vertical == reversed_word and diagonal2 == word) or
            (vertical == reversed_word and diagonal2 == reversed_word)
        )

    count = 0
    for r in range(rows):
        for c in range(cols):
            if check_x_mas(r, c):
                count += 1
    return count

# Example usage
filename = "words.txt"
result = find_x_mas_in_file(filename)
print(f"Total X-MAS patterns found: {result}")
