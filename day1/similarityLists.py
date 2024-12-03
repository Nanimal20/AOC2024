from collections import Counter

def read_lists_from_file(filename):
    left_list = []
    right_list = []
    
    with open(filename, 'r') as file:
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
    
    return left_list, right_list

def calculate_similarity_score(left_list, right_list):
    # Count occurrences of each number in the right list
    right_count = Counter(right_list)
    
    # Calculate similarity score
    similarity_score = sum(num * right_count[num] for num in left_list)
    
    return similarity_score

# Read lists from file
filename = 'lists.txt'
left_list, right_list = read_lists_from_file(filename)

# Calculate similarity score
similarity_score = calculate_similarity_score(left_list, right_list)
print("Total Similarity Score:", similarity_score)
