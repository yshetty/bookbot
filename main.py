import sys
from stats import get_num_words, get_char_frequency, sort_char_frequency

#function to read file content given file path
def get_file_text(filepath):
    with open(filepath, 'r') as file:
        content = file.read()
    return content



#define main
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    num_words = get_num_words(get_file_text(sys.argv[1]))
    # print(f'Found {num_words} total words')

    char_freq = get_char_frequency(get_file_text(sys.argv[1]))
    # print(f'Character frequency: {char_freq}')

    # Generate character report
    char_report = sort_char_frequency(char_freq)

    # Print formatted report
    print("\n========= BOOKBOT ===========")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    # Print top 10 characters (matches assignment format)
    for item in char_report:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

    # print(sys.argv)
    # print(sys.argv[0])
    # print(sys.argv[1])

main()