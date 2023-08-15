#!/usr/bin/python3
def create_people_file(filename):
    people_data = [
        ["Alice", "Johnson", 28, "Engineer"],
        ["Bob", "Smith", 35, "Teacher"],
        ["Eve", "Brown", 22, "Artist"],
        ["Daniel", "Miller", 40, "Doctor"]
    ]
    
    with open(filename, "w") as file:
        file.write("First Name,Last Name,Age,Profession\n")
        for person in people_data:
            file.write(f"{person[0]},{person[1]},{person[2]},{person[3]}\n")

def sort_people_by_column(input_filename, output_filename, column_index):
    with open(input_filename, "r") as input_file:
        lines = input_file.readlines()
    
    # Remove the header line
    header = lines.pop(0)
    
    sorted_lines = sorted(lines, key=lambda line: line.split(',')[column_index])
    
    with open(output_filename, "w") as output_file:
        output_file.write(header)
        output_file.writelines(sorted_lines)

# Create the original people.txt file
create_people_file("people.txt")

# Prompt the user for column choice
column_choice = input("Enter the name of the column to sort by (First Name, Last Name, Age, Profession): ")
column_choice = column_choice.lower().strip()

# Determine column index based on user input
column_indices = {
    "first name": 0,
    "last name": 1,
    "age": 2,
    "profession": 3
}
if column_choice in column_indices:
    sort_column_index = column_indices[column_choice]
    sort_people_by_column("people.txt", "sorted_people.txt", sort_column_index)
    print("File sorted_people.txt created.")
else:
    print("Invalid column choice.")

