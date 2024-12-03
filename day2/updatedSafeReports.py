def is_safe(report):
    # Check if the levels are strictly increasing or strictly decreasing
    increasing = all(report[i] < report[i+1] for i in range(len(report)-1))
    decreasing = all(report[i] > report[i+1] for i in range(len(report)-1))
    
    if not (increasing or decreasing):
        return False

    # Check if all adjacent differences are between 1 and 3
    valid_differences = all(1 <= abs(report[i] - report[i+1]) <= 3 for i in range(len(report)-1))
    
    return valid_differences

def is_safe_with_removal(report):
    if is_safe(report):
        return True
    
    # Try removing each level and check if the report becomes safe
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe(modified_report):
            return True

    return False

def count_safe_reports_with_removal(filename):
    safe_count = 0
    
    with open(filename, 'r') as file:
        for line in file:
            report = list(map(int, line.split()))
            if is_safe_with_removal(report):
                safe_count += 1
    
    return safe_count

# Replace 'reports.txt' with the actual path to your file
filename = 'levels.txt'
safe_reports_count = count_safe_reports_with_removal(filename)

print(f"Number of Safe Reports (with removal rule): {safe_reports_count}")
