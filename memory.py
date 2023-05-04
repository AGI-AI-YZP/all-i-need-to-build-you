import json

class DataManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.load_data()

    def save_data(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.data, file)

    def load_data(self):
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {"training_data": [], "search_data": [], "learning_data": []}
        return data

    def add_data(self, category, entry):
        if category in self.data:
            self.data[category].append(entry)
            self.save_data()
        else:
            print(f"Invalid category: {category}")

    def get_data(self, category):
        if category in self.data:
            return self.data[category]
        else:
            print(f"Invalid category: {category}")
            return None

if __name__ == "__main__":
    file_path = "data.json"
    data_manager = DataManager(file_path)

    # Add data
    data_manager.add_data("training_data", {"input": "text3", "output": "result3"})
    data_manager.add_data("search_data", {"query": "Python programming", "results": [{"title": "Title2", "url": "URL2"}]})
    data_manager.add_data("learning_data", {"lesson": "Lesson2", "topic": "Topic2", "resources": ["Resource3", "Resource4"]})

    # Get data
    training_data = data_manager.get_data("training_data")
    search_data = data_manager.get_data("search_data")
    learning_data = data_manager.get_data("learning_data")

    print("Training Data:", training_data)
    print("Search Data:", search_data)
    print("Learning Data:", learning_data)