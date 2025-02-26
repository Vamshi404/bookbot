# stats.py

def get_num_text(file_path):
    with open(file_path, 'r') as f:
        count = 0
        file_contents = f.read()
        # Split by any whitespace (spaces, newlines, tabs)
        words = file_contents.split()  # Automatically handles multiple spaces and newlines
        count = len(words)  # Get the number of words by getting the length of the list
    return count

def get_each_char(file_path):
    with open(file_path, 'r') as f:
        all_char = {}
        file_contents = f.read()
        lowercase = file_contents.lower()
        
        for char in lowercase:
            # Check if the character is alphanumeric (letters and digits)
            if char.isalnum():
                if char in all_char:
                    all_char[char] += 1
                else:
                    all_char[char] = 1
    return all_char

# Function to sort the dictionary of character counts
def sort_char_counts(char_count_dict):
    # Sort the dictionary by the count (value), in descending order
    sorted_counts = sorted(char_count_dict.items(), key=lambda x: x[1], reverse=True)
    
    # Convert the sorted list of tuples back to a list of dictionaries or strings
    sorted_dict_list = [f"{char}: {count}" for char, count in sorted_counts]
    
    return sorted_dict_list
