def main():
    # Read the file contents once
    with open("books/frankenstein.txt") as f:
        text = f.read()

    # Count words in the document
    word_count = len(text.split())

    # Remove non-alphabetic characters and convert to lowercase
    lowered_string = ''.join(char for char in text.lower() if char.isalpha())

    # Count character frequencies
    freq = {}
    for letter in lowered_string:
        if letter in freq:
            freq[letter] += 1
        else:
            freq[letter] = 1

    # Convert frequency dictionary to a sorted list of dictionaries
    letters = [{"char": x, "num": freq[x]} for x in freq]
    letters.sort(key=lambda d: d["num"], reverse=True)

    

    # Print the sorted list
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")

    for entry in letters:
        line = (f"The '{entry['char']}' character was found {entry['num']} times")
        print(line)

    print("--- End report ---")



if __name__ == "__main__":
    main()

