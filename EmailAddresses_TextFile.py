count = 0  # Initialize the count variable to 0

with open('mbox-short.txt', 'r') as file:  # Open the file
    for line in file:  # Loop through each line in the file
        if line.startswith('From ') and not line.startswith('From:'):  # Check if the line starts with 'From ' but not 'From:'
            words = line.split()  # Split the line into words
            print(words[1])  # Print the second word
            count += 1  # Increment the count variable

print("There were",count,"lines in the file with From as the first word ")
