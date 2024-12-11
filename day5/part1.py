def parse_input(file_path):
    """Reads and parses the input file into a list of ordering rules and a list of updates."""
    with open(file_path, 'r') as file:
        rules_section, updates_section = file.read().strip().split("\n\n")
        
        # Parse ordering rules as pairs of (X, Y)
        rules = [tuple(map(int, line.split("|"))) for line in rules_section.splitlines()]
        
        # Parse updates as lists of page numbers
        updates = [list(map(int, line.split(","))) for line in updates_section.splitlines()]
        
    return rules, updates


def is_update_valid(update, rules):
    """Checks if an update follows the ordering rules."""
    page_positions = {page: i for i, page in enumerate(update)}  # Position of each page in the update
    for x, y in rules:
        if x in page_positions and y in page_positions:
            if page_positions[x] >= page_positions[y]:  # X must appear before Y
                return False  # Rule is broken
    return True


def get_middle_page(update):
    """Returns the middle page of the update."""
    n = len(update)
    middle_index = n // 2  # Integer division (0-indexed, so floor)
    return update[middle_index]


def process_updates(file_path):
    """Processes the input file and calculates the sum of the middle pages of the valid updates."""
    rules, updates = parse_input(file_path)
    total_middle_sum = 0
    
    for update in updates:
        if is_update_valid(update, rules):
            middle_page = get_middle_page(update)
            total_middle_sum += middle_page
    
    return total_middle_sum


if __name__ == "__main__":
    file_path = "input.txt"  # Input file path
    result = process_updates(file_path)
    print(f"Total sum of middle pages of correctly-ordered updates: {result}")