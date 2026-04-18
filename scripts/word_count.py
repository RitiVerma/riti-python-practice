import sys

def count_words(filepath):
    """Reads a file and returns the total number of words."""
    try:
        total_words = 0
        with open(filepath, 'r', encoding='utf-8') as file:
            for line in file:
                total_words += len(line.split())
        return total_words
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        return -1
    except Exception as e:
        print(f"An error occurred: {e}")
        return -1

if __name__ == "__main__":
    # Ensure a filename is passed as an argument
    if len(sys.argv) < 2:
        print("Usage: python3 word_count.py <filename>")
        sys.exit(1)
    
    filename = sys.argv[1]
    word_count = count_words(filename)
    
    if word_count >= 0:
        print(f"The file '{filename}' contains {word_count} words.")
