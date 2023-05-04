import json
import csv

def process_json_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    print("JSON data:")
    print(data)

def process_csv_file(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        print("CSV data:")
        for row in reader:
            print(row)

def process_text_file(filename):
    with open(filename, 'r') as file:
        text = file.read()
    print("Text data:")
    print(text)

def process_file(filename):
    if filename.endswith('.json'):
        process_json_file(filename)
    elif filename.endswith('.csv'):
        process_csv_file(filename)
    elif filename.endswith('.txt'):
        process_text_file(filename)
    else:
        print(f"Unsupported file type: {filename}")

if __name__ == "__main__":
    filenames = [
        'example.json',
        'example.csv',
        'example.txt'
    ]

    for filename in filenames:
        try:
            process_file(filename)
            print('-' * 30)
        except FileNotFoundError:
            print(f"FileNotFoundError: {filename} not found. Please check the file path.")