def perform_transaction(username):
    # List of valid usernames
    valid_usernames = ["user1", "user2", "user3"]

    # Check if the entered username is in the list of valid usernames
    if username in valid_usernames:
        # Perform the transaction
        print("Transaction successful for user:", username)
        # Insert transaction logic here
    else:
        print("Invalid username. Transaction aborted.")

# Example usage
input_username = input("Enter your username: ")
perform_transaction(input_username)
