from collections import defaultdict

# Directions: up, right, down, left (row_offset, col_offset)
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up, Right, Down, Left
DIRECTION_CHARS = ['^', '>', 'v', '<']

def read_input_from_file(filename='input.txt'):
    """Reads the grid from an input file."""
    with open(filename, 'r') as file:
        grid = [line.strip() for line in file.readlines()]
    return grid

def parse_input(grid):
    """Parses the grid and returns the initial position, direction, and set of obstacles."""
    obstacles = set()
    start_pos = None
    start_dir = None
    
    for r, line in enumerate(grid):
        for c, char in enumerate(line):
            if char == '#':
                obstacles.add((r, c))
            elif char in DIRECTION_CHARS:
                start_pos = (r, c)
                start_dir = DIRECTION_CHARS.index(char)
    
    return obstacles, start_pos, start_dir

def simulate_guard(obstacles, start_pos, start_dir, new_obstruction=None):
    """Simulate the guard's path with an optional new obstruction."""
    if new_obstruction:
        obstacles.add(new_obstruction)
    
    r, c = start_pos
    direction = start_dir
    visited = set()
    start_state = (r, c, direction)
    
    while True:
        state = (r, c, direction)
        
        # Check if the guard has returned to the starting position with the same direction
        if state != start_state and state in visited:
            break  # If this state is visited again, loop detected
        
        # If we've returned to the original state, count this as a "valid loop"
        if state == start_state and len(visited) > 0:
            if new_obstruction:
                obstacles.remove(new_obstruction)
            return True  # We found a loop
        
        visited.add(state)
        
        # Calculate next position in front of the guard
        dr, dc = DIRECTIONS[direction]
        front_pos = (r + dr, c + dc)
        
        # Check if the front position is valid to move into
        if front_pos in obstacles or not (0 <= front_pos[0] < len(grid) and 0 <= front_pos[1] < len(grid[0])):
            # Turn right (clockwise)
            direction = (direction + 1) % 4
        else:
            # Move forward
            r, c = front_pos
    
    if new_obstruction:
        obstacles.remove(new_obstruction)
        
    return False

def count_obstruction_positions_for_loops(grid):
    """Part 2: Find how many positions where placing an obstruction causes a loop."""
    obstacles, start_pos, start_dir = parse_input(grid)
    start_state = (start_pos[0], start_pos[1], start_dir)
    total_positions = set((r, c) for r in range(len(grid)) for c in range(len(grid[0])))
    valid_positions = set()
    
    for pos in total_positions:
        if pos in obstacles or pos == start_pos:
            continue  # Ignore existing obstacles or start position
        
        # Simulate guard movement with obstruction at position `pos`
        causes_loop = simulate_guard(obstacles, start_pos, start_dir, new_obstruction=pos)
        
        if causes_loop:
            valid_positions.add(pos)
    
    return len(valid_positions)

# Main Execution
if __name__ == "__main__":
    grid = read_input_from_file('input.txt')

    # Part 2
    obstruction_positions = count_obstruction_positions_for_loops(grid)
    print(f"Number of obstruction positions causing a loop: {obstruction_positions}")

