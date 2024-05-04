def count_substring(original_string, substring):
    return original_string.count(substring)

# Read input
original_string = input().strip()
substring = input().strip()

# Calculate the count
result = count_substring(original_string, substring)

# Print the result
print(result)


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)