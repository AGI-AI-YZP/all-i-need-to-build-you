import json

def read_json_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def word_to_numbers(word):
    word = word.lower()
    numbers = [ord(char) - ord('a') + 1 for char in word]
    return numbers

def mathematical_operations(numbers):
    total = sum(numbers)
    mean = total / len(numbers)
    product = 1
    for num in numbers:
        product *= num
    return total, mean, product

if __name__ == "__main__":
    filename = 'words.json'
    
    try:
        words = read_json_file(filename)
        for word in words:
            numbers = word_to_numbers(word)
            total, mean, product = mathematical_operations(numbers)

            print(f"Word: {word}")
            print(f"Letter to number conversion: {numbers}")
            print(f"Sum of numbers: {total}")
            print(f"Mean of numbers: {mean:.2f}")
            print(f"Product of numbers: {product}")
            print("-" * 30)
    except FileNotFoundError:
        print(f"FileNotFoundError: {filename} not found. Please check the file path.")
