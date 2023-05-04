# Collecting data from a user
name = input("What's your name? ")
age = input("How old are you? ")

# Storing data in a text file
with open('user_data.txt', 'w') as file:
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")