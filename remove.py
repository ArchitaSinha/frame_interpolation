def remove_string_from_file(file_path, string_to_remove):
    
    try:
        # Read the content of the file
        with open(file_path, 'r') as file:
            content = file.read()

        # Remove the specified string
        updated_content = content.replace(string_to_remove, '')

        # Write the updated content back to the file
        with open(file_path, 'w') as file:
            file.write(updated_content)

        print(f'String "{string_to_remove}" removed from {file_path}')
    except FileNotFoundError:
        print(f'File not found: {file_path}')
    except Exception as e:
        print(f'An error occurred: {e}')

# Example usage
# Example usage
file_path = 'tri.txt'
string_to_remove = 'sequences/'
remove_string_from_file(file_path, string_to_remove)
