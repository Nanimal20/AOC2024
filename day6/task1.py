def simulate_guard_path(map_str):
    # Convert the map string into a 2D grid of characters
    grid = [list(row) for row in map_str.splitlines()]
    
    # Directions represent Up, Right, Down, Left (clockwise)
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # (row_change, col_change)
    direction_index = None
    
    # Find the guard's starting position and set the initial direction
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == '^':
                start_r, start_c = r, c
                direction_index = 0  # Initially facing Up
                grid[r][c] = '.'  # Clear the initial position (change from ^ to empty)
                break
        if direction_index is not None:
            break
    
    visited_positions = set()  # To store distinct positions visited
    current_r, current_c = start_r, start_c

    while True:
        # Mark the current position as visited
        visited_positions.add((current_r, current_c))
        
        # Calculate the next position in the current direction
        next_r = current_r + directions[direction_index][0]
        next_c = current_c + directions[direction_index][1]
        
        # Check if the next position is within bounds and if there is an obstacle
        if 0 <= next_r < len(grid) and 0 <= next_c < len(grid[0]):
            if grid[next_r][next_c] != '#':  # No obstacle, move forward
                current_r, current_c = next_r, next_c
            else:  # Obstacle in the way, turn right
                direction_index = (direction_index + 1) % 4
        else:  # The guard reached the edge of the map (out of bounds)
            break  # Exit the loop if the guard leaves the map
    
    # Return the number of distinct positions visited
    return len(visited_positions)

# Read the map from input.txt
with open('input.txt', 'r') as file:
    map_input = file.read()

# Run the simulation with the map read from the file
distinct_positions = simulate_guard_path(map_input)
print(f"Distinct positions visited: {distinct_positions}")
