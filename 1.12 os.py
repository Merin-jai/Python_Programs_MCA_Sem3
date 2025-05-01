import os

# Create a directory
def create_directory(directory_name):
    try:
        os.makedirs(directory_name)
        print(f"Directory '{directory_name}' created.")
    except FileExistsError:
        print(f"Directory '{directory_name}' already exists.")

# List contents of a directory
def list_directory_contents(directory):
    try:
        contents = os.listdir(directory)
        print(f"Contents of '{directory}': {contents}")
    except FileNotFoundError:
        print(f"Directory '{directory}' not found.")

# Search for ".py" files
def search_python_files(directory):
    try:
        python_files = [f for f in os.listdir(directory) if f.endswith('.py')]
        print("Python files found:", python_files)
    except FileNotFoundError:
        print(f"Directory '{directory}' not found.")

# Remove a specific file
def remove_file(file_path):
    try:
        os.remove(file_path)
        print(f"File '{file_path}' removed.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")

# Example usage
if __name__ == "__main__":
    dir_name = 'example_directory'
    
    # Create a directory
    create_directory(dir_name)
    
    # List contents of the current directory
    list_directory_contents('.')
    
    # Search for Python files in the current directory
    search_python_files('.')
    
    # Remove a specific file (replace with the actual file name you want to remove)
    file_to_remove = 'sample.py'  # Change this to your file name
    remove_file(file_to_remove)
