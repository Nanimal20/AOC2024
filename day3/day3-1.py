import re

def extract_and_sum_mul_operations(file_path):
    # Regular expression to match valid mul(X,Y) instructions
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    
    total = 0
    try:
        # Open and read the file
        with open(file_path, 'r') as file:
            for line in file:
                # Find all matches in the current line
                matches = re.findall(pattern, line)
                # Compute the sum of all valid multiplications in this line
                total += sum(int(x) * int(y) for x, y in matches)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

    return total

# File path to the input data
file_path = 'day3-1.txt'

# Calculate the result
result = extract_and_sum_mul_operations(file_path)

# Output the result if computation was successful
if result is not None:
    print(f"The sum of all valid multiplications is: {result}")
