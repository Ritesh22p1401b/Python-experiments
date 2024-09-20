# Initialize an empty dictionary to store user data
users = {}

# number of user we want to enter in dictionary
num_users = int(input("How many users do you want to enter? "))

# Collect user details
for i2 in range(num_users):
    user_id = input("Enter user ID: ")
    user_name = input("Enter user name: ")
    user_age = input("Enter user age: ")
    
    # Store user details in the dictionary
    users[user_id] = {'name': user_name, 'age': user_age}

# Ask for a user ID to retrieve details
search_id = input("Enter the user ID which we want to search for: ")

# Retrieve and print user details based on the provided ID
if search_id in users:
    user_details = users[search_id]
    print(f"User ID: {search_id}")
    print(f"User Name: {user_details['name']}")
    print(f"User Age: {user_details['age']}")
else:
    print("User ID not found in our Database")

