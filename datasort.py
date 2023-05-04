def sort_data_alphabetically(data, key):
    sorted_data = sorted(data, key=lambda x: x[key].lower())
    return sorted_data

if __name__ == "__main__":
    data = [
        {"title": "Python Programming", "url": "https://example1.com"},
        {"title": "Artificial Intelligence", "url": "https://example2.com"},
        {"title": "Machine Learning", "url": "https://example3.com"},
        {"title": "Deep Learning", "url": "https://example4.com"},
    ]

    sorted_data = sort_data_alphabetically(data, "title")
    print(sorted_data)