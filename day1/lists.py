def read_lists_from_file(filename):
    left_list = []
    right_list = []
    
    with open(filename, 'r') as file:
        for line in file:
            # Split the line by whitespace and append to respective lists
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
    
    return left_list, right_list

def total_distance(left_list, right_list):
    # Step 1: Sort both lists
    sorted_left = sorted(left_list)
    sorted_right = sorted(right_list)
    
    # Step 2: Calculate pairwise differences
    differences = [abs(a - b) for a, b in zip(sorted_left, sorted_right)]
    
    # Step 3: Sum the differences
    return sum(differences)

# Read lists from file
filename = 'lists.txt'
left_list, right_list = read_lists_from_file(filename)

# Calculate total distance
result = total_distance(left_list, right_list)
print("Total Distance:", result)
