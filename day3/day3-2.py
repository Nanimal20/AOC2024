import re

def extract_and_sum_mul_operations(file_path):
    """
    Extracts valid mul(X,Y) instructions from the corrupted memory file,
    considering do() and don't() instructions that enable or disable mul operations.
    Returns the sum of all enabled multiplications.
    """
    # Regular expression to match do(), don't(), and mul(X,Y) instructions
    pattern = re.compile(
        r"(?P<do>do\(\))|(?P<dont>don't\(\))|mul\((?P<x>\d{1,3}),(?P<y>\d{1,3})\)"
    )
    
    total = 0
    mul_enabled = True  # Mul instructions are enabled at the start

    try:
        # Open and read the file content
        with open(file_path, 'r') as file:
            content = file.read()
        
        # Find all matches in the content in the order they appear
        for match in pattern.finditer(content):
            if match.group('do'):
                mul_enabled = True
                # Debug statement
                # print(f"do() found at position {match.start()}: mul_enabled set to True")
            elif match.group('dont'):
                mul_enabled = False
                # Debug statement
                # print(f"don't() found at position {match.start()}: mul_enabled set to False")
            elif match.group('x') and match.group('y'):
                if mul_enabled:
                    x = int(match.group('x'))
                    y = int(match.group('y'))
                    product = x * y
                    total += product
                    # Debug statement
                    # print(f"mul({x},{y}) found at position {match.start()}: {x} * {y} = {product}, total = {total}")
                else:
                    # Debug statement
                    # print(f"mul({match.group('x')},{match.group('y')}) found at position {match.start()} but mul is disabled.")
                    pass  # Mul is disabled; ignore this instruction
        return total

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

# File path to the input data
file_path = 'day3-1.txt'

# Calculate the result
result = extract_and_sum_mul_operations(file_path)

# Output the result if computation was successful
if result is not None:
    print(f"The sum of all valid multiplications is: {result}")
