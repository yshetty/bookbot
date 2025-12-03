def get_num_words(text):
    words = text.split()
    return len(words)


#function to read file content given file path
test_text = "It was the best of times, it was the worst of times"

def get_char_frequency(text):
    text = text.lower()
    freq = {}
    for char in text:
        if char.isalpha():
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
    return freq

def sort_char_frequency(freq_dict):
    """Convert dict to sorted list of dictionaries"""
    # Create list of {char: count} dicts
    char_list = [{"char": char, "num": count} for char, count in freq_dict.items()]
    
    # Sort by count descending (highest first)
    return sorted(char_list, key=lambda x: x["num"], reverse=True)


if __name__ == "__main__":
    print(get_char_frequency(test_text))